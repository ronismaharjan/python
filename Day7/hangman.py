import random, hangman_art, hangman_words
print(hangman_art.logo)
print("\n")

choosen_word = random.choice(hangman_words.word_list)
print(choosen_word)
dashed = []
life = 6
end_of_game = False

for num in range(0, len(choosen_word)):
  dashed.append("_")

while not end_of_game:
  print(dashed)
  print(life)

  guess = str(input("Guess a letter: ")).lower()
  for index in range(len(choosen_word)):
    
    letter = choosen_word[index]
    if(guess == letter):
      dashed[index] = guess
     
      
  if guess not in choosen_word:
    
    life -= 1
    print(hangman_art.stages[life])
  if "_" not in dashed:
    print("you won")
    end_of_game = True
  elif(life == 0):
    print("you loose")
    end_of_game = True
  