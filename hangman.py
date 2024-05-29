import tkinter
canvas = tkinter.Canvas(bg="white", height=400, width=300)
canvas.pack()

print("\nWelcome to Hangman!")
print("(to exit the game type=> exit)")

def choose_word():
    word = input("\nEnter a word for the Hangman game: ")
    return word.lower()
    

def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '_'
    return display

def hangman():
    word_to_guess = choose_word()
    guessed_letters = [" "]
    attempts = 12
    
    while attempts > 0:
        print("\nWord:", display_word(word_to_guess, guessed_letters))
        guess = input("Guess a letter: ").lower()
        
        if guess == "exit":
            break

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word_to_guess:
            print("Good guess!")
        else:
            print("Wrong guess!")

            attempts -= 1
            print("Attempts: ", attempts)

         
            if attempts == 11:
                canvas.create_arc(50, 300, 150, 230, start=0, extent=180, fill="white", outline="black", width=2)
                canvas.create_line(45, 265, 155, 265, fill="white", width=2)
            elif attempts == 10 : 
                canvas.create_line(100, 230, 100, 100, width=2)
            elif attempts == 9 :
                canvas.create_line(100, 100, 200, 100, width=2)
            elif attempts == 8 :
                canvas.create_line(100, 130, 130, 100)
            elif attempts == 7 :
                canvas.create_line(200, 100, 200, 130, width=2)
            elif attempts == 6 :
                canvas.create_oval(180, 130, 220, 170)
            elif attempts == 5 :
                canvas.create_line(200, 170, 200, 210)
            elif attempts == 4 :
                canvas.create_line(200, 210, 180, 240)
            elif attempts == 3 :
                canvas.create_line(200, 210, 220, 240)
            elif attempts == 2 :
                canvas.create_line(200, 170, 180, 200)
            elif attempts == 1 :
                canvas.create_line(200, 170, 220, 200)
            else:
                print("you lost!")

            

        if set(word_to_guess) == set(guessed_letters) & set(word_to_guess):
            print("\nCongratulations! You've guessed the word:", word_to_guess)
            break

    if attempts == 0:
        print("\nSorry, you're out of attempts. The word was:", word_to_guess)

hangman()
print("Thanks for playing :)")




