# bmi_module.py

def calculate_bmi(weight_kg, height_m):
    """
    Calculate the Body Mass Index (BMI) given weight in kilograms and height in meters.
    Formula: BMI = weight (kg) / (height (m) ** 2)
    """
    if height_m <= 0:
        raise ValueError("Height should be a positive value in meters.")
    
    return weight_kg / (height_m ** 2)

def interpret_bmi(bmi_value):
    """
    Interpret the BMI value and provide a health category.
    """
    if bmi_value < 16:
        return "Severely underweight"
    elif 16 <= bmi_value < 16.9:
        return "Underweight"
    elif 17 <= bmi_value < 18.4:
        return "Mildly underweight"
    elif 18.5 <= bmi_value < 24.9:
        return "Normal weight"
    elif 25 <= bmi_value < 29.9:
        return "Overweight"
    elif 30 <= bmi_value < 34.9:
        return "Obesity Class I (Moderate)"
    elif 35 <= bmi_value < 39.9:
        return "Obesity Class II (Severe)"
    else:
        return "Obesity Class III (Very severe or morbidly obese)"

