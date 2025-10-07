def calculate_body_fat_percentage(sex, height, neck, waist, hip=None):
    import math
    if sex.lower() == "male":
        # U.S. Navy Method for men
        body_fat = 86.010 * math.log10(waist - neck) - 70.041 * math.log10(height) + 36.76
    elif sex.lower() == "female":
        # U.S. Navy Method for women
        if hip is None:
            raise ValueError("Hip measurement is required for females.")
        body_fat = 163.205 * math.log10(waist + hip - neck) - 97.684 * math.log10(height) - 78.387
    else:
        raise ValueError("Invalid sex. Enter 'male' or 'female'.")
    return round(body_fat, 2)

def main():
    print("Body Fat Percentage Calculator (U.S. Navy Method)")
    sex = input("Enter sex (male/female): ").strip()
    height = float(input("Enter height in cm: "))
    neck = float(input("Enter neck circumference in cm: "))
    waist = float(input("Enter waist circumference in cm: "))
    hip = None
    if sex.lower() == "female":
        hip = float(input("Enter hip circumference in cm: "))
    body_fat = calculate_body_fat_percentage(sex, height, neck, waist, hip)
    print(f"Estimated Body Fat Percentage: {body_fat}%")

if __name__ == "__main__":
    main()
