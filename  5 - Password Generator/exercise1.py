sum_of_heights = 0
heights_length = 0

student_heights=input("Input a list of student heights: ").split()

for n in range(0,len(student_heights)):
    student_heights[n] = int(student_heights[n])
    print(student_heights[n])

    sum_of_heights += student_heights[n]

    heights_length += 1 

# for item in student_heights:
    
print(sum_of_heights)
print(heights_length)
print(sum_of_heights/heights_length)