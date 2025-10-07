import math

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Enter a valid number.")

def main():
    gender = input("Enter gender (male/female): ").strip().lower()
    age = get_float_input("Enter age (years): ")
    height = get_float_input("Enter height (cm): ")
    neck = get_float_input("Enter neck circumference (cm): ")
    waist = get_float_input("Enter waist circumference (cm): ")

    hip = 0
    if gender == "female":
        hip = get_float_input("Enter hip circumference (cm): ")

    if gender == "male":
        # U.S. Navy Method for males
        body_fat = 495 / (1.0324 - 0.19077 * math.log10(waist - neck) + 0.15456 * math.log10(height)) - 450
    elif gender == "female":
        # U.S. Navy Method for females
        body_fat = 495 / (1.29579 - 0.35004 * math.log10(waist + hip - neck) + 0.22100 * math.log10(height)) - 450
    else:
        print("Invalid gender input. Please enter 'male' or 'female'.")
        return

    print(f"\nEstimated Body Fat Percentage: {body_fat:.2f}%")

if __name__ == "__main__":
    main()