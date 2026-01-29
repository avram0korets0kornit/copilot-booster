# Copilot Booster - Node.js Implementation 🚀

This directory contains a Node.js/JavaScript implementation of the Copilot Simulator, providing the same functionality as the Python version for developers more familiar with JavaScript.

## 🎯 Features

- **Core Simulator**: Complete JavaScript implementation of the Copilot simulation pipeline
- **REST API Server**: Express.js server with RESTful endpoints
- **Interactive Examples**: Basic and advanced usage examples
- **Full Parity**: Same functionality as Python version, adapted for JavaScript idioms

## 📦 Installation

Install dependencies using npm:

```bash
npm install
```

## 🚀 Quick Start

### 1. Run the Basic Simulator

```bash
node copilot_simulator.js
```

This runs the built-in examples showing how Copilot generates suggestions.

### 2. Start the REST API Server

```bash
npm start
# or
node server.js
```

The server will start on `http://localhost:3000`.

### 3. Run Examples

```bash
# Basic examples
npm run examples:basic

# Advanced examples
npm run examples:advanced
```

## 🔌 REST API Usage

### Start the Server

```bash
npm start
```

### API Endpoints

#### GET `/`
Returns API documentation and available endpoints.

```bash
curl http://localhost:3000/
```

#### GET `/api/health`
Health check endpoint.

```bash
curl http://localhost:3000/api/health
```

#### POST `/api/suggestions`
Get code suggestions based on context.

**Request Body:**
```json
{
  "fileContent": "function calculateSum(a, b) {",
  "cursorPosition": [1, 0],
  "filePath": "math.js",
  "verbose": false
}
```

**Example with curl:**
```bash
curl -X POST http://localhost:3000/api/suggestions \
  -H "Content-Type: application/json" \
  -d '{
    "fileContent": "function calculateSum(a, b) {",
    "cursorPosition": [1, 0],
    "filePath": "math.js"
  }'
```

**Response:**
```json
{
  "suggestions": [
    {
      "text": "    // Function implementation explaining purpose and parameters",
      "confidence": 0.85,
      "reasoning": "Common pattern: Add comment or implementation after function definition"
    },
    {
      "text": "    return;",
      "confidence": 0.70,
      "reasoning": "Alternative: Placeholder return statement"
    }
  ],
  "metadata": {
    "totalSuggestions": 2,
    "filePath": "math.js",
    "cursorPosition": [1, 0],
    "timestamp": "2024-01-15T10:30:00.000Z"
  }
}
```

#### GET `/api/examples`
Get example requests for testing.

```bash
curl http://localhost:3000/api/examples
```

## 📖 Using as a Library

```javascript
const { CopilotSimulator } = require('./copilot_simulator');

// Create simulator instance
const simulator = new CopilotSimulator();

// Your code
const code = `
function calculateTotal(items) {
`;

// Get suggestions
const suggestions = simulator.getSuggestions(
    code,
    [2, 0],  // cursor position: [line, column]
    'example.js',
    true  // verbose mode
);

// Use the suggestions
suggestions.forEach(suggestion => {
    console.log(`Suggestion: ${suggestion.text}`);
    console.log(`Confidence: ${suggestion.confidence}`);
    console.log(`Reasoning: ${suggestion.reasoning}`);
});
```

## 🧩 Components

### Core Classes

- **`CodeContext`**: Represents the context gathered from the code editor
- **`Suggestion`**: Represents a code suggestion with confidence and reasoning
- **`ContextGatherer`**: Gathers context from file content and cursor position
- **`PromptGenerator`**: Creates optimized prompts for the language model
- **`SuggestionEngine`**: Simulates ML model that generates suggestions
- **`SuggestionRanker`**: Ranks and filters suggestions
- **`CopilotSimulator`**: Main orchestrator for the complete pipeline

### Server Components

- **Express.js Server**: RESTful API with CORS support
- **Error Handling**: Comprehensive error handling and validation
- **Health Checks**: Monitoring endpoint for uptime checks

## 🔬 How It Works

The simulator follows the same 4-phase pipeline as the Python version:

1. **Context Gathering** 📚
   - Extracts imports, comments, and surrounding code
   - Analyzes file structure and language

2. **Prompt Generation** 💭
   - Creates structured prompts for the ML model
   - Includes relevant context and cursor position

3. **Suggestion Generation** 🤖
   - Pattern matching based on common code structures
   - Generates multiple candidate suggestions

4. **Ranking & Filtering** 🔍
   - Ranks by confidence scores
   - Filters low-quality suggestions

## 📝 Examples

### Example 1: Function Definition

```javascript
const { CopilotSimulator } = require('./copilot_simulator');

const code = 'function calculateArea(radius) {';
const simulator = new CopilotSimulator();
const suggestions = simulator.getSuggestions(code, [1, 0], 'geometry.js');

console.log(suggestions[0].text);
// Output: "    // Function implementation explaining purpose and parameters"
```

### Example 2: Using the REST API with JavaScript

```javascript
const axios = require('axios');

async function getSuggestions() {
    const response = await axios.post('http://localhost:3000/api/suggestions', {
        fileContent: 'class Calculator {',
        cursorPosition: [1, 0],
        filePath: 'calculator.js'
    });
    
    console.log(response.data.suggestions);
}
```

### Example 3: Verbose Mode

```javascript
const simulator = new CopilotSimulator();
const suggestions = simulator.getSuggestions(
    'class Database {',
    [1, 0],
    'db.js',
    true  // Enable verbose mode to see all phases
);
```

## 🔄 Comparison with Python Version

| Feature | Python | Node.js |
|---------|--------|---------|
| Core Simulator | ✅ | ✅ |
| Pattern Recognition | ✅ | ✅ |
| Context Gathering | ✅ | ✅ |
| Verbose Mode | ✅ | ✅ |
| REST API Server | ❌ | ✅ |
| Examples | ✅ | ✅ |

The Node.js version adds a REST API server that's not present in the Python version, making it easy to integrate with web applications.

## 🎓 Learning Resources

The Node.js implementation follows the same educational principles as the Python version. See the main README for learning resources about:

- How GitHub Copilot works
- Prompt engineering
- Large language models
- Code completion systems

## 🤝 Contributing

Contributions are welcome! You can:
- Add more pattern recognition examples
- Improve the suggestion engine
- Add more language support
- Enhance the REST API
- Improve documentation

## ⚠️ Disclaimer

This is a simplified educational simulation. Real GitHub Copilot is far more sophisticated and uses proprietary technology from GitHub and OpenAI.
