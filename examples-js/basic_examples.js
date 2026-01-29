/**
 * Basic Examples - Copilot Simulator
 * 
 * This file demonstrates basic usage of the Copilot simulator
 * with simple, common coding scenarios.
 */

const { CopilotSimulator } = require('../copilot_simulator');

function exampleFunctionDocstring() {
    console.log('\n' + '='.repeat(70));
    console.log('EXAMPLE: Function Documentation Suggestion');
    console.log('='.repeat(70));

    const code = `function calculateAverage(numbers) {`;

    const simulator = new CopilotSimulator();
    const suggestions = simulator.getSuggestions(
        code,
        [1, 0],
        'math_utils.js',
        false
    );

    console.log(`\nCode context:\n${code}`);
    console.log(`\nCursor position: Line 1, Column 0`);
    console.log(`\nTop suggestions:`);
    suggestions.slice(0, 3).forEach((sug, i) => {
        console.log(`\n${i + 1}. Confidence: ${(sug.confidence * 100).toFixed(0)}%`);
        console.log(`   Reasoning: ${sug.reasoning}`);
        console.log(`   Suggestion:\n${sug.text}`);
    });
}

function exampleClassInitialization() {
    console.log('\n' + '='.repeat(70));
    console.log('EXAMPLE: Class Initialization Suggestion');
    console.log('='.repeat(70));

    const code = `class UserAccount {`;

    const simulator = new CopilotSimulator();
    const suggestions = simulator.getSuggestions(
        code,
        [1, 0],
        'models.js',
        false
    );

    console.log(`\nCode context:\n${code}`);
    console.log(`\nCursor position: Line 1, Column 0`);
    console.log(`\nTop suggestions:`);
    suggestions.slice(0, 3).forEach((sug, i) => {
        console.log(`\n${i + 1}. Confidence: ${(sug.confidence * 100).toFixed(0)}%`);
        console.log(`   Reasoning: ${sug.reasoning}`);
        console.log(`   Suggestion:\n${sug.text}`);
    });
}

function exampleCommentToCode() {
    console.log('\n' + '='.repeat(70));
    console.log('EXAMPLE: Comment to Code Suggestion');
    console.log('='.repeat(70));

    const code = `// Loop through all users and validate their email addresses`;

    const simulator = new CopilotSimulator();
    const suggestions = simulator.getSuggestions(
        code,
        [1, 0],
        'validation.js',
        false
    );

    console.log(`\nCode context:\n${code}`);
    console.log(`\nCursor position: Line 1, Column 0`);
    console.log(`\nTop suggestions:`);
    suggestions.slice(0, 3).forEach((sug, i) => {
        console.log(`\n${i + 1}. Confidence: ${(sug.confidence * 100).toFixed(0)}%`);
        console.log(`   Reasoning: ${sug.reasoning}`);
        console.log(`   Suggestion:\n${sug.text}`);
    });
}

function exampleWithContext() {
    console.log('\n' + '='.repeat(70));
    console.log('EXAMPLE: Suggestions with Rich Context');
    console.log('='.repeat(70));

    const code = `const fs = require('fs');
const path = require('path');

class DataProcessor {
    constructor(configPath) {
        this.configPath = configPath;
        this.data = [];
    }

    loadData(filePath) {
        // Load JSON data from file
`;

    const simulator = new CopilotSimulator();
    const suggestions = simulator.getSuggestions(
        code,
        [11, 0],
        'processor.js',
        false
    );

    const lines = code.split('\n');
    console.log(`\nCode context (showing last 5 lines):`);
    console.log(lines.slice(-5).join('\n'));
    console.log(`\nCursor position: Line 11, Column 0`);
    console.log(`\nTop suggestions:`);
    suggestions.slice(0, 3).forEach((sug, i) => {
        console.log(`\n${i + 1}. Confidence: ${(sug.confidence * 100).toFixed(0)}%`);
        console.log(`   Reasoning: ${sug.reasoning}`);
        console.log(`   Suggestion:\n${sug.text}`);
    });
}

function main() {
    console.log('\n' + '='.repeat(70));
    console.log('COPILOT SIMULATOR - BASIC EXAMPLES');
    console.log('='.repeat(70));
    console.log('\nThese examples demonstrate how Copilot generates suggestions');
    console.log('in common coding scenarios.\n');

    exampleFunctionDocstring();
    exampleClassInitialization();
    exampleCommentToCode();
    exampleWithContext();

    console.log('\n' + '='.repeat(70));
    console.log('ALL EXAMPLES COMPLETE');
    console.log('='.repeat(70));
    console.log('\nKey Takeaways:');
    console.log('1. Copilot analyzes the code context around your cursor');
    console.log('2. It recognizes common patterns (functions, classes, comments)');
    console.log('3. It generates multiple suggestions with confidence scores');
    console.log('4. Higher confidence suggestions are ranked first');
    console.log('5. The suggestions are based on learned patterns from training data');
    console.log('\n');
}

if (require.main === module) {
    main();
}

module.exports = { main };
