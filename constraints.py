# Class and period configuration
classes = [
    'Jr. KG A', 'Jr. KG B', 'Jr. KG C', 'Jr. KG D',
    'Sr. KG A', 'Sr. KG B', 'Sr. KG C', 'Sr. KG D',
    '1A', '1B', '1C', '1D'
]
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
periods_jr_sr_kg = 6  # Jr and Sr KG have 6 periods per day
periods_grade_1 = 10  # Grade 1 has 10 periods per day

# Subjects
subjects = [
    'English', 'Hindi', 'Marathi', 'Mathematics', 'EVS', 'Environmental Education',
    'Computer Studies', 'Physical Education', 'Circle Time', 'Life Skills',
    'Art', 'Clay Modeling', 'Music', 'Dance', 'DEED', 'Wonder Time',
    'Yoga', 'Karate', 'Assembly', 'Library', 'Role Play', 'Play Pen', 'Music T'
]

# Teachers list
teachers = [
    'Nupur FT', 'Pooja R', 'Maria', 'Banu', 'Shireen', 'Riya J', 'Sheetal', 'Anjum',
    'Ruksaar', 'Darshana', 'Bhakti', 'Laxmipriya', 'Shubha FT', 'Priyanka', 'Ankita', 'Jyoti V',
    'Remya', 'Saraswati -FT', 'Kanak', 'Matilda', 'Rishita', 'Shashwati', 'Charu', 'Maariyah',
    'Reshma', 'Dakshata', 'Santosh K', 'Pratibha', 'Sayantani', 'Trupti', 'Naval', 'Beena',
    'Priyanka A', 'Arjun', 'Vanita J', 'Zamora', 'Shridevi', 'Kiran', 'Sanjukta', 'Shlok',
    'Pooja B', 'Isha', 'Neesha.R', 'Shilpa.K', 'Shubhi', 'Priyanka.Saha', 'New Sports Tr', 'RAJU', 'Pankaj'
]

# Homeroom assignments for each class
HOMEROOM = {
    'Jr. KG A': 'Nupur FT', 'Jr. KG B': 'Maria', 'Jr. KG C': 'Shireen', 'Jr. KG D': 'Sheetal',
    'Sr. KG A': 'Ruksaar', 'Sr. KG B': 'Bhakti', 'Sr. KG C': 'Shubha FT', 'Sr. KG D': 'Ankita',
    '1A': 'Remya', '1B': 'Kanak', '1C': 'Rishita', '1D': 'Charu'
}

# Teacher assignments per subject and class
teacher_assignments = [
    # English Teachers
    {'subject': 'English', 'class': 'Jr. KG A', 'teachers': ['Nupur FT', 'Pooja R']},
    {'subject': 'English', 'class': 'Jr. KG B', 'teachers': ['Maria', 'Banu']},
    {'subject': 'English', 'class': 'Jr. KG C', 'teachers': ['Shireen', 'Riya J']},
    {'subject': 'English', 'class': 'Jr. KG D', 'teachers': ['Sheetal', 'Anjum']},
    {'subject': 'English', 'class': 'Sr. KG A', 'teachers': ['Ruksaar', 'Darshana']},
    {'subject': 'English', 'class': 'Sr. KG B', 'teachers': ['Bhakti', 'Laxmipriya']},
    {'subject': 'English', 'class': 'Sr. KG C', 'teachers': ['Shubha FT', 'Priyanka']},
    {'subject': 'English', 'class': 'Sr. KG D', 'teachers': ['Ankita', 'Jyoti V']},
    {'subject': 'English', 'class': '1A', 'teachers': ['Remya', 'Saraswati -FT']},
    {'subject': 'English', 'class': '1B', 'teachers': ['Kanak', 'Matilda']},
    {'subject': 'English', 'class': '1C', 'teachers': ['Rishita', 'Shashwati']},
    {'subject': 'English', 'class': '1D', 'teachers': ['Charu', 'Maariyah']},

    # Hindi Teachers (Homeroom)
    {'subject': 'Hindi', 'class': 'Jr. KG A', 'teachers': [HOMEROOM['Jr. KG A']]},
    {'subject': 'Hindi', 'class': 'Jr. KG B', 'teachers': [HOMEROOM['Jr. KG B']]},
    {'subject': 'Hindi', 'class': 'Jr. KG C', 'teachers': [HOMEROOM['Jr. KG C']]},
    {'subject': 'Hindi', 'class': 'Jr. KG D', 'teachers': [HOMEROOM['Jr. KG D']]},
    {'subject': 'Hindi', 'class': 'Sr. KG A', 'teachers': [HOMEROOM['Sr. KG A']]},
    {'subject': 'Hindi', 'class': 'Sr. KG B', 'teachers': [HOMEROOM['Sr. KG B']]},
    {'subject': 'Hindi', 'class': 'Sr. KG C', 'teachers': [HOMEROOM['Sr. KG C']]},
    {'subject': 'Hindi', 'class': 'Sr. KG D', 'teachers': [HOMEROOM['Sr. KG D']]},
    {'subject': 'Hindi', 'class': '1A', 'teachers': ['Reshma']},
    {'subject': 'Hindi', 'class': '1B', 'teachers': ['Reshma']},
    {'subject': 'Hindi', 'class': '1C', 'teachers': ['Santosh K']},
    {'subject': 'Hindi', 'class': '1D', 'teachers': ['Santosh K']},

    # Marathi Teachers (Homeroom)
    {'subject': 'Marathi', 'class': '1A', 'teachers': ['Reshma']},
    {'subject': 'Marathi', 'class': '1B', 'teachers': ['Reshma']},
    {'subject': 'Marathi', 'class': '1C', 'teachers': ['Santosh K']},
    {'subject': 'Marathi', 'class': '1D', 'teachers': ['Santosh K']},

    # Mathematics Teachers (Homeroom)
    {'subject': 'Mathematics', 'class': 'Jr. KG A', 'teachers': [HOMEROOM['Jr. KG A']]},
    {'subject': 'Mathematics', 'class': 'Jr. KG B', 'teachers': [HOMEROOM['Jr. KG B']]},
    {'subject': 'Mathematics', 'class': 'Jr. KG C', 'teachers': [HOMEROOM['Jr. KG C']]},
    {'subject': 'Mathematics', 'class': 'Jr. KG D', 'teachers': [HOMEROOM['Jr. KG D']]},
    {'subject': 'Mathematics', 'class': 'Sr. KG A', 'teachers': [HOMEROOM['Sr. KG A']]},
    {'subject': 'Mathematics', 'class': 'Sr. KG B', 'teachers': [HOMEROOM['Sr. KG B']]},
    {'subject': 'Mathematics', 'class': 'Sr. KG C', 'teachers': [HOMEROOM['Sr. KG C']]},
    {'subject': 'Mathematics', 'class': 'Sr. KG D', 'teachers': [HOMEROOM['Sr. KG D']]},
    {'subject': 'Mathematics', 'class': '1A', 'teachers': [HOMEROOM['1A']]},
    {'subject': 'Mathematics', 'class': '1B', 'teachers': [HOMEROOM['1B']]},
    {'subject': 'Mathematics', 'class': '1C', 'teachers': [HOMEROOM['1C']]},
    {'subject': 'Mathematics', 'class': '1D', 'teachers': [HOMEROOM['1D']]},

    # EVS Teachers (Homeroom)
    {'subject': 'EVS', 'class': 'Jr. KG A', 'teachers': [HOMEROOM['Jr. KG A']]},
    {'subject': 'EVS', 'class': 'Jr. KG B', 'teachers': [HOMEROOM['Jr. KG B']]},
    {'subject': 'EVS', 'class': 'Jr. KG C', 'teachers': [HOMEROOM['Jr. KG C']]},
    {'subject': 'EVS', 'class': 'Jr. KG D', 'teachers': [HOMEROOM['Jr. KG D']]},
    {'subject': 'EVS', 'class': 'Sr. KG A', 'teachers': [HOMEROOM['Sr. KG A']]},
    {'subject': 'EVS', 'class': 'Sr. KG B', 'teachers': [HOMEROOM['Sr. KG B']]},
    {'subject': 'EVS', 'class': 'Sr. KG C', 'teachers': [HOMEROOM['Sr. KG C']]},
    {'subject': 'EVS', 'class': 'Sr. KG D', 'teachers': [HOMEROOM['Sr. KG D']]},
    {'subject': 'EVS', 'class': '1A', 'teachers': ['Reshma']},
    {'subject': 'EVS', 'class': '1B', 'teachers': ['Reshma']},
    {'subject': 'EVS', 'class': '1C', 'teachers': ['Santosh K']},
    {'subject': 'EVS', 'class': '1D', 'teachers': ['Santosh K']},

    # Environmental Education Teachers (Homeroom)
    {'subject': 'Environmental Education', 'class': 'Jr. KG A', 'teachers': [HOMEROOM['Jr. KG A']]},
    {'subject': 'Environmental Education', 'class': 'Jr. KG B', 'teachers': [HOMEROOM['Jr. KG B']]},
    {'subject': 'Environmental Education', 'class': 'Jr. KG C', 'teachers': [HOMEROOM['Jr. KG C']]},
    {'subject': 'Environmental Education', 'class': 'Jr. KG D', 'teachers': [HOMEROOM['Jr. KG D']]},
    {'subject': 'Environmental Education', 'class': 'Sr. KG A', 'teachers': [HOMEROOM['Sr. KG A']]},
    {'subject': 'Environmental Education', 'class': 'Sr. KG B', 'teachers': [HOMEROOM['Sr. KG B']]},
    {'subject': 'Environmental Education', 'class': 'Sr. KG C', 'teachers': [HOMEROOM['Sr. KG C']]},
    {'subject': 'Environmental Education', 'class': 'Sr. KG D', 'teachers': [HOMEROOM['Sr. KG D']]},
    {'subject': 'Environmental Education', 'class': '1A', 'teachers': [HOMEROOM['1A']]},
    {'subject': 'Environmental Education', 'class': '1B', 'teachers': [HOMEROOM['1B']]},
    {'subject': 'Environmental Education', 'class': '1C', 'teachers': [HOMEROOM['1C']]},
    {'subject': 'Environmental Education', 'class': '1D', 'teachers': [HOMEROOM['1D']]},

    # Computer Studies Teachers
    {'subject': 'Computer Studies', 'class': 'Jr. KG A', 'teachers': ['Sayantani']},
    {'subject': 'Computer Studies', 'class': 'Jr. KG B', 'teachers': ['Sayantani']},
    {'subject': 'Computer Studies', 'class': 'Jr. KG C', 'teachers': ['Sayantani']},
    {'subject': 'Computer Studies', 'class': 'Jr. KG D', 'teachers': ['Sayantani']},
    {'subject': 'Computer Studies', 'class': 'Sr. KG A', 'teachers': ['Sayantani']},
    {'subject': 'Computer Studies', 'class': 'Sr. KG B', 'teachers': ['Sayantani']},
    {'subject': 'Computer Studies', 'class': 'Sr. KG C', 'teachers': ['Sayantani']},
    {'subject': 'Computer Studies', 'class': 'Sr. KG D', 'teachers': ['Sayantani']},
    {'subject': 'Computer Studies', 'class': '1A', 'teachers': ['Trupti']},
    {'subject': 'Computer Studies', 'class': '1B', 'teachers': ['Sayantani']},
    {'subject': 'Computer Studies', 'class': '1C', 'teachers': ['Sayantani']},
    {'subject': 'Computer Studies', 'class': '1D', 'teachers': ['Sayantani']},

    # Physical Education Teachers
    {'subject': 'Physical Education', 'class': 'Jr. KG A', 'teachers': ['Naval']},
    {'subject': 'Physical Education', 'class': 'Jr. KG B', 'teachers': ['Naval']},
    {'subject': 'Physical Education', 'class': 'Jr. KG C', 'teachers': ['Beena']},
    {'subject': 'Physical Education', 'class': 'Jr. KG D', 'teachers': ['Beena']},
    {'subject': 'Physical Education', 'class': 'Sr. KG A', 'teachers': ['Priyanka A']},
    {'subject': 'Physical Education', 'class': 'Sr. KG B', 'teachers': ['Priyanka A']},
    {'subject': 'Physical Education', 'class': 'Sr. KG C', 'teachers': ['New Sports Tr']},
    {'subject': 'Physical Education', 'class': 'Sr. KG D', 'teachers': ['New Sports Tr']},
    {'subject': 'Physical Education', 'class': '1A', 'teachers': ['Arjun']},
    {'subject': 'Physical Education', 'class': '1B', 'teachers': ['Arjun']},
    {'subject': 'Physical Education', 'class': '1C', 'teachers': ['Priyanka A']},
    {'subject': 'Physical Education', 'class': '1D', 'teachers': ['Naval']},

    # Circle Time Teachers (Homeroom)
    {'subject': 'Circle Time', 'class': 'Jr. KG A', 'teachers': [HOMEROOM['Jr. KG A']]},
    {'subject': 'Circle Time', 'class': 'Jr. KG B', 'teachers': [HOMEROOM['Jr. KG B']]},
    {'subject': 'Circle Time', 'class': 'Jr. KG C', 'teachers': [HOMEROOM['Jr. KG C']]},
    {'subject': 'Circle Time', 'class': 'Jr. KG D', 'teachers': [HOMEROOM['Jr. KG D']]},
    {'subject': 'Circle Time', 'class': 'Sr. KG A', 'teachers': [HOMEROOM['Sr. KG A']]},
    {'subject': 'Circle Time', 'class': 'Sr. KG B', 'teachers': [HOMEROOM['Sr. KG B']]},
    {'subject': 'Circle Time', 'class': 'Sr. KG C', 'teachers': [HOMEROOM['Sr. KG C']]},
    {'subject': 'Circle Time', 'class': 'Sr. KG D', 'teachers': [HOMEROOM['Sr. KG D']]},
    {'subject': 'Circle Time', 'class': '1A', 'teachers': [HOMEROOM['1A']]},
    {'subject': 'Circle Time', 'class': '1B', 'teachers': [HOMEROOM['1B']]},
    {'subject': 'Circle Time', 'class': '1C', 'teachers': [HOMEROOM['1C']]},
    {'subject': 'Circle Time', 'class': '1D', 'teachers': [HOMEROOM['1D']]},

    # Life Skills Teachers
    {'subject': 'Life Skills', 'class': 'Jr. KG A', 'teachers': ['Vanita J']},
    {'subject': 'Life Skills', 'class': 'Jr. KG B', 'teachers': ['Vanita J']},
    {'subject': 'Life Skills', 'class': 'Jr. KG C', 'teachers': ['Vanita J']},
    {'subject': 'Life Skills', 'class': 'Jr. KG D', 'teachers': ['Vanita J']},
    {'subject': 'Life Skills', 'class': 'Sr. KG A', 'teachers': ['Vanita J']},
    {'subject': 'Life Skills', 'class': 'Sr. KG B', 'teachers': ['Vanita J']},
    {'subject': 'Life Skills', 'class': 'Sr. KG C', 'teachers': ['Vanita J']},
    {'subject': 'Life Skills', 'class': 'Sr. KG D', 'teachers': ['Vanita J']},
    {'subject': 'Life Skills', 'class': '1A', 'teachers': ['Zamora']},
    {'subject': 'Life Skills', 'class': '1B', 'teachers': ['Zamora']},
    {'subject': 'Life Skills', 'class': '1C', 'teachers': ['Zamora']},
    {'subject': 'Life Skills', 'class': '1D', 'teachers': ['Zamora']},

    # Art Teachers (Homeroom for KG classes, specific teachers for Grade 1)
    {'subject': 'Art', 'class': 'Jr. KG A', 'teachers': [HOMEROOM['Jr. KG A']]},
    {'subject': 'Art', 'class': 'Jr. KG B', 'teachers': [HOMEROOM['Jr. KG B']]},
    {'subject': 'Art', 'class': 'Jr. KG C', 'teachers': [HOMEROOM['Jr. KG C']]},
    {'subject': 'Art', 'class': 'Jr. KG D', 'teachers': [HOMEROOM['Jr. KG D']]},
    {'subject': 'Art', 'class': 'Sr. KG A', 'teachers': [HOMEROOM['Sr. KG A']]},
    {'subject': 'Art', 'class': 'Sr. KG B', 'teachers': [HOMEROOM['Sr. KG B']]},
    {'subject': 'Art', 'class': 'Sr. KG C', 'teachers': [HOMEROOM['Sr. KG C']]},
    {'subject': 'Art', 'class': 'Sr. KG D', 'teachers': [HOMEROOM['Sr. KG D']]},
    {'subject': 'Art', 'class': '1A', 'teachers': ['Pankaj']},
    {'subject': 'Art', 'class': '1B', 'teachers': ['Shridevi']},
    {'subject': 'Art', 'class': '1C', 'teachers': ['Shridevi']},
    {'subject': 'Art', 'class': '1D', 'teachers': ['Kiran']},

    # Clay Modeling Teachers
    {'subject': 'Clay Modeling', 'class': 'Jr. KG A', 'teachers': ['Shridevi']},
    {'subject': 'Clay Modeling', 'class': 'Jr. KG B', 'teachers': ['Shridevi']},
    {'subject': 'Clay Modeling', 'class': 'Jr. KG C', 'teachers': ['Shridevi']},
    {'subject': 'Clay Modeling', 'class': 'Jr. KG D', 'teachers': ['Shridevi']},
    {'subject': 'Clay Modeling', 'class': 'Sr. KG A', 'teachers': ['Shridevi']},
    {'subject': 'Clay Modeling', 'class': 'Sr. KG B', 'teachers': ['Shridevi']},
    {'subject': 'Clay Modeling', 'class': 'Sr. KG C', 'teachers': ['Shridevi']},
    {'subject': 'Clay Modeling', 'class': 'Sr. KG D', 'teachers': ['Shridevi']},
    {'subject': 'Clay Modeling', 'class': '1A', 'teachers': ['Pankaj']},
    {'subject': 'Clay Modeling', 'class': '1B', 'teachers': ['Pankaj']},
    {'subject': 'Clay Modeling', 'class': '1C', 'teachers': ['Shridevi']},
    {'subject': 'Clay Modeling', 'class': '1D', 'teachers': ['Kiran']},

    # Music Teachers
    {'subject': 'Music', 'class': 'Jr. KG A', 'teachers': ['Sanjukta']},
    {'subject': 'Music', 'class': 'Jr. KG B', 'teachers': ['Sanjukta']},
    {'subject': 'Music', 'class': 'Jr. KG C', 'teachers': ['Shlok']},
    {'subject': 'Music', 'class': 'Jr. KG D', 'teachers': ['Shlok']},
    {'subject': 'Music', 'class': 'Sr. KG A', 'teachers': ['Sanjukta']},
    {'subject': 'Music', 'class': 'Sr. KG B', 'teachers': ['Sanjukta']},
    {'subject': 'Music', 'class': 'Sr. KG C', 'teachers': ['Shlok']},
    {'subject': 'Music', 'class': 'Sr. KG D', 'teachers': ['Shlok']},
    {'subject': 'Music', 'class': '1A', 'teachers': ['Sanjukta']},
    {'subject': 'Music', 'class': '1B', 'teachers': ['Sanjukta']},
    {'subject': 'Music', 'class': '1C', 'teachers': ['Shlok']},
    {'subject': 'Music', 'class': '1D', 'teachers': ['Shlok']},

    # Dance Teachers
    {'subject': 'Dance', 'class': 'Jr. KG A', 'teachers': ['Pooja B']},
    {'subject': 'Dance', 'class': 'Jr. KG B', 'teachers': ['Pooja B']},
    {'subject': 'Dance', 'class': 'Jr. KG C', 'teachers': ['Pooja B']},
    {'subject': 'Dance', 'class': 'Jr. KG D', 'teachers': ['Pooja B']},
    {'subject': 'Dance', 'class': 'Sr. KG A', 'teachers': ['Pooja B']},
    {'subject': 'Dance', 'class': 'Sr. KG B', 'teachers': ['Pooja B']},
    {'subject': 'Dance', 'class': 'Sr. KG C', 'teachers': ['Pooja B']},
    {'subject': 'Dance', 'class': 'Sr. KG D', 'teachers': ['Pooja B']},
    {'subject': 'Dance', 'class': '1A', 'teachers': ['Pooja B']},
    {'subject': 'Dance', 'class': '1B', 'teachers': ['Pooja B']},
    {'subject': 'Dance', 'class': '1C', 'teachers': ['Pooja B']},
    {'subject': 'Dance', 'class': '1D', 'teachers': ['Pooja B']},

    # DEED Teachers
    {'subject': 'DEED', 'class': 'Jr. KG A', 'teachers': ['Isha']},
    {'subject': 'DEED', 'class': 'Jr. KG B', 'teachers': ['Isha']},
    {'subject': 'DEED', 'class': 'Jr. KG C', 'teachers': ['Isha']},
    {'subject': 'DEED', 'class': 'Jr. KG D', 'teachers': ['Isha']},
    {'subject': 'DEED', 'class': 'Sr. KG A', 'teachers': ['Isha']},
    {'subject': 'DEED', 'class': 'Sr. KG B', 'teachers': ['Isha']},
    {'subject': 'DEED', 'class': 'Sr. KG C', 'teachers': ['Isha']},
    {'subject': 'DEED', 'class': 'Sr. KG D', 'teachers': ['Isha']},
    {'subject': 'DEED', 'class': '1A', 'teachers': ['Isha']},
    {'subject': 'DEED', 'class': '1B', 'teachers': ['Isha']},
    {'subject': 'DEED', 'class': '1C', 'teachers': ['Isha']},
    {'subject': 'DEED', 'class': '1D', 'teachers': ['Isha']},

    # Wonder Time Teachers
    {'subject': 'Wonder Time', 'class': 'Jr. KG A', 'teachers': ['Neesha R']},
    {'subject': 'Wonder Time', 'class': 'Jr. KG B', 'teachers': ['Neesha R']},
    {'subject': 'Wonder Time', 'class': 'Jr. KG C', 'teachers': ['Neesha R']},
    {'subject': 'Wonder Time', 'class': 'Jr. KG D', 'teachers': ['Neesha R']},
    {'subject': 'Wonder Time', 'class': 'Sr. KG A', 'teachers': ['Neesha R']},
    {'subject': 'Wonder Time', 'class': 'Sr. KG B', 'teachers': ['Neesha R']},
    {'subject': 'Wonder Time', 'class': 'Sr. KG C', 'teachers': ['Neesha R']},
    {'subject': 'Wonder Time', 'class': 'Sr. KG D', 'teachers': ['Neesha R']},
    {'subject': 'Wonder Time', 'class': '1A', 'teachers': ['Shilpa K']},
    {'subject': 'Wonder Time', 'class': '1B', 'teachers': ['New Sports Tr']},
    {'subject': 'Wonder Time', 'class': '1C', 'teachers': ['Shubhi']},
    {'subject': 'Wonder Time', 'class': '1D', 'teachers': ['Priyanka Saha']},

    # Yoga Teachers
    {'subject': 'Yoga', 'class': 'Jr. KG A', 'teachers': ['New Sports Tr']},
    {'subject': 'Yoga', 'class': 'Jr. KG B', 'teachers': ['New Sports Tr']},
    {'subject': 'Yoga', 'class': 'Jr. KG C', 'teachers': ['New Sports Tr']},
    {'subject': 'Yoga', 'class': 'Jr. KG D', 'teachers': ['New Sports Tr']},
    {'subject': 'Yoga', 'class': 'Sr. KG A', 'teachers': ['New Sports Tr']},
    {'subject': 'Yoga', 'class': 'Sr. KG B', 'teachers': ['New Sports Tr']},
    {'subject': 'Yoga', 'class': 'Sr. KG C', 'teachers': ['New Sports Tr']},
    {'subject': 'Yoga', 'class': 'Sr. KG D', 'teachers': ['New Sports Tr']},
    {'subject': 'Yoga', 'class': '1A', 'teachers': ['New Sports Tr']},
    {'subject': 'Yoga', 'class': '1B', 'teachers': ['New Sports Tr']},
    {'subject': 'Yoga', 'class': '1C', 'teachers': ['New Sports Tr']},
    {'subject': 'Yoga', 'class': '1D', 'teachers': ['New Sports Tr']},

    # Karate Teachers
    {'subject': 'Karate', 'class': '1A', 'teachers': ['RAJU']},
    {'subject': 'Karate', 'class': '1B', 'teachers': ['RAJU']},
    {'subject': 'Karate', 'class': '1C', 'teachers': ['RAJU']},
    {'subject': 'Karate', 'class': '1D', 'teachers': ['RAJU']}, 
    
    # Assembly
    {'subject': 'Assembly', 'class': 'Jr. KG A', 'teachers': [HOMEROOM['Jr. KG A']]},
    {'subject': 'Assembly', 'class': 'Jr. KG B', 'teachers': [HOMEROOM['Jr. KG B']]},
    {'subject': 'Assembly', 'class': 'Jr. KG C', 'teachers': [HOMEROOM['Jr. KG C']]},
    {'subject': 'Assembly', 'class': 'Jr. KG D', 'teachers': [HOMEROOM['Jr. KG D']]},
    {'subject': 'Assembly', 'class': 'Sr. KG A', 'teachers': [HOMEROOM['Sr. KG A']]},
    {'subject': 'Assembly', 'class': 'Sr. KG B', 'teachers': [HOMEROOM['Sr. KG B']]},
    {'subject': 'Assembly', 'class': 'Sr. KG C', 'teachers': [HOMEROOM['Sr. KG C']]},
    {'subject': 'Assembly', 'class': 'Sr. KG D', 'teachers': [HOMEROOM['Sr. KG D']]},
    {'subject': 'Assembly', 'class': '1A', 'teachers': [HOMEROOM['1A']]},
    {'subject': 'Assembly', 'class': '1B', 'teachers': [HOMEROOM['1B']]},
    {'subject': 'Assembly', 'class': '1C', 'teachers': [HOMEROOM['1C']]},
    {'subject': 'Assembly', 'class': '1D', 'teachers': [HOMEROOM['1D']]},
]

teacher_assignments.extend([
    {'subject': 'Library', 'class': 'Jr. KG A', 'teachers': ['Pooja S']},
    {'subject': 'Library', 'class': 'Jr. KG B', 'teachers': ['Pooja S']},
    {'subject': 'Library', 'class': 'Jr. KG C', 'teachers': ['Pooja S']},
    {'subject': 'Library', 'class': 'Jr. KG D', 'teachers': ['Pooja S']},
    {'subject': 'Library', 'class': 'Sr. KG A', 'teachers': ['Pooja S']},
    {'subject': 'Library', 'class': 'Sr. KG B', 'teachers': ['Pooja S']},
    {'subject': 'Library', 'class': 'Sr. KG C', 'teachers': ['Pooja S']},
    {'subject': 'Library', 'class': 'Sr. KG D', 'teachers': ['Pooja S']},
    {'subject': 'Library', 'class': '1A', 'teachers': ['Pooja S']},
    {'subject': 'Library', 'class': '1B', 'teachers': ['Pooja S']},
    {'subject': 'Library', 'class': '1C', 'teachers': ['Pooja S']},
    {'subject': 'Library', 'class': '1D', 'teachers': ['Pooja S']}
])

# Role Play (assigned to Homeroom teachers)
teacher_assignments.extend([
    {'subject': 'Role Play', 'class': 'Jr. KG A', 'teachers': [HOMEROOM['Jr. KG A']]},
    {'subject': 'Role Play', 'class': 'Jr. KG B', 'teachers': [HOMEROOM['Jr. KG B']]},
    {'subject': 'Role Play', 'class': 'Jr. KG C', 'teachers': [HOMEROOM['Jr. KG C']]},
    {'subject': 'Role Play', 'class': 'Jr. KG D', 'teachers': [HOMEROOM['Jr. KG D']]},
    {'subject': 'Role Play', 'class': 'Sr. KG A', 'teachers': [HOMEROOM['Sr. KG A']]},
    {'subject': 'Role Play', 'class': 'Sr. KG B', 'teachers': [HOMEROOM['Sr. KG B']]},
    {'subject': 'Role Play', 'class': 'Sr. KG C', 'teachers': [HOMEROOM['Sr. KG C']]},
    {'subject': 'Role Play', 'class': 'Sr. KG D', 'teachers': [HOMEROOM['Sr. KG D']]},
    {'subject': 'Role Play', 'class': '1A', 'teachers': [HOMEROOM['1A']]},
    {'subject': 'Role Play', 'class': '1B', 'teachers': [HOMEROOM['1B']]},
    {'subject': 'Role Play', 'class': '1C', 'teachers': [HOMEROOM['1C']]},
    {'subject': 'Role Play', 'class': '1D', 'teachers': [HOMEROOM['1D']]}
])

# Play Pen (assigned to Homeroom teachers)
teacher_assignments.extend([
    {'subject': 'Play Pen', 'class': 'Jr. KG A', 'teachers': [HOMEROOM['Jr. KG A']]},
    {'subject': 'Play Pen', 'class': 'Jr. KG B', 'teachers': [HOMEROOM['Jr. KG B']]},
    {'subject': 'Play Pen', 'class': 'Jr. KG C', 'teachers': [HOMEROOM['Jr. KG C']]},
    {'subject': 'Play Pen', 'class': 'Jr. KG D', 'teachers': [HOMEROOM['Jr. KG D']]},
    {'subject': 'Play Pen', 'class': 'Sr. KG A', 'teachers': [HOMEROOM['Sr. KG A']]},
    {'subject': 'Play Pen', 'class': 'Sr. KG B', 'teachers': [HOMEROOM['Sr. KG B']]},
    {'subject': 'Play Pen', 'class': 'Sr. KG C', 'teachers': [HOMEROOM['Sr. KG C']]},
    {'subject': 'Play Pen', 'class': 'Sr. KG D', 'teachers': [HOMEROOM['Sr. KG D']]},
    {'subject': 'Play Pen', 'class': '1A', 'teachers': [HOMEROOM['1A']]},
    {'subject': 'Play Pen', 'class': '1B', 'teachers': [HOMEROOM['1B']]},
    {'subject': 'Play Pen', 'class': '1C', 'teachers': [HOMEROOM['1C']]},
    {'subject': 'Play Pen', 'class': '1D', 'teachers': [HOMEROOM['1D']]}
])

# Adding SGI and Class Tests for Grade 1 with homeroom (HR) teachers
teacher_assignments.extend([
    # SGI - Self-Guided Instruction
    {'subject': 'SGI', 'class': '1A', 'teachers': [HOMEROOM['1A']]},
    {'subject': 'SGI', 'class': '1B', 'teachers': [HOMEROOM['1B']]},
    {'subject': 'SGI', 'class': '1C', 'teachers': [HOMEROOM['1C']]},
    {'subject': 'SGI', 'class': '1D', 'teachers': [HOMEROOM['1D']]}
])

teacher_assignments.extend([
    # Class Tests
    {'subject': 'Class Tests', 'class': '1A', 'teachers': [HOMEROOM['1A']]},
    {'subject': 'Class Tests', 'class': '1B', 'teachers': [HOMEROOM['1B']]},
    {'subject': 'Class Tests', 'class': '1C', 'teachers': [HOMEROOM['1C']]},
    {'subject': 'Class Tests', 'class': '1D', 'teachers': [HOMEROOM['1D']]}
])


teacher_assignments.extend([
    # Music T
    {'subject': 'Music T', 'class': '1A', 'teachers': ['Sanjukta']},
    {'subject': 'Music T', 'class': '1B', 'teachers': ['Sanjukta']},
    {'subject': 'Music T', 'class': '1C', 'teachers': ['Shlok']},
    {'subject': 'Music T', 'class': '1D', 'teachers': ['Shlok']},
])


# Subject constraints (two-week schedule, doubling weekly values)
subject_constraints = {
    'English': {'Jr. KG': 10, 'Sr. KG': 10, '1': 16},
    'Hindi': {'Jr. KG': 8, 'Sr. KG': 8, '1': 12},
    'Marathi': {'1': 4},
    'Mathematics': {'Jr. KG': 8, 'Sr. KG': 9, '1': 14},
    'EVS': {'Jr. KG': 4, 'Sr. KG': 6, '1': 10},
    'Environmental Education': {'Jr. KG': 4, 'Sr. KG': 2, '1': 2},
    'Computer Studies': {'Jr. KG': 1, 'Sr. KG': 1, '1': 4},
    'Physical Education': {'Jr. KG': 4, 'Sr. KG': 4, '1': 4},
    'Circle Time': {'Jr. KG': 1, 'Sr. KG': 1, '1': 2},
    'Life Skills': {'Jr. KG': 1, 'Sr. KG': 1, '1': 2},
    'Art': {'Jr. KG': 4, 'Sr. KG': 4, '1': 4},
    'Clay Modeling': {'Jr. KG': 2, 'Sr. KG': 2, '1': 2},
    'Music': {'Jr. KG': 2, 'Sr. KG': 2, '1': 2},
    'Music T': {'1': 2},
    'Dance': {'Jr. KG': 2, 'Sr. KG': 2, '1': 2},
    'DEED': {'Jr. KG': 2, 'Sr. KG': 1, '1': 2},
    'Wonder Time': {'Jr. KG': 2, 'Sr. KG': 2, '1': 2},
    'Yoga': {'Jr. KG': 1, 'Sr. KG': 1, '1': 2},
    'Karate': {'1': 2},
    'Assembly': {'Jr. KG': 2, 'Sr. KG': 1, '1': 2},
    'Library': {'Jr. KG': 1, 'Sr. KG': 2, '1': 2},
    'Role Play': {'Jr. KG': 1},
    'Play Pen': {'Jr. KG': 1, 'Sr. KG': 1},
    'SGI': {'1': 4},
    'CLASS TESTS': {'1': 2}
}
