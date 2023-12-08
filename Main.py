from random import randint
run = True
while (run):
     Target = randint(0,100)
     i = 1
     while (i<=5):
      print("You have %d attempts"%(6-i))
      Guess = int(input("Guess my number: "))
      if Guess == Target:
         choice = input('Your Right\nContinue?\nyes or no:')
         if choice == 'yes':
            run = True
            break
         else:
            run = False
            break
      elif Guess < Target:
         print("Your Guess is low than Target")
      else:
         print("Your Guess is high than Target")
      i += 1
     if i == 6:
        print("The right answer is %d"%(Target))
        choice = input('Continue?\nyes or no:')
        if choice == 'yes':
            run = True
           
        else:
            run = False
