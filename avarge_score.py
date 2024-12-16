grades = [[5,3,3,5,4], [2,2,2,3], [4,5,5,2], [4,4,3], [5,5,5,4,5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(students)
students.sort()
avarge_score = {}
avarge_score.update({str(students[0]): sum(grades[0])/len(grades[0]),
                     str(students[1]): sum(grades[1])/len(grades[1]),
                     str(students[2]): sum(grades[2])/len(grades[2]),
                     str(students[3]): sum(grades[3])/len(grades[3]),
                     str(students[4]): sum(grades[4])/len(grades[4])})#sum(grades[0])/len(grades[0])
print(avarge_score)