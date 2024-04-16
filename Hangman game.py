import random

word_list = ['mug', 'trains', 'steam', 'young', 'permit', 'prepare', 'marvelous', 'join', 'correct', 'exist', 'raspy', 'next', 'ignorant', 'wooden', 'noxious', 'sugar', 'wax', 'crime', 'honey', 'strip', 'superb', 'yielding', 'squeal', 'copy', 'demonic', 'dam', 'moon', 'safe', 'wanting', 'shoe', 'guard', 'sin', 'spray', 'finicky', 'release', 'thirsty', 'striped', 'snatch','blue', 'thank', 'war', 'basket', 'grass', 'chase', 'nutritious', 'crayon', 'desire', 'distinct', 'self', 'drink', 'fascinated', 'feeling', 'offbeat', 'mushy', 'encouraging', 'bag', 'rifle', 'expect', 'sidewalk', 'thick']

system_guess = random.choice(word_list).lower()
allowance = 0
chances = len(system_guess) + allowance

print(f"""
    
    Hangman Game is Started. You have only {chances} chances.
    My word is a {len(system_guess)} letter word, can you guess it?
    """)

playing = True
correct_guess = 0

print(f"Hint: word is                                               >>{system_guess}")

display = []
for letter in system_guess:
    display.append('_')

while chances > 0 and playing:
    print(' '.join(display))
    print(f"""

    """)
    user_guess = input("Guess a letter: ").lower()

    if user_guess in system_guess:
        index_count = 0
        correct_guess += 1

        if user_guess in display:
            print("Good work, but you guessed that letter already..")
            continue
        else:
            for letter in system_guess:
                if letter == user_guess:
                    display[index_count] = letter
                index_count += 1
        
        if correct_guess == len(system_guess) or ''.join(display) == system_guess:
            print("Congratulations! You guessed right.")
            print(f"The word was {system_guess}")
            break
        
    else:
        chances -= 1
        print(f"Wrong guess! Still {chances} left")
    continue
else:
    if chances == 0:
        playing = False
        print("You are dead and out of chances")
    if playing is False:
        print("You are dead and out of chances")





