# task-2

def calculate_bmi(weight_kg, height_m):
    bmi = weight_kg / (height_m ** 2)
    return bmi

weight_kg = 70.0  # Example weight in kg
height_m = 1.8  # Example height in m
bmi = calculate_bmi(weight_kg, height_m)
print("BMI:", bmi)