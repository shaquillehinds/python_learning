from random import choice
# baby question
questions = ['Why does the sun shine?', 'Why is the sky blue?',
             "Why can we talk and animals can't?", "Why are there only 7 days?"]
question = choice(questions)
# my answer
answer = input(question)
while(answer.lower().strip() != 'just because'):
    # baby asking why
    question = 'But why?'
    # my response
    answer = input(question)

# baby final response
print('Oh... Okay! :)')
