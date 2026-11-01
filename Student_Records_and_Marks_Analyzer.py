# Student Records and Marks Analyzer
print("===== STUDENT RECORDS AND MARKS ANALYZER =====")
students = {}
stuppel = ("PYTHON", "MATH", "DBMS")

print(stuppel)

ch = int(input("\nhow many student want to add? "))

for i in range(0, ch):
    marks = []

    stud_id = int(input("\nStudent ID: "))
    name1 = input("Name: ")

    for subject in stuppel:
        while True:
            mark1 = int(input(subject +" Marks : "))

            if mark1 < 0 or mark1 > 100:
                print("invalid marks, enter again")
            else:
                marks.append(mark1)
                break

    student = {
        stud_id: {"name": name1, "mark": marks}
    }

    students.update(student)


print("\n========== STUDENT REPORTS ==========")

for roll in students:
    print("Roll_No:", roll)
    print("Name:", students[roll]["name"])
    print("Marks:", students[roll]["mark"])


# highest average marks

highest = -1
highest_name = ""

for roll in students:
    mark = students[roll]["mark"]
    average = sum(mark)/len(mark)
    if average>highest:
        highest = average
        highest_name = students[roll]["name"]

print("\nhighest marks:")
if len(students) >0:
    print(highest_name, "-", highest)


# lowest marks

lowest = 101
lowest_name = ""

for roll in students:
    mark = students[roll]["mark"]
    average = sum(mark) / len(mark)

    if average <lowest:
        lowest =average
        lowest_name = students[roll]["name"]

print("\nlowest marks:")
if len(students)>0:
    print(lowest_name,"-",lowest)


# average marks

total = 0
count = 0
for roll in students:
    mark =students[roll]["mark"]
    total= total + sum(mark)
    count=count +len(mark)

if count>0:
    average =total/ count
    print("\naverage marks:",  average)
else:
    print("\nno student records")


# students above 80

print("\nstudents above 80:")

for roll in students:
    mark = students[roll]["mark"]
    avg = sum(mark) / len(mark)

    if avg > 80:
        print(students[roll]["name"],"-",  avg)


# search student by roll number

roll = int(input("\nenter roll number to search: "))

if roll in students:
    print("student found:")
    print("name:",students[roll]["name"])
    print("marks:",  students[roll]["mark"])

    mark= students[roll]["mark"]

    if sum(mark)/len(mark) >=40 and min(mark)>= 33:
        print("PASS")
    else:
        print("FAIL")
else:
    print("student not found")