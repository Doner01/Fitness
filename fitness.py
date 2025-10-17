name = input("Enter your name: ")
weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))
age = int(input("Enter your age (years): "))
gender = input("Enter your gender (M/F): ").upper()
days_exercised = int(input("Days exercised in past 30 days: "))
avg_duration = float(input("Average exercise duration per session (minutes): "))
push_ups = int(input("Push-ups in one set: "))
squats = int(input("Squats in one set: "))
goal = int(input("Fitness goal (1=Weight loss, 2=Muscle gain, 3=General fitness): "))

is_male = (gender == "M")
is_female = (gender == "F")

bmi = weight / (height ** 2)

BMR = (
    (is_male)   * (88.362 + (13.397 * weight) + (4.799 * height * 100) - (5.677 * age))
    + (is_female) * (447.593 + (9.247 * weight) + (3.098 * height * 100) - (4.330 * age))
)

sedentary_TDEE = BMR * 1.2
active_TDEE = BMR * 1.375

exercise_frequency = (days_exercised / 30) * 100
total_exercise_minutes = days_exercised * avg_duration

fitness_score = (push_ups * 2) + (squats * 1.5)

weight_loss_target = active_TDEE - 500
muscle_gain_target = active_TDEE + 300
maintenance_target = active_TDEE

calorie_target = (
    (goal == 1) * weight_loss_target +
    (goal == 2) * muscle_gain_target +
    (goal == 3) * maintenance_target
)

bmi_reasonable = 18.5 <= bmi < 30
exercise_freq_good = exercise_frequency >= 60
exercise_freq_excellent = exercise_frequency >= 80
exercise_duration_adequate = avg_duration >= 30

basic_pushup_strength = push_ups >= 5
basic_squat_strength = squats >= 10
good_pushup_strength = push_ups >= 10
good_squat_strength = squats >= 20

consistency_strong = exercise_frequency >= 70 and avg_duration >= 30
basic_strength_present = push_ups >= 5 and squats >= 10
ready_for_progression = consistency_strong and basic_strength_present

print("\n--- BEGINNER FITNESS PROFILE ---")
print(f"Name: {name}")
print(f"Gender: {gender}")
print(f"Age: {age}")

print("\n--- Physical Measurements ---")
print(f"Weight: {weight} kg")
print(f"Height: {height} m")
print(f"BMI: {bmi:.2f}")

print("\n--- Metabolic Calculations ---")
print(f"BMR: {BMR:.2f}")
print(f"Sedentary TDEE: {sedentary_TDEE:.2f}")
print(f"Active TDEE: {active_TDEE:.2f}")

print("\n--- Monthly Exercise Statistics ---")
print(f"Days exercised (out of 30): {days_exercised}")
print(f"Exercise frequency: {exercise_frequency:.1f}%")
print(f"Average duration per session: {avg_duration} min")
print(f"Total exercise minutes in month: {total_exercise_minutes} min")

print("\n--- Strength Assessment ---")
print(f"Push-ups in one set: {push_ups}")
print(f"Squats in one set: {squats}")
print(f"Fitness score: {fitness_score:.1f}")

print("\n--- Calorie Targets ---")
print(f"Weight Loss Target: {weight_loss_target}")
print(f"Muscle Gain Target: {muscle_gain_target}")
print(f"General Fitness Target: {maintenance_target}")
print(f"Selected Goal: {goal} → Target: {calorie_target}")

print("\n--- Progress Indicators ---")
print(f"1. BMI in reasonable range: {bmi_reasonable}")
print(f"2. Exercise frequency good: {exercise_freq_good}")
print(f"3. Exercise frequency excellent: {exercise_freq_excellent}")
print(f"4. Exercise duration adequate: {exercise_duration_adequate}")
print(f"5. Basic push-up strength: {basic_pushup_strength}")
print(f"6. Basic squat strength: {basic_squat_strength}")
print(f"7. Good push-up strength: {good_pushup_strength}")
print(f"8. Good squat strength: {good_squat_strength}")
print(f"9. Consistency strong: {consistency_strong}")
print(f"10. Basic strength present: {basic_strength_present}")
print(f"11. Ready for progression: {ready_for_progression}")

# Please I tried my best I don't know if there any way😥(if is best option for this)
