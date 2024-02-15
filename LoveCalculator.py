print(
    
    '''
                       $$$$$$$$$$$$$$$$$$$$$$$$$
                       $$$$$$$$$$$$$$$$$$$$$$$$$
                       $$$$$'`$$$$$$$$$$$$$'`$$$
                       $$$$$$  $$$$$$$$$$$  $$$$
                       $$$$$$$  '$/ `/ `$' .$$$$
                       $$$$$$$$. i  i  /! .$$$$$
                       $$$$$$$$$.--'--'   $$$$$$
                       $$^^$$$$$'        J$$$$$$
                       $$$   ~""   `.   .$$$$$$$
                       $$$$$e,      ;  .$$$$$$$$
                       $$$$$$$$$$$.'   $$$$$$$$$
                       $$$$$$$$$$$$.    $$$$$$$$
                       $$$$$$$$$$$$$     $by&TL$
                       -------------------------
                             I LOVE YOU
                       -------------------------
       
  '''
)

# Display an introductory message
print("The Love calculator is calculating your score...\n")

# Prompt the user to enter two full names
Name1 = input("Please Enter your first full name: ")
Name2 = input("Please Enter your second full name: ")

# Combine the two names and convert them to lowercase
Combined_Name = Name1 + Name2
lower_names = Combined_Name.lower()

# Count occurrences of specific letters in the combined lowercase name
# for the first part of the love score calculation (t, r, u, e)
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e 

# Count occurrences of specific letters in the combined lowercase name
# for the second part of the love score calculation (l, o, v, e)
l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

# Concatenate the two digits to form the love score
score = int(str(first_digit) + str(second_digit))

# Determine the interpretation of the love score and display the result
if (score < 10) or (score > 90):
    print(f"Your score is {score}, you go together like coke & mentos.")
elif (score >= 40) and (score <= 50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
