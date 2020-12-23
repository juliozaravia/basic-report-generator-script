> **Note:** *It's my intention that the script serve other programmers who are starting in Python as a basis for their own practices and implementations. Developing this script has been very useful for me, I've tried to leave a detailed explanation of its programming logic in the comments of the code.*

## **1. What does this script do?**
This script allows you to process a CSV file delivered by the Human Resources department (as a practical example) in order to count the number of employees that exist per department.

## **2. What's the structure of the CSV file?**
For any CSV file processing operation, **a previous structure must be defined that allows knowing how to extract and organize the data according to the requirement.**

In this case, the CSV file has a "header block" that has been organized as follows:

`FirstName, LastName, FullName, User, Department`

![CSV File Structure](http://www.juliozaravia.com/git-images/csv_file_structure.jpg "CSV File Structure")

## **3. What's the structure of the generated report?**
The report has a basic format. In general, as I explained above, the total number of employees in each department of the company is recorded as follows:

![Department Report](http://www.juliozaravia.com/git-images/department_report.jpg "Department Report")

## **4. Do you want to modify, improve or increase the functionality of the script?**
You're welcome to do so. **I recommend that you first define the structure of the content of your CSV file before filling in the data**. For example, you could add an email field to check how many employees don't yet have company email, among other ideas.

## **5. How do I generate my own data?**
I share with you a CSV file generator that has been too useful for me, in which you can define the fields you need or generate them in a personalized way.
- [CSV File Generator](https://extendsclass.com/csv-generator.html "CSV File Generator")

I must indicate that I have not developed this website or its functionality in whole or in part, I give full credit to [Cyril](https://github.com/cyrilbois "Cyril") (the author) and send him my best wishes for having developed something so useful.

## **6. And now, what's next?**
I'll try to update this script to cover different cases like:
- Number of users who do not yet have the corporate email.
- Average result of evaluations by department.
- Conditional application of bonuses according to performance ratio, And others that I can think of.
