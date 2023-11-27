print("Hey Welcome to the quiz game.")
play = input("Do u wanna play? (Y/N) : ").lower()

if play != 'yes':
    quit()
print("Okay!! Let's play....")
score = 0
answer = input("What CPU stands for? ").lower()
if answer == 'central processing unit':
    print("Correct")
    score += 1
else:
    print("Incorrect")
answer = input("What GPU stands for? ").lower()
if answer == 'graphics processing unit':
    print("Correct")
    score += 1
else:
    print("Incorrect")
answer = input("What RAM stands for? ").lower()
if answer == 'random access memory':
    print("Correct")
    score += 1
else:
    print("Incorrect")
answer = input("What ROM stands for? ").lower()
if answer == 'read only memory':
    print("Correct")
    score += 1
else:
    print("Incorrect")
answer = input("What SSD stands for? ").lower()
if answer == 'solid state drive':
    print("Correct")
    score += 1
else:
    print("Incorrect")

print(f'U got {score} questions correct')
print("U got "+ str(score/5*100) + "%.")