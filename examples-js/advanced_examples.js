/**
 * Advanced Examples - Copilot Simulator
 * 
 * This file demonstrates advanced features of the Copilot simulator,
 * showing how it handles complex scenarios and provides detailed insights.
 */

const { CopilotSimulator, ContextGatherer } = require('../copilot_simulator');

function exampleVerboseMode() {
    console.log('\n' + '='.repeat(70));
    console.log('EXAMPLE: Verbose Mode - See All Internal Phases');
    console.log('='.repeat(70));

    const code = `const axios = require('axios');

async function fetchUserData(userId) {
    // Fetch user data from API
`;

    const simulator = new CopilotSimulator();

    console.log('\nRunning simulation with verbose=true to see internal phases...');
    console.log('\n');

    const suggestions = simulator.getSuggestions(
        code,
        [4, 0],
        'api_client.js',
        true  // This shows all internal phases
    );

    console.log('\n📊 Analysis:');
    console.log(`  - Total suggestions generated: ${suggestions.length}`);
    if (suggestions.length > 0) {
        console.log(`  - Highest confidence: ${(suggestions[0].confidence * 100).toFixed(0)}%`);
    } else {
        console.log('  - No suggestions');
    }
}

function exampleContextAnalysis() {
    console.log('\n' + '='.repeat(70));
    console.log('EXAMPLE: Context Gathering Analysis');
    console.log('='.repeat(70));

    const code = `#!/usr/bin/env node
// Module for processing customer data.

const fs = require('fs');
const path = require('path');

// Configure logging
const logger = console;

class CustomerProcessor {
    // Processes customer data and generates reports.

    constructor(config) {
        this.config = config;
        this.customers = [];
    }

    addCustomer(customerData) {
        // Validate customer data before adding
`;

    const context = ContextGatherer.gatherContext(code, [19, 0], 'customer_processor.js');

    console.log('\n📋 Gathered Context Details:');
    console.log(`  File: ${context.filePath}`);
    console.log(`  Language: ${context.language}`);
    console.log(`  Cursor Position: Line ${context.cursorLine}, Column ${context.cursorColumn}`);
    console.log(`\n  Total lines before cursor: ${context.linesBeforeCursor.length}`);
    console.log(`  Total lines after cursor: ${context.linesAfterCursor.length}`);

    console.log(`\n  📦 Imports found (${context.imports.length}):`);
    context.imports.forEach(imp => {
        console.log(`    - ${imp}`);
    });

    console.log(`\n  💬 Comments found (${context.comments.length}):`);
    context.comments.slice(0, 5).forEach(comment => {
        console.log(`    - ${comment.trim()}`);
    });

    console.log(`\n  📝 Last 3 lines before cursor:`);
    context.linesBeforeCursor.slice(-3).forEach((line, i) => {
        console.log(`    ${i + 1}. ${line}`);
    });

    // Now get suggestions
    const simulator = new CopilotSimulator();
    const suggestions = simulator.getSuggestions(
        code,
        [19, 0],
        'customer_processor.js',
        false
    );

    console.log(`\n  💡 Generated ${suggestions.length} suggestions`);
    if (suggestions.length > 0) {
        console.log(`\n  Top suggestion (confidence: ${(suggestions[0].confidence * 100).toFixed(0)}%):`);
        console.log(`    ${suggestions[0].text}`);
    }
}

function exampleMultipleScenarios() {
    console.log('\n' + '='.repeat(70));
    console.log('EXAMPLE: Comparing Suggestions Across Scenarios');
    console.log('='.repeat(70));

    const scenarios = [
        {
            name: 'After Function Definition',
            code: 'function processPayment(amount, currency) {',
            cursor: [1, 0],
            file: 'payment.js'
        },
        {
            name: 'After Class Definition',
            code: 'class PaymentGateway {',
            cursor: [1, 0],
            file: 'gateway.js'
        },
        {
            name: 'After Loop Comment',
            code: '// Iterate through all transactions',
            cursor: [1, 0],
            file: 'transactions.js'
        },
        {
            name: 'After Validation Comment',
            code: '// Check if the user has sufficient balance',
            cursor: [1, 0],
            file: 'balance.js'
        }
    ];

    const simulator = new CopilotSimulator();

    scenarios.forEach(scenario => {
        console.log(`\n${'─'.repeat(70)}`);
        console.log(`📍 Scenario: ${scenario.name}`);
        console.log(`   Code: ${scenario.code}`);

        const suggestions = simulator.getSuggestions(
            scenario.code,
            scenario.cursor,
            scenario.file,
            false
        );

        console.log(`\n   Suggestions (${suggestions.length} total):`);
        suggestions.slice(0, 2).forEach((sug, i) => {
            console.log(`\n   ${i + 1}. Confidence: ${(sug.confidence * 100).toFixed(0)}%`);
            console.log(`      Reasoning: ${sug.reasoning}`);
            const preview = sug.text.length > 60 ? sug.text.substring(0, 60) + '...' : sug.text;
            console.log(`      Code: ${preview}`);
        });
    });
}

function exampleConfidenceScores() {
    console.log('\n' + '='.repeat(70));
    console.log('EXAMPLE: Understanding Confidence Scores');
    console.log('='.repeat(70));

    console.log('\nConfidence scores indicate how certain Copilot is about a suggestion:');
    console.log('  - 0.90+ : Very high confidence (common, well-established patterns)');
    console.log('  - 0.70-0.89: High confidence (likely correct)');
    console.log('  - 0.50-0.69: Medium confidence (reasonable suggestion)');
    console.log('  - 0.40-0.49: Low confidence (speculative)');
    console.log('  - Below 0.40: Filtered out (too uncertain)');

    const testCases = [
        ['class Database {', 'Class definitions almost always start with constructor'],
        ['function calculate(x, y) {', 'Functions often start with comments or implementation'],
        ['// Loop through items', 'Comment suggests iteration, but implementation varies']
    ];

    const simulator = new CopilotSimulator();

    testCases.forEach(([code, explanation]) => {
        console.log(`\n${'─'.repeat(70)}`);
        console.log(`Code: ${code}`);
        console.log(`Why: ${explanation}`);

        const suggestions = simulator.getSuggestions(
            code,
            [1, 0],
            'test.js',
            false
        );

        if (suggestions.length > 0) {
            console.log(`\nTop suggestion confidence: ${(suggestions[0].confidence * 100).toFixed(0)}%`);
            process.stdout.write('Interpretation: ');
            const conf = suggestions[0].confidence;
            if (conf >= 0.90) {
                console.log('Very confident - this is a well-established pattern');
            } else if (conf >= 0.70) {
                console.log('Confident - this is a likely correct suggestion');
            } else if (conf >= 0.50) {
                console.log('Moderate - this is a reasonable possibility');
            } else {
                console.log('Low - this is more speculative');
            }
        }
    });
}

function main() {
    console.log('\n' + '='.repeat(70));
    console.log('COPILOT SIMULATOR - ADVANCED EXAMPLES');
    console.log('='.repeat(70));
    console.log('\nThese examples demonstrate advanced features and provide');
    console.log('deeper insights into how Copilot works internally.\n');

    exampleVerboseMode();
    exampleContextAnalysis();
    exampleMultipleScenarios();
    exampleConfidenceScores();

    console.log('\n' + '='.repeat(70));
    console.log('ALL ADVANCED EXAMPLES COMPLETE');
    console.log('='.repeat(70));
    console.log('\nKey Insights:');
    console.log('1. Context gathering is comprehensive (imports, comments, code structure)');
    console.log('2. Prompt generation structures context optimally for the ML model');
    console.log('3. Confidence scores reflect pattern frequency and certainty');
    console.log('4. Different code patterns trigger different suggestion strategies');
    console.log('5. Verbose mode helps understand the internal decision-making process');
    console.log('\n');
}

if (require.main === module) {
    main();
}

module.exports = { main };
