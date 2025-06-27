from random import randint

import prompt


def start():
    print("Welcome to the Brain Games!")

    name = prompt.string('May I have your name? ')
    print(f'Hello, {name.strip()}')
    
    step = True
    i = 0

    print('Answer "yes" if the number is even, otherwise answer "no".')

    while step and i < 3:
        number = randint(1, 100)
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        answer = answer.lower().strip()

        step = (
		is_right_answer(answer, number) 
		if answer in {'yes', 'no'} 
		else False
	)

        if step:
            print('Correct!')
        else:
            print(
		f"'{answer}' is wrong answer ;(."
		f"Correct answer was '{get_right_answer(number)}'."
		)
            print(f"Let's try again, {name}!")
            return
        i += 1

    print(f'Congratulations, {name}!')


def is_right_answer(answer, number):
    return answer == get_right_answer(number)


def get_right_answer(number):
    return 'yes' if is_even(number) else 'no'


def is_even(number):
    return number % 2 == 0

