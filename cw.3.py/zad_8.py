import random

print("Welcome to this game!")


def multipli_game():
    correct_answer = 0
    wrong_answer = 0

    for i in range(1, 11):
        first_random = random.randint(1, 9)
        second_random = random.randint(1, 9)
        expected_answer = first_random * second_random
        answer = int(input(f"Question {i}: {first_random} * {second_random} = "))

        if answer == expected_answer:
            print("Correct answer!")
            correct_answer += 1
        else:
            print(f"Wrong answer! The correct answer is ", expected_answer)
            wrong_answer += 1

    print("Game Over!")
    print("Number of correct answers: ", correct_answer)
    print("Number of wrong answers: ", wrong_answer)


multipli_game()