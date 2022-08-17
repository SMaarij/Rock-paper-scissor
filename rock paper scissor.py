Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# import random
#
#
#
# comp=print('Computer Turn: Rock(R),Paper(P) or Scissor(S),\n(The computer has chosen it\'s choice secretly) ')
# rand=random.randint(1,3)
# if rand==1:
#     comp='R'
# elif rand==2:
#     comp='P'
# elif rand==3:
#     comp='S'
# p2=input('Your choice: Rock(R),Paper(P) or Scissor(S):')
#
#
#
# def gamewin(comp,p2):
#     if comp==p2:
#         return False
#     elif comp=='R':
#         if p2=='P':
#             return True
#         elif p2=='S':
#             return False
#
#     elif comp=='P':
#         if p2=='R':
#             return False
#         elif p2=='S':
#             return True
#
#     elif comp=='S':
#         if p2=='R':
#             return True
#         elif p2=='P':
#             return False
#
#
# a=gamewin(comp,p2)
# if comp==p2:
#     print('The game is a tie')
#
# elif a:
#     print('You won the game congratulations')
#
# else :
#     print('You lost the game,better luck next time')
#
# print(f'The computer chose {comp}')
# print(f'The player chose {p2}')