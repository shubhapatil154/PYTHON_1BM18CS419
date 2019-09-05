import string
import random

def pwd_generate(num_of_char):
    lower_case = [random.choice(string.ascii_lowercase) for lc in range(num_of_char)]
    upper_case = [random.choice(string.ascii_uppercase) for uc in range(num_of_char)]
    punctuation = [random.choice(string.punctuation) for p in range(num_of_char)]
    numbers = [random.choice(string.digits) for d in range(num_of_char)]
    password = ''.join(upper_case+lower_case+punctuation+numbers)
    #print(password)
    #print(len(password))
    generated_pwd =''.join(random.choice(password) for i in range(num_of_char))
    print(generated_pwd)

num_of_char=int(input("ENTER  THE NUMBER OF CHARACTERS: "))
print("YOUR PASSWORD IS: ")
pwd_generate(num_of_char)
