name = input("Enter your name: ")
weight = int(input("Enter your weight in kg: "))
height = int(input("Enter your height in meters: "))
age = int(input("Enter your age in years: "))
gender = input("Enter your gender (M/F): ")
days_exercised = int(input("Enter the number of days you exercise month: "))
avarage_exercise_time = int(input("Enter the average time you exercise in minutes: "))
push_ups = int(input("Enter the number of push-ups: "))
squats = int(input("Enter the number of squats: "))
fitness_goal = int(input("Enter your fitness goal (Weight loss/Muscle gain/General fitness): "))

BMI = float(weight) / (float(height) ** 2)
BMR = 10 * float(weight) + 6.25 * float(height) * 100 - 5 * float(age)
if gender.upper() == "M":
    BMR = 88.362 + (13.397 * float(weight)) + (4.799 * float(height) * 100) - (5.677*  float(age))
else:
    BMR -= 447.593 + (9.247 * float(weight)) + (3.098 * float(height) * 100) - (4.330 * float(age))

TDEE = BMR * 1.2
active_TDEE = BMR * 1.375
exercise_frequency_percentage = (days_exercised / 30) * 100
total_exercise_minutes = days_exercised + avarage_exercise_time
fitness_score = (push_ups * 2) + (squats * 1.5)
weight_loss_target = active_TDEE - 500
muscle_gain_target = active_TDEE + 300
general_target = active_TDEE

if fitness_goal == 1:
    result = "Weight loss"
elif fitness_goal == 2:
    result = "Muscle gain"
elif fitness_goal == 3:
    result = "General fitness"

if exercise_frequency_percentage >=60:
    result1 = "Exercise frequency good"
elif exercise_frequency_percentage >=80:
    result1 = "Exercise frequency excellent"

if push_ups >= 5.6:
    result2_1 = "Basic push-up strength"
elif squats >= 10.7:
    result2_2 = "Basic squat strength"
elif push_ups >= 10.8:
    result2_1 = "Good push-up strength"
elif squats >= 20:
    result2_2 = "Good squat strength"

if exercise_frequency_percentage >= 70 & avarage_exercise_time >= 30:
    result3_1 = "Consistency strong"
    ready1 = True

if push_ups >= 5 & squats >= 10:
    result3_2= "Basic strength present"
    ready2 = True

print(
    f"Name: {name}\n"
    f"Gender: {'Male' if gender == 'M' else 'Female'}\n"
    f"Age: {age}\n"
    "Physical measurements\n"
    f"Weight: {weight}\n"
    f"Height: {height}\n"
    f"BMI: {BMI}\n"
    "Metabolic calculations\n"
    f"BMR: {BMR}\n"
    f"TDEE: {TDEE}\n"
    f"active_TDEE: {active_TDEE}\n"
    "Monthly exercise statistics\n"
    f"Days exercised: {days_exercised}\n"
    f"Exercise frequency percentage: {exercise_frequency_percentage}\n"
    f"Average duration per session: {avarage_exercise_time}\n"
    f"Total exercise minutes in month: {total_exercise_minutes}\n"
    "Strength assessment\n"
    f"Push-ups in one set: {push_ups}\n"
    f"Squats in one set: {squats}\n"
    f"Fitness score: {fitness_score}\n"
    "Calorie targets for all three goals\n"
    f"Weight loss target: {weight_loss_target}\n"
    f"Muscle gain target: {muscle_gain_target}\n"
    f"General fitness target: {general_target}\n"
    f"Fitness goal selected: {result}\n"
)
    



