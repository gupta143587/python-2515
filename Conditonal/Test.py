a=4
b=5
if a>b:
    print(f"{a} is Greater that {b}")
    print("next statement")
else:
    print(f"{a} is Lesser Than {b}")
    print("next statement")


# i=int(input("enter the name:"))
# if i>=18:
#     print("Applicable to Vote")
# else:
#     print("Not Applicable to Vote")
    

# age=int(input("Enter the Age:"))
# nationality=input("Enter the Nationality:")
# if age>=18 and nationality=="Indian":
#     print("You can Vote")
# else:
#     print("You can't Vote")
    
    
choice=4
match choice:
    case 1:
        print("one")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case _:
        print("Invalid")