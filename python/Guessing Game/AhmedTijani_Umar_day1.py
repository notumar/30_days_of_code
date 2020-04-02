def guess_my_number(attempts,answer):
    '''
    takes a guess from a user and returns the difference between their final guess and the actual value
    
    Parameters to use
    ----------
    guess: int 
    a value between 0 and 100
    
    attempts: int
        the number of guesses you wish to allow
    answer: int
        The target number
    '''
    while attempts > 0:
        guess = int(input("Please enter a number between 0 and 100: "))
        if guess > 100 or guess < 0:
            guess= int(input("Kindly enter a number between 0 and 100: "))
            continue
        else:
            if guess == answer:
                return f"Youre right! The number was guess: {guess} and answer: {answer}"
                break

            elif guess > answer:
                return "guess lower"
                attempts -=1
                print(f"you have {attempts} attempts left")

            elif guess < answer:
                print ("guess higher")
                attempts -=1
                print(f"you have {attempts} attempts left")
    else:
        return f"you have {attempts} attempts left... thanks for guessing!"




print (guess_my_number(4,12))
