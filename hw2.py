'''
This program demonstrates the test average and grade. It also covers geometry
Course: ITMD 513
Author: Yewande Ogunedina
'''

# Prompt user to enter option #1, #2 and #3 to exit
import math
grade1= 'A'
grade2 = 'B'
grade3= 'C'
grade4= 'D'
grade5 = 'F'

#List options for user to select
def menu():
    print('\n 1. To calculate average score and test grade \n 2. To calculate area of triangle. \
\n 3. Exit')
    choice = int(input('Enter Choice 1-3: '))
    if choice == 1:
        calc_average()
    if choice == 1:
        determine_grade()
    elif choice == 2:
        calc_area_s()
    elif choice == 3:
        print('Program exit')
        exit
    else:
        print('Invalid choice. Please enter 1-3')
        menu()


# Return the average of all five scores.        
def average_score(score1, score2, score3, score4, score5):
        result = (score1 + score2 + score3 + score4 + score5) /5
        return(result)
    
def calc_average():
        a = eval(input('Enter first score: '))
        b = eval(input('Enter second score: '))
        c = eval(input('Enter third score: '))
        d = eval(input('Enter fourth score: '))
        e = eval(input('Enter fifth score: '))
        average = average_score(a,b,c,d,e)
        print('The average score is', format(average, '.1f'))

# This function is to determine the grade letter.        
def determine_grade():
    test_score = eval(input("Enter your test score between 0 and 100: "))
    if test_score >= 90 and test_score <=100:
        print('Your letter grade is:', grade1)
    elif test_score >= 80 and test_score <=89:
        print ('Your letter grade is:', grade2)
    elif test_score >=70 and test_score <=79 :
        print ('Your letter grade is:', grade3)
    elif test_score>= 60 and test_score <=69:
        print ('Your letter grade is:', grade4)
    elif test_score <60 and test_score >0 :
        print ('Your letter grade is:', grade5)
    else:
        print('Invalid number. Please enter a number between 1 - 100')

    
# Function for geography : area of a triangle
def calc_area_s():
    side_1 = eval(input('Enter side value of triangle: '))
    side_2 = eval(input('Enter side value of triangle: '))
    side_3 = eval(input('Enter side value of triangle: '))
    s_area = (side_1+ side_2+ side_3)/2
    s_area_triangle = math.sqrt (s_area*(s_area-side_1)*(s_area-side_2)*(s_area-side_3))
    print('The S is', s_area)
    print('The area of the triangle is',format( s_area_triangle, '.2f'))

# start program. After option 1 runs, prompt user to select a new option
restart = 'y'
while (restart == 'y'):
    menu()
    restart = input('Do you want to see the options again? y/n: ')



