#change code to implement abstraction ,i.e., oops
#check for all possible errors from user or code
import numpy as np
import getch
root = "groot"
#add code to make sure valid root
wordlength = len(root)

root = list(root)

chartrack = np.empty(26)
chartrack.fill(0)

answer = ""
initial = "-"
for i in range(wordlength):
	answer += initial

#print(answer)

for i in range(wordlength):
	print(answer[i],end = "")
print()

answer = list(answer)

attempts = 0

limit = 10#make the attempt limit more realistic, dynamic wrt the word taken as root

remaining = wordlength

choices = ""

while attempts < limit :
	print("Enter your guess : ",end = "",flush = True)
	guess = getch.getche()
	print()
	if guess.isalpha() == False :
		print("Invalid input!!! Please give an alphabet.")
		continue	
	if guess in choices:
		print("Enter a new guess!!!")
		continue
	else:
		choices += guess
	attempts += 1
	if guess in root:
		for i in range(wordlength):
			if(root[i] == guess):	
				answer[i] =	root[i]
				remaining -= 1
	if remaining <= 0:
		print("Congrats!!! You got it right!!! =b=b")
		break
	print("Current state : ",end = "")
	for i in range(wordlength):
		print(answer[i],end = "")
	print(" and remaining attempts are ", limit - attempts)
if remaining > 0 :
	print("Mission Failed. We'll get them next time.")
print("Reached end of game")

#handle why not printing before getch
#add code to make sure no penalization for duplicate attempts
#add code to make sure no invalid guesses