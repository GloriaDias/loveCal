print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_name=name1+name2

convertCombined_name=combined_name.lower();
t=convertCombined_name.count("t")
r=convertCombined_name.count("r")
u=convertCombined_name.count("u")
e=convertCombined_name.count("e")
true=t+r+u+e
l=convertCombined_name.count("l")
o=convertCombined_name.count("o")
v=convertCombined_name.count("v")
e=convertCombined_name.count("e")
love=l+o+v+e
score_love=str(true) + str(love)
print(score_love)
if(int(score_love)<20 or int(score_love)>90):
  print(f"Your score is {score_love}, you go together like coke and mentos.")
elif(int(score_love)>=40 and int(score_love)<=50):
  print(f"Your score is {score_love}, you are alright together.")
else:
  print(f"Your score is {score_love}")