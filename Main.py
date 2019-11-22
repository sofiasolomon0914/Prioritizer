"""

This is my main file for this program
__author__ = Sofia Solomon
This program will help people prioritize their activities and interests,
hopefully leaving them more relaxed and organized.

"""

# Print welcome statement
print("\nHello, Welcome to Prioritizer! This program will help you organize "
      "\nall of your responsibilities, activities, and interests. This "
      "\nprogram is ideal for people who hate having their lives controlled "
      "by "
      "\nrigid schedules and planners but at the same time like feeling "
      "\norganized. This program will first ask you questions concerning you "
      "\nresponsibilities, involvements, and interests. It will then go one "
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
pursue_first = str(input("\nThink of interests you have wanted to pursue for "
                         "\nsome time. This can be projects, books, classes, "
                         "\nor hobbies you have wanted to start. You can only "
                         "choose five.\n\nEnter your first activity: "))
pursue_second = str(input("\nEnter you second activity: "))
pursue_third = str(input("\nEnter your third activity: "))
pursue_fourth = str(input("\nEnter your fourth activity: "))
pursue_fifth = str(input("\nEnter your fifth activity: "))
"""
Now, ask the user to input any appointments of commitments they have for the
upcoming week. Program will keep asking user for inputs until they type no.
"""
print("\nCongratulations you finished the first part! Now it is time to "
      "\norganize your appointments and commitments. First you will be "
      "\nasked about the upcoming week, then the upcoming month, "
      "\nand finally the upcoming year. ")
