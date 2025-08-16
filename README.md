# Timetable-Generator
College timetable generator using genetic algorithm in django

Timetable Generation System leveraging a Backtracking Algorithm  to automate scheduling while ensuring efficiency, fairness, and compliance with institutional constraints. The system dynamically allocates subjects and practical sessions while preventing conflicts, optimizing faculty workload, and improving student experience.

**Key Features, Constraints & Problem Solving:**
1. Automated Scheduling – Eliminates manual errors and inefficiencies in timetable creation.
2. Quick Generation -Generates timetable in seconds based on given input subjects and corresponding faculty.
3. Constraint Handling:– Adheres to strict academic rules, including: 
 - No overlapping subjects in an hour; maintain frequency of each subject per week
 - Practical sessions spanning continuous 2-hour slots per batch.
 - Each practical session appears once per day per batch.
 - Two well-defined break periods.
4. Optimized Faculty Workload – Distributes lectures fairly among teachers.
5. Scalable & Adaptable – Customized as per academic requirements. New faculties and subjects can be added.
6. Security- Secured access available to admin using Django framework.
7. UI/UX- User friendly , dynamic content rendering .
8. CAN MAKE TIMETABLE FOR 2 CLASSES AT A TIME SHARING SAME TEACHERS AND SUBJECTS.

**DIRECTIONS**
Install django, set it up ; extract all files from zip;run the following on terminal:  
cd mywebsite\mywebsite

python manage.py runserver 8000

then Visit: http://127.0.0.1:8000/
