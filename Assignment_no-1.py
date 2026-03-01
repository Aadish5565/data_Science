
employee = {
    101 : {"name": "John Doe", "age": 30, "department": "HR" , "salary": 50000},
    102 : {"name": "Jane Smith", "age": 25, "department": "IT", "salary": 60000}
}



def main():
    flag = 1
    while(flag != 4):
        print("1. Add Employee")
        print("2. Display Employee")
        print("3. Search for Employee")
        print("4. Exit")
        flag = int(input("Enter your choice: "))

        if(flag == 1):
            add_employee()

        elif(flag == 2):
            display_employee()

        elif(flag == 3):
            search_employee(int(input("Enter Employee ID to search: ")))

def add_employee():
    emp_id = int(input("Enter Employee ID: "))
    name = input("Enter Employee Name: ")
    age = int(input("Enter Employee Age: "))
    department = input("Enter Employee Department: ")
    salary = int(input("Enter Employee Salary: "))
    
    employee[emp_id] = {"name": name, "age": age, "department": department, "salary": salary}

def display_employee():
    for emp_id in employee:
        print(f"Employee ID: {emp_id}, Name: {employee[emp_id]['name']}, Age: {employee[emp_id]['age']}, Department: {employee[emp_id]['department']}, Salary: {employee[emp_id]['salary']}")

def search_employee(emp_id):
    if emp_id in employee:
        print(f"Employee ID: {emp_id}, Name: {employee[emp_id]['name']}, Age: {employee[emp_id]['age']}, Department: {employee[emp_id]['department']}, Salary: {employee[emp_id]['salary']}")
    else:
        print("Employee not found")

main()