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
