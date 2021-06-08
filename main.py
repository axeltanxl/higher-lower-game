import random
from art import logo, vs
from game_data import data
import os

# Main game loop
def main():
    global score, answer, account_a, account_b
    score = 0
    answer = 1
    account_a = account_generator()
    account_b = account_generator()
    while account_b == account_a:
        account_b = account_generator()
    while answer != 0:
        print(logo)
        if score > 0:
            print(f"You're right! Current score: {score}")
        main_print(account_a, account_b)
        answer = input("Who has more followers? Type 'A' or 'B': ")
        check_answer()
        cls()
        if answer == 0:
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            break
        else:
            account_a = account_b
            account_b = account_generator()
            continue

# Clear screen to update score and accounts
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

# Generate accounts to compare
def account_generator():
    return random.choice(data)

# Printing function
def main_print(account_a, account_b):
    print(
        f"Compare A: {account_a['name']}, a {account_a['description']}, from {account_a['country']}.")
    print(vs)
    print(
        f"Against B: {account_b['name']}, a {account_b['description']}, from {account_b['country']}.")

# Check answer and update score
def check_answer():
    global score, answer
    if answer.lower() == 'a' and account_a['follower_count'] > account_b['follower_count']:
        score += 1
    elif answer.lower() == 'b' and account_b['follower_count'] > account_a['follower_count']:
        score += 1
    else:
        answer = 0


main()
