from unittest import result


print("WELCOME TO MY PYTHON QUIZ GAME....")

playing = input("Do You Want to Play Quiz Game? Yes/No: ")

score = 0

if playing.lower()!= 'yes':
    quit()

print("Okay! Let's play.")
result = input("What does CPU stands for? ")
if result.lower() == 'central processing unit':
      print("correct!")
      score += 1
else:
      print("Incorrect!")

result = input("What does ALU stands for? ")
if result.lower() == 'arithmetic logic unit':
      print("correct!")
      score += 1
else:
      print("Incorrect!")

result = input("What does CU stands for? ")
if result.lower() == 'control unit':
      print("correct!")
      score += 1
else:
      print("Incorrect!")

result = input("What does ATM stands for? ")
if result.lower() == 'automated teller machine':
      print("correct!")
      score += 1
else:
      print("Incorrect!")

result = input("What does TCP stands for? ")
if result.lower() == 'transmission control protocol':
      print("correct!")
      score += 1
else:
      print("Incorrect!")

print("you got " + str(score) + " questions correct!")