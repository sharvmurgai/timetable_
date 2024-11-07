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

# Initialize a 5D tensor with None as placeholder for each period
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
            
            # Split periods evenly or as close to even as possible between weeks
            if frequency % 2 == 0:
                week_frequency = frequency // 2
                subject_list.extend([(subject, teacher, 0)] * week_frequency)  # Assign for week 0
                subject_list.extend([(subject, teacher, 1)] * week_frequency)  # Assign for week 1
            else:
                week_0_freq = (frequency // 2) + 1
                week_1_freq = frequency // 2
                subject_list.extend([(subject, teacher, 0)] * week_0_freq)  # Assign majority to week 0
                subject_list.extend([(subject, teacher, 1)] * week_1_freq)  # Assign remainder to week 1

    # Shuffle the subject list to distribute randomly across periods
    random.shuffle(subject_list)
    subject_list = subject_list[:total_periods]  # Ensure we only have enough subjects for the schedule
    
    # Fill the timetable for each week and day
    period_counter = 0
    for week in range(weeks):
        week_schedule = [s for s in subject_list if s[2] == week]
        random.shuffle(week_schedule)  # Shuffle within each week for variety

        # Fill in periods for the week
        period_idx = 0
        for day in range(num_days):
            for period in range(periods_per_day(class_name)):
                if period_idx < len(week_schedule):
                    subject, teacher, _ = week_schedule[period_idx]
                    timetable[week, day, period, class_idx] = {'subject': subject, 'teacher': teacher}
                    period_idx += 1
                else:
                    # Attempt to allocate any free periods with subjects that have unmet constraints
                    remaining_subjects = [s for s in subject_list if s[2] == week]
                    if remaining_subjects:
                        subject, teacher, _ = random.choice(remaining_subjects)
                        timetable[week, day, period, class_idx] = {'subject': subject, 'teacher': teacher}

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
