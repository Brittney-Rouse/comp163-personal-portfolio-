import math
from collections import namedtuple

#Personal Information Storage (strings)
full_name = "Brittney Rouse"
student_email = "barouse1@ncat.edu"
hometown = "Greensboro, NC"
graduation_semester = "Spring 2029"
major = "Computer Science"

#Academic Data Organization (lists)
current_courses_list = ["COMP 163", "MATH 150", "ENG 101", "HIS 105"]
completed_courses_list = ["Biology", "Chemistry", "Calculus", "Spanish II", "World History"]
credit_hours_list = [3, 3, 3, 3]
GPA_history_list = [3.2, 3.6, 3.4, 3.7]

#Contact Information Storage (tuples)
emergency_contact = ("Mom", "Hannah Smith", "704-555-0199")
home_address = ("456 Oak Street", "Charlotte, NC", "28202")
instagram_info = ("Instagram", "@jordan_codes", 312)
twitter_info = ("Twitter", "@jordandev", 127)
birthday = ("Birthday", "5", "22", "2006")

#Interest Tracking (sets)
current_skills = {"Python basics", "HTML", "Problem solving", "Time management", "Photography"}
skills_to_learn = {"JavaScript", "Data structures", "Git", "Web design", "Public speaking"}
career_interests = {"Software development", "Web development", "Data science", "Game development"}
hobbies = {"Gaming", "Photography", "Reading", "Soccer", "Music"}
entertainment_backlog = {"One Piece", "Barry", "Life", "Incantation", "Memento"}

#Organizational Mapping (dictionaries)
course_credits = {"COMP 163": 3, "MATH 150": 3, "ENG 101": 3, "HIS 105": 3}
course_professors = {"COMP 163": "Prof. Rhodes", "MATH 150": "Dr. Lee", "ENG 101": "Dr. Martinez", "HIS 105": "Dr. Brown"}
course_rooms = {"COMP 163": "M-Eric 300", "MATH 150": "Marteena 201", "ENG 101": "Crosby 121", "HIS 105": "Crosby 210"}
monthly_budget = {"Food": 450, "Entertainment": 200, "Books": 125, "Transportation": 100}
study_hours_per_subject = {"Programming": 10, "Math": 8, "English": 4, "History": 3}
contact_directory = {"Mom": "704-555-0199", "Roommate": "336-555-7821", "Academic Advisor": "336-334-5000"}

#Required Calculations (using data structures)
#a. Total current credits from credit hours lists
total_credit_hours = sum(credit_hours_list)
#b. Cumulative GPA from GPA history list 
cumulative_GPA = sum(GPA_history_list) / 4
#c. Count of completed courses 
count_of_completed_courses = len(completed_courses_list)
#d. Total weekly study hours from study hours dictionary 
total_weekly_study_hours = study_hours_per_subject["Programming"] + study_hours_per_subject["Math"] + study_hours_per_subject["English"] + study_hours_per_subject["History"]
#e. Academic load (credits + study hours combined)
credits = course_credits["COMP 163"] + course_credits["MATH 150"] + course_credits["ENG 101"] + course_credits["HIS 105"]
academic_load = credits + total_weekly_study_hours
#f. Monthly budget total from all categories 
monthly_budget_total = monthly_budget["Food"] + monthly_budget["Entertainment"] + monthly_budget["Books"] + monthly_budget["Transportation"]
#g. Daily food budget (food amount ÷ 30, rounded to 2 decimals) 
daily_food_budget = round(monthly_budget["Food"] / 30)
#h. Annual budget projection (monthly total × 12) 
annual_budget_projection = monthly_budget_total * 12
#i. Study cost per hour (books budget ÷ total study hours, rounded to 2 decimals)
study_cost_per_hours = round((monthly_budget["Books"] / total_weekly_study_hours), 2)

#Analytics Calculations
#a. Total social media followers from platform tuples 
total_social_media_followers = (instagram_info[2] + twitter_info[2])
total_social_media_platforms = (instagram_info[0], twitter_info[0])
#b. Skills count comparison (current vs. learning goals)
skills_count_comparison = (len(current_skills) / len(skills_to_learn))
#c. Contact directory size analysis 
contact_directory_size_analysis = len(contact_directory)
#d. Entertainment backlog management count
entertainment_backlog_management_count = len(entertainment_backlog)
#e. Academic workload assessment
academic_load_assessment = len(current_courses_list)

print(f"================================================================")
print(f"              PERSONAL ACADEMIC & LIFE PORTFOLIO")
print(f"================================================================")
print(f"Student: {full_name} | Email: {student_email}")
print(f"From: {hometown} | Graduating: {graduation_semester}")
print(f"Major: {major}\n")
print(f"=== ACADEMIC PROFILE ===")
print(f"Current Semester: {credits} credits across {academic_load_assessment} courses")
print(f"Cumulative GPA: {round(cumulative_GPA, 2)}")
print(f"Weekly Study Time: {total_weekly_study_hours} hours")
print(f"Academic Investment: ${study_cost_per_hours} per study hour\n")
print(f"Current Courses:")
print(current_courses_list[0], "-", course_credits["COMP 163"], "credits", "-", course_professors["COMP 163"], "-", course_rooms["COMP 163"])
print(current_courses_list[1], "-", course_credits["MATH 150"], "credits", "-", course_professors["MATH 150"], "-", course_rooms["MATH 150"])
print(current_courses_list[2], "-", course_credits["ENG 101"], "credits", "-", course_professors["ENG 101"], "-", course_rooms["ENG 101"])
print(f"{current_courses_list[3]} - {course_credits["HIS 105"]} credits - {course_professors["HIS 105"]} - {course_rooms["HIS 105"]}\n")
print(f"=== PERSONAL DEVELOPMENT ===")
print(f"Current Skills:", current_skills)
print(f"Learning Goals:", skills_to_learn)
print(f"Career Interests:", career_interests)
print(f"Skills Currently Have:", len(current_skills))
print(f"Skills Want to Learn: {len(skills_to_learn)}\n")
print(f"=== FINANCIAL OVERVIEW ===")
print(f"Monthly Budget: ${monthly_budget_total}")
print(f"Food: ${monthly_budget["Food"]} (${round(monthly_budget["Food"] / 30, 3)}/day)")
print(f"Entertainment: ${monthly_budget["Entertainment"]}")
print(f"Books: ${monthly_budget["Books"]}")
print(f"Transportation: ${monthly_budget["Transportation"]}")
print(f"Annual Projection: ${annual_budget_projection}\n")
print(f"=== CONNECTIONS & CONTACTS ===")
print(f"Emergency Contact: {emergency_contact[1]} ({emergency_contact[0]}) - {emergency_contact[2]}")
print(f"Home Address: {home_address[0]}, {home_address[1]} {home_address[2]}")
print(f"Social Media Presence: {total_social_media_followers} followers across {len(total_social_media_platforms)} platforms")
print(f"Key Contacts: {contact_directory_size_analysis} people in directory\n")
print(f"=== LIFE STATISTICS ===")
print(f"Total Courses Completed: {len(completed_courses_list)}")
print(f"Current Academic Load: {academic_load} weekly commitments")
print(f"Entertainment Backlog: {entertainment_backlog_management_count} items")
print(f"Current Hobbies: {len(hobbies)} activities")
print(f"================================================================")

