from random import randint

import prompt


def start(games_name):
    print("Welcome to the Brain Games!")

    name = prompt.string("May I have your name? ")
    print(f"Hello, {name.strip()}")

    step = True
    i = 0
    steps_count = 3

    greeting(games_name)

    while step and i < steps_count:
        question = get_question(games_name)
        print(f"Question: {question['question']}")

        answer = answer_processing(games_name)

        step = guard_ex(games_name, answer)

        if step:
            step = answer == question["right_answer"]

        if step:
            print("Correct!")
        else:
            print(
                f"'{answer}' is wrong answer ;(."
                f"Correct answer was '{question['right_answer']}'."
            )
            print(f"Let's try again, {name}!")
            return
        i += 1

    print(f"Congratulations, {name}!")


def get_question(games_name):
    max_random_border = 100
    match games_name:
        case "even":
            number = randint(1, max_random_border)
            return {
                "question": str(number),
                "right_answer": "yes" if is_even(number) else "no",
            }
        case "calc":
            list_of_signs = [" + ", " - ", " * "]
            a = str(randint(1, max_random_border))
            b = str(randint(1, max_random_border))
            sign = list_of_signs[randint(0, len(list_of_signs) - 1)]
            return {
                "question": a + sign + b,
                "right_answer": eval(a + sign + b),
            }
        case "gcd":
            set = (randint(1, max_random_border), randint(1, max_random_border))
            return {
                "question": f'{set[0]} {set[1]}',
                "right_answer": euclids_algorithm(set),
            }
        case "progression":
            progression_list = get_progression()
            x_pos = randint(1, len(progression_list) - 2)
            represent = ""
            for i in range(len(progression_list)):
                if i == x_pos:
                    represent += ".. "
                else:
                    represent += str(progression_list[i]) + " "
            return {
                "question": represent,
                "right_answer": progression_list[x_pos],
            }
        case "simple":
            number = randint(1, max_random_border)
            return {
                "question": str(number),
                "right_answer": "yes" if is_simple(number) else "no",
            }


def is_even(number):
    return number % 2 == 0


def euclids_algorithm(number):
    a, b = number

    if a == 0 or b == 0:
        return 1
    if a == b:
        return a
    if a > b:
        max = a
        min = b
    else:
        max = b
        min = a

    balance = max

    while min != 0:
        while balance >= min:
            balance -= min
        max = min
        min = balance
        balance = max

    return max


def is_simple(number):
    if number < 2:
        return False
    i = 2
    while i <= number // 2:
        if number % i != 0:
            i += 1
        else:
            return False
    return True


def get_progression():
    first = randint(1, 100)
    diff = randint(1, 9)
    progression_len = 10

    return [first + diff * i for i in range(progression_len)]


def answer_processing(games_name):
    match games_name:
        case "even":
            answer = prompt.string("Your answer: ")
            return answer.lower().strip()
        case "calc":
            return prompt.integer("Your answer: ")
        case "gcd":
            return prompt.integer("Your answer: ")
        case "progression":
            return prompt.integer("Your answer: ")
        case "simple":
            answer = prompt.string("Your answer: ")
            return answer.lower().strip()


def guard_ex(games_name, answer):
    match games_name:
        case "even":
            return answer in {"yes", "no"}
        case "calc":
            return isinstance(answer, int)
        case "gcd":
            return isinstance(answer, int)
        case "progression":
            return isinstance(answer, int)
        case "simple":
            return answer in {"yes", "no"}


def greeting(games_name):
    match games_name:
        case "even":
            print('Answer "yes" if the number is even, otherwise answer "no".')
        case "calc":
            print("What is the result of the expression?")
        case "gcd":
            print("Find the greatest common divisor of given numbers.")
        case "progression":
            print("What number is missing in the progression?")
        case "simple":
            print(
                'Answer "yes" if given number is prime. Otherwise answer "no".'
            )
