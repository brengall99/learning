# Write your solution here

results = ""
points_list = []
fails = 0
sum_points = 0
grades_list = []

while results != " ":
    results = str(input("Exam points and excercises completed: "))
    list1 = results.split(" ")

    if results == " ":
        break

    exam_points = int(list1[0])
    excercises = int(list1[1])

    if exam_points < 10:
        grades_list.append(0)
        
    else:
        for i in range(1, 10):
            if 0 <= excercises  <= 9:
                excercise_points = 0

            elif 90 <= excercises <= 100:
                excercise_points = 10
            
            elif i*10 <= excercises < 90:
                excercise_points = i

        total_points = excercise_points + exam_points
        points_list.append(total_points)

        for i in points_list:
            sum_points += i

            if 0 <= i <= 14:
                grades_list.append(0)
            elif 15 <= i <= 17:
                grades_list.append(1)
            elif 18 <= i <= 20:
                grades_list.append(2)
            elif 21 <= i <= 23:
                grades_list.append(3)
            elif 24 <= i <= 27:
                grades_list.append(4)
            else: 
                grades_list.append(5)
9
for i in grades_list:
    if i == 0:
        fails += 1
     
# for j in grades_list:
    # if j-1 == grades_list:

if sum_points == 0:
    points_average = 0
    pass_percentage = 0
else:
    points_average = sum_points/len(points_list)
    pass_percentage = (fails/len(grades_list))*100

    

print("Statistics: ")
print(f"Points average: {points_average:.1f}")
print(f"Pass percentage: {pass_percentage:.1f}")
print("Grade distribution: ")

