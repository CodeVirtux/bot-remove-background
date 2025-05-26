# withh=float(input('enter you nomber with: '))
# heigth=float(input('enter your nomber hiegth: '))
# total=withh*heigth
# prix=float(input('how much fo on emter: '))
# tprix= total*prix
# print('yoor area is: ', total)
# print( 'so give the man: ' ,tprix,'dh')

#================================================================

# minc=int(input('enter count second your cours: '))
# hours= minc // 3600
# mint= minc % 3600
# second= mint // 60
# print(f"hours: {hours} mint {mint} and  {second} second")

#==================================================================

# year=int(input('enter nombe year: '))
# month= year // 30
# day= year % 30
# print(f"month is {month} and days is {day}")

#=======================================================================

# qo=int(input('neter you age: '))
# if qo>0:
#     print('+')
# elif qo<0:
#     print('-')
# else:
#     print('0')

#========================================================

# num=int(input('enter your not: '))
# if num>=90:
#     print('very good')
# elif num>=75:
#     print('good')
# elif num>=50:
#     print('moyan')
# elif num<50:
#     print('low')

#=============================================================

# tic=int(input('neter number chear: '))
# if tic!=13:
#     print('welcom')
# else:
#     print('sorry')

#==================================================================

# ver=input('enter yes or no or maybe: ')
# if ver.lower()=='yes':
#     print('you type yes: ')
# elif ver.lower()=='no':
#     print('you type no')
# elif ver.lower()=='maybe':
#     print('you type maybe')
# else:
#     print('try again')

#======================================================

# coun=input('enter (tan) or (bom) or (rita): ')
# if coun.lower()== 'tan' and coun.lower()=='bom' and coun.lower()=='rita':
#     print('you wone')
# else :
#     print(f'this {coun} is folse please try again')

#============================================================
# age=int(input('enter you age please: ')).lower()
# licen=input('you have licen: ').lower()
# if age>=18 and licen=='yes':
#     print('you can drive')
# elif age<18 or licen=='no':
#     print("you can't not drive")
# else:
#     print(f"i'm sorry i dont understend this '{licen}'")

#=========================================================

# q1=input("are you from morocco? ").lower()
# if q1=='yes':
#     q2=input('you age is abave 18? ').lower()
#     if q2=='yes':
#         print('you can use the app ✅')
#     else :
#         print('sorry can no not use the app ❌')
# else:
#     print('we want just the moroccing pepeol! ')

#============================================================

# print('''

#  .d8888b.                888         888     888 d8b         888                      
# d88P  Y88b               888         888     888 Y8P         888                      
# 888    888               888         888     888             888                      
# 888         .d88b.   .d88888  .d88b. Y88b   d88P 888 888d888 888888 888  888 888  888 
# 888        d88""88b d88" 888 d8P  Y8b Y88b d88P  888 888P"   888    888  888 `Y8bd8P' 
# 888    888 888  888 888  888 88888888  Y88o88P   888 888     888    888  888   X88K   
# Y88b  d88P Y88..88P Y88b 888 Y8b.       Y888P    888 888     Y88b.  Y88b 888 .d8""8b. 
#  "Y8888P"   "Y88P"   "Y88888  "Y8888     Y8P     888 888      "Y888  "Y88888 888  888 
                                                                                      
                                                                                      
                                                                                      

# ''')
# print('welcom to my dark web hhh')
# print('you have two doors : red🚪and blue🚪  ')
# door=input(' so what is the door you make?').lower()
# if door=='blue':
#     print('''!!opes you chese the crocoday door
#     game over 🐊
#     ''')

# elif door=='red':
#     print('you foand three box: 🎁whit , 🎁black , 🎁green ')
#     box=input('which the box do you open? ').lower()
#     if box=='whit':
#         print('!! opes you open a box filad wich snaks 🐍')
#     elif box=='black':
#         print('!! opes you open a box filad wich spiders🕸️ ')
#     elif box=='green':
#         print('cangratulation! you found the tresher! 💰💸 ')
#     else:
#         print('invaled choise 🤷‍♂️ , please choise 🎁whit ,or 🎁black ,or 🎁green')

# else:
#     print('invaled choise 🤷‍♂️🤷‍♂️')

#==============================================================================

# print('welcom to test ')
# q1=input('you are moroking? ')
# q2=input('''You are standing now at the train station
# what will you take: a taxi🚕, a bus🚌 or a horse🐴 ?''').lower()
# if q2=='horse':
#     print('If you knew how to ride')
# elif q2=='bus':
#     print('is no tworking in morocco ❌')
# elif q2=='taxi':
#     print('Correct choice✅')
#     print('you have three taxi: "whit🤍" and "red❤️" and "green💚"')
#     q3=input('what is the taxi do you want?').lower()
#     if q3=='green':
#         print('this color is Not available in taxi')
#     elif q3=='red':
#         print('He is also not here , We are not in Paris hh')
#     elif q3=='whit':
#         q4=input('Pay cash or visa?').lower()
#         if q4=='visa':
#             print('Where are you from? There is no visa in Morocco.')
#         elif q4=='cash':
#             print('You are now Moroccan 🎉🎉🎉')
#         else:
#             print('!! opes,please type  :cash or visa ')
#     else:
#         print('!! opes, please type : "whit🤍" or "red❤️" or "green💚" ')
# else :
#     print('!! opes , please type taxi or bus or horse ')

#=================================================================

# import random
# num0=random.randint(1000,9999)
# num=int(input('enter code have four nomber: '))
# if len(str(num))==4:
#     if num==num0:
#         print('congratiltion🎉🎉')
#     else:
#         print(f'the code is not corect the resolet corect is "{num0}"')
# else:
#     print('please enter foor nomber')

#========================================================================

# import random
# print('welcome to best game🖐️🎯')
# # input('enter star if you ready to play')
# play=random.randint(0,1)
# if play>=1:
#     print('head')
# else:
#     print('star')

#================================================================
# import random
# print('welocm to my play🙂')
# way=input('''
# chose a method to toss the coin:
# 1.using random.random()
# 2.using random.randint()
# enter your choice (1 or 2):
# ''')
# ran1= random.randint(0,1)
# ran2= random.random()
# use=input('enter your Guess (heads or Tails): ')
# if way==ran1 or way==ran2:
#     if use==ran1 or use==ran2:
#         print('''
#         congratulations! You won!
#         the computer's coin toss result was: {ran1}
#         ''')
#     else:
#         print('''
#         sorry, you lost!
#         the computer's coin toss result was: {ran1}
#         ''')
# else:
#     print('invalid choise. please select either 1 or 2.')

#==============================

