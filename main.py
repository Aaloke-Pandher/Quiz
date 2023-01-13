# Create a Quiz Assignment 

# Score 
score = 0 

# Question 1 
answer1 = input("What is 5 + 5? ").lower()
if answer1.lower() == "10" or answer1 == "ten": 
    print("Correct")
    score = score + 1
else: 
    print("Incorrect")

# Question 2 
answer2 = input("What are prompts called in python? ").lower()
if answer2.lower() == "input" or answer2 == "inputs": 
    print("Correct")
    score = score + 1
else: 
    print("Incorrect")

# Question 3 
answer3 = input("Who is the Prime Minister of Canada? ").lower()
if answer3.lower() == "justin trudeau" or answer3 == "trudeau" or answer3 == "justin": 
    print("Correct")
    score = score + 1
else: 
    print("Incorrect")

# Question 4 
answer4 = input("What year is it? ").lower()
if answer4.lower() == "2023": 
    print("Correct")
    score = score + 1
else: 
    print("Incorrect") 

# Output Results
print("You got " + str(score) + "/4.") 

if score == 4: 
    print("Good Job!") 
elif score == 3:
    print("Almost There.")
elif score == 2: 
    print("Atleast you passed.") 
elif score == 1:
    print("Put in some more effort.")
else: 
    print("Try again and do better.")