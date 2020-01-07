
total = int(input('How much money do you have in your pocket\n'))

# YOUR CODE HERE
if total > 100:
    total = "Give me your money!"
    print(total)
elif total > 50:
    total = "Buy me some coffee you cheap!"
    print(total)
else:
    print("You are a poor guy, go away!")
