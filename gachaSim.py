#!/usr/bin/python
#Importing random plug-in
import random

#Pull rate to pull that 1 SSR you want, assumed to be 1 since it's 1%
pullRate = 1
counter = 0
amount = 0

#Loop runs until the ssrValue hits your designated pullRate number
while True:
    ssrValue = random.randint(1,100)
    if ssrValue == pullRate:
        counter += 1
        amount = (counter/10) * 35
        print(ssrValue, " is your ssrValue")
        print(pullRate, " is your pullRate")
        print("Congrats you pulled the SSR")
        print("It only took you ", counter, "pulls and it totals to $",amount, "dollars on a $35 per multi rate\n")
        break
    else:
        counter += 1
        print(ssrValue, " is your ssrValue")
        print(pullRate, " is your pullRate")
        print("You did not roll the SSR you needed, keep rolling\n")
        
      


