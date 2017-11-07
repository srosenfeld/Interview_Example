'''
Interview project
------------------
This project is designed to help you build an automated assistant
which can help you prepare for high school interviews! Here are a
few examples from the Secondary School Placement office.

1. Tell me about your classes (Favorite, hardest, most interesting, etc...)
2. What are some of your extra curricular activities?
3. What have you read recently?
4. How was the summer?
5. Talk about your academic and personal strengths and weaknesses
 
'''


#Interview Function

def question(question):
    global answer
    answer = input(question)
    print(answer)



#Interview Questions
    
question("What's your name?")


question("What's your favorite class?")
if answer == "Math":
    question("Wonderful, what are you learning now?")
    print("Wow, I can almost remember studying " + answer + " when I was your age!")


question("Do you play any sports?")

