from random import randint,shuffle
import random

def question1():

  a = randint(1, 50)
  b = randint(40, 70)
  c = randint(1, 30)
  d = randint(1, 30)
  sum = 180-b
  sum2 = b-c

  print("We know one angle is",b,"°. What is the other angle a?")
  print(sum,"°")
  print(sum-10,"°")
  print(sum+5,"°")
  print(b,"°")
  
for i in range(1,6):
  print(i,".")
  question1()
  print("")

def question2():

  a = randint(1, 180)
  b = randint(40, 70)
  c = randint(1, 30)
  d = randint(1, 30)
  sum = 180-a
  sum2 = b-c

  print("What is angle b when angle a is",a,"° ?")
  print(sum,"°")
  print(sum-10,"°")
  print(sum+5,"°")
  print(b,"°")
  
for i in range(6,11):
  print(i,".")
  question2()
  print("")

def question3():

  a = randint(90, 180)
  b = randint(40, 70)
  c = randint(1, 30)
  d = randint(1, 30)
  sum = 180-a
  sum2 = b-c

  print("What is the value of the missing angle?")
  print(a)
  print(sum,"°")
  print(sum-10,"°")
  print(sum+5,"°")
  print(b,"°")
  
for i in range(6,11):
  print(i,".")
  question3()
  print("")

from random import randint,shuffle
import random

def question4():

  a = randint(10, 90)
  b = randint(40, 70)
  c = randint(1, 30)
  d = randint(1, 30)
  sum = 180-a
  sum2 = b-c

  print("Find the value of the missing angle?")
  print(a)
  print(sum,"°")
  print(sum-10,"°")
  print(sum+5,"°")
  print(b,"°")
  
for i in range(16,21):
  print(i,".")
  question4()
  print("")


from random import randint,shuffle
import random

def question5():

  a = randint(10, 45)
  b = randint(10, 45)
  c = randint(1, 30)
  d = randint(1, 30)
  sum = 180-a-b
  sum2 = b-c

  print("Find the angle of c??")
  print(a,",",b)
  print(sum,"°")
  print(sum-10,"°")
  print(sum+5,"°")
  print(b,"°")
  
for i in range(11,16):
  print(i,".")
  question5()
  print("")
  

from random import randint,shuffle
import random

def question6():

  a = randint(60, 180)
  b = randint(10, 45)
  c = randint(1, 30)
  d = randint(1, 30)
  sum = 180-a
  sum2 = b-c

  print("In a straight line, if one angle is",a,", what is the missing angle?")
  print(sum,"°")
  print(sum-10,"°")
  print(sum+5,"°")
  print(b,"°")
  
for i in range(23,26):
  print(i,".")
  question6()
  print("")

a=randint(100,190)
interiorAngles=[144,150,175,162,174]
#interiorAngles=[60,90,108,120,135,140,144,150,175,162,174]
def questions7():
  for i in range(len(interiorAngles)):

    print(i+1,'- Calculate the size of the exterior angles of a regular polygon which has interior angles of',interiorAngles[i])

    print('correct answer =',180-interiorAngles[i])
    
    print('')
    print('wrong answer =',(180-interiorAngles[i])-1)
    print('wrong answer =',(180-interiorAngles[i])+1)
    print('wrong answer =',a)
    print('')

questions7()

a=randint(100,190)
#regularPolygon=['hexagon','pentagon','octagon','nonagon','decagon']
sidesPolygon=[6,5,8,9,10]
def questions8():
  for i in range(len(sidesPolygon)):

    print(5+(i+1),'- Calculate the size of the exterior and interior angles of ',regularPolygon[i])

    print('correct exterior =',360/sidesPolygon[i],'| correct interior =',180-(360/sidesPolygon[i]))
    print('')
    print('wrong answer =',(180-sidesPolygon[i])-1)
    print('wrong answer =',(180-sidesPolygon[i])+1)
    print('wrong answer =',a)
    print('')

questions8()

a=randint(100,190)
interiorAngles=[156,165,172,175,176,150,175,162,171,174]
exteriorAngles=[24,15,8,5,4,30,5,18,9,6]
def questions9():
  for i in range(len(interiorAngles)):

    sides=360/exteriorAngles[i]


    print(10+(i+1),'- Calculate the number of sides of a regular polygon with interior angles of ',interiorAngles[i])

    print('correct side =',sides)
    print('')
    print('wrong answer =',(180-exteriorAngles[i])-1)
    print('wrong answer =',(180-exteriorAngles[i])+1)
    print('wrong answer =',a)
    print('')

questions9()

a=randint(100,190)
interiorAngles=[156,165,172,175,176,150,175,162,171,174]
exteriorAngles=[24,15,8,5,4,30,5,18,9,6]
def questions10():
  for i in range(len(interiorAngles)):

    sides=360/exteriorAngles[i]


    print(10+(i+1),'- Calculate the number of sides of a regular polygon with interior angles of ',interiorAngles[i])

    print('correct side =',sides)
    print('')
    print('wrong answer =',(180-exteriorAngles[i])-1)
    print('wrong answer =',(180-exteriorAngles[i])+1)
    print('wrong answer =',a)
    print('')

questions10()
