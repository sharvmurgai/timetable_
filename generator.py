import numpy as np
import random
#from constraints import classes, days, periods_jr_sr_kg, periods_grade_1, subjects, teachers, HOMEROOM, teacher_assignments, subject_constraints

# Define the dimensions for the tensor (1 week)
num_days = len(days)  # 5 days (Monday to Friday)
num_classes = len(classes)  # 12 classes

# Determine the number of periods per day based on class level
def periods_per_day(class_name):
    return periods_grade_1 if class_name.startswith('1') else periods_jr_sr_kg

# Initialize a 4D tensor with None as placeholder for each period
timetable = np.empty((num_days, max(periods_jr_sr_kg, periods_grade_1), num_classes), dtype=object)

# Helper function to get teacher for a specific subject and class
def get_teacher_for_subject(class_name, subject):
    for assignment in teacher_assignments:
        if assignment['subject'] == subject and assignment['class'] == class_name:
            return random.choice(assignment['teachers'])
    return None  # Return None if no teacher is found

# Allocate subjects for each class based on the subject constraints
for class_idx, class_name in enumerate(classes):
    class_level = '1' if class_name.startswith('1') else 'Jr. KG' if 'Jr. KG' in class_name else 'Sr. KG'
    total_periods = periods_per_day(class_name) * num_days

    # Create separate lists for 0.5 frequency and full frequency subjects
    half_period_subjects = []
    full_period_subjects = []

    # Build the subject list based on constraints
    for subject, levels in subject_constraints.items():
        if class_level in levels:
            frequency = levels[class_level]
            teacher = get_teacher_for_subject(class_name, subject)

            # Split full and 0.5 frequency subjects
            if frequency == 0.5:
                half_period_subjects.append((subject, teacher))
            else:
                full_period_subjects.extend([(subject, teacher)] * int(frequency))

    # Pair 0.5 frequency subjects with slashes
    half_period_pairs = []
    for i in range(0, len(half_period_subjects), 2):
        if i + 1 < len(half_period_subjects):
            subject_1, teacher_1 = half_period_subjects[i]
            subject_2, teacher_2 = half_period_subjects[i + 1]
            half_period_pairs.append((f"{subject_1} / {subject_2}", f"{teacher_1} / {teacher_2}"))
        else:
            half_period_pairs.append(half_period_subjects[i])  # Last unpaired subject, if odd

    # Combine full subjects and half-period pairs
    full_period_subjects.extend(half_period_pairs)
    random.shuffle(full_period_subjects)
    full_period_subjects = full_period_subjects[:total_periods]

    # Fill the timetable for each day and period
    period_counter = 0
    for day in range(num_days):
        for period in range(periods_per_day(class_name)):
            if period_counter < len(full_period_subjects):
                subject, teacher = full_period_subjects[period_counter]
                timetable[day, period, class_idx] = {'subject': subject, 'teacher': teacher}
                period_counter += 1
            else:
                timetable[day, period, class_idx] = 'Free'

# Function to print the generated timetable for a specific class
def print_timetable(class_name):
    class_idx = classes.index(class_name)
    print(f"\n--- Timetable for {class_name} ---")
    for day_idx, day in enumerate(days):
        print(f"{day}:")
        for period in range(periods_per_day(class_name)):
            entry = timetable[day_idx, period, class_idx]
            if entry and isinstance(entry, dict):
                subject = entry['subject']
                teacher = entry['teacher']
                print(f"    Period {period + 1}: {subject} by {teacher}")
            else:
                print(f"    Period {period + 1}: Free")
        print()  # Newline for better readability

# Display the timetable for all classes
if __name__ == "__main__":
    for class_name in classes:
        print_timetable(class_name)
