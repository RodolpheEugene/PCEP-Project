# Rodolphe Eugene

# This program is a studying tool for the PCEP- Cerftified Entry-Level Python Programmer Certification Exam and it will breakdown the programming concepts.
# There will be some practice questions and interactive activities along the way to make the process a lot more fun.

# Received help from Andrew Krupp
# Received help from Robert McNiven Jr.
# Reference: Robert McNiven Jr, he reminded me to to use "\n" for line spacing.
print("Hey!,welcome to my program\n")
print(
    "Using this studying tool will help you get your certificate for the PCEP Examp!")
print(
    "This program will help you prepare for the PCEP Certification Exam. \n There will be some questions to answer for practice along the way\n")

print("This is an example of how simple input and output can be used:\n")
print("HELLO, " * 2)
# I used the * string literal above to ask the program to print "Hello" 2 times.
print("\n")
name = input("What is your name? \n")
print("\n")
print("Tell me about yourself", name)
print("\n")
movie = input("what is your favorite movie to watch? \n")
print("I will keep that in mind that your favorite movie is", movie)

print("\n")

input("Where are you from? \n")
print("\n")
input("What is your favorite color? \n")
print("\n")
print("Great!!! " * 2)
# I used the "*" string literal to command the program to display "Great!!!" two times.
print("\n")
# I used an input function to command the user to press ENTER to continue.
input("press ENTER continue.....\n")

print("\n")

print("This frst example wasn't too bad,",
      "Now let's move on to more deeper concepts in programming.\n")

print(
    "Now, Let's go over an example of how you can use the 'end=' and 'sep=' argument to format a print output.\n")
# the "end=" statement can be use to space out sentences as well or you can input information inside the quotes too.
print("Example: \n Now that you have told me your favorite movie", end=". ")
print("\n")
print("It seems that you are really into that movie that you picked", end=". ")
print("\n")
print("Now we're gonna move on to using the sep = argument", end=".\n")
print("\n")
input("press ENTER to coninue..... \n")

print("\n")
# I used the "sep=" argument in the example below. the "sep=" can be use to seperate sentences.
num_first = 5
num_second = 6
print("num_first", num_first, sep=": ")
print("num_second", num_second, sep=": ")
print("\n")
print(
    "If I want to solve the input above by addition, I can write this code below to get:\n")
num_first = 5
num_second = 6
print(
    num_first + num_second)  # I used the "+" addition operator to show an example of how it can be use above.
print("\n")
print(
    "As demonstrated in the sentences above, this is a way the end = and sep = argument can be implemented to combine and seperates sentences \n")

print("\n")
# I used a  "+" string literal to combine the two strings. Python will not let you combine string with an integer.
print("Here is one instance where you can use the + string literal\n")
year = "2000"
nummy = "I was born in"
num = nummy + year
print(num)

print("\n")

input(
    "The password to start the quiz below is 'START'. IMPORTANT INFORMATION, tap ENTER to continue")

print("Now let's take quiz that goes over the operators that python uses \n")
password = input("What is the password to start the quiz: ")

# I used an input funtion ask the user for the password.
print("\n")
if password == "START":
    print(" You have been granted access to the Quiz!\n")

    print(
        "Quiz instructions: Choose the correct answer for each math expression below. At the end I will show you how to write the codes in python to get the answer.\n")

    score = 0
    # A DEMONSTRATION OF EACH OPERATOR WILL BE SHOWN IN THE ANSWER KEY.

    # I used "+" addition in this example to show how it works.
    # Reference: https://youtu.be/myJ36xIR7Yg. I used this video as a reference to better understad the IF and Else arguments.
    # Question 1
    print("Question 1:")
    answer_1 = input(
        "What is the solution to this expression? \n62 + 5: \nA. 66 \nB. 67 \nC. 69 \nD. 68 \nWhat is your answer: ")
    if answer_1 == "67" or answer_1 == "B":
        score += 1  # Reference: W3 schools, assignment Operators. URL: https://www.w3schools.com/python/python_conditions.asp
        print("Correct Answer")
        print("Score: ", score)
        print("\n")
    else:
        print("Wrong Answer, The answer is 67.")
        print("Score: ", score)
        print("\n")
    # I used "-" sutraction in this example to show how it can be use.
    # Question 2
    print("Question 2:")
    answer_2 = input(
        "What is the solution to this expression? \n30 - 15: \nA. 14 \nB. 13 \nC. 20 \nD. 15 \nWhat is your answer: ")
    if answer_2 == "15" or answer_2 == "D":
        score += 1  # Reference: W3 schools, assignment Operators. URL: https://www.w3schools.com/python/python_conditions.asp
        print("Correct Answer")
        print("Score: ", score)
        print("\n")
    else:
        print("Wrong Answer, The answer is 15.")
        print("Score: ", score)
        print("\n")
    # I used "/" division in this example to show how it works in the problem.
    # Question 3
    print("Question 3:")
    answer_3 = input(
        "What is the solution to this expression? \n30 / 15: \nA. 1 \nB. 2 \nC. 3 \nD. 4 \nWhat is your answer: ")
    if answer_3 == "2" or answer_3 == "B":
        score += 1  # Reference: W3 schools, assignment Operators. URL: https://www.w3schools.com/python/python_conditions.asp
        print("Correct Answer")
        print("Score: ", score)
        print("\n")
    else:
        print("Wrong Answer, The answer is 2.")
        print("Score: ", score)
        print("\n")
    # I used "*" Multiplication in this example to show its functions.
    # Question 4
    print("Question 4:")
    answer_4 = input(
        "What is the solution to this expression? \n10 * 10: \nA. 1000 \nB. 120 \nC. 100 \nD. 1 \nWhat is your answer: ")
    if answer_4 == "100" or answer_4 == "C":
        score += 1  # Reference: W3 schools, assignment Operators. URL: https://www.w3schools.com/python/python_conditions.asp
        print("Correct Answer")
        print("Score: ", score)
        print("\n")
    else:
        print("Wrong Answer, The answer is 100.")
        print("Score: ", score)
        print("\n")

    # Question 5
    print("Question 5:")
    answer_5 = input(
        "What is the solution to this expression? \n4 ** 3: \nA. 62 \nB. 65 \nC. 12 \nD. 64 \nWhat is your answer: ")
    if answer_5 == "64" or answer_5 == "D":
        score += 1  # Reference: W3 schools, assignment Operators. URL: https://www.w3schools.com/python/python_conditions.asp
        print("Correct Answer")
        print("Score: ", score)
        print("\n")
    else:
        print("Wrong Answer, The answer is 64.")
        print("Score: ", score)
        print("\n")
    # I used "**" Exponentation in this example to show how it functions.
    # Question 6
    print("Question 6:")
    answer_6 = input(
        "What is the solution to this expression? \n18 // 3: \nA. 6 \nB. 5 \nC. 4 \nD. 3 \nWhat is your answer: ")
    if answer_6 == "6" or answer_6 == "A":
        score += 1  # Reference: W3 schools, assignment Operators. URL: https://www.w3schools.com/python/python_conditions.asp
        print("Correct Answer")
        print("Score: ", score)
        print("\n")
    else:
        print("Wrong Answer, The answer is 6.")
        print("Score: ", score)
        print("\n")
    # I used "//" Floor Devision operator in this example to show how it works.
    # Question 7
    print("Question 7:")
    answer_7 = input(
        "What is the solution to this expression? \n9 % 2: \nA. 2 \nB. 1 \nC. 18 \nD. 18 \nWhat is your answer: ")
    if answer_7 == "1" or answer_7 == "B":
        score += 1  # Reference: W3 Schools, assignment Operators. URL: https://www.w3schools.com/python/python_conditions.asp
        print("Correct Answer")
        print("Score: ",
              score)  # I used "%" Modulus ooperator in this example to show how it functions.
        print("\n")
    else:
        print("Wrong Answer, The answer is 1.")
        print("Score: ", score)
        print("\n")

    if score <= 1:
        print("Your total score:", score, "- YOU NEED SOME MORE PRACTICE!")
    elif score == 6:
        print("Your total score:", score, "- YOU DID A GOOD JOB!!!")
    else:
        print("Your total score:", score, "- YOU ACED IT!!!!!")

    print("\n")
    answer_1 = input(
        "Do you wanna see the answer KEY?( Answer YES or NO Below)")
    answer_2 = input("Yes or No: ")
    print(answer_1,
          answer_2)  # Reference: W3 School. https://www.w3schools.com/python/python_operators.asp

    print("ANSWER KEY: \n")
    print("\n")
    # I used the addition operator to add 62 and 5 together.
    print("Question 1: Addition")
    num1 = 62
    num2 = 5
    print(num1 + num2)
    print("\n")
    # I used the subtraction operator to subtract the two values. 
    print("Question 2: Subtraction")
    num1 = 30
    num2 = 15
    print(num1 - num2)
    print("\n")
    # I used a Division opeerator to divide 30 by 15.                                                      
    print("Question 3: Division")
    num1 = 30
    num2 = 15
    print(num1 / num2)
    print("\n")
    # I used a Multiplication operator to multiply 10 and 10.
    print("Question 4: Multiplication")
    num1 = 10
    num2 = 10
    print(num1 * num2)
    print("\n")
    # I used an Exponentation operator to calculate the values for 4 and 3.
    print("Question 5: Exponentation")
    num1 = 4
    num2 = 3
    print(num1 ** num2)
    print("\n")
    # I used a Floor Division operator to calculate the values 18 and 3.
    print("Question 6: Floor Devision")
    num1 = 18
    num2 = 3
    print(num1 // num2)
    print("\n")
    # I used the Modulus operator to find the remainder of 9 and 2.
    print("Question 7: Modulus")
    num1 = 9
    num2 = 2
    print(num1 % num2)

    print("\n")
    input("press Enter to coninue.....")
    print("\n")
    print(
        "THANK YOU! FOR PARTICIPATING IN TESTING MY STUDYING TOOL FOR THE PCEP EXAM. DON'T FORGET TO DO THE SURVEY IN THE END.\n")
    print("I HOPE YOU GET CERTIFIED!")
    print("\n")
    print("Survey:")
    print("\n")
    print("On a scale of 1 to 10, how helpful was this studying tool? \n")
    input("What is your answer: ")
    print("\n")
    print("Thank you for the feedback! \n")

    input("Press ENTER to CLOSE!")

else:
    print('fail')
