/**
 * Copilot Simulator - Express.js REST API Server
 * 
 * This server provides a REST API for the Copilot simulator,
 * allowing clients to request code suggestions via HTTP.
 * 
 * Endpoints:
 * - POST /api/suggestions - Get code suggestions
 * - GET /api/health - Health check
 * - GET / - API documentation
 */

const express = require('express');
const { CopilotSimulator } = require('./copilot_simulator');

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(express.json());

// CORS middleware for development
app.use((req, res, next) => {
    res.header('Access-Control-Allow-Origin', '*');
    res.header('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept');
    res.header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
    next();
});

// Create simulator instance
const simulator = new CopilotSimulator();

/**
 * Root endpoint - API documentation
 */
app.get('/', (req, res) => {
    res.json({
        name: 'Copilot Simulator API',
        version: '1.0.0',
        description: 'REST API for GitHub Copilot simulation',
        endpoints: {
            'POST /api/suggestions': {
                description: 'Get code suggestions based on context',
                body: {
                    fileContent: 'string (required) - The content of the file',
                    cursorPosition: 'array (required) - Cursor position as [line, column]',
                    filePath: 'string (optional) - Path to the file (default: "example.js")',
                    verbose: 'boolean (optional) - Include detailed phase information (default: false)'
                },
                example: {
                    fileContent: 'function calculateSum(a, b) {',
                    cursorPosition: [1, 0],
                    filePath: 'math.js',
                    verbose: false
                }
            },
            'GET /api/health': {
                description: 'Health check endpoint'
            },
            'GET /api/examples': {
                description: 'Get example requests and responses'
            }
        }
    });
});

/**
 * Health check endpoint
 */
app.get('/api/health', (req, res) => {
    res.json({
        status: 'healthy',
        timestamp: new Date().toISOString(),
        uptime: process.uptime()
    });
});

/**
 * Get examples endpoint
 */
app.get('/api/examples', (req, res) => {
    res.json({
        examples: [
            {
                name: 'Function Definition',
                request: {
                    fileContent: 'function calculateArea(radius) {',
                    cursorPosition: [1, 0],
                    filePath: 'geometry.js'
                }
            },
            {
                name: 'Class Definition',
                request: {
                    fileContent: 'class Calculator {',
                    cursorPosition: [1, 0],
                    filePath: 'calculator.js'
                }
            },
            {
                name: 'Comment to Code',
                request: {
                    fileContent: '// Loop through all items and process them',
                    cursorPosition: [1, 0],
                    filePath: 'processor.js'
                }
            }
        ]
    });
});

/**
 * Main suggestions endpoint
 * POST /api/suggestions
 * 
 * Request body:
 * {
 *   "fileContent": "function test() {",
 *   "cursorPosition": [1, 0],
 *   "filePath": "example.js",  // optional
 *   "verbose": false            // optional
 * }
 */
app.post('/api/suggestions', (req, res) => {
    try {
        const { fileContent, cursorPosition, filePath, verbose } = req.body;

        // Validate required fields
        if (!fileContent) {
            return res.status(400).json({
                error: 'Bad Request',
                message: 'fileContent is required'
            });
        }

        if (!cursorPosition || !Array.isArray(cursorPosition) || cursorPosition.length !== 2) {
            return res.status(400).json({
                error: 'Bad Request',
                message: 'cursorPosition must be an array of [line, column]'
            });
        }

        // Get suggestions
        const suggestions = simulator.getSuggestions(
            fileContent,
            cursorPosition,
            filePath || 'example.js',
            verbose || false
        );

        // Format response
        const response = {
            suggestions: suggestions.map(sug => ({
                text: sug.text,
                confidence: sug.confidence,
                reasoning: sug.reasoning
            })),
            metadata: {
                totalSuggestions: suggestions.length,
                filePath: filePath || 'example.js',
                cursorPosition: cursorPosition,
                timestamp: new Date().toISOString()
            }
        };

        res.json(response);
    } catch (error) {
        console.error('Error processing request:', error);
        res.status(500).json({
            error: 'Internal Server Error',
            message: error.message
        });
    }
});

/**
 * 404 handler
 */
app.use((req, res) => {
    res.status(404).json({
        error: 'Not Found',
        message: `Endpoint ${req.method} ${req.path} not found`
    });
});

/**
 * Error handler
 */
app.use((err, req, res, next) => {
    console.error('Error:', err);
    res.status(500).json({
        error: 'Internal Server Error',
        message: err.message
    });
});

// Start server
if (require.main === module) {
    app.listen(PORT, () => {
        console.log('='.repeat(60));
        console.log('🚀 Copilot Simulator Server');
        console.log('='.repeat(60));
        console.log(`Server running on http://localhost:${PORT}`);
        console.log(`API docs available at http://localhost:${PORT}`);
        console.log(`Health check at http://localhost:${PORT}/api/health`);
        console.log('='.repeat(60));
    });
}

module.exports = app;
