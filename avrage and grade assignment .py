
#CS 175/501A
#Nakshatra Nitin Kawthale
#average and grade assignment


def cal_average(scores):
    total = sum(scores)
    average = total / len(scores)
    return average

def determine_grade(score):
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score < 90:
        return "B"
    elif 70 <= score < 80:
        return "C"
    elif 60 <= score < 70:
        return "D"
    else:
        return "F"

def repeat():
    while True:
        scores = []
        print("score     numeric grade    letter grade")
        for i in range(5):
            sub = int(input(f"Enter score {i + 1}:"))
            scores.append(sub)
            each_grade = determine_grade(sub)
            print(f"The grade for the average score is {each_grade}")
            
            

        average_score = cal_average(scores)
        grade = determine_grade(average_score)

       

        print(f"The average score is {average_score}")
        print(f"The grade for the average score is {grade}")

        another_calculation = input("Do you want to do another calculation? (yes/no): ").lower()
        if another_calculation != 'yes':
            break

repeat()
