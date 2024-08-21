import random
import time
alphabet=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
amount_tries=0
monkey_typing=True
user_input=input("Type the words you want it to find: ").upper()
individual_letters=list(user_input)
start=time.time()
while monkey_typing:
    random_string=[]
    for letter in individual_letters:
        randomletter=random.choice(alphabet)
        random_string.append(randomletter)
        amount_tries+=1
        print(f"Monkey Typing: {randomletter} Attempting to find {individual_letters}")
    if random_string==individual_letters:
        monkey_typing=False
end=time.time()
print(f"Number of tries: {amount_tries}")
print(f"{end - start:.2f} seconds elapsed.")