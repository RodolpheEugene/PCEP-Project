# Rodolphe Eugene
# This program is a studying tool for the PCEP- Cerftified Entry-Level Python Programmer Certification Exam and it will breakdown the programming concepts.
# There will be some practice questions and interactive activities along the way to make the process a lot more fun.

# Received help from Andrew Krupp. He helped me with the def functions.
# Received help from Robert McNiven Jr.
# Reference: Robert McNiven Jr, he reminded me to to use "\n" for line spacing.
# Received help from Paulo Drefahl. He helped me with the def functions
def user_age_for_movie(user_age):
    pass


def main():
    # I used "def main()" to define the line of codes below and I called it at the end by writing "main()".
    print("HELLO! My name is Rodolphe Eugene. Welcome to my studying tool.\n")
    print(
        "Using this studying tool will help you get your certificate for the"
        " PCEP Examp!")
    print(
        "This program will help you prepare for the PCEP Certification "
        "Exam. \nThere will be some questions to answer for practice "
        "along the way\n")
    print("This is an example of how simple input and output can be used:\n")
    # I used a -for, -in, and -range to print 3 lines repeating "Hello".
    first_1 = 0
    for first_1 in range(4):
        print("HELLO, " * first_1)
    # I used the * string literal above to ask the program to print "Hello" in 3 lines inside the "for" loop..
    print("\n")
    name = input("What is your name? \n")
    print("\n")
    print("Tell me about yourself", name)
    print("\n")
    movie = input("what is your favorite movie to watch? \n")
    print("I will keep that in mind that your favorite movie is", movie)
    user_age = user_information()
    user_age_for_movie(user_age)


def user_information():
    print("\n")

    input("Where are you from? \n")

    input("What is your favorite color? \n")

    age = int(input("what is your age? "))
    print("Great!!! " * 2)
    # I used the "*" string literal to command the program to display "Great!!!" two times.
    print("\n")
    # I used an input function to command the user to press ENTER to continue.
    input("press ENTER continue.....\n")

    print("This first example wasn't too bad,",
          "Now let's move on to more deeper concepts in programming.\n")

    print(
        "Now, Let's go over an example of how you can use the 'end=' "
        "and 'sep=' "
        "argument to format a print output.\n")
    # the "end=" statement can be use to space out sentences as well or you can input information inside the quotes too.
    print("Example: \nNow that you have told me your favorite movie", end=". ")
    print("\n")
    print("It seems that you are really into that movie that you "
          "picked", end=". ")
    print("Now we're gonna move on to using the sep = argument", end=".\n")
    print("\n")
    input("press ENTER to continue..... \n")

    # I used the "sep=" argument in the example below. the "sep=" can be use to seperate sentences.
    num_first = 5
    num_second = 6
    print("num_first", num_first, sep=": ")
    print("num_second", num_second, sep=": ")
    print("\n")
    print(
        "If I want to solve the input above by addition, I can "
        "write this code below to get:\n")
    num_first = 5
    num_second = 6
    print(
        num_first + num_second)  # I used the "+" addition operator to show an example of how it can be use above.
    print("\n")
    print(
        "As demonstrated in the sentences above, this is a way the end = and "
        "sep = argument can be implemented to combine and seperates sentences "
        "\n")

    print("\n")
    # I used a  "+" string literal to combine the two strings. Python will not let you combine string with an integer.
    print("Here is one instance where you can use the + string literal\n")
    year = "2000"
    nummy = "I was born in"
    num = nummy + year
    print(num)
    print("\n")
    print("This is an example of how parameter passing functions in python.\n")

    # I used the def function to write a function that accepts parameters using simple addition.
def simple_addition(number_1, number_2):
    answer = number_1 + number_2
    print("number_1 is", number_1)
    print("number_2 is", number_2)
    print(answer)

    simple_addition(6, 5)

    print("\n")
    print("Now, I will demonstrate the easiest way to implement the and "
          "boolean operator.\n")
    first_value = False
    second_value = True
    # I used the "and" boolean operator to make a comparison between two expressions.
    if first_value and second_value:
        print("Both first value and second value are True")
    else:
        print("First value is False or second value is False or "
              "both first value and second value are false")
    print("\n")
    print("complete this exercise where =<, >= and != relational "
          "operator were used to determine how much you have to "
          "pay to go see a movie.\n")

    age = 0

def user_age_for_movie(age):
    pass
    while age != 100:
        # I used != because I am saying when the age is not 70, the person have to pay a certain amount to go see the movie.
        age = int(input("What is your age: "))
        if age >= 10 and age <= 100:
            age = 100
            print("Your ticket price is $15")
            # I used a greater than, less than or equal below because if the person's age is less than 10, they are supposed to pay less for the movie.
        elif age <= 10 and age >= 1:
            age = 100
            print("Your ticket price is $0.")
        else:
            age = 100
            print('You are not allowed to go see the movie')


    print("\n")
    input('Press Enter to continue: \n')
    print("Another useful boolean operator that python uses is -not operator. "
          "Here is an example of how it works in python:")
    # I used the boolean operator -not to signfify that when something is not true, it is false and vice versa.
    variable_1 = True
    variable_2 = not variable_1
    print("not", variable_1, "is:", variable_2)

    variable_3 = False
    variable_4 = not variable_3
    print("not", variable_3, "is:", variable_4)

    print("\n")
    input(
        "The password to start the quiz below is 'START'. IMPORTANT " \
        "INFORMATION, tap ENTER to continue")

    print("Now let's take quiz that goes over the operators that python uses")

    # I used an input function ask the user for the password.
    print("\n")
    # I used a while statement to continue to ask the user for the password, until the user enters the right one.

    password = ""
    while True:
        password = input("What is the password to start the quiz: ")
        if password == "START" or password == "start":
            print("You have been granted access to the Quiz!\n")
            # I used -or above because I want the program to accept both versions of the password START and start.
            print(
                "Quiz instructions: Choose the correct answer for each math"
                " expression below. At the end I will show you how to "
                "write the codes in python to get the answer.\n")
            score = 0
            # A DEMONSTRATION OF EACH OPERATOR WILL BE SHOWN IN THE ANSWER KEY.

            # I used "+" addition in this example to show how it works.
            # Reference: https://youtu.be/myJ36xIR7Yg. I used this video as a reference to better understad the IF and Else arguments.
            # Question 1
            print("Question 1:")
            answer_1 = input(
                "What is the solution to this expression? \n62 + 5: "
                "\nA. 66 \nB. "
                "67 \nC. 69 \nD. 68 \nWhat is your answer: ")
            # I used an -if, -else statement because I want to check if the user inputs the correct answer.
            if answer_1 == "67" or answer_1 == "B":
                # I used the equal "==" relational operator and "or" boolean operator accept two different versions of the same answer.
                score += 1  # Reference: W3 schools, assignment Operators. URL: https://www.w3schools.com/python/python_conditions.asp
                print("Correct Answer")
                print("Score: ", score)
                print("\n")
            else:
                print("Wrong Answer, The answer is 67.")
                print("Score: ", score)
                print("\n")
            # I used "-" subtraction in this example to show how it can be use.
            # Question 2
            print("Question 2:")
            answer_2 = input(
                "What is the solution to this expression? \n30 - 15: "
                "\nA. 14 \nB. "
                "13 \nC. 20 \nD. 15 \nWhat is your answer: ")
            if answer_2 == "15":
                score += 1  # Reference: W3 schools, assignment Operators. URL: https://www.w3schools.com/python/python_conditions.asp
                print("Correct Answer")
                print("Score: ", score)
                print("\n")
            elif answer_2 == "D":
                score += 1
                print("Corret Answer")
                print("Score: ", score)
                print("\n")
            else:
                print("Wrong Answer, The answer is 15.")
                print("Score: ", score)
                print("\n")
            # I used the conditional statements -if, -elif, -else instead of the -or operator to accept two different versions of the same answer.
            # I used "/" division in this example to show how it works in the problem Question 3.
            print("Question 3:")
            answer_3 = input(
                "What is the solution to this expression? \n30 / 15: \nA. 1 "
                "\nB. 2 \nC. 3 \nD. 4 \nWhat is your answer: ")
            if answer_3 == "2" or answer_3 == "B":
                score += 1  # Reference: W3 schools, assignment Operators. URL: https://www.w3schools.com/python/python_conditions.asp
                # I used the "+=" shortcut operator to add the total to variable "total= 0". Also, I used it to look cool.
                print("Correct Answer")
                print("Score: ", score)
                print("\n")
            else:
                print("Wrong Answer, The answer is 2.")
                print("Score: ", score)
                print("\n")
            # I used "*" Multiplication in this example to show its functions question 4
            print("Question 4:")
            answer_4 = input(
                "What is the solution to this expression? \n10 * "
                "10: \nA. 1000 "
                "\nB. 120 \nC. 100 \nD. 1 \nWhat is your answer: ")
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
            # I used the boolean -or operator to accept 64 and D as the correct answer.
            print("Question 5:")
            answer_5 = input(
                "What is the solution to this expression? \n4 ** "
                "3: \nA. 62 \nB. "
                "65 \nC. 12 \nD. 64 \nWhat is your answer: ")
            if answer_5 == "64" or answer_5 == "D":
                score += 1  # Reference: W3 schools, assignment Operators. URL: https://www.w3schools.com/python/python_conditions.asp
                print("Correct Answer")
                print("Score: ", score)
                print("\n")
            else:
                print("Wrong Answer, The answer is 64.")
                print("Score: ", score)
                print("\n")
            # I used "**" Exponentation in this example to show how it functions Question 6.
            print("Question 6:")
            answer_6 = input(
                "What is the solution to this expression? \n18 // "
                "3: \nA. 6 \nB. 5 \nC. 4 \nD. 3 \nWhat is your answer: ")
            if answer_6 == "6" or answer_6 == "A":
                score += 1  # Reference: W3 schools, assignment Operators. URL: https://www.w3schools.com/python/python_conditions.asp
                print("Correct Answer")
                print("Score: ", score)
                print("\n")
            else:
                print("Wrong Answer, The answer is 6.")
                print("Score: ", score)
                print("\n")
            # I used "//" Floor Division operator in this example to show how it
            # works.
            # Question 7
            print("Question 7:")
            answer_7 = input(
                "What is the solution to this expression? \n9 % "
                "2: \nA. 2 \nB. 1 \nC. 18 \nD. 19 \nWhat is your answer: ")
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
            # I used -if, -elif, -else statements to create a system that keeps track of how many answers the user answers correct and offer feedback.
            if score <= 3:
                print("Your total score:", score, "- YOU "
                                                  "NEED SOME MORE PRACTICE!")
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
            print("On a scale of 1 to 10, how helpful was "
                  "this studying tool? \n")
            input("What is your answer: ")
            print("\n")
            print("Thank you for the feedback! \n")

            input("Press ENTER to CLOSE!")
            break

        else:
            print('Wrong Password. Please try again!')


main()
