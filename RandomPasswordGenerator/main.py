# Random_Password_Generator
# importing required packages
import random
import string


def shuffling(passwrd):
    lst = list(passwrd)
    random.shuffle(lst)
    passwrd = ''.join(lst)
    return passwrd


def random_password_generator():
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_symbols = list("!@#$%^&*?|_")
    print("Enter number of\nuppercase_letters  lowercase_letters  digits  symbols:")
    k1, k2, k3, k4 = map(int,input().split())
    result = "".join(random.choices(uppercase_letters,k=k1)+random.choices(lowercase_letters,k=k2)+
                       random.choices(digits,k=k3)+random.choices(special_symbols,k=k4))
    result = shuffling(result)
    return result


if __name__ == "__main__":
    while True:
        choice = int(input("Enter choice:\n1)Generate Password 2)Exit\n"))
        if choice == 1:
            password = random_password_generator()
            print("Generated Password: ", password)
        elif choice == 2:
            break
        else:
            print("Invalid Choice")
