"""

This is my main file for this program
__author__ = Sofia Solomon
This program will help people prioritize their activities and interests,
hopefully leaving them more relaxed and organized.

"""
import random

# Print welcome statement
print("\nHello, Welcome to Prioritizer! This program will help you organize "
      "\nall of your responsibilities, activities, and interests. This "
      "\nprogram is ideal for people who hate having their lives controlled "
      "by "
      "\nrigid schedules and planners but at the same time like feeling "
      "\norganized. This program will first ask you questions concerning you "
      "\nresponsibilities, involvements, and interests. It will then go on "
      "to "
      "\nask you about upcoming appointments and commitments. Finally, "
      "\nthis program will present all the information you entered but in an "
      "\norganized format that you can hopefully use for your benefit. "
      "Enjoy! ")

"""
First, ask the user what their major responsibilities are. The user may only
input three activities. Save these activities as variables.
"""
responsibility_first = str(input("\nThink of your major responsibilities. "
                                 "This "
                                 "can include work, school,\nfamily "
                                 "obligations, ect. You will only be "
                                 "aloud "
                                 "to enter three, so choose "
                                 "wisely.\n\nEnter "
                                 "your first major responsibility: "))
responsibility_second = str(input("\nEnter a second major "
                                  "responsibility: "))
responsibility_third = str(input("\nEnter your third major "
                                 "responsibility: "))
"""
Second, ask the user other activities and hobbies they engage in frequently. 
The user may only choose four activities. Store these activities as variables.
"""
activity_first = str(input("\nThink of activities you engage in besides your "
                           "\nmajor responsibilities. This can include "
                           "\nsports/exercise, an art class, important "
                           "\nhobbies, ect. Choose wisely as you can only "
                           "submit three.\n\nEnter your first activity: "))
activity_second = str(input("\nEnter your second activity: "))
activity_third = str(input("\nEnter your third activity: "))
"""
Third, ask the user to enter any projects, interests, or hobbies they want 
to begin. There can only be five. Save them all as variables.
"""
interest_first = str(input("\nThink of interests you have wanted to pursue "
                           "for \nsome time. This can be projects, books, "
                           "classes, \nor hobbies you have wanted to start. "
                           "You can only choose five.\n\nEnter your first "
                           "activity: "))
interest_second = str(input("\nEnter you second activity: "))
interest_third = str(input("\nEnter your third activity: "))
interest_fourth = str(input("\nEnter your fourth activity: "))
interest_fifth = str(input("\nEnter your fifth activity: "))
print("\nCongratulations you finished the first part! Now it is time to "
      "\norganize your appointments and commitments. First you will be "
      "\nasked about the upcoming week, then the upcoming month, "
      "\nand finally the upcoming year. This does not include your "
      "\nwork schedule or class times, this refers to doctors "
      "\nappointments, going out with friends, vacations, ect. Things that "
      "\nare not part of your regular routine.")


def activity():
    """
The following summarizes all the information entered by the user. It prints the
information so the user can see it.
    """
    print("\nYour major responsibilities include:\n      " +
          responsibility_first +
          ", "
          + responsibility_second + ", " + responsibility_third +
          ". \nActivities that you are involved in besides your major "
          "responsibilities include:\n      " + activity_first + ", " +
          activity_second + ", " + activity_third +
          ". \nInterests and activities you would like to begin or pursue "
          "include:\n      " + interest_first + ", " + interest_second + ", "
          + interest_third + ", " + interest_fourth + ", " + interest_fifth +
          ".")


"""
Now, ask the user to input any appointments of commitments they have for the
upcoming week. Program will keep asking user for inputs until they type no. 
Each input should be stored to a new variable.
"""
list_week = []
variable_week = str(input("\nDo you have any appointments, meetings, "
                          "\nor other commitments scheduled for this "
                          "coming week? \nPlease answer yes or no: "))
week_activities = True
while week_activities:
    if variable_week == "yes":
        week_activity = str(input("\nEnter an appointment/commitment "
                                  "scheduled for this week. Enter the "
                                  "\nname of the activity followed by the "
                                  "day and time. If no more activities "
                                  "\nto enter, then enter no.(Example: "
                                  "Doctor apt Thursday at 3pm) "
                                  "\nEnter here: "))
        if week_activity == "no":
            week_activities = False
        else:
            list_week.append(week_activity)
    elif variable_week == "no":
        print("Yay, you are now finished with this weeks commitments! Now "
              "it's time to go over appointments for this coming month.")
        week_activities = False
week = str(len(list_week))
list_month = []
variable_month = str(input("\nDo you have any appointments, meetings, "
                           "or other commitments scheduled for this coming "
                           "month? \nThese do not include the activities "
                           "entered in the week section. \nPlease answer yes "
                           "or no:  "))
month_activities = True
while month_activities:
    if variable_month == "yes":
        month_activity = str(input("\nEnter an appointment/commitment "
                                   "scheduled for this month. Enter the "
                                   "\nname of the activity followed by the "
                                   "day and time. If no more activities "
                                   "\nto enter, then enter no.(Example: "
                                   "Hawaii vacation Mon-Fri 6pm leave) "
                                   "\nEnter here: "))
        if month_activity == "no":
            month_activities = False
        else:
            list_month.append(month_activity)
    elif variable_month == "no":
        print("Yay, you are now finished with this months commitments! \nNow "
              "it's time to go over dates for this coming year.")
        month_activities = False
month = str(len(list_month))
list_year = []
variable_year = str(input("\nDo you have any appointments, meetings, "
                          "\nor other commitments scheduled for this "
                          "coming year? \nPlease answer yes or no: "))
year_activities = True
while year_activities:
    if variable_year == "yes":
        year_activity = str(input("\nEnter any commitments "
                                  "scheduled for this year. Usually this "
                                  "\nwill include vacation trips, reunions, "
                                  "weddings, ect. Not holidays and stuff "
                                  "like that.Enter the "
                                  "\nname of the activity followed by the "
                                  "month and day. If no more activities "
                                  "\nto enter, then enter no.(Example: "
                                  "Wedding June 4) "
                                  "\nEnter here: "))
        if year_activity == "no":
            year_activities = False
        else:
            list_year.append(year_activity)
    elif variable_year == "no":
        print("Congratulations!!! You have now completed all the questions! "
              "\nBelow you can find all the information you entered. Enjoy!")
        year_activities = False
year = str(len(list_year))

activity()

"""
The following will print the information in regard to upcoming appointment
and commitments for the week, month, and year in a user-friendly format.
"""
print("\nYou have " + week + " activities this week. They include:")
for x in list_week:
    print(x, end=', ')
print("\n\nYou have " + month + " activities this coming month. They "
                                "include:")
for x in list_month:
    print(x, end=', ')
print("\n\nYou have " + year + " important dates this coming year. They "
                               "include:")
for x in list_year:
    print(x, end=', ')
print("\n\nGood job! Now that you have done all the hard work you can play "
      "\na fun guessing game our programmer set up for you. If do not want "
      "\nto go ahead and exit out of the program. ")
n = random.randrange(1, 99)
guess = int(input("\nEnter an integer from 1 to 99: "))
while n != "guess":
    if guess < n:
        print("The guess is too low, try a higher number!")
        guess = int(input("Enter an integer from 1 to 99: "))
    elif guess > n:
        print("The guess is too high, try a lower number!")
        guess = int(input("Enter an integer from 1 to 99: "))
    else:
        print("Yay, you guessed it!")
        break
