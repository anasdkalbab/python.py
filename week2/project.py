import csv
import sys

students = []

try:
    with open("students.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append({"first name" : row["first name"],"last name":row["last name"],"id":row["id"] ,"marks":row["marks"]})
except FileNotFoundError:
    with open("students.csv","w")as file:
        writer = csv.DictWriter(file,fieldnames=["first name" ,"last name" ,"id","marks"])
        writer.writeheader()
  

def main():
    while True:
        print("===student manage system===")
        print("1. Add a student")
        print("2. Add grades")
        print("3. View all students")
        print("4. Search for a student")
        print("5. View class statistics")
        print("6. Quit")
        profile = input("Enter your choice: ")
        profile =  profile.lower().strip()
        if profile == "1":
            add_student()
        elif profile == "2":
            add_marks()
        elif profile == "3":
            show_all()
        elif profile == "4":
            find_student()
        elif profile == "5":
            rank_students()
        elif profile == "6":
            with open("students.csv","w") as file:
                writer = csv.DictWriter(file,fieldnames=["first name","last name","mark","avg"])
                for student in students:
                    writer.writerow({"first name":student["first name"],"last name":student["last name"],"avg":student["avg"]})
                    
                

            sys.exit()




def get_student(student):
    return(student["first name"])

def get_id(student):
    return (student["id"])


        
def add_student():
    
    first_name = input("What is your students name? ")
    last_name = input("What is your studnets last name?")
    student = {"first name":first_name ,"last name":last_name}
    students.append(student) 
    sorted_students = sorted(students,key = get_student) 
    for number, name in enumerate(sorted_students, start=1):
        name["id"] = number
    


def show_all():
    for student in sorted(students,key=get_id):
        print(student)

def add_marks():
    marks = ["math" ,"science","phisics","english"]

    while True:
        try:  
            if students !=[]:
                for student in students:
                    print(f"{student["id"]}.{student["first name"]} {student["last name"]}")
                name = input("To which student do you want to give marks?").strip()
                if input("Do you want to enter the whole marks or only one? ") == "only one":
                    print("====marks====")
                    print("1.math")
                    print("2.science")
                    print("3.phisics")
                    print("4.english")
                    subject = input("What subject do you want to add.").strip()
                    mark = input("How much have he got?")
                    for student in students:
                        if student["first name"] == name or student["last name"] == name:
                            student[subject] = mark 
                            break
                else:
                    for student in students:
                        if student["first name"] == name or student["last name"] == name:
                            student["marks"] = {}
                            for mark in marks:
                                student["marks"][mark] = input(f"Enter score for {mark}: ")
                    break

            else:
                print("You have no students to add marks to. ")
                break
            
            
        except ValueError:
            print("Their was a mistake please try again. ")
            pass

def find_student():
    name = input("What is the students name? ")
    for student in students:
        if student["first name"] == name or student["last name"] == name:
            print(student)

def add_avg():
    for student in students:
        total_marks = len(student["marks"])
        all_scores = list(student["marks"].values())
        student["avg"] = 0
        for i in range(total_marks):
            student["avg"] += int(all_scores[i])
        student["avg"] = student["avg"]/(total_marks)
#        print(f"{student["first name"]}: {student["avg"]}")

def get_avg(student):
    if student["marks"]
        add_avg()
        return int(student["avg"])
    
def rank_students():
        sorted_students = sorted(students, key = get_avg, reverse = True) 
        for number, name in enumerate(sorted_students , start=1):
           print(f"{number} {name["first name"]} {name["last name"]}:{name["avg"]}")

    

if __name__=="__main__":    
    main()

'''
def show_data():
    while True:
        try:
            name = input('What is the students name ')
            print (students[name])
            break
        except KeyError :
            pass    

def remove_student():
    student =input("Which student do you want to remove?")
    del students[student]

'''