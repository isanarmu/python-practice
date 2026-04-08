
name = input("your name here:")
print(f"Hi {name} let`s play a game, you have to guess what number i'm thnking of, less than 100 and more than 83 ;)")



def number_given_by_user():
    secret_number = 89
    secret_guess = int(input(" try a random numeber here: "))
    while secret_number != secret_guess:
        other_guess = int(input("Try again here: "))
        secret_guess = other_guess 
        print(other_guess)
    else:
        print("CONGRATULATIONS youu guessed it right")

    
number_given_by_user()