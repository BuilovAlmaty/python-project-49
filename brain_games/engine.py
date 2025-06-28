from random import randint
import prompt

def start(games_name):
    print("Welcome to the Brain Games!")

    name = prompt.string('May I have your name? ')
    print(f'Hello, {name.strip()}')
    
    step = True
    i = 0

    greeting(games_name)    

    while step and i < 3:
        number = get_question(games_name)
        print(f'Question: {number}')

        answer = answer_processing(games_name)

        step = guard_ex(games_name, answer)
        
        if step:
            step = is_right_answer(answer, number, games_name) 

        if step:
            print('Correct!')
        else:
            print(
		    f"'{answer}' is wrong answer ;(."
		    f"Correct answer was '{get_right_answer(number, games_name)}'."
		    )
            print(f"Let's try again, {name}!")
            return
        i += 1

    print(f'Congratulations, {name}!')

def is_right_answer(answer, number, games_name):
    return answer == get_right_answer(number, games_name)

def get_right_answer(number, games_name): 
    match games_name:
        case 'even':
            return 'yes' if is_even(number) else 'no'
        case 'calc':
            return eval(number)
        
def get_question(games_name):
    match games_name:
        case 'even':
            return randint(1, 100)
        case 'calc':
            list_of_signs = [" + ", " - ", " * "]
            a = str(randint(1, 100))
            b = str(randint(1, 100))
            sign = list_of_signs[randint(0, 2)]
            return a + sign + b    

def is_even(number):
    return number % 2 == 0

def answer_processing(games_name):
    match games_name:
        case 'even':
            answer = prompt.string('Your answer: ')
            return answer.lower().strip()
        case 'calc':
            return prompt.integer('Your answer: ')

def guard_ex(games_name, answer):
    match games_name:
        case 'even':
            return answer in {'yes', 'no'}
        case 'calc':
            return isinstance(answer, int)
        
def greeting(games_name):  
    match games_name:
        case 'even':
            print('Answer "yes" if the number is even, otherwise answer "no".')
        case 'calc':
            print('What is the result of the expression?')
