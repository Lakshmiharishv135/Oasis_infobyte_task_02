# BMI Calculator

## Overview
This is a simple **BMI (Body Mass Index) Calculator** built using the `CustomTkinter` library in Python. The calculator takes the user’s weight (in kilograms) and height (in centimeters), and computes the BMI value along with the corresponding category (Underweight, Normal weight, Overweight, or Obese). It features a user-friendly GUI to make the calculations easy and efficient.

## Features
- **User-Friendly Interface**: The GUI uses `CustomTkinter` for modern and clean design.
- **BMI Calculation**: Computes BMI using the formula:  
  \[
  \text{BMI} = \frac{\text{weight (kg)}}{\text{height (m)}^2}
  \]
- **BMI Categories**:
  - Underweight: BMI < 18.5
  - Normal weight: 18.5 ≤ BMI < 24.9
  - Overweight: 25 ≤ BMI < 29.9
  - Obese: BMI ≥ 30
- **Input Validation**: Ensures that the user enters valid numerical data.

## Requirements
- Python 3.x
- `customtkinter` library

To install `customtkinter`, run:

```bash
pip install customtkinter
```

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/bmi-calculator.git
   ```
2. Navigate to the project directory:
   ```bash
   cd bmi-calculator
   ```
3. Run the Python script:
   ```bash
   python bmi_calculator.py
   ```

## Usage
1. Enter your weight in kilograms.
2. Enter your height in centimeters.
3. Click on the **"Calculate BMI"** button.
4. The result will display your BMI value and the corresponding category.

