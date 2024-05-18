# Childcare Affordability Calculator User Guide

## Introduction
The Childcare Affordability Calculator helps you determine if both parents can afford to return to work by calculating the net gain or loss after considering childcare costs, parents' net monthly income, and expenses.

## Getting Started
1. **Open the Application**: Run `python main.py` to start the application.
2. **Enter Data**: Fill in the required fields with your financial data.

## Features

### Calculate
- **Childcare Costs (£/month)**: Enter your monthly childcare costs.
- **Parent 1 Net Income (£/month)**: Enter the net monthly income of the first parent.
- **Parent 2 Net Income (£/month)**: Enter the net monthly income of the second parent.
- **Expenses (£/month)**: Enter the total monthly expenses.

Click the **Calculate** button to see the net gain or loss.

### Reset
Click the **Reset** button to clear all input fields.

### Save Scenario
Click the **Save Scenario** button to save your current data to a JSON file.

### Load Scenario
Click the **Load Scenario** button to load data from a previously saved JSON file.

### Show Graph
Click the **Show Graph** button to display a pie chart showing the financial breakdown.

## Example Scenarios
Refer to `data/sample_data.json` for example scenarios that can be loaded into the application.

## Troubleshooting
- **Invalid Input**: Ensure all fields are filled with numeric values.
- **File Errors**: Ensure you have read/write permissions for the file operations.
