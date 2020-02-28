def main():
  import random
  
  dice_rolls = int(input('How many dice to roll?'));
  dice_size = int(input('How sides are of the dice?'));
  dice_sum = 0;
  
  for i in range(0, dice_rolls):
    roll = random.randint(1,dice_size)
    #roll1 = random.randint(1,6);
    dice_sum += roll;
    if roll == 1:
      print(f'you rolled a {roll}, thats a 1')
    elif roll ==6:
      print(f'you rolled a {roll}, thats a 6')
    else:
      print(f'You rolled a  {roll}')
    
  print(f'You rolled a total of {dice_sum}')
  
if __name__== "__main__":
  main()

  
