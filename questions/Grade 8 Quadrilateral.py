def question1():

  a = "square"
  b = "rectangle"
  c = "rhombus"
  d = "parallelogram"
  e = "kite"
  f = "trapezium"

  A = randint(1, 50)
  B = randint(1, 50)  
  C = randint(1, 50)
  d1 = randint(6, 15)
  d2 = randint(6, 15)
  base = randint(6, 15)
  base1 = randint(6, 15)
  height = randint(6, 15)

  select1 = [a,b,c,d,e,f] 
  select = random.choice(select1)
  print(select)

  #if "square" in select1:
  if select == a: #square
    print("Find perimeter and area of square if each sides are",A)

    PerimeterSquare = A+A+A+A
    AreaSquare = A*A
    print("correct perimeter =",PerimeterSquare,"correct area =",AreaSquare)
    print("wrong perimeter = ",PerimeterSquare+1,"wrong area =",AreaSquare+1)
    print("wrong perimeter = ",PerimeterSquare-1,"wrong area =",AreaSquare-1)
    print("wrong perimeter = ",PerimeterSquare/2,"wrong area =",AreaSquare/2)

  #elif "rectangle" in select1:
  elif select==b: #rectangle
    print("Calculate the perimeter and area of",b,"if the side of a is",A,"and the side of b is",B,"?")

    PerimeterRectangle = (2*A)+(2*B)
    AreaRectangle = A*B
   

    print("correct perimeter =",PerimeterRectangle,"correct area =",AreaRectangle)
    print("wrong perimeter = ",PerimeterRectangle+1,"wrong area =",AreaRectangle+1)
    print("wrong perimeter = ",PerimeterRectangle-1,"wrong area =",AreaRectangle-1)
    print("wrong perimeter = ",PerimeterRectangle/2,"wrong area =",AreaRectangle/2)


  elif select==c: #rhombus
    print("Calculate the perimeter and area of a rhombus having diagonals equal to",d1,"and",d2,".")
    print("round up hypotenuse to 2 decimal places")

    x=d1/2
    y=d2/2
    h2=pow(x,2)+pow(y,2)

    PerimeterRhombus = 4*round(math.sqrt(h2),2)
    AreaRhombus = 1/2*d1*d2
    

   
    print("h=",round(math.sqrt(h2),2))
    print("correct perimeter =",PerimeterRhombus,"correct area =",AreaRhombus)
    print("wrong perimeter = ",PerimeterRhombus+1,"wrong area =",AreaRhombus+1)
    print("wrong perimeter = ",PerimeterRhombus-1,"wrong area =",AreaRhombus-1)
    print("wrong perimeter = ",PerimeterRhombus/2,"wrong area =",AreaRhombus/2)
 
  elif select==d:#parallelogram 
    print("Find the perimeter of a parallelogram whose slant height is",A,", and breadth is",B,".")
    print("Calculate the perimeter and area of a parallelogram having base equal to",base,"and height=",height,".")


    PerimeterParallelogram = 2*(A+B)
    AreaParallelogram  = base*height

    print("correct perimeter =",PerimeterParallelogram,"correct area =",AreaParallelogram )
    print("wrong perimeter = ",AreaParallelogram+1,"wrong area =",AreaParallelogram+1)
    print("wrong perimeter = ",AreaParallelogram-1,"wrong area =",AreaParallelogram-2)
    print("wrong perimeter = ",AreaParallelogram/2,"wrong area =",B)
 
  elif select==e:#kite

    shortSide = randint(1, 8)
    longSide = randint(10, 20)

    print("If the short side of a kite has a length of ",shortSide,", and the long side of a kite has a length of",longSide,". What is the perimeter of the kite?")
    print("Calculate the area of a kite having diagonals equal to",d1,"and",d2,".")
    
   
    PerimeterKite = (2*shortSide) + (2*longSide)
    AreaKite  = 1/2*d1*d2

    print("correct perimeter =",PerimeterKite,"correct area =",AreaKite)
    print("wrong perimeter = ",PerimeterKite+1,"wrong area =",AreaKite+1)
    print("wrong perimeter = ",PerimeterKite-1,"wrong area =",AreaKite-1)
    print("wrong perimeter = ",B,"wrong area",C)
 
  elif select==f: #trapezium

    print("Find the area of a trapezium with parallel bases of",base,"and",base1,", and a height of",height,)

    
    AreaTrapezium = 1/2*(base+base1)*height

    print("correct answer =",AreaTrapezium)
    print("wrong answer =",AreaTrapezium+1)
    print("wrong answer =",AreaTrapezium-2)
    print("wrong answer =",B)

 
for i in range(1,21):
  print(i,".")
  question1()
  print("")

def question2():

  a = "square"
  b = "rectangle"
  c = "rhombus"
  d = "parallelogram"
  e = "kite"
  f = "trapezium"
  g = "isosceles trapezium"

  select1 = [a,b,c,d,e,f] 
  select = random.choice(select1)
  print(select)

  #if "square" in select1:
  if select == a:
    print("A quadrilateral with 4 right angles and all sides of equal length. What kinds of quadrilateral is being describe?")

    print("correct answer =square")
    print("wrong answer = rectangle")
    print("wrong answer = rhombus")
    print("wrong answer = parallelogram")

  #elif "rectangle" in select1:
  elif select==b:
    print("A quadrilateral with 4 right angles . What kinds of quadrilateral is being describe?")
  
    print("correct answer =rectangle")
    print("wrong answer = square")
    print("wrong answer = rhombus")
    print("wrong answer = parallelogram")

  elif select==c:
    print("A quadrilateral with all sides of equal length. What kinds of quadrilateral is being describe?")

    print("correct answer =rhombus")
    print("wrong answer = square")
    print("wrong answer = rectangle")
    print("wrong answer = parallelogram")
 
  elif select==d:
    print("A quadrilateral with 2 sets of parallel sides. What kinds of quadrilateral is being describe?")

    print("correct answer =parallelogram")
    print("wrong answer = square")
    print("wrong answer = rhombus")
    print("wrong answer = rectangle")
 
  elif select==e:
    print("A quadrilateral with 2 pairs of equal sides . What kinds of quadrilateral is being describe?")

    print("correct answer =kite")
    print("wrong answer = square")
    print("wrong answer = rhombus")
    print("wrong answer = parallelogram")
 
  elif select==f:
    print("A quadrilateral  with 1 set of parallel sides. What kinds of quadrilateral is being describe?")

    print("correct answer =trapezium")
    print("wrong answer = square")
    print("wrong answer = rhombus")
    print("wrong answer = parallelogram")

  elif select==g:
    print("A quadrilateral  with 1 set of parallel sides and 1 pair of equal sides. What kinds of quadrilateral is being describe?")

    print("correct answer =isosceles trapezium")
    print("wrong answer = square")
    print("wrong answer = rhombus")
    print("wrong answer = parallelogram")
 
for i in range(1,21):
  print(i,".")
  question2()
  print("")
