# import turtle
# import time
#
# my_turtle = turtle.Turtle()
#
# def square(num):
#     my_turtle.forward(num)
#     my_turtle.right(90)
#     my_turtle.forward(num)
#     my_turtle.right(90)
#     my_turtle.forward(num)
#     my_turtle.right(90)
#     my_turtle.forward(num)
#
# square(250)
# time.sleep(5)



# import random
#
# #create a list of play options
# t = ["Rock", "Paper", "Scissors"]
#
# #assign a random play to the computer
# computer = t[random.randint(0,2)]
#
# #set player to False
# player = False
#
# while player == False:
# #set player to True
#     player = input("Rock, Paper, Scissors?")
#     if player == computer:
#         print("Tie!")
#     elif player == "Rock":
#         if computer == "Paper":
#             print("You lose!", computer, "covers", player)
#         else:
#             print("You win!", player, "smashes", computer)
#     elif player == "Paper":
#         if computer == "Scissors":
#             print("You lose!", computer, "cut", player)
#         else:
#             print("You win!", player, "covers", computer)
#     elif player == "Scissors":
#         if computer == "Rock":
#             print("You lose...", computer, "smashes", player)
#         else:
#             print("You win!", player, "cut", computer)
#     else:
#         print("That's not a valid play. Check your spelling! FYI first letter capital...")
#     #player was set to True, but we want it to be False so the loop continues
#     player = False
#     computer = t[random.randint(0,2)]

