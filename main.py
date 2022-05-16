import cat
import dog
import random 

def main():
  try: 
    playing = True 
    DogFacts = dog.DogFacts()
    CatFacts = cat.CatFacts()
    DogFacts.getFact()
    CatFacts.getFact()

  except Exception as e: 
    print(e)
    print("Do you like cats or dogs?")

  else:
    while playing == True:
      DogFacts.getFact()
      CatFacts.getFact()
      print("-------------------------------------\n")
      print("Do you like dogs and cats? Here are some facts about them below. \n")
      int = random.randint(1, 2)
      print("The fun fact is:\n")
      if int == 1:
        print(DogFacts.fact)
        correct_answer = 'a true Dog Fact'
      if int == 2: 
        print(CatFacts.fact)
        correct_answer = 'a true Cat Fact'
      if int == 3: 
        print(DogFacts.fact)
        correct_answer = 'a false Dog Fact'
      if int == 4: 
        print(CatFacts.fact)
        correct_answer = 'a false Cat Fact'
      print(input('\n Hit enter to continue'))
      print("-----------------------------------\n")
      print("\n Is this fact about a dog or cat? Is the fact true?\n")
      answer = input('Enter \n 1: Dog Fact is true \n 2: Cat Fact is true \n 3: Dog Fact is false\n 4: Cat Fact is false\n Answer: ')
      if answer == str(int):
        print(f"Correct! Nice job. That fact was {correct_answer}")
      else:
        print(f"Incorrect! That fact is  {correct_answer}")
      play_again = input("\nWould you like to play again? If yes, press enter. Otherwise, input 'Q'\n")
      if play_again == "Q":
        playing = False


main()
    
      
