"""CS 108 Lab 10.0

This driver uses the Employee class to compute and save corporate statistics.

@author: Gunju Yoo (gy24)
@date: Spring, 2021
"""

from employee import Employee
employees = []
# Load an employee object for each employee specified in 'employees.txt' into the employees list.
openfile = open("employees.txt", "r")
count = 0


for employee_line in openfile:
    value = employee_line.strip().split(',')
    given_name = value[0] # Set the first index of value to be given_name
    family_name = value[1] # Set the second index of value to be family_name
    rank = value[2] # Set the third index of value to be rank
    salary = int(value[3]) # Set the last index of value to be salary, and make the salary be an integer
    employee = Employee(given_name, family_name, rank, salary)
    employees.append(employee) # Put all the information in employees
    count += 1 # Get total number of employees

totals = {} # Create an empty dictionary for total salary for each rank
counts = {} # Create an empty dictionary for counting how many people are in same rank
max_employee = employees[0] 
min_employee = employees[0]
for employee in employees:
    if employee.rank in totals:
        totals[employee.rank] += employee.salary # Increment the value for that rank by the current employee salary in the totals dictionary.
        counts[employee.rank] += 1 # Increment the count for that rank by 1 in the counts dictionary.
    else:
        totals[employee.rank] = employee.salary # Add a new entry for this rank to the totals dictionary. 
        counts[employee.rank] = 1 # Add a new entry for this rank to the counts dictionary, and set the initial value to 1.
# Compare the salary and find who gets the maximum salary and who gets minimum salary        
    if employee.salary > max_employee.salary:
        max_employee = employee
    else:
        max_employee = max_employee
    if employee.salary < min_employee.salary:
        min_employee = employee
    else:
        min_employee = min_employee
        
openfile.close()


# Write the total number of employees into the 'employee-count.txt' file.
employee_count = open('employee-count.txt', 'w')
employee_count.write(str(count))
employee_count.close()

# Write the statistics of employees into the 'employee-stats.txt' file.
employee_stats = open('employee-stats.txt', 'w')
employee_stats.write('Maximum Salary: ')
employee_stats.write(str(max_employee))
employee_stats.write('\n')

employee_stats.write('Minimum Salary: ')
employee_stats.write(str(min_employee))
employee_stats.write('\n')

employee_stats.write('Rank')
employee_stats.write('\t')
employee_stats.write('Average Salary')
employee_stats.write('\n')

for rank in totals:
    avg = '{:.2f}'.format(totals[rank] / counts[rank])
    employee_stats.write(rank)
    employee_stats.write('\t')
    employee_stats.write(avg)
    employee_stats.write('\n')

employee_stats.close()







