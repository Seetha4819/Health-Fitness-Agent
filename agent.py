def calculate_bmi(weight, height):
    height_m = height / 100
    return round(weight / (height_m ** 2), 2)

def fitness_agent(age, weight, height, goal):
    bmi = calculate_bmi(weight, height)

    if bmi < 18.5:
        plan = "Gain Weight"
        calories = 2500
        exercises = ["Push-ups", "Squats", "Protein-rich meals"]
        tips = ["Eat more calories than you burn.", "Include nuts, milk, eggs."]
    elif 18.5 <= bmi <= 24.9:
        plan = "Maintain"
        calories = 2200
        exercises = ["Yoga", "Walking 30 min", "Cycling 15 min"]
        tips = ["Maintain balance between diet and exercise."]
    else:
        plan = "Lose Weight"
        calories = 1800
        exercises = ["Jogging 30 min", "Skipping", "HIIT workout"]
        tips = ["Avoid sugar, fried foods, and increase cardio."]

    return {
        "bmi": bmi,
        "plan": plan,
        "calories": calories,
        "exercises": exercises,
        "tips": tips
    }
