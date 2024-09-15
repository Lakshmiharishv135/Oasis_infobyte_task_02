import customtkinter  as ctk

# Function to calculate BMI
def calculate_bmi(weight, height):
    return weight / (height ** 2)

# Function to categorize the BMI result
def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

# Function to handle button click and calculate BMI
def on_calculate_bmi():
    try:
        # Get user inputs and convert them to float
        weight = float(entry1.get())
        height = float(entry2.get()) / 100  # Convert cm to meters

        # Calculate BMI
        bmi = calculate_bmi(weight, height)

        # Categorize BMI
        category = bmi_category(bmi)

        # Display result in the result_label
        result_label.configure(text=f"Your BMI is: {bmi:.2f}\nCategory: {category}")

    except ValueError:
        result_label.config(text="Please enter valid numbers.")

# Main program
if __name__ == "__main__":
    # GUI setup
    root = ctk.CTk()
    root.geometry("300x400+100+20")
    root.resizable(0,0)
    root.title("BMI Calculator")

    Header = ctk.CTkLabel(root, text="Welcome to the BMI Calculator", font=('Arial', 18, 'bold'))
    Header.pack(pady=20, anchor='center')

    # Takes weight value
    label1 = ctk.CTkLabel(root, text="Weight (in kilograms)", font=('Arial', 13))
    label1.pack(padx=20, pady=8, anchor='w')
    entry1 = ctk.CTkEntry(root, width=200,font=('Arial', 13))
    entry1.pack(pady=5, padx=20, anchor='w')

    # Takes height value
    label2 = ctk.CTkLabel(root, text="Height (in centimeters)", font=('Arial', 13))
    label2.pack(padx=20, pady=8, anchor='w')
    entry2 = ctk.CTkEntry(root, width=200,font=('Arial', 13))
    entry2.pack(pady=5, padx=20, anchor='w')

    # Button to calculate BMI
    button = ctk.CTkButton(root, text="Calculate BMI", command=on_calculate_bmi)
    button.pack(pady=20, anchor='center')

    # Label to display result
    result_label = ctk.CTkLabel(root, text="", font=('Arial', 16,'bold'), text_color="blue")
    result_label.pack(pady=10, anchor='center')

    root.mainloop()
