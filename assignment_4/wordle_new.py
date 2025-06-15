import random
def generation_secret_word(words_list):
    secret_word = random.choice(words_list)
    return secret_word
def length_check(secret_word, guess_secret_word):
        if len(guess_secret_word)!= len(secret_word):   
            print("Wrong length. Expected", len(secret_word))
            return True
        return False
def win_check(secret_word, guess_secret_word):
     if guess_secret_word == secret_word: 
        print("You win!!!")
        return True
     return False
def checking_letters_in_guess(secret_word, guess_secret_word):
    display=[]
    i = 0
    while i < len(secret_word):
        if guess_secret_word[i] == secret_word[i]:
            display.append("["+guess_secret_word[i].upper()+"]")
            print(guess_secret_word[i],"is in the right place")
        elif guess_secret_word[i] in secret_word:
            display.append("("+guess_secret_word[i]+")")
            print(guess_secret_word[i],"is in the word, but in the other place")
        else:
            display.append(" "+guess_secret_word[i]+" ")
            print(guess_secret_word[i],"isn't in the word")
        i += 1
    print("Result:", *display)
def lose_of_game(tries, secret_word):
    if tries == 0:
            print("You lose! The word was:", secret_word)

words_list = ['apple',    'bread', 'candy', 'dream','eagle','flame','grape','house','input','joker']

while True:
    print("Welcome to Wordle! \n Guess the",len(words_list[1]),"-letter word. You have", 6, "tries.\n If you want to leave the game, write: leave")
    secret_word = generation_secret_word(words_list)
    tries = 6
    try:
         while tries!= 0:
              guess_secret_word = input("Attempt "+str(7 - tries)+"/6 – Enter guess: ").lower()
              if guess_secret_word == "leave":
                  print("It's the end")
                  break

              if length_check(secret_word, guess_secret_word) == True:
                   continue         
              checking_letters_in_guess(secret_word, guess_secret_word)
              if win_check(secret_word, guess_secret_word)== True or tries <= 0:
                 break
              tries -= 1
              lose_of_game(tries, secret_word)
         leave_or_stay = input("Write again, if you want to play again\n Write leave if you want to leave the game")
         if leave_or_stay == "leave":
                break
    except Exception as e:
      print(e)
    



