#@title requirements
import matplotlib
import matplotlib.pyplot as plt 
from random import randint 
from random import randint,shuffle
from io import BytesIO
import base64
import requests,json


class Q_type:
  multichoice="multichoice"
  singlechoice="singlechoice"
  photo="photo"
  shortreply="shortreply"

def send(info):
  url="https://thebotserver.herokuapp.com/api/broadcast/64"
  #url="https://vocab.ngrok.io/api/broadcast/64"
  payload={
      #"message":{"photo":info},
      "message":info,
  }
  headers={
      "Content-Type":'application/json'
  }
  r=requests.request("POST",url,headers=headers,data=json.dumps(payload))
  print(r)
  
  import random
def workout_Que():

    n1 = random.randint(0, 100)
    n2 = random.randint(1, 15)
    n3 = random.randint(1, 15)

    correctAns = n1 - n2 * n3
    choices = [correctAns] #initialise choices with the correct answer
    #Make 3 more wrong answer so it makes up to 4 choices for the MCQ
    for _ in range(3):
        while(True):
            wrongAns = correctAns + random.choice([i for i in range(-20, 20) if i != 0])
            if wrongAns not in choices: #if the answer is not already in the list, append it
              choices.append(wrongAns)
              break

    random.shuffle(choices) #shuffle the choices including the correct and wrong answers

    question = f"""\
    1  Work out:
                           {n1} - {n2} x {n3}
                           
    A. {choices[0]}
    B. {choices[1]}
    C. {choices[2]}
    D. {choices[3]}

    Answer: {correctAns} """

    #just to convert to png
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1]) #add_axes(rect) where rect = [x0, y0, width, height]
    plt.axis('off')

    ax.text(0.1, 0.5, question,
        horizontalalignment='left',
        verticalalignment='center',
        fontsize=15, color='black',
        transform=ax.transAxes)

    #this is to convert the graph to the text format to send
    #plt.show() #show the figure
    image = BytesIO()
    plt.savefig(image, format='png')
    image.seek(0)
    I=base64.encodebytes(image.getvalue())
    return {"photo": I.decode(), "Type":Q_type.multichoice, "Author":"Bennie"}

    # the send command is to send to the group, just make sure the cell, first cell, has been run before
send(workout_Que())

import random
def listOutPrimes():

    n1 = random.choice([i for i in range(10, 101) if i % 10 == 0])
    n2 = n1 + 10
    correctAns = []
    for i in range(n1, n2+1):
        isPrime = True
        for j in range(2, i):
            if (i % j == 0): #check if number is prime
                isPrime = False
                break
        if (isPrime):
            correctAns.append(i)

    choices = [correctAns] #initialise choices with the correct answer
    #Make 3 more wrong answer so it makes up to 4 choices for the MCQ
    for _ in range(3):
        while(True):
            exist = False
            wrongAns = []
            for _ in range(random.randint(2, 9)): #create a random list of number to make wrong answer
                n = random.randint(n1, n2)
                if (n not in wrongAns):
                    wrongAns.append(n)
            for i in choices:
                i.sort()
                wrongAns.sort()
                if wrongAns == i: #if the answer is already in the list, break current loop
                  exists = True
                  break
            if (not exist):
                choices.append(wrongAns)
                break

    random.shuffle(choices) #shuffle the choices including the correct and wrong answers

    question = f"""\
    2  Write down the prime numbers
        between {n1} and {n2}:

    A. {choices[0]}
    B. {choices[1]}
    C. {choices[2]}
    D. {choices[3]}

    Answer: {correctAns} """

    #just to convert to png
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1]) #add_axes(rect) where rect = [x0, y0, width, height]
    plt.axis('off')

    ax.text(0.1, 0.5, question,
        horizontalalignment='left',
        verticalalignment='center',
        fontsize=15, color='black',
        transform=ax.transAxes)

    #this is to convert the graph to the text format to send
    #plt.show() #show the figure
    image = BytesIO()
    plt.savefig(image, format='png')
    #plt.savefig('image.png')
    image.seek(0)
    I=base64.encodebytes(image.getvalue())
    return {"photo": I.decode(), "Type":Q_type.multichoice, "Author":"Bennie"}

    # the send command is to send to the group, just make sure the cell, first cell, has been run before
send(listOutPrimes())

import random
import inflect
def words_to_figures():
    p = inflect.engine()
    # a)
    correctAns = random.randint(5000, 100000)
    figures = p.number_to_words(correctAns)

    choicesA = [correctAns] #initialise choices with the correct answer
    #Make 3 more wrong answer so it makes up to 4 choices for the MCQ
    for _ in range(3):
        while(True):
            if (random.choice([0,1])):
                wrongAnswer = correctAns / random.choice([10, 100, 1000])
            else:
                wrongAnswer = correctAns * random.choice([10, 100])
            if wrongAnswer not in choicesA:
                choicesA.append(wrongAnswer)
                break
    # b)
    SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
    correctAnsB = correctAns
    for i in range(len(str(correctAns))-1):
        correctAnsB /= 10
    correctAnsB = float(('%.5f' % correctAnsB).rstrip('0').rstrip('.'))

    choicesB = [len(str(correctAns))-1]

    for _ in range(3):
        while(True):
            wrongAnswerB = len(str(correctAns))-1 + random.randint(-5, 5)
            if wrongAnswerB not in choicesB:
                choicesB.append(wrongAnswerB)
                break

    random.shuffle(choicesA) #shuffle the choices including the correct and wrong answers
    random.shuffle(choicesB) #shuffle the choices including the correct and wrong answers
    question = f"""\
    4  A city has a population of
    {figures}.

    Write the size of the population

    (a) in figures,
        A. {choicesA[0]}
        B. {choicesA[1]}
        C. {choicesA[2]}
        D. {choicesA[3]}
    Answer: {correctAns}

    (b) in standard form,
        A. {correctAnsB} x 10{(str(choicesB[0])).translate(SUP)}
        B. {correctAnsB} x 10{(str(choicesB[1])).translate(SUP)}
        C. {correctAnsB} x 10{(str(choicesB[2])).translate(SUP)}
        D. {correctAnsB} x 10{(str(choicesB[3])).translate(SUP)}
    Answer: {correctAnsB} x 10{str(len(str(correctAns))-1).translate(SUP)} """

    #just to convert to png
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1]) #add_axes(rect) where rect = [x0, y0, width, height]
    plt.axis('off')

    ax.text(0.1, 0.5, question,
        horizontalalignment='left',
        verticalalignment='center',
        fontsize=15, color='black',
        transform=ax.transAxes)

    #this is to convert the graph to the text format to send
    #plt.show() #show the figure
    image = BytesIO()
    plt.savefig(image, format='png')
    #plt.savefig('image.png')
    image.seek(0)
    I=base64.encodebytes(image.getvalue())
    return {"photo": I.decode(), "Type":Q_type.multichoice, "Author":"Bennie"}

    # the send command is to send to the group, just make sure the cell, first cell, has been run before
send(words_to_figures())

import random
import math
def significant_figure():

    # a)
    n1 = round(random.uniform(0, 30), 1)
    n2 = round(random.uniform(0, 30), 5)
    n3 = round(random.uniform(0, 30), 2)
    significant_num = random.randint(1, 4)
    figure = r'$\frac{{ {} \times {} }}{{ {} }}$'.format(n1, n2, n3)

    n1_correct = round(n1, significant_num - int(math.floor(math.log10(abs(n1)))) - 1)
    n2_correct = round(n2, significant_num - int(math.floor(math.log10(abs(n2)))) - 1)
    n3_correct = round(n3, significant_num - int(math.floor(math.log10(abs(n3)))) - 1)
    figure_correct = r'$\frac{{ {} \times {} }}{{ {} }}$'.format(n1_correct, n2_correct, n3_correct)

    choicesA = [figure_correct] #initialise choices with the correct, then generate 3 wrong answer to make up MCQ

    #generate wrong answers
    for _ in range(3):
        while(True):
            n1_wrong = n1_correct + random.randint(-1, 1)
            n2_wrong = round(n2, (random.choice([i for i in range(1, 5) if i != significant_num])) - int(math.floor(math.log10(abs(n2)))) - 1)
            #n2_wrong = n2_correct + round(random.uniform(-2, 2), random.choice([1, 2, 3]))
            n3_wrong = round(n3, (random.choice([i for i in range(1, 5) if i != significant_num])) - int(math.floor(math.log10(abs(n2)))) - 1)
            #n3_wrong = n3_correct + round(random.uniform(-2, 2), 2)
            figure_wrong = r'$\frac{{ {} \times {} }}{{ {} }}$'.format(round(n1_wrong, 1), n2_wrong, n3_wrong)
            if figure_wrong not in choicesA:
                choicesA.append(figure_wrong)
                break

    #b)
    value_correct = round((n1_correct * n2_correct / n3_correct), 2)
    choicesB = [value_correct]

    #generate wrong answers
    for _ in range(3):
        while(True):
            value_wrong = round(value_correct + round(random.uniform(-10, 10), 2), 2)
            if value_wrong not in choicesB:
                choicesB.append(value_wrong)
                break

    random.shuffle(choicesA) #shuffle the choices including the correct and wrong answers
    random.shuffle(choicesB) #shuffle the choices icluding the correct and wrong answers

    vars = {
        'figure':figure,
        'significant_num':significant_num,
        'choicesA1':choicesA[0],
        'choicesA2':choicesA[1],
        'choicesA3':choicesA[2],
        'choicesA4':choicesA[3],
        'figure_correct':figure_correct,
        'choicesB1':choicesB[0],
        'choicesB2':choicesB[1],
        'choicesB3':choicesB[2],
        'choicesB4':choicesB[3],
        'value_correct':value_correct
    }
    question = """
    5              p = {figure}

(a) In the spaces provided, write each number in this calculation
    correct to {significant_num} significant figure.
    A. {choicesA1}
    B. {choicesA2}
    C. {choicesA3}
    D. {choicesA4}
    Answer: {figure_correct}

(b) Use your answer to part (a) to estimate the value of p.
    A. {choicesB1}
    B. {choicesB2}
    C. {choicesB3}
    D. {choicesB4}
    Answer: {value_correct}
    """.format(**vars)


    #just to convert to png
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1]) #add_axes(rect) where rect = [x0, y0, width, height]
    plt.axis('off')

    ax.text(0.1, 0.5, question,
        horizontalalignment='left',
        verticalalignment='center',
        fontsize=12, color='black',
        transform=ax.transAxes)

    #this is to convert the graph to the text format to send
    #plt.show() #show the figure
    image = BytesIO()
    plt.savefig(image, format='png')
    #plt.savefig('image.png')
    image.seek(0)
    I=base64.encodebytes(image.getvalue())
    return {"photo": I.decode(), "Type":Q_type.multichoice, "Author":"Bennie"}

    # the send command is to send to the group, just make sure the cell, first cell, has been run before
send(significant_figure())

import random
def solve_equation():
    """
    Equation: (n - num[0]) / num[1] = num[2]
    """

    num = [random.randint(1, 20) for _ in range(3)]
    correctAns = num[2] * num[1] + num[0]

    choices = [correctAns] #initialise choices with the correct, then generate 3 wrong answer to make up MCQ

    #generate wrong answers
    for _ in range(3):
        while(True):
            wrongAnswer = correctAns + random.choice([-2*num[0]] + [random.randint(-4, 4) for _ in range(2)])
            if wrongAnswer not in choices:
                choices.append(wrongAnswer)
                break

    random.shuffle(choices) #shuffle the choices including the correct and wrong answers
    figure = r'$ \frac{{ n - {} }}{{ {} }} = {}$'.format(num[0], num[1], num[2])
    vars = {
        'figure':figure,
        'choices1':choices[0],
        'choices2':choices[1],
        'choices3':choices[2],
        'choices4':choices[3],
        'correctAns':correctAns,
    }
    question = """
    6   Solve the equation.

                                {figure}
    A. {n} = {choices1}
    B. {n} = {choices2}
    C. {n} = {choices3}
    D. {n} = {choices4}
    Answer: {correctAns}
    """.format(**vars, n = r'$\mathit{n}$') #unpack vars dict into string


    #just to convert to png
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1]) #add_axes(rect) where rect = [x0, y0, width, height]
    plt.axis('off')

    ax.text(0.1, 0.5, question,
        horizontalalignment='left',
        verticalalignment='center',
        fontsize=12, color='black',
        transform=ax.transAxes)

    #this is to convert the graph to the text format to send
    #plt.show() #show the figure
    image = BytesIO()
    plt.savefig(image, format='png')
    #plt.savefig('image.png')
    image.seek(0)
    I=base64.encodebytes(image.getvalue())
    return {"photo": I.decode(), "Type":Q_type.multichoice, "Author":"Bennie"}

    # the send command is to send to the group, just make sure the cell, first cell, has been run before
send(solve_equation())

import random
def work_outAB():

    numA = (random.randint(-10, 15), random.randint(-10, 15))
    numB = (random.randint(-10, 15), random.randint(-10, 15))
    correctAns = (numA[0] - 2*numB[0], numA[1] - 2*numB[1])

    choices = [correctAns] #initialise choices with the correct, then generate 3 wrong answer to make up MCQ

    #generate wrong answers
    for _ in range(3):
        while(True):
            wrongAnswer = (numA[0] - 2 * numB[0] + random.randint(-5, 5), numA[1] - 2 * numB[1] + random.randint(-5, 5))
            if wrongAnswer not in choices:
                choices.append(wrongAnswer)
                break

    random.shuffle(choices) #shuffle the choices including the correct and wrong answers
    figureA = r'$\binom{{ {} }}{{ {} }}$'.format(numA[0], numA[1])
    figureB = r'$\binom{{ {} }}{{ {} }}$'.format(numB[0], numB[1])
    vars = {
        'figureA':figureA,
        'figureB':figureB,
        'choices1': r'$\binom{{ {} }}{{ {} }}$'.format(*choices[0]),
        'choices2': r'$\binom{{ {} }}{{ {} }}$'.format(*choices[1]),
        'choices3': r'$\binom{{ {} }}{{ {} }}$'.format(*choices[2]),
        'choices4': r'$\binom{{ {} }}{{ {} }}$'.format(*choices[3]),
        'correctAns': r'$\binom{{ {} }}{{ {} }}$'.format(*correctAns)
    }
    question = """
    7          a = {figureA}      b = {figureB}

        work out a - 2b.

    A. {choices1}
    B. {choices2}
    C. {choices3}
    D. {choices4}
    Answer: {correctAns}
    """.format(**vars) #unpack vars dict into string

    #just to convert to png
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1]) #add_axes(rect) where rect = [x0, y0, width, height]
    plt.axis('off')

    ax.text(0.1, 0.5, question,
        horizontalalignment='left',
        verticalalignment='center',
        fontsize=15, color='black',
        transform=ax.transAxes)

    #this is to convert the graph to the text format to send
    #plt.show() #show the figure
    image = BytesIO()
    plt.savefig(image, format='png')
    #plt.savefig('image.png')
    image.seek(0)
    I=base64.encodebytes(image.getvalue())
    return {"photo": I.decode(), "Type":Q_type.multichoice, "Author":"Bennie"}

    # the send command is to send to the group, just make sure the cell, first cell, has been run before
send(work_outAB())

import random
def nearest_cm():

    n1 = random.randint(10, 1000)
    correctAns = (n1-0.5, n1+0.5)

    choices = [correctAns] #initialise choices with the correct, then generate 3 wrong answer to make up MCQ

    #generate wrong answers
    for _ in range(3):
        while(True):
            wrongAnswer = (n1 + random.choice([random.randint(-3, 0) for _ in range(2)] + [-0.15, -0.1, -0.75]), n1 + random.choice([random.randint(0, 3) for _ in range(2)] + [0.15, 0.1, 0.75]))
            if wrongAnswer not in choices:
                choices.append(wrongAnswer)
                break

    random.shuffle(choices) #shuffle the choices including the correct and wrong answers
    vars = {
        'n1': n1,
        'choices1': r'$ {} \leq \mathit{{w}} < {} $'.format(*choices[0]),
        'choices2': r'$ {} \leq \mathit{{w}} < {} $'.format(*choices[1]),
        'choices3': r'$ {} \leq \mathit{{w}} < {} $'.format(*choices[2]),
        'choices4': r'$ {} \leq \mathit{{w}} < {} $'.format(*choices[3]),
        'correctAns': r'$ {} \leq \mathit{{w}} < {} $'.format(*correctAns)
    }
    question = """
    8   The width, {w} cm, of a carpet is {n1} cm,
         correct to the nearest centimetre.

        Complete the statement about the value of {w}.

    A. {choices1}
    B. {choices2}
    C. {choices3}
    D. {choices4}
    Answer: {correctAns}
    """.format(**vars, w=r'$ \mathit{w} $') #unpack vars dict into string

    #just to convert to png
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1]) #add_axes(rect) where rect = [x0, y0, width, height]
    plt.axis('off')

    ax.text(0.1, 0.5, question,
        horizontalalignment='left',
        verticalalignment='center',
        fontsize=15, color='black',
        transform=ax.transAxes)

    #this is to convert the graph to the text format to send
    #plt.show() #show the figure
    image = BytesIO()
    plt.savefig(image, format='png')
    #plt.savefig('image.png')
    image.seek(0)
    I=base64.encodebytes(image.getvalue())
    return {"photo": I.decode(), "Type":Q_type.multichoice, "Author":"Bennie"}

    # the send command is to send to the group, just make sure the cell, first cell, has been run before
send(nearest_cm())

import random
from fractions import Fraction
def simplest_form():

    n1 = random.choice([i for i in range(2, 20) if i % 2 == 0])
    valueX = random.choice([i for i in range(2, 10) if i % 2 == 0])
    correctAns = Fraction(n1, valueX ** 2) + Fraction(valueX ** 2, n1)
    correctAns = (correctAns.numerator, correctAns.denominator)

    choices = [correctAns] #initialise choices with the correct, then generate 3 wrong answer to make up MCQ

    #generate wrong answers
    for _ in range(3):
        while(True):
            n1_wrong = n1 + random.randint(-5, 5)
            valueX_wrong = valueX + random.randint(-5, 5)
            if (not(n1_wrong == 0 or valueX_wrong == 0)):
                wrongAnswer = Fraction(n1_wrong, valueX_wrong ** 2) + Fraction(valueX_wrong ** 2, n1_wrong)
                wrongAnswer = (wrongAnswer.numerator, wrongAnswer.denominator)
                if wrongAnswer not in choices:
                    choices.append(wrongAnswer)
                    break

    random.shuffle(choices) #shuffle the choices including the correct and wrong answers
    figure = r'$ \mathit{{y}} = \frac{{ {n1} }}{{ \mathit{{x}}^{{2}} }} + \frac{{ \mathit{{x}}^{{2}} }}{{ {n1} }}$'.format(n1=n1, valueX=valueX)
    vars = {
        'figure': figure,
        'n1': n1,
        'valueX': valueX,
        'choices1': r'$ \frac{{ {} }}{{ {} }} $'.format(*choices[0]),
        'choices2': r'$ \frac{{ {} }}{{ {} }} $'.format(*choices[1]),
        'choices3': r'$ \frac{{ {} }}{{ {} }} $'.format(*choices[2]),
        'choices4': r'$ \frac{{ {} }}{{ {} }} $'.format(*choices[3]),
        'correctAns': r'$ \frac{{ {} }}{{ {} }} $'.format(*correctAns)
    }
    question = """
    9       {figure}

    Find the value of {y} when {x} = {valueX}.
    Give your answer as a mixed number in its simplest form.

    A. {choices1}
    B. {choices2}
    C. {choices3}
    D. {choices4}
    Answer: {correctAns}
    """.format(**vars, y=r'$ \mathit{y} $', x=r'$ \mathit{x} $') #unpack vars dict into string

    #just to convert to png
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1]) #add_axes(rect) where rect = [x0, y0, width, height]
    plt.axis('off')

    ax.text(0.1, 0.5, question,
        horizontalalignment='left',
        verticalalignment='center',
        fontsize=13, color='black',
        transform=ax.transAxes)

    #this is to convert the graph to the text format to send
    #plt.show() #show the figure
    image = BytesIO()
    plt.savefig(image, format='png')
    #plt.savefig('image.png')
    image.seek(0)
    I=base64.encodebytes(image.getvalue())
    return {"photo": I.decode(), "Type":Q_type.multichoice, "Author":"Bennie"}

    # the send command is to send to the group, just make sure the cell, first cell, has been run before
send(simplest_form())

import random, math
def workout_2dec():

    n1 = random.randint(1, 10)
    n2 = random.randint(1, 10)
    n3 = random.randint(1, 10)
    n3_pow = random.randint(-3, 3)
    correctAns = round(math.sqrt(n1/n2) + (n3**n3_pow), 2)

    choices = [correctAns] #initialise choices with the correct, then generate 3 wrong answer to make up MCQ

    #generate wrong answers
    for _ in range(3):
        while(True):
            n1_wrong = random.randint(1, 10)
            n2_wrong = random.randint(1, 10)
            n3_wrong = random.randint(1, 10)
            n3_pow_wrong = random.randint(-3, 3)
            wrongAnswer = round(math.sqrt(n1_wrong/n2_wrong) + (n3_wrong**n3_pow_wrong), 2)
            if wrongAnswer not in choices:
                choices.append(wrongAnswer)
                break

    random.shuffle(choices) #shuffle the choices including the correct and wrong answers
    figure = r'$ \sqrt{{ \frac{{ {} }}{{ {} }} }} + {}^{{ {} }} $'.format(n1, n2, n3, n3_pow)
    vars = {
        'figure': figure,
        'choices1': choices[0],
        'choices2': choices[1],
        'choices3': choices[2],
        'choices4': choices[3],
        'correctAns': correctAns
    }
    question = """
    10  Use your calculator to work out  {figure}

    Give your answer correct to 2 decimal places.

    A. {choices1}
    B. {choices2}
    C. {choices3}
    D. {choices4}
    Answer: {correctAns}
    """.format(**vars) #unpack vars dict into string

    #just to convert to png
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1]) #add_axes(rect) where rect = [x0, y0, width, height]
    plt.axis('off')

    ax.text(0.1, 0.5, question,
        horizontalalignment='left',
        verticalalignment='center',
        fontsize=15, color='black',
        transform=ax.transAxes)

    #this is to convert the graph to the text format to send
    #plt.show() #show the figure
    image = BytesIO()
    plt.savefig(image, format='png')
    #plt.savefig('image.png')
    image.seek(0)
    I=base64.encodebytes(image.getvalue())
    return {"photo": I.decode(), "Type":Q_type.multichoice, "Author":"Bennie"}

    # the send command is to send to the group, just make sure the cell, first cell, has been run before
send(workout_2dec())

import random, math
from matplotlib import patches
def find_Angle():
    #generate angles
    a1 = random.randint(90, 150)
    a2 = random.randint(75, 110)
    a3 = 360 - a1 - a2
    correctAns = a1
    print(f"{a1}, {a2}, {a3}")
    choices = [correctAns] #initialise choices with the correct, then generate 3 wrong answer to make up MCQ

    #generate wrong answers
    for _ in range(3):
        while(True):
            wrongAnswer = correctAns + random.randint(-30, 30)
            if wrongAnswer not in choices:
                choices.append(wrongAnswer)
                break

    randomAngle = random.choice([a1, a2, a3])
    if randomAngle > 180:
        correctAnsB = "Reflex Angle"
    elif randomAngle == 180:
        correctAnsB = "Straight Angle"
    elif randomAngle > 90:
        correctAnsB = "Obtuse Angle"
    elif randomAngle == 90:
        correctAnsB = "Right Angle"
    else:
        correctAnsB = "Acute Angle"
    choicesB = ["Reflex Angle", "Straight Angle", "Obtuse Angle", "Right Angle", "Acute Angle"]
    random.shuffle(choices) #shuffle the choices including the correct and wrong answers
    random.shuffle(choicesB) #shuffle the choices including the correct and wrong answers

    vars = {
        'choices1': choices[0],
        'choices2': choices[1],
        'choices3': choices[2],
        'choices4': choices[3],
        'correctAns': correctAns,
        'angle': str(randomAngle) + u"\u00b0",
        'choicesB1': choicesB[0],
        'choicesB2': choicesB[1],
        'choicesB3': choicesB[2],
        'choicesB4': choicesB[3],
        'choicesB5': choicesB[4],
        'correctAnsB': correctAnsB
    }
    question = """
    3



(a) Find the value of {x}
    A. {choices1}
    B. {choices2}
    C. {choices3}
    D. {choices4}
    Answer: {correctAns}

(b) One of the angles is {angle}.
    What type of angle is this?
    A. {choicesB1}
    B. {choicesB2}
    C. {choicesB3}
    D. {choicesB4}
    E. {choicesB5}
    Answer: {correctAnsB}
    """.format(**vars, x = r'$ \mathit{x} $') #unpack vars dict into string

    #just to convert to png
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1]) #add_axes(rect) where rect = [x0, y0, width, height]
    plt.axis('off')
    ax.set_ylim([0, 10])   # set the bounds to be 10, 10
    ax.set_xlim([0, 10])

    ax.text(0.1, 0.5, question,
        horizontalalignment='left',
        verticalalignment='center',
        fontsize=12, color='black',
        transform=ax.transAxes)

#PLOT FIGURE
    x, y = (6.5, 7) #figure center point
    angle = [a1, a2, a3]
    startingAngle = -20 #random.randint(-20, 20)
    length = 3 #lines length
    arcLength = [1.5, 2, 2.35]
    textPos = [(x+0.2, y+0.1), (x-0.8, y+0.2), (x-0.3, y-0.8)]
    lastAngle = startingAngle
    for i in range(len(angle)):
        # find the end point
        a = angle[i]
        endy = y + length * math.sin(math.radians(a + lastAngle))
        endx = x + length * math.cos(math.radians(a + lastAngle))
        ax.plot([x, endx], [y, endy], 'k', linewidth=1)
        angle_plot = patches.Arc([x, y], arcLength[i], arcLength[i], lastAngle, 0, a, color='black', label = str(a)+u"\u00b0")
        ax.add_patch(angle_plot)
        if i == 0:
            ax.text(*textPos[i], r'$ \mathit{x} $'+u"\u00b0")
        else:
            ax.text(*textPos[i], angle_plot.get_label())
        lastAngle += a

    #this is to convert the graph to the text format to send
    #plt.show() #show the figure
    image = BytesIO()
    plt.savefig(image, format='png')
    #plt.savefig('image.png')
    image.seek(0)
    I=base64.encodebytes(image.getvalue())
    return {"photo": I.decode(), "Type":Q_type.multichoice, "Author":"Bennie"}

    # the send command is to send to the group, just make sure the cell, first cell, has been run before
find_Angle()

import random, math
from matplotlib import patches
def cuboid_height():

    h = random.randint(5, 20)
    w = random.randint(5, 20)
    l = random.randint(10, 35)
    volume = h * w * l
    correctAns = h
    print(f"{h}, {w}, {l}")
    choices = [correctAns] #initialise choices with the correct, then generate 3 wrong answer to make up MCQ

    #generate wrong answers
    for _ in range(3):
        while(True):
            wrongAnswer = correctAns + random.randint(-15, 15)
            if wrongAnswer not in choices:
                choices.append(wrongAnswer)
                break

    random.shuffle(choices) #shuffle the choices including the correct and wrong answers

    vars = {
        'w': w,
        'l': l,
        'volume': volume,
        'choices1': choices[0],
        'choices2': choices[1],
        'choices3': choices[2],
        'choices4': choices[3],
        'correctAns': correctAns
    }
    question = """
    11







    The volume of this cuboid is {volume} cm{cube}
    The width is {w}cm and the length is {l}cm.

    Calculate {h}, the height of the cuboid.
    A. {choices1}cm
    B. {choices2}cm
    C. {choices3}cm
    D. {choices4}cm
    Answer: {correctAns}cm
    """.format(**vars, cube = r'$ ^{3} $', h = r'$ \mathit{h} $') #unpack vars dict into string

    #just to convert to png
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1]) #add_axes(rect) where rect = [x0, y0, width, height]
    plt.axis('off')
    ax.set_ylim([0, 10])   # set the bounds to be 10, 10
    ax.set_xlim([0, 10])

    ax.text(0.1, 0.5, question,
        horizontalalignment='left',
        verticalalignment='center',
        fontsize=12, color='black',
        transform=ax.transAxes)
#Draw CUBOID
    x, y = (4, 6) #starting point of rect
    rectangle = plt.Rectangle((x, y), 1.8, 1.5, fc='w', ec='k')
    ax.add_patch(rectangle)
    length = 3 #length of l
    offset = [[1.8, 0], [0, 1.5], [1.8, 1.5]] #offset for each corners
    for i in range(3): #draw 3 solid line for each corner
        endy = y + length * math.sin(math.radians(45))
        endx = x + length * math.cos(math.radians(45))
        ax.plot([x + offset[i][0], endx + offset[i][0]], [y + offset[i][1], endy + offset[i][1]], 'k', linewidth=0.5)
    #draw 1 dotted line for the other corner
    endy = y + length * math.sin(math.radians(45))
    endx = x + length * math.cos(math.radians(45))
    ax.plot([x, endx], [y, endy], 'k', linewidth=0.5, linestyle='dashed')
    rectangle = plt.Rectangle((endx, endy), 1.8, 1.5, fc='w', ec='k', linestyle='dashed')
    ax.add_patch(rectangle)
#Add text on respective sides
    ax.text(x - 0.5, y + 0.8, r'$ \mathit{h} $', fontsize=12)
    ax.text(x + 0.5, y - 0.5, f'{w}cm', fontsize=12)
    ax.text(x + 3, y + 1, f'{l}cm', fontsize=12)
#Add NOT TO SCALE LABEL
    ax.text(x - 1, y + 3, "NOT TO SCALE")
    
    #this is to convert the graph to the text format to send
    #plt.show() #show the figure
    image = BytesIO()
    plt.savefig(image, format='png')
    #plt.savefig('image.png')
    image.seek(0)
    I=base64.encodebytes(image.getvalue())
    return {"photo": I.decode(), "Type":Q_type.multichoice, "Author":"Bennie"}

    # the send command is to send to the group, just make sure the cell, first cell, has been run before
send(cuboid_height())

import random, math
def exchange_rate():
    rates = [1.3, 1.4, 1.5, 1.6, 1.7]
    n1 = random.randint(200, 1550)
    rate = random.choice(rates)
    rates.pop(rates.index(rate))
    newRate = random.choice(rates)
    n2 = round((n1 * rate / newRate), 2)
    correctAns = newRate
    choices = [correctAns] #initialise choices with the correct, then generate 3 wrong answer to make up MCQ

    #generate wrong answers
    for _ in range(3):
        while(True):
            wrongAnswer = random.choice(rates)
            if wrongAnswer not in choices:
                choices.append(wrongAnswer)
                break

    random.shuffle(choices) #shuffle the choices including the correct and wrong answers

    vars = {
        'n1': n1,
        'rate': rate,
        'n2': n2,
        'choices1': choices[0],
        'choices2': choices[1],
        'choices3': choices[2],
        'choices4': choices[3],
        'correctAns': correctAns
    }
    question = """
15  Carlo changed {n1} euros ({euro}) into dollars for his
    holiday when the exchange rate was {euro}1 = ${rate}.
    His holiday was then cancelled.
    He changed all his dollars back into euros and
    he received {euro}{n2}.

    Find the new exchange rate.
    A. {choices1}
    B. {choices2}
    C. {choices3}
    D. {choices4}
    Answer: {correctAns}
    """.format(**vars, euro=r'€') #unpack vars dict into string

    #just to convert to png
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1]) #add_axes(rect) where rect = [x0, y0, width, height]
    plt.axis('off')
    ax.set_ylim([0, 10])   # set the bounds to be 10, 10
    ax.set_xlim([0, 10])

    ax.text(0.1, 0.5, question,
        horizontalalignment='left',
        verticalalignment='center',
        fontsize=12, color='black',
        transform=ax.transAxes)

    #this is to convert the graph to the text format to send
    #plt.show() #show the figure
    image = BytesIO()
    plt.savefig(image, format='png')
    #plt.savefig('image.png')
    image.seek(0)
    I=base64.encodebytes(image.getvalue())
    return {"photo": I.decode(), "Type":Q_type.multichoice, "Author":"Bennie"}

    # the send command is to send to the group, just make sure the cell, first cell, has been run before
send(exchange_rate())

import random, math, string
def simplify():
    ra1 = random.choice(string.ascii_lowercase)
    power11 = random.randint(1, 10)
    power12 = random.randint(1, 10)

    correctAns1 = r'$\mathit{{ {} }}^{{ {} }}$'.format(ra1, power11+power12)
    choices1 = [correctAns1] #initialise choices with the correct, then generate 3 wrong answer to make up MCQ

    #generate wrong answers
    for _ in range(3):
        while(True):
            wrongAns = power11 + power12 + random.randint(-5, 5)
            wrongAnswer = r'$\mathit{{ {} }}^{{ {} }}$'.format(ra1, wrongAns)
            if wrongAnswer not in choices1:
                choices1.append(wrongAnswer)
                break

    ra2 = random.choice(string.ascii_lowercase)
    power21 = random.randint(1, 10)
    power22 = random.randint(1, 10)

    correctAns2 = r'$\mathit{{{}}}^{{ {} }}$'.format(ra2, power21-power22)
    choices2 = [correctAns2] #initialise choices with the correct, then generate 3 wrong answer to make up MCQ

    #generate wrong answers
    for _ in range(3):
        while(True):
            wrongAns = power21 + power22 + random.randint(-5, 5)
            wrongAnswer = r'$\mathit{{{}}}^{{ {} }}$'.format(ra2, wrongAns)
            if wrongAnswer not in choices2:
                choices2.append(wrongAnswer)
                break

    raB = random.choice([i for i in string.ascii_lowercase if i != 'k'])
    powerB1 = random.randint(1, 10)
    powerK = random.randint(1, 10)
    powerB2 = powerB1 * powerK

    random.shuffle(choices1) #shuffle the choices including the correct and wrong answers
    random.shuffle(choices2) #shuffle the choices including the correct and wrong answers

    vars = {
        'n1': r'$\mathit{{{}}}^{{{}}}$'.format(ra1, power11),
        'n2': r'$\mathit{{{}}}^{{{}}}$'.format(ra1, power12),
        'n3': r'$\mathit{{{}}}^{{{}}}$'.format(ra2, power21),
        'n4': r'$\mathit{{{}}}^{{{}}}$'.format(ra2, power22),
        'n5': r'$\mathit{{{}}}^{{{}}}$'.format(raB, powerB1),
        'n6': r'$\mathit{{{}}}^{{{}}}$'.format(raB, powerB2),
        'choices11': choices1[0],
        'choices12': choices1[1],
        'choices13': choices1[2],
        'choices14': choices1[3],
        'correctAns1': correctAns1,
        'choices21': choices2[0],
        'choices22': choices2[1],
        'choices23': choices2[2],
        'choices24': choices2[3],
        'correctAns2': correctAns2
    }
    question = """
16  (a) Simplify the expressions.
            (i) {n1} x {n2}
            A. {choices11}
            B. {choices12}
            C. {choices13}
            D. {choices14}
            Answer: {correctAns1}

            (ii) {n3} {div} {n4}
            A. {choices21}
            B. {choices22}
            C. {choices23}
            D. {choices24}
            Answer: {correctAns2}

    (b) ({n5}){pow_k} = {n6}    Find the value of {k}

    """.format(**vars, div=r'$\div$', pow_k=r'$^{ \mathit{k} }$', k=r'$\mathit{k}$') #unpack vars dict into string

    #just to convert to png
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1]) #add_axes(rect) where rect = [x0, y0, width, height]
    plt.axis('off')
    #ax.set_ylim([0, 10])   # set the bounds to be 10, 10
    #ax.set_xlim([0, 10])

    ax.text(0.1, 0.5, question,
        horizontalalignment='left',
        verticalalignment='center',
        fontsize=12, color='black',
        transform=ax.transAxes)

    #this is to convert the graph to the text format to send
    #plt.show() #show the figure
    image = BytesIO()
    plt.savefig(image, format='png')
    #plt.savefig('image.png')
    image.seek(0)
    I=base64.encodebytes(image.getvalue())
    return {"photo": I.decode(), "Type":Q_type.multichoice, "Author":"Bennie"}

    # the send command is to send to the group, just make sure the cell, first cell, has been run before
send(simplify())

import random, math
from matplotlib import patches

def plotLines(ax, x, y, length, angle = 0):
    #ax.annotate(text='123', xy=(x,y), xytext=(0,0), arrowprops=dict(arrowstyle='->'))
    endy = y + length * math.sin(math.radians(angle))
    endx = x + length * math.cos(math.radians(angle))
    ax.plot([x, endx], [y, endy], 'k', linewidth=1)
    return endx, endy

def findAngle():
    angle = random.randint(110, 130)
    angle_a = 180 - ((180 - angle) * 2)
    angle_b = angle - angle_a
    print(angle, angle_a, angle_b)
    correctAns = angle_a
    choices = [correctAns] #initialise choices with the correct, then generate 3 wrong answer to make up MCQ

    #generate wrong answers
    for _ in range(3):
        while(True):
            wrongAnswer = correctAns + random.randint(-20, 20)
            if wrongAnswer not in choices:
                choices.append(wrongAnswer)
                break

    correctAnsB = angle_b
    choicesB = [correctAnsB] #initialise choices with the correct, then generate 3 wrong answer to make up MCQ

    #generate wrong answers
    for _ in range(3):
        while(True):
            wrongAnswer = correctAnsB + random.randint(-20, 20)
            if wrongAnswer not in choicesB:
                choicesB.append(wrongAnswer)
                break

    random.shuffle(choices) #shuffle the choices including the correct and wrong answers
    random.shuffle(choicesB) #shuffle the choices including the correct and wrong answers

    vars = {
        'angle': angle,
        'choices1': choices[0],
        'choices2': choices[1],
        'choices3': choices[2],
        'choices4': choices[3],
        'correctAns': correctAns,
        'choices1B': choicesB[0],
        'choices2B': choicesB[1],
        'choices3B': choicesB[2],
        'choices4B': choicesB[3],
        'correctAnsB': correctAnsB
    }
    question = """
16  The diagram shows an isosceles triangle {ABC}.
    {DCB} is a straight line and is parallel to {AE}.
    Angle {DCA} = {angle}.
    Find the value of
    (a) {a},                    (b) {b},
        A. {choices1}                   A. {choices1B}
        B. {choices2}                   B. {choices2B}
        C. {choices3}                   C. {choices3B}
        D. {choices4}                   D. {choices4B}
        Answer: {correctAns}        Answer: {correctAnsB}

    """.format(**vars, ABC=r'$\mathit{ABC}$', DCB=r'$\mathit{DCB}$', AE=r'$\mathit{AE}$', DCA=r'$\mathit{DCA}$', a=r'$\mathit{a}$', \
    b=r'$\mathit{b}$') #unpack vars dict into string

    #just to convert to png
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1]) #add_axes(rect) where rect = [x0, y0, width, height]
    plt.axis('off')
    ax.set_ylim([0, 10])   # set the bounds to be 10, 10
    ax.set_xlim([0, 10])

    #DCB
    ax.text(2, 6.5 - 0.3, "D")
    endx, endy = plotLines(ax, *(2, 6.5), 5)
    ax.text(endx + 0.1, endy - 0.3, "B")

    #BA
    endx, endy = plotLines(ax, *(endx, endy), 3, angle)
    ax.text(endx, endy + 0.3, "A")

    #AC
    endx1, endy1 = plotLines(ax, *(endx, endy), 3, angle + 180 - angle_a)
    angle_plot = patches.Arc([endx1, endy1], 1.8, 1.8, 180-angle, 0, angle, color='black', label = r'$\mathit{{{}}}$'.format(angle)+u"\u00b0")
    ax.add_patch(angle_plot)
    ax.text(endx1 - 0.4, endy1 + 0.25, angle_plot.get_label())
    ax.text(endx1 - 0.15, endy1 - 0.3, "C")

    #AE
    angle_plot = patches.Arc([endx, endy], 1.5, 1.5, -angle_b, 0, angle_b, color='black', label = r'$\mathit{b}$'+u"\u00b0")
    ax.add_patch(angle_plot)
    ax.text(endx + 0.35, endy - 0.3, angle_plot.get_label())
    angle_plot = patches.Arc([endx, endy], 1.7, 1.7, -angle_b - angle_a, 0, angle_a, color='black', label = r'$\mathit{a}$'+u"\u00b0")
    ax.add_patch(angle_plot)
    ax.text(endx - 0.15, endy - 0.5, angle_plot.get_label())
    endx, endy = plotLines(ax, *(endx, endy), 3)
    ax.text(endx, endy + 0.3, "E")

    ax.text(0.1, 0.3, question,
        horizontalalignment='left',
        verticalalignment='center',
        fontsize=12, color='black',
        transform=ax.transAxes)

    #this is to convert the graph to the text format to send
    #plt.show() #show the figure
    image = BytesIO()
    plt.savefig(image, format='png')
    #plt.savefig('image.png')
    image.seek(0)
    I=base64.encodebytes(image.getvalue())
    return {"photo": I.decode(), "Type":Q_type.multichoice, "Author":"Bennie"}

    # the send command is to send to the group, just make sure the cell, first cell, has been run before
send(findAngle())

import random, math
from matplotlib import patches

def plotLines(ax, x, y, length, angle = 0):
    #ax.annotate(text='123', xy=(x,y), xytext=(0,0), arrowprops=dict(arrowstyle='->'))
    endy = y + length * math.sin(math.radians(angle))
    endx = x + length * math.cos(math.radians(angle))
    ax.plot([x, endx], [y, endy], 'k', linewidth=1)
    return endx, endy

def findHypotenuse():
    QR_l = random.randint(3, 15)
    PQ_l = random.randint(QR_l+5, QR_l+20)
    PR_l = round(math.sqrt(QR_l**2 + PQ_l**2), 2)
    radius = PR_l / 2
    print(QR_l, PQ_l, PR_l)
    correctAns = PR_l
    choices = [correctAns] #initialise choices with the correct, then generate 3 wrong answer to make up MCQ

    #generate wrong answers
    for _ in range(3):
        while(True):
            wrongAnswer = round(correctAns + random.uniform(-20, 20), 2)
            if wrongAnswer not in choices:
                choices.append(wrongAnswer)
                break

    random.shuffle(choices) #shuffle the choices including the correct and wrong answers

    vars = {
        'PQ_l': PQ_l,
        'QR_l': QR_l,
        'choices1': choices[0],
        'choices2': choices[1],
        'choices3': choices[2],
        'choices4': choices[3],
        'correctAns': correctAns
    }
    question = """
17  The diagram shows a circle, centre {O}.
    {P}, {Q} and {R} are points on the circumference.
    {PQ} = {PQ_l}cm and {QR} = {QR_l}cm.

    (a) Explain why angle {P}{Q}{R} is 90{degree}.
        Answer(a)....................................................................
    (b) Calculate the length {P}{R}.
        A. {choices1}cm
        B. {choices2}cm
        C. {choices3}cm
        D. {choices4}cm
        Answer: {correctAns}cm
    """.format(**vars, P=r'$\mathit{P}$', Q=r'$\mathit{Q}$', R=r'$\mathit{R}$', PQ=r'$\mathit{PQ}$', QR=r'$\mathit{QR}$', \
    O=r'$\mathit{O}$', degree=u"\u00b0") #unpack vars dict into string

    #just to convert to png
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1]) #add_axes(rect) where rect = [x0, y0, width, height]
    plt.axis('off')
    ax.set_ylim([0, 10])   # set the bounds to be 10, 10
    ax.set_xlim([0, 10])

    #DCB
    # ax.text(2, 6.5 - 0.3, "D")
    # endx, endy = plotLines(ax, *(2, 6.5), 5)
    # ax.text(endx + 0.1, endy - 0.3, "B")
    circle_r = 2 #radius of circle in figure
    circle = patches.Circle((5, 7.8), circle_r, fc='w', ec='k')
    ax.add_patch(circle)
    ax.plot(5, 7.8, "o", color='k') #plot center of circle with a black circle
    ax.text(5, 7.8-0.4, "O")
    ax.text(5-circle_r-0.25, 7.8, "P")
    endx, endy = plotLines(ax, *(5-circle_r, 7.8), circle_r * 2)
    ax.text(5, 7.8-0.4, "O")
    ax.text(endx+0.1, endy, "R")
    endx, endy = plotLines(ax, *(endx, endy), 2, 180-60)
    ax.text(endx-0.2, endy-1, str(QR_l)+"cm")
    ax.text(endx-2, endy-0.7, str(PQ_l)+"cm")
    ax.text(endx, endy+0.2, "Q")
    endx, endy = plotLines(ax, *(endx, endy), 3.45, 180-60+90)

    ax.text(0.1, 0.3, question,
        horizontalalignment='left',
        verticalalignment='center',
        fontsize=11, color='black',
        transform=ax.transAxes)

    #this is to convert the graph to the text format to send
    #plt.show() #show the figure
    image = BytesIO()
    plt.savefig(image, format='png')
    #plt.savefig('image.png')
    image.seek(0)
    I=base64.encodebytes(image.getvalue())
    return {"photo": I.decode(), "Type":Q_type.multichoice, "Author":"Bennie"}

    # the send command is to send to the group, just make sure the cell, first cell, has been run before
send(findHypotenuse())

import random, math, statistics
from matplotlib import patches

def tableAVG():
    #a1
    month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    temperature = [round(random.uniform(-20, 20), 1) for _ in range(12)]
    maxTemp = max(temperature)
    minTemp = min(temperature)
    print(temperature)
    print(sorted(temperature))
    correctAns = round(maxTemp - minTemp, 2)
    choices = [correctAns] #initialise choices with the correct, then generate 3 wrong answer to make up MCQ

    #generate wrong answers
    for _ in range(3):
        while(True):
            wrongAnswer = round(correctAns + random.uniform(-20, 20), 2)
            if wrongAnswer not in choices:
                choices.append(wrongAnswer)
                break

    #a2
    median = round(statistics.median(temperature), 2)
    correctAns2 = median
    choices2 = [correctAns2]

    #generate wrong answers
    for _ in range(3):
        while(True):
            wrongAnswer = random.choice(temperature)
            if wrongAnswer not in choices2:
                choices2.append(wrongAnswer)
                break

    #b
    belowZero = 0
    n = len(temperature)
    for i in temperature:
        if i < 0:
            belowZero += 1
    probability = round(belowZero / n, 2)
    correctAns3 = probability

    random.shuffle(choices) #shuffle the choices including the correct and wrong answers
    random.shuffle(choices2) #shuffle the choices including the correct and wrong answers

    vars = {
        'choices1': choices[0],
        'choices2': choices[1],
        'choices3': choices[2],
        'choices4': choices[3],
        'correctAns': correctAns,
        'choices21': choices2[0],
        'choices22': choices2[1],
        'choices23': choices2[2],
        'choices24': choices2[3],
        'correctAns2': correctAns2,
        'correctAns3': correctAns3
    }
    question = """
19 The table shows the average monthly temperature ({degree}C) for
 Fairbanks, Alaska.
 (a) Find
    (i) the difference between the highest and the lowest temperature
        A. {choices1}
        B. {choices2}
        C. {choices3}
        D. {choices4}
        Answer: {correctAns}
    (ii) the median.
        A. {choices21}
        B. {choices22}
        C. {choices23}
        D. {choices24}
        Answer: {correctAns2}
  (b) A month is chosen at random from the table.
    Find the probability that its average temperature is below zero.
                                                                Answer: {correctAns3}
    """.format(**vars, degree=u'\u00b0') #unpack vars dict into string

    #just to convert to png
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1]) #add_axes(rect) where rect = [x0, y0, width, height]
    plt.axis('off')
    #ax.set_ylim([0, 10])   # set the bounds to be 10, 10
    #ax.set_xlim([0, 10])

    ax.text(0.05, 0.4, question,
        horizontalalignment='left',
        verticalalignment='center',
        fontsize=10, color='black',
        transform=ax.transAxes)

    table = ax.table(
        cellText = [[i for i in temperature]],
        rowLabels = ['Temperature'],
        colLabels = month,
        cellLoc = 'center',
        bbox=[0.18, 0.8, 0.8, 0.2])
    #this is to convert the graph to the text format to send
    #plt.show() #show the figure
    image = BytesIO()
    plt.savefig(image, format='png')
    #plt.savefig('image.png')
    image.seek(0)
    I=base64.encodebytes(image.getvalue())
    return {"photo": I.decode(), "Type":Q_type.multichoice, "Author":"Bennie"}

    # the send command is to send to the group, just make sure the cell, first cell, has been run before
send(tableAVG())

import random

def operatingTime():
    #a
    day = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    startTime = [random.randint(5, 15) for _ in range(6)]
    startTime.append(random.randint(13, 16))
    finishTime = [random.randint(22, 24) for _ in range(7)]
    totalHours = 0
    for i in range(7):
        totalHours += finishTime[i] - startTime[i]
    correctAns = totalHours
    choices = [correctAns] #initialise choices with the correct, then generate 3 wrong answer to make up MCQ

    #generate wrong answers
    for _ in range(3):
        while(True):
            wrongAnswer = correctAns + random.randint(-20, 20)
            if wrongAnswer not in choices:
                choices.append(wrongAnswer)
                break

    #b
    correctAns2 = startTime[-1] - 12
    correctAns2STR = '{:0>2}'.format(correctAns2)+' 00 pm'
    choices2 = [correctAns2STR] #initialise choices with the correct, then generate 3 wrong answer to make up MCQ

    #generate wrong answers
    for _ in range(3):
        while(True):
            wrongAnswer = correctAns2 + random.randint(-5, 5)
            if wrongAnswer == 0:
                wrongAnswer = '{:0>2}'.format(wrongAnswer + 12)+' 00 pm'
            elif wrongAnswer < 0:
                wrongAnswer = '{:0>2}'.format(wrongAnswer + 12)+' 00 am'
            else:
                wrongAnswer = '{:0>2}'.format(wrongAnswer)+' 00 pm'
            if wrongAnswer not in choices2:
                choices2.append(wrongAnswer)
                break

    random.shuffle(choices) #shuffle the choices including the correct and wrong answers
    random.shuffle(choices2) #shuffle the choices including the correct and wrong answers

    vars = {
        'choices1': choices[0],
        'choices2': choices[1],
        'choices3': choices[2],
        'choices4': choices[3],
        'correctAns': correctAns,
        'choices21': choices2[0],
        'choices22': choices2[1],
        'choices23': choices2[2],
        'choices24': choices2[3],
        'correctAns2': '{:0>2}'.format(correctAns2)+' 00 pm'
    }
    question = """
20 A bus company in Dubai has the following operating times.
    (a) Calculate the total number of hours that the bus company
    operates in one week.
        A. {choices1}
        B. {choices2}
        C. {choices3}
        D. {choices4}
        Answer: {correctAns}
    (b) Write the starting time on Friday in the 12-hour clock.
        A. {choices21}
        B. {choices22}
        C. {choices23}
        D. {choices24}
        Answer: {correctAns2}
    """.format(**vars) #unpack vars dict into string

    #just to convert to png
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1]) #add_axes(rect) where rect = [x0, y0, width, height]
    plt.axis('off')
    #ax.set_ylim([0, 10])   # set the bounds to be 10, 10
    #ax.set_xlim([0, 10])

    ax.text(0.05, 0.3, question,
        horizontalalignment='left',
        verticalalignment='center',
        fontsize=11, color='black',
        transform=ax.transAxes)

    cellText = [['{:0>2}'.format(startTime[i])+" 00", '{:0>2}'.format(finishTime[i])+" 00"] for i in range(7)]

    table = ax.table(
        cellText = cellText,
        rowLabels = day,
        colLabels = ['Starting Time', 'Finishing Time'],
        cellLoc = 'center',
        bbox=[0.18, 0.6, 0.5, 0.4])
    #this is to convert the graph to the text format to send
    #plt.show() #show the figure
    image = BytesIO()
    plt.savefig(image, format='png')
    #plt.savefig('image.png')
    image.seek(0)
    I=base64.encodebytes(image.getvalue())
    return {"photo": I.decode(), "Type":Q_type.multichoice, "Author":"Bennie"}

    # the send command is to send to the group, just make sure the cell, first cell, has been run before
operatingTime()

import random, math
from matplotlib import patches

def plotLines(ax, x, y, length, angle = 0):
    #ax.annotate(text='123', xy=(x,y), xytext=(0,0), arrowprops=dict(arrowstyle='->'))
    endy = y + length * math.sin(math.radians(angle))
    endx = x + length * math.cos(math.radians(angle))
    ax.plot([x, endx], [y, endy], 'k')
    return endx, endy

def areaOfCircle():
    #a
    side = random.randint(5, 20)
    r = side / 2
    area = math.pi * r**2
    correctAns = round(area, 2)
    choices = [correctAns] #initialise choices with the correct, then generate 3 wrong answer to make up MCQ

    #generate wrong answers
    for _ in range(3):
        while(True):
            wrongAnswer = round(correctAns + random.uniform(-5, 5), 2)
            if wrongAnswer not in choices:
                choices.append(wrongAnswer)
                break

    random.shuffle(choices) #shuffle the choices including the correct and wrong answers

    vars = {
        'side' : side,
        'choices1': choices[0],
        'choices2': choices[1],
        'choices3': choices[2],
        'choices4': choices[3],
        'correctAns': correctAns
    }
    question = """
21 The diagram shows a circle inside a square.
    The circumference of the circle touches all four sides of the square.

    (a) Calculate the area of the circle when the side of the square is {side}cm
        A. {choices1}{cm2}
        B. {choices2}{cm2}
        C. {choices3}{cm2}
        D. {choices4}{cm2}
        Answer: {correctAns}{cm2}
    (b) Draw all the lines of symmetry on the diagram.

                                Answer: 4 symmetry lines
    """.format(**vars, cm2=r'$cm^{2}$') #unpack vars dict into string

    #just to convert to png
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1]) #add_axes(rect) where rect = [x0, y0, width, height]
    plt.axis('off')
    ax.set_ylim([0, 10])   # set the bounds to be 10, 10
    ax.set_xlim([0, 10])

    ax.text(0.05, 0.3, question,
        horizontalalignment='left',
        verticalalignment='center',
        fontsize=10, color='black',
        transform=ax.transAxes)

    square = plt.Rectangle((3, 6), 4, 4, fc='gray', ec='black')
    ax.add_patch(square)
    circle = patches.Circle((5, 8), 2, fc='w', ec='black')
    ax.add_patch(circle)

    #b answer
    square = plt.Rectangle((7, 0.3), 2, 2, fc='gray', ec='black')
    ax.add_patch(square)
    circle = patches.Circle((8, 1.3), 1, fc='w', ec='black')
    ax.add_patch(circle)
    plotLines(ax, 7, 0.3, 2.8, 45)
    plotLines(ax, 9, 0.3, 2.8, 180-45)
    plotLines(ax, 8, 0.3, 2, 90)
    plotLines(ax, 7, 1.3, 2)
    #this is to convert the graph to the text format to send
    #plt.show() #show the figure
    image = BytesIO()
    plt.savefig(image, format='png')
    #plt.savefig('image.png')
    image.seek(0)
    I=base64.encodebytes(image.getvalue())
    return {"photo": I.decode(), "Type":Q_type.multichoice, "Author":"Bennie"}

    # the send command is to send to the group, just make sure the cell, first cell, has been run before
send(areaOfCircle())

import random, math
from matplotlib import patches

def plotLines(ax, x, y, length, angle = 0):
    #ax.annotate(text='123', xy=(x,y), xytext=(0,0), arrowprops=dict(arrowstyle='->'))
    endy = y + length * math.sin(math.radians(angle))
    endx = x + length * math.cos(math.radians(angle))
    ax.plot([x, endx], [y, endy], 'k')
    return (endx, endy)

def trigoBearing():
    #a
    AB_l = random.randint(10, 40)
    AC_l = random.randint(AB_l, AB_l+20)
    ACB = math.asin(AB_l/AC_l) / 3.142 * 180
    correctAns = round(ACB, 1)
    choices = [correctAns] #initialise choices with the correct, then generate 3 wrong answer to make up MCQ

    #generate wrong answers
    for _ in range(3):
        while(True):
            wrongAnswer = round(correctAns + random.uniform(-5, 5), 1)
            if wrongAnswer not in choices:
                choices.append(wrongAnswer)
                break

    correctAns2 = 180 - correctAns
    choices2 = [correctAns2]

    #generate wrong answers
    for _ in range(3):
        while(True):
            wrongAnswer = round(correctAns2 + random.uniform(-5, 5), 1)
            if wrongAnswer not in choices2:
                choices2.append(wrongAnswer)
                break

    random.shuffle(choices) #shuffle the choices including the correct and wrong answers
    random.shuffle(choices2) #shuffle the choices including the correct and wrong answers

    vars = {
        'AB_l' : AB_l,
        'AC_l' : AC_l,
        'choices1': choices[0],
        'choices2': choices[1],
        'choices3': choices[2],
        'choices4': choices[3],
        'correctAns': correctAns,
        'choices21': choices2[0],
        'choices22': choices2[1],
        'choices23': choices2[2],
        'choices24': choices2[3],
        'correctAns2': correctAns2
    }
    question = """
22  In the diagram, {B} is {AB_l} metres due east of {A}.
    {C} is {AC_l} metres from {A} and due south of {B}.

    (a) Using trigonometry, calculate angle {A}{C}{B}.
        A. {choices1}{degree}
        B. {choices2}{degree}
        C. {choices3}{degree}
        D. {choices4}{degree}
        Answer: {correctAns}{degree}

    (b) Find the bearing of {C} from {A}.
        A. {choices21}{degree}
        B. {choices22}{degree}
        C. {choices23}{degree}
        D. {choices24}{degree}
        Answer : {correctAns2}{degree}
    """.format(**vars, A=r'$\mathit{A}$', B=r'$\mathit{B}$', C=r'$\mathit{C}$', degree=u"\u00b0") #unpack vars dict into string

    #just to convert to png
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1]) #add_axes(rect) where rect = [x0, y0, width, height]
    plt.axis('off')
    ax.set_ylim([0, 10])   # set the bounds to be 10, 10
    ax.set_xlim([0, 10])

    ax.text(0.05, 0.35, question,
        horizontalalignment='left',
        verticalalignment='center',
        fontsize=11, color='black',
        transform=ax.transAxes)

    ax.text(1.2, 8.3, 'NOT TO SCALE')
    plt.arrow(4, 7.5, 0, 1.8, head_width=0.1, fc='black')
    ax.text(4, 9.5, 'North')
    a = (4, 8.5)
    ax.text(a[0]-0.25, a[1], r'$\mathit{A}$')
    b = plotLines(ax, *a, 4)
    ax.text((a[0]+b[0])/2, b[1]+0.1, f'{AB_l}m')

    ax.text(b[0]+0.1, b[1], r'$\mathit{B}$')
    c = plotLines(ax, *b, 2.5, -90)
    ax.text(c[0]+0.1, c[1]-0.2, r'$\mathit{C}$')
    plotLines(ax, *c, 4.7, -212)
    ax.text((a[0]+c[0])/2-0.4, (a[1]+c[1])/2-0.4, f'{AC_l}m')
    #this is to convert the graph to the text format to send
    #plt.show() #show the figure
    image = BytesIO()
    plt.savefig(image, format='png')
    #plt.savefig('image.png')
    image.seek(0)
    I=base64.encodebytes(image.getvalue())
    return {"photo": I.decode(), "Type":Q_type.multichoice, "Author":"Bennie"}

    # the send command is to send to the group, just make sure the cell, first cell, has been run before
send(trigoBearing())

import random, math
from matplotlib import patches
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)

def milesKmConversion():
    #a
    travelsMiles = random.randint(10, 50)
    travelsMins = random.randint(10, 60)
    correctAns = round(travelsMiles * 1.609 / travelsMins * 60)
    choices = [correctAns] #initialise choices with the correct, then generate 3 wrong answer to make up MCQ

    #generate wrong answers
    for _ in range(3):
        while(True):
            wrongAnswer = correctAns + random.randint(-5, 10)
            if wrongAnswer not in choices:
                choices.append(wrongAnswer)
                break

    random.shuffle(choices) #shuffle the choices including the correct and wrong answers

    vars = {
        'travelsMiles': travelsMiles,
        'travelsMins': travelsMins,
        'choices1': choices[0],
        'choices2': choices[1],
        'choices3': choices[2],
        'choices4': choices[3],
        'correctAns': correctAns
    }
    question = """
13  The graph can be used to convert between miles and kilometres.
    A train travels {travelsMiles} miles in {travelsMins} minutes.
    Find its average speed in kilometres per hour.                  Answer: {correctAns}km/h
    """.format(**vars) #unpack vars dict into string
    #just to convert to png
    fig = plt.figure()
    #plot miles to km graph
    ax = fig.add_axes([0.25, 0.28, 0.5, 0.7]) #add_axes(rect) where rect = [x0, y0, width, height]
    ax2 = fig.add_axes([0, 0, 1, 0.18]) #add_axes(rect) where rect = [x0, y0, width, height]
    ax2.axis('off')
    ax.set_ylabel('Kilometres')
    ax.set_xlabel('Miles')
    #plt.axis('off')
    #ax.set_ylim([0, 10])   # set the bounds to be 10, 10
    #ax.set_xlim([0, 10])
    # Set axis ranges; by default this will put major ticks every 25.
    ax.set_xlim(0, 50)
    ax.set_ylim(0, 80)
    # Change major ticks to show every 20.
    ax.xaxis.set_major_locator(MultipleLocator(10))
    ax.yaxis.set_major_locator(MultipleLocator(10))

    # Change minor ticks to show every 5. (20/4 = 5)
    ax.xaxis.set_minor_locator(AutoMinorLocator(5))
    ax.yaxis.set_minor_locator(AutoMinorLocator(5))
    #ax.grid(which='both', color='#CCCCCC')
    ax.grid(which='major', color='#CCCCCC', linestyle='--')
    ax.grid(which='minor', color='#CCCCCC', linestyle=':')
    ax.plot([0, 50], [0, 80], color='black')

    ax2.text(0.05, 0.7, question,
        horizontalalignment='left',
        verticalalignment='center',
        fontsize=11, color='black',
        transform=ax2.transAxes)

    #this is to convert the graph to the text format to send
    #plt.show() #show the figure
    image = BytesIO()
    plt.savefig(image, format='png')
    #plt.savefig('image.png')
    image.seek(0)
    I=base64.encodebytes(image.getvalue())
    return {"photo": I.decode(), "Type":Q_type.multichoice, "Author":"Bennie"}

    # the send command is to send to the group, just make sure the cell, first cell, has been run before
send(milesKmConversion())

import random, math

def workout():
    #a
    n1 = random.randint(1, 10)
    n2 = random.randint(n1, n1+10)
    n3 = random.randint(1, 10)
    n3_pow = random.randint(-3, 3)
    correctAns = round(math.sqrt(n1/n2) + n3**n3_pow, 2)
    choices = [correctAns] #initialise choices with the correct, then generate 3 wrong answer to make up MCQ

    #generate wrong answers
    for _ in range(3):
        while(True):
            wrongAnswer = round(correctAns + random.uniform(-5, 5), 2)
            if wrongAnswer not in choices:
                choices.append(wrongAnswer)
                break

    random.shuffle(choices) #shuffle the choices including the correct and wrong answers

    figure = r'$ \sqrt{{ \frac{{ {} }}{{ {} }} }} + {}^{{ {} }} $'.format(n1, n2, n3, n3_pow)

    vars = {
        'figure': figure,
        'choices1': choices[0],
        'choices2': choices[1],
        'choices3': choices[2],
        'choices4': choices[3],
        'correctAns': correctAns
    }
    question = """
1   Use your calculator to work out {figure}.
    Give your answer correct to 2 decimal places.

    A. {choices1}
    B. {choices2}
    C. {choices3}
    D. {choices4}
    Answer: {correctAns}
    """.format(**vars) #unpack vars dict into string

    #just to convert to png
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1]) #add_axes(rect) where rect = [x0, y0, width, height]
    plt.axis('off')
    ax.set_ylim([0, 10])   # set the bounds to be 10, 10
    ax.set_xlim([0, 10])

    ax.text(0.1, 0.5, question,
        horizontalalignment='left',
        verticalalignment='center',
        fontsize=15, color='black',
        transform=ax.transAxes)

    #this is to convert the graph to the text format to send
    #plt.show() #show the figure
    image = BytesIO()
    plt.savefig(image, format='png')
    #plt.savefig('image.png')
    image.seek(0)
    I=base64.encodebytes(image.getvalue())
    return {"photo": I.decode(), "Type":Q_type.multichoice, "Author":"Bennie"}

    # the send command is to send to the group, just make sure the cell, first cell, has been run before
workout()

import random, math

def orderOfSize():
    ls =[i*0.5 for i in range(2*0, 2*10+1) if i != 0]
    print(ls)
    num = random.choice(ls)
    print(num)
    order = [round(num**2, 2), round(num, 2), round(num**3, 2), round(num**(1/3), 2)]
    orderDic = {round(num**2, 2):r'${}^{{2}}$'.format(num), round(num, 2):r'${}$'.format(num), round(num**3, 2):r'${}^{{3}}$'.format(num), round(num**(1/3), 2):r'$\sqrt[3]{{ {} }}$'.format(num)}
    correctAns = sorted(order)
    correctAnsFig = orderDic[correctAns[0]] + ' < ' + orderDic[correctAns[1]] + ' < ' + orderDic[correctAns[2]] + ' < ' + orderDic[correctAns[3]]
    print(correctAnsFig)
    choices = [correctAnsFig] #initialise choices with the correct, then generate 3 wrong answer to make up MCQ

    #generate wrong answers
    for c in range(3):
        while(True):
            ok = True
            random.shuffle(order)
            wrongAnswer = order.copy()
            wrongAnsFig = orderDic[wrongAnswer[0]] + ' < ' + orderDic[wrongAnswer[1]] + ' < ' + orderDic[wrongAnswer[2]] + ' < ' + orderDic[wrongAnswer[3]]
            # if wrongAnswer not in choices:
            #     choices.append(wrongAnswer)
            #     break
            for i in choices:
                if wrongAnswer == i:
                    ok = False
                    break
            if (ok):
                choices.append(wrongAnsFig)
                break


    random.shuffle(choices) #shuffle the choices including the correct and wrong answers

    figure = r'$ {num}^{{2}}\ \ \ \ {num}\ \ \ \ {num}^{{3}}\ \ \ \ \sqrt[3]{{ {num} }}$'.format(num=num)

    vars = {
        'figure': figure,
        'choices1': choices[0],
        'choices2': choices[1],
        'choices3': choices[2],
        'choices4': choices[3],
        'correctAns': correctAnsFig
    }
    question = """
5   Write the following in order of size, smallest first.
            {figure}

    A. {choices1}
    B. {choices2}
    C. {choices3}
    D. {choices4}
    Answer: {correctAns}
    """.format(**vars) #unpack vars dict into string

    #just to convert to png
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1]) #add_axes(rect) where rect = [x0, y0, width, height]
    plt.axis('off')
    ax.set_ylim([0, 10])   # set the bounds to be 10, 10
    ax.set_xlim([0, 10])

    ax.text(0.1, 0.5, question,
        horizontalalignment='left',
        verticalalignment='center',
        fontsize=15, color='black',
        transform=ax.transAxes)

    #this is to convert the graph to the text format to send
    #plt.show() #show the figure
    image = BytesIO()
    plt.savefig(image, format='png')
    #plt.savefig('image.png')
    image.seek(0)
    I=base64.encodebytes(image.getvalue())
    return {"photo": I.decode(), "Type":Q_type.multichoice, "Author":"Bennie"}

    # the send command is to send to the group, just make sure the cell, first cell, has been run before
send(orderOfSize())
