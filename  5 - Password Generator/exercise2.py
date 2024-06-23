student_scores = input("Input a list of student scores: ").split()

highest_score = 0
for score in student_scores:
    score = int(score)
    if score>highest_score:
        highest_score=score

print(f"The highest score in the class is {highest_score}")