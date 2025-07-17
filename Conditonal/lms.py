print("LMS Fee")
student_name=input("Enter The Name:")
student_grade_level=int(input("Enter the Student Grade(1-12):"))
base_tution_fee=float(input("Enter the Tution Fee:"))

is_academic_topper_input=input("Academic Topper ? (yes/no)")
is_academic_topper=is_academic_topper_input=="yes"
discount=0.0

if 1<=student_grade_level<=12:
    print(f"{student_name} discount applied")
    
    if student_grade_level>=9 and student_grade_level<=12:
        if is_academic_topper:
            discount=0.20
            print("Discount Applied for Acedameic Toppers")
        else:
            discount=0.10
            print("discount Applied for Primary")
    elif student_grade_level>=6 and student_grade_level<=8:
        discount=0.05
        print("discount applied for middle grade")
    else:
        discount=0.0
        print("No discount Applied")
    
    match student_grade_level:
        case 10: 
            discount+=0.03
        case 12:
            discount+=0.05
        case _:
            discount+=0.0
    
    discount_amount=base_tution_fee * discount  
    dis_counted_fee=base_tution_fee - discount_amount
    
    print("===== LMS Fee Discount Calculator =====")
    print(f"Student Name:{student_name}")
    print(f"Student Grade:{student_grade_level}")
    print(f"Acedamic Topper:{is_academic_topper}")
    print(f"Base Tution Fee:{base_tution_fee}")
    print(f"Total Discount:{discount}")
    print(f"Discount Amount:{discount_amount}")
    print(f"Tution Fee After Discount:{dis_counted_fee}")
    print("---------------------------------------------")
    print("Excellent")

else:
    print("Invalid")

