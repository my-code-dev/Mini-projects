import random

def get_user_choice():
    user_input = input("Enter rock, paper, or scissors : ").lower()
    while user_input not in ['rock','paper','scissors']:
        print("Invalid choice. Please try again.")
        user_input = input("Enter rock, paper, or scissors : ").lower()
    return user_input

def get_computer_choice():
    return random.choice(['rock','paper','scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
        (user_choice == 'paper' and computer_choice == 'rock') or \
        (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "You lose!"
    
def play_game():
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(result)
        play_again = input("Play again ? (y/n):").lower()
        while play_again not in ['y','n','yes','no']:
            play_again = input("Play again ? (y/n):").lower()
        if play_again in ['no','n']:
            print("Bye bye")
            break

if __name__ == "__main__":
    play_game()


