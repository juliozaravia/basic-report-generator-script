import csv

# Global variables that contain the paths that will be required for operations.
csv_file_path = 'file_to_process.csv'
report_file_path = 'department_report.txt'
# Global variables that contain the names of the headers that identify each field within the CSV file.
department_header = 'Department'

# Description: This function receives a CSV file as a parameter and returns a list of dictionaries from that file.
def employee_list_generator(csv_file_location):
    # We create a 'dialect', a dialect is a way to control the format flexibility that a CSV document has.
    # It allows us to apply parameters in such a way that the data can be processed according to a controlled format and with less probability of error.
    # For more details you can visit the documentation written about this: https://docs.python.org/3/library/csv.html#csv-fmt-params
    dialect_name = 'control_dialect' 
    csv.register_dialect(dialect_name, skipinitialspace=True, strict=True)
    # We create an object called 'group_of_employees' by using the DictReader function.
    # The DIctReader function reads the file like any other read function, however it respects the dialect established above.
    # Additionally, it processes the information and divides it according to the headers assigned in the CSV file.
    # Once the information is processed, it is grouped into individual dictionaries.
    group_of_employees = csv.DictReader(open(csv_file_location), dialect=dialect_name)
    # We create a list that will be filled with the dictionary container object. 
    # In this way we will be able to go through the list in a more adequate way and access the dictionaries and their respective contents.
    list_of_employees = list()
    # We use a loop to go through the object full of dictionaries.
    for employee in group_of_employees:
        # We add each dictionary (which contains the processed data of each employee) one by one within the list.
        list_of_employees.append(employee)
    return list_of_employees

# Description: This function receives the 'list_of_empoyees' as a parameter and returns a dictionary indicating the department and its number of employees.
def employees_per_department_calculator(list_of_employees):
    # We create a list that will be filled with the name of the department to which each employee belongs.
    list_of_department_names = list()
    # We use a loop to go through the list that contains the employee data in the form of dictionaries.
    for employee in list_of_employees:
        # We add the department name of each employee to 'list_of_department_names'.
        list_of_department_names.append(employee[department_header])
    # We create the dictionary that will be filled with the total number of employees for each department.
    employees_per_department = dict()
    # We apply the set() function to the list of department names in order to have a structure that does not contain repeated department names. 
    unique_list_of_department_names = set(list_of_department_names)
    # We use a loop to go through our new structure of unique department names.
    for department_name in unique_list_of_department_names:
        # We use the count() function to count the number of times a department name appears within the list of department names.
        # Once the number of times has been calculated, it is assigned to the dictionary 'employees_per_department'... 
        # ... associating it with the name of the respective department.
        employees_per_department[department_name] = list_of_department_names.count(department_name)
    return employees_per_department

# Description: It allows the creation of the necessary report based on the information previously processed.
def department_report_generator(employees_per_department, report_file_path):
    # We open the file in writing mode.
    # For this particular example, we use this mode to create the document as well.
    with open(report_file_path, 'w') as report_file:
        # We write the header of the report
        report_file.write('\n')
        report_file.write('*******************************************\n')
        report_file.write('****** Total employees by department ******\n')
        report_file.write('*******************************************\n')
        report_file.write('\n')
        # We 'modify' the order of the container items (in this case) alphabetically to improve the presentation.
        # We use a loop to go through the container. Additionally we use the items() property to extract its key and value.
        # We define a counter that will allow us to write the number of items.
        counter = 1
        for key, value in sorted(employees_per_department.items()):
            # We write the previously processed values in the file. 
            # We use the format() function to improve the readability of the code.
            report_file.write('### ' + str(counter) + '\n')
            report_file.write('{}: {}\n'.format(department_header, key))
            report_file.write('Total of employees: {}\n'.format(str(value)))
            report_file.write('\n')
            counter += 1
        report_file.close()

# We make the call to the functions that will perform the operations and pass the respective parameters.
list_of_employees = employee_list_generator(csv_file_path)
employees_per_department = employees_per_department_calculator(list_of_employees)
department_report_generator(employees_per_department, report_file_path)
