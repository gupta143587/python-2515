# Python Strings With LMS
print("="*30)
print("LMS Grade Tracking System")
print("="*30)

# While Reading ID, id should be positive 
student_id_valid = False
while not student_id_valid:
    student_id = input("Enter Your ID: ")
    # check if the given input is only numbers
    if student_id.isdigit():
        student_id = int(student_id)
        # check if the number is positive
        if student_id > 0:
            student_id_valid = True
        else:
            print("Please Enter Positive Number or Above Zero")
    else:
        print("Please Enter Numbers Only, Other characters not allowed")

# print(f"Your ID: {student_id}")

# Fromat Student ID 
institute_code = "DE-"
formatted_id = institute_code+"STU"+str(student_id).zfill(5)
print(formatted_id)

# Implement name validations
student_name_valid = False
while not student_name_valid:
    student_name = input("Enter Your Full Name: ")

    # remove spaces and ravi krishna → Ravi Krishna
    student_name = student_name.strip().title()
    # print(student_name)
    
    # name should be only alaphabets and also spaces allowed
    # name check with only spaces allowed
    name_check = student_name.replace(" ","")

    # Minimum 3 characters length validation
    if name_check.isalpha() and len(student_name) >=3:
        student_name_valid = True
        print("Welcome, "+student_name)
    else:
        if not name_check.isalpha():
            print("Name should contain only letters and spaces")
        elif len(student_name) < 3:
            print("Name should contain atleast 3 characters")

# system generated unique email id
name_parts = student_name.split()
# print(name_parts)
first_name = name_parts[0].lower()
# Generate university email
student_email = first_name + "."+str(student_id)+"@edify.edu"
print(student_email)

# Course Fee Input and Discount Calculation
base_course_fee_valid = False
while not base_course_fee_valid:
    base_course_fee = input("Enter Base Course Fee: ")
    if base_course_fee.isdigit():
        base_course_fee = int(base_course_fee)
        if base_course_fee > 10000:
            base_course_fee_valid = True
        else:
            print("Enter Course Fee Above 10000")
    else:
        print("Please Enter Numbers Only, Other characters not allowed")

discount = 0
description = input("Enter Description: ")
description = description.lower()

if "reference" in description:
    discount+= 5000
if "scholarship" in description:
    discount+= 7000
if "promo" in description:
    discount+= 3000
# using in operator     
# if description.find("referal") >=0: --> using in built string method

final_fee = base_course_fee - discount

student_attendance_validation=False
while not student_attendance_validation:
    student_attendance=input("Enter Student Attendance: ")
    if student_attendance.isdigit():
        student_attendance=float(student_attendance)
        if student_attendance >=0 and student_attendance <=100:
            student_attendance_validation=True
        else:
            print("Please Enter Positive Number and also enter the number between 1 to 100 only")
    else:
        print("Please Enter Numbers Only, Other characters not allowed")

number_of_subjects = 0  # Number of subjects
total_score = 0  # Initialize total score

continue_input_validation = False
while not continue_input_validation:
    continue_input=input("Enter the Input(Yes/No): ")
    if continue_input.isalpha() and len(continue_input)==3:
        continue_input_validation=True
        
        number_of_subjects = 0  # Number of subjects
        total_score = 0  # Initialize total score
        
        while continue_input == 'yes' or continue_input == 'Yes' or continue_input == "Ok" or continue_input == "ok":
            current_score_valid=False
            while not current_score_valid:
                current_score = input(f"\nEnter score for Subject {number_of_subjects + 1}: ")
                if current_score.isdigit():
                    current_score=int(current_score)
                    if 1 < current_score < 100:
                        current_score_valid=True
                        number_of_subjects += 1
                        total_score += current_score
                    else:
                        print("Please Enter the Number Between 1 to 100")
                else:
                    print("Please Enter Numbers Only, Other characters not allowed")
                
            next_input_valid=False
            while not next_input_valid:
                continue_input=input("Enter the Input(Yes/No): ")
                if continue_input.isalpha() and len(continue_input)==3:
                    next_input_valid=True
                elif continue_input=="no" or continue_input=="No":
                    break             
                else:
                    print("Input conatins Three leters Only")
    else:
        print("Input conatins Three leters Only")
        
# Calculate average score
average_score = total_score / number_of_subjects

# Determine performance level
if average_score >= 85:
   performance = "Excellent"
elif average_score >= 70:
   performance = "Good"
elif average_score >= 50:
   performance = "Average"
else:
   performance = "Needs Improvement"
   
# Check Attendance Status
attendance_status = "WARNING - Low Attendance" if student_attendance < 75 else "OK - Attendance Satisfied"
                         
print("="*30)
print("FEE DETAILS")
print("="*30)

print(f"Actual Fee: {base_course_fee}")
print(f"Discount Given: {discount}")
print(f"Final Fee To Pay: {final_fee}")
               
print("="*30)
print("STUDENT DETAILS")
print("="*30)              
print(f"Student ID: {student_id}")
print(f"Student Name: {student_name}")
print(f"Student Unique Email: {student_email}")
print(f"Student Attedance: {student_attendance}")
print(f"Total Number of Subjects: {number_of_subjects}")
print(f"Total Score: {total_score}")
print(f"Average Score: {average_score}")
print(f"Performance: {performance}")
print(f"Attendance: {attendance_status}")