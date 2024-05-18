# Childcare Affordability Calculator

## Overview
The Childcare Affordability Calculator is a desktop application designed to help parents assess whether they can afford childcare so that both parents can return to work. The application calculates the net gain or loss after considering childcare costs, parents' net monthly income, and expenses. It also includes features for saving and loading scenarios, as well as visualizing the financial breakdown with a pie chart.

## Features
- **Calculate Net Gain/Loss**: Input monthly childcare costs, parents' net income, and expenses to calculate the net gain/loss.
- **Scenario Management**: Save and load different scenarios to compare financial outcomes.
- **Graphical Representation**: Visualize the financial breakdown with a pie chart.
- **Help and Guidance**: Access a comprehensive help section to understand how to use the application.

## Requirements
- Python 3.x
- `matplotlib` library for graphical representation

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/suni639/childcare_affordability_calculator.git
   cd childcare_affordability_calculator

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt

## Usage
1. **Run the Application**:
   ```bash
   python main.py

2. **Run Tests**:
   ```bash
   python -m unittest discover -s tests

## Usage
- **Input Data**: Enter the monthly costs for childcare, the net income of both parents, and expenses.
- **Calculate**: Click the "Calculate" button to compute the net gain or loss.
- **Reset**: Use the "Reset" button to clear all input fields.
- **Save Scenario**: Save the current input data to a file for future reference.
- **Load Scenario**: Load a previously saved scenario from a file.
- **Show Graph**: Visualize the financial breakdown using a pie chart.
- **Help**: Access the help section for detailed guidance on how to use the application.

## License
This project is licensed under the MIT License.