import random


for i in range(10):
    integer = random.randint(1 , 100)
    number = random.randint(1 , 100)
    print(integer)
    print(number)
    product = integer * number
    useranswer = int(input("what is your answer?"))
    if useranswer == product:
       print("correct")
    else:
       print("Incorrect the answer is" ,product)
    score = i
    if useranswer == product :
        score = score + 1
        print("Score:" , score)