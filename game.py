word = []
guess = []
def main():
    f = open("words.txt","r")
    fl = f.readlines()
    choice = int(input("Enter a number between 1 and " + str(len(fl)) +": "))
    choice = fl[choice-1][:-1]
    guesses = 6
    x=0
    while(x<len(choice)):
        if -len(choice)+1+x is 0:
            end = None
        else:
            end = -len(choice)+1+x
        word.append(choice[x:end])
        x+=1
    x=0
    while(x<len(word)):
        if word[x] is " ":
            guess.append(" ")
        else:
            guess.append("_")
        x+=1
    end = False
    while(not end):
        print(*guess)
        print("you have " + str(guesses) + " guesses left.")
        letter = input("Guess a letter: ")
        if not check(letter):
            guesses -=1
        if win():
            print(*guess)
            print("You guessed the word! Good job.")
            end = True
        if guesses is 0:
            print("You lost. The word was", end = " ")
            print(choice+".")
            end = True
def win():
    x=0
    win = True
    while(x<len(guess)):
        if guess[x] is "_":
            win = False
        x+=1
    return(win)
def check(letter):
    x=0
    swapped = False
    while(x<len(word)):
        if word[x] is letter:
            guess[x] = letter
            swapped = True
        x+=1
    return(swapped)
if __name__== "__main__":
    main()
