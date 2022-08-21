print("WELCOME TO MY QUIZ GAME")

start=input("Do you Want to get started? ")

if start.lower() != "yes":
    quit()
else:
    print("Great let's start...")   

name=input("Enter your name ")     
score=0
total_ques=0

question= input("what is CPU ") 
total_ques+=1 
if question.lower() == "centeral processing unit":
    print("Correct")
    score +=1
else:
    print("Sorry the answer is Centeral Processing Unit ")  

question= input("What do you call a type of shape that has five sides? ")  
total_ques+=1 
if question.lower() == "pentagon":
    print("Correct")
    score +=1
else:
    print("Sorry the answer is Pentagon  ")  

question= input("Which way is anti-clockwise, left or right? ")  
total_ques+=1 
if question.lower() == "left":
    print("Correct")
    score +=1
else:
    print("Sorry the answer is Left ")  

question= input("How many equal sides does an isosceles triangle have? ")  
total_ques+=1 
if question.lower() == "2":
    print("Correct")
    score +=1
else:
    print("Sorry the answer is 2 ")  

question= input("Which is the coldest location in the earth? ")  
total_ques+=1 
if question.lower() == "east antarctica":
    print("Correct")
    score +=1
else:
    print("Sorry the answer is East Antarctica")  

question= input('''The largest ‘Democracy’ in the world? ''')  
total_ques+=1 
if question.lower() == "india":
    print("Correct")
    score +=1
else:
    print("Sorry the answer is India  ")  

# question= input(" ")  
# total_ques+=1 
# if question.lower() == "":
#     print("Correct")
#     score +=1
# else:
#     print("Sorry the answer is  ")  

# question= input(" ")  
# total_ques+=1 
# if question.lower() == "":
#     print("Correct")
#     score +=1
# else:
#     print("Sorry the answer is  ")  

# question= input(" ")  
# total_ques+=1 
# if question.lower() == "":
#     print("Correct")
#     score +=1
# else:
#     print("Sorry the answer is  ")  

# question= input(" ")  
# total_ques+=1 
# if question.lower() == "":
#     print("Correct")
#     score +=1
# else:
#     print("Sorry the answer is  ")  


print("Congratulation "+ name +" you have got " + str(score) + " question right out of " + str(total_ques))
