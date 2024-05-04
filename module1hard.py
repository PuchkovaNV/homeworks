grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

dict = {}
for student in students:
    for grade in grades:
        avg = sum(grade) / len(grade)
        dict[student] = avg

print(dict)