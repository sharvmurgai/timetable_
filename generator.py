import numpy as np
import random
from constraints import classes, days, periods_jr_sr_kg, periods_grade_1, teacher_assignments, subject_constraints

# Define the dimensions for the tensor
weeks = 2
num_days = len(days)  # 5 days (Monday to Friday)
num_classes = len(classes)  # 12 classes

# Determine number of periods per day based on class level
def periods_per_day(class_name):
    return periods_grade_1 if class_name.startswith('1') else periods_jr_sr_kg

# Initialize a 5D tensor with None as a placeholder for each period
timetable = np.empty((weeks, num_days, max(periods_jr_sr_kg, periods_grade_1), num_classes), dtype=object)

# Helper function to get teacher for a specific subject and class
def get_teacher_for_subject(class_name, subject):
    for assignment in teacher_assignments:
        if assignment['subject'] == subject and assignment['class'] == class_name:
            return random.choice(assignment['teachers'])
    return None  # Return None if no teacher is found

# Allocate subjects for each class based on the subject constraints
for class_idx, class_name in enumerate(classes):
    # Determine class level (Jr. KG, Sr. KG, or Grade 1) for frequency lookup
    class_level = '1' if class_name.startswith('1') else 'Jr. KG' if 'Jr. KG' in class_name else 'Sr. KG'
    total_periods = periods_per_day(class_name) * num_days * weeks

    # Generate a list of subjects according to frequency requirements
    subject_list = []
    for subject, levels in subject_constraints.items():
        if class_level in levels:
            frequency = levels[class_level]
            teacher = get_teacher_for_subject(class_name, subject)

            # Split periods equally, or assign one extra to a random week if frequency is odd
            week_0_freq = (frequency // 2) + (frequency % 2 if random.choice([True, False]) else 0)
            week_1_freq = frequency - week_0_freq
            subject_list.extend([(subject, teacher, 0)] * week_0_freq)
            subject_list.extend([(subject, teacher, 1)] * week_1_freq)

    # Shuffle subject list for random distribution across periods
    random.shuffle(subject_list)

    # Fill timetable with constraints
    for week in range(weeks):
        week_schedule = [s for s in subject_list if s[2] == week]
        random.shuffle(week_schedule)

        # Day and period control to meet constraints on repetition
        day_schedule = {day: [] for day in range(num_days)}

        period_idx = 0
        for day in range(num_days):
            periods_in_day = periods_per_day(class_name)
            day_fill = 0

            while day_fill < periods_in_day:
                if period_idx >= len(week_schedule):
                    period_idx = 0
                    random.shuffle(week_schedule)

                subject, teacher, _ = week_schedule[period_idx]
                if (class_level == '1' and day_schedule[day].count(subject) < 2) or \
                   (class_level != '1' and day_schedule[day].count(subject) < 1):
                    timetable[week, day, day_fill, class_idx] = {'subject': subject, 'teacher': teacher}
                    day_schedule[day].append(subject)
                    day_fill += 1
                period_idx += 1

# Function to print the generated timetable for a specific class
def print_timetable(class_name):
    class_idx = classes.index(class_name)
    for week in range(weeks):
        print(f"\n--- {class_name} - Week {week + 1} ---")
        for day_idx, day in enumerate(days):
            print(f"{day}:")
            for period in range(periods_per_day(class_name)):
                entry = timetable[week, day_idx, period, class_idx]
                if entry:
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
