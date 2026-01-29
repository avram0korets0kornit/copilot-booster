/**
 * Example Client for Copilot Simulator API
 * 
 * This demonstrates how to use the REST API to get code suggestions
 * from the Copilot Simulator server.
 * 
 * Usage:
 * 1. Start the server: npm start
 * 2. Run this client: node examples-js/api_client_example.js
 */

const axios = require('axios');

const API_URL = 'http://localhost:3000';

async function testHealthCheck() {
    console.log('\n' + '='.repeat(70));
    console.log('Testing Health Check Endpoint');
    console.log('='.repeat(70));
    
    try {
        const response = await axios.get(`${API_URL}/api/health`);
        console.log('\nServer Status:', response.data.status);
        console.log('Uptime:', Math.floor(response.data.uptime), 'seconds');
    } catch (error) {
        console.error('Error:', error.message);
        console.log('\nMake sure the server is running: npm start');
        process.exit(1);
    }
}

async function getSuggestions(fileContent, cursorPosition, filePath) {
    console.log('\n' + '='.repeat(70));
    console.log(`Getting suggestions for: ${filePath}`);
    console.log('='.repeat(70));
    console.log(`\nCode:\n${fileContent}`);
    console.log(`\nCursor Position: Line ${cursorPosition[0]}, Column ${cursorPosition[1]}`);
    
    try {
        const response = await axios.post(`${API_URL}/api/suggestions`, {
            fileContent,
            cursorPosition,
            filePath
        });
        
        console.log(`\nReceived ${response.data.suggestions.length} suggestions:\n`);
        
        response.data.suggestions.forEach((suggestion, i) => {
            console.log(`${i + 1}. Confidence: ${(suggestion.confidence * 100).toFixed(0)}%`);
            console.log(`   Reasoning: ${suggestion.reasoning}`);
            console.log(`   Suggestion:`);
            console.log(`   ${suggestion.text}\n`);
        });
    } catch (error) {
        console.error('Error:', error.message);
        if (error.response) {
            console.error('Response:', error.response.data);
        }
    }
}

async function main() {
    console.log('\n' + '='.repeat(70));
    console.log('COPILOT SIMULATOR - API CLIENT EXAMPLE');
    console.log('='.repeat(70));
    console.log('\nThis example demonstrates using the REST API to get code suggestions.');
    
    // Test health check
    await testHealthCheck();
    
    // Example 1: Function definition
    await getSuggestions(
        'function calculateTotal(items) {',
        [1, 0],
        'calculator.js'
    );
    
    // Example 2: Class definition
    await getSuggestions(
        'class ShoppingCart {',
        [1, 0],
        'cart.js'
    );
    
    // Example 3: Comment to code
    await getSuggestions(
        '// Validate user input and sanitize data',
        [1, 0],
        'validator.js'
    );
    
    // Example 4: Complex context
    await getSuggestions(
        `const express = require('express');
const app = express();

app.get('/users/:id', async (req, res) => {
    const userId = req.params.id;
    // Fetch user from database
`,
        [6, 0],
        'routes.js'
    );
    
    console.log('\n' + '='.repeat(70));
    console.log('ALL API EXAMPLES COMPLETE');
    console.log('='.repeat(70));
    console.log('\nKey Points:');
    console.log('1. The API accepts POST requests with file content and cursor position');
    console.log('2. Responses include suggestions with confidence scores and reasoning');
    console.log('3. The API can be integrated into any application that needs code suggestions');
    console.log('4. Use the health endpoint to check if the server is running');
    console.log('\n');
}

if (require.main === module) {
    main().catch(console.error);
}

module.exports = { testHealthCheck, getSuggestions };
