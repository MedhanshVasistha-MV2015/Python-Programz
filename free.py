from datetime import date, datetime
import turtle
import random
screen = turtle.Screen()
screen.bgcolor("white")
turtle.title('Loading...')
turtle.speed(1) 
turtle.color("black", random.choice(['red', 'green', 'blue', 'yellow', 'orange', 'purple']))
radius = 100
turtle.penup()
turtle.title('Loaded 25%') 
turtle.goto(0, -radius)
turtle.title('Loaded 50%') 
turtle.pendown()
turtle.title('Loaded 90%')
turtle.begin_fill() 
turtle.circle(radius)
turtle.end_fill()
turtle.title('Please close this window to continue...') 
turtle.hideturtle()

print('Loading complete.')

tnc = input(str('Do you want to read the terms and conditions? (Y/N): '))
if tnc == 'Y' or tnc == 'y':
    print('Terms and Conditions: \n 1. This program is for Coding purposes only. \n 2. The user must provide accurate information when prompted. \n 3. The program does not store any personal data entered by the user. \n 4. The user is responsible for any actions taken based on the information provided by the program. \n 5. Codingal has the right to modify or terminate the program at any time without prior notice. \n 6. By using this program, the user agrees to these terms and conditions.')
elif tnc == 'N' or tnc == 'n':
    print('You have chosen not to read the terms and conditions.') 
    class Time:
        def __init__(self, hour, minute):
            self.hour = hour
            self.minute = minute

    class Date:
        def __init__(self, day, month, year):
            self.day = day
            self.month = month
            self.year = year
    
    class DateTime(Date, Time):
        def __init__(self, day, month, year, hour, minute):
            Date.__init__(self, day, month, year)
            Time.__init__(self, hour, minute)
            self.user_name = None

        def display(self, user_name=None):
            if user_name is None:
                self.user_name = input(str('Please enter your name: '))
            else:
                self.user_name = user_name
            print('Hello, ', self.user_name, ', You have registered for the Date and Time program!')
            print('The date is: ', self.day,'/', self.month,'/', self.year)
            print('The time is: ', self.hour,':', self.minute)

    obj = DateTime(date.today().day, date.today().month, date.today().year, datetime.now().hour, datetime.now().minute)
    obj.display()
    print('Thank you for using the Date and Time program ', obj.user_name, '! We hope you found it useful. Have a good day!')
else:
    print('Invalid input. Please enter Y or N.')


