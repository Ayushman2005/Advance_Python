import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ayushman@2005",
    database="salary_db"
)
cursor = db.cursor()
def add_employee():
    name = input("Enter name: ")
    dept = input("Enter department: ")
    basic = float(input("Enter basic salary: "))
    bonus = float(input("Enter bonus: "))
    deductions = float(input("Enter deductions: "))
    total = basic + bonus - deductions
    sql = """INSERT INTO employees
             (name, department, basic_salary, bonus, deductions, total_salary)
             VALUES (%s, %s, %s, %s, %s, %s)"""
    values = (name, dept, basic, bonus, deductions, total)
    cursor.execute(sql, values)
    db.commit()
    print("Employee added successfully!")
def view_employees():
    cursor.execute("SELECT * FROM employees")
    records = cursor.fetchall()
    for row in records:
        print(row)
def update_salary():
    emp_id = int(input("Enter employee ID: "))
    bonus = float(input("Enter new bonus: "))
    deductions = float(input("Enter new deductions: "))
    cursor.execute("SELECT basic_salary FROM employees WHERE emp_id=%s", (emp_id,))
    basic = cursor.fetchone()[0]
    total = basic + bonus - deductions
    sql = """UPDATE employees 
             SET bonus=%s, deductions=%s, total_salary=%s
             WHERE emp_id=%s"""
    values = (bonus, deductions, total, emp_id)
    cursor.execute(sql, values)
    db.commit()
    print("Salary updated successfully!")
def delete_employee():
    emp_id = int(input("Enter employee ID to delete: "))
    cursor.execute("DELETE FROM employees WHERE emp_id=%s", (emp_id,))
    db.commit()
    print("Employee deleted successfully!")
while True:
    print("\n--- Salary Management System ---")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Update Salary")
    print("4. Delete Employee")
    print("5. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        add_employee()
    elif choice == "2":
        view_employees()
    elif choice == "3":
        update_salary()
    elif choice == "4":
        delete_employee()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice!")