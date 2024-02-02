import random

characs=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H',
'I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','!','@','#','$','%','^','*','(',')']
class PasswordGenerator:
    def Gen(self):
        OK=True
        while OK:
            password=""
            print("Enter the following info: ")
            length=int(input("How many characters should be in you password? Enter in integer form."))
            for i in range(length):
                password+=random.choice(characs)
            print(f"Your password is {password}")
            OK=input("Do you want to try again and regenerate. Yes or No? ")
            if OK=="Yes":
                OK=True
            elif OK=="No":
                OK=False





Generator=PasswordGenerator()
Generator.Gen()