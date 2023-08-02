def input_from_user():
    exam_points = []
    exercises_completed = []
    while True:
        inputs = input("Exam points and exercises completed: ")
        if inputs == '':
            break
        points = inputs.split()
        exam_points.append(points[0])
        exercises_completed.append(points[1])
    
    #Change list items from strings to integers
    i = 0
    while i < len(exam_points):
        exam_points[i] = int(exam_points[i])
        exercises_completed[i] = int(exercises_completed[i])//10 #change my_list2 items to 10th. i.e. 87 t0 8
        i += 1
    return exam_points, exercises_completed

def points_average(my_list1, my_list2):
    new = []
    for i in range(len(my_list1)):
        new.append(my_list1[i] + my_list2[i])
    average = round(sum(new) / len(new), 1)
    print(f"Points average: {average}")


def statistics(my_list1, my_list2):
    grade0 = '  0: '
    grade1 = '  1: '
    grade2 = '  2: '
    grade3 = '  3: '
    grade4 = '  4: '
    grade5 = '  5: '
    i = 0
    passed = 0
    while i < len(my_list1):
        if my_list1[i] < 10 or my_list1[i] + my_list2[i] <= 14:
            grade0 += '*'
        else:
            if my_list1[i] + my_list2[i] <= 17 and my_list1[i] + my_list2[i] >= 15:
                grade1 += '*'
            elif my_list1[i] + my_list2[i] <= 20 and my_list1[i] + my_list2[i] >= 18:
                grade2 += '*'
            elif my_list1[i] + my_list2[i] <= 23 and my_list1[i] + my_list2[i] >= 21:
                grade3 += '*'
            elif my_list1[i] + my_list2[i] <= 27 and my_list1[i] + my_list2[i] >= 24:
                grade4 += '*'
            elif my_list1[i] + my_list2[i] <= 30 and my_list1[i] + my_list2[i] >= 28:
                grade5 += '*'
            passed += 1
        i += 1
    print("Statistics:")
    points_average(my_list1, my_list2)
    pass_percentage = round((passed * 100)/len(my_list1), 1)
    print(f"Pass percentage: {pass_percentage}")
    print("Grade distribution:")
    print(grade5, grade4, grade3, grade2, grade1, grade0, sep='\n')

x, y = input_from_user()
statistics(x, y)