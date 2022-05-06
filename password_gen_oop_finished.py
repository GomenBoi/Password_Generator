import random
import string

# OOP version of password generator made by Roberto Da Silva on 06/05/2022 - Note: You can replace the ascii random generation with arrays which would in theory make the time complexity O(n) rather than O(n^2) but it is fine for time being.

class password_gen():
    def __init__(self, database):
        self.__username = ""
        self.__password = ""
        self.sizes = {
            "Sum" : 0
            }
        self.limits = [[0, "uppercase", 65, 90],[0, "lowercase", 97, 122],[0, "symbol"],[0, "numeric"]]
        self.__database = database

    def generatePassword(self):
        self.inputSizes()
        self.generateCharactersWithAscii()
        self.shufflePassword()
        self.outputPassword()
        self.appendToFile()
        self.promptGenerate()

    def inputSizes(self):
        try:
            counter = 0 
            self.sizes["Size"] = abs(int(input("Enter length of password: ")))
            while self.sizes["Sum"] != self.sizes["Size"]:
                self.limits[counter][0] = abs(int(input(f"Enter number of {self.limits[counter][1]} characters: \n")))
                self.sizes["Sum"] += self.limits[counter][0]
                counter += 1
                if counter > 3:
                    self.sizes["Sum"] = 0 if self.sizes["Sum"] != self.sizes["Size"] else self.sizes["Size"]
                    counter = 0
        except ValueError:
            print("Invalid input entered, please try again.\n")

    def generateCharactersWithAscii(self):
        counter = 0
        punctuationArr = string.punctuation
        while counter <= 1:
            for i in range(self.limits[counter][0]):
                self.__password += chr(random.randint(self.limits[counter][2], self.limits[counter][3]))
            counter += 1
        for i in range(self.limits[2][0]):
            self.__password += random.choice(punctuationArr)
        for i in range(self.limits[3][0]):
            self.__password += str(random.randint(0, 9))
    
    def shufflePassword(self):
        stringList = list(self.__password)
        random.shuffle(stringList)
        self.__password = ''.join(stringList)

    def outputPassword(self):
        print(f"Your password that you generated is {self.__password}, with username {self.__username}.")

    def verifyUsername(self):
        with open(self.__database, "a+") as file:
            file.seek(0)
            for line in file:
                if self.__username in line.split(":"):
                    print("That username is taken!\n")
                    return True
        return False

    def promptGenerate(self):
        varinput = input("Do you want to generate a new username and password?: (y/n) ")
        if varinput.lower() == "y":
            self.resetVars()
            self.promptUsername()
            self.generatePassword()
        print(f"Thank you very much for using our service {self.__username}, :)")

    def promptUsername(self):
        try:
            self.__username = input("Enter your username: ")
            while self.verifyUsername():
                self.__username = input("Enter your username: ")
        except ValueError:
            print("Invalid input entered, please try again.\n")

    def resetVars(self):
        self.__username = ""
        self.__password = ""
        self.sizes = {
            "Sum" : 0
            }
        self.limits = [[0, "uppercase", 65, 90],[0, "lowercase", 97, 122],[0, "symbol"],[0, "numeric"]]

    def appendToFile(self):
        found = False
        with open(self.__database, "a+") as file:
            file.seek(0)
            for line in file:
                if self.__password in line.split(":")[1]:
                    found = True
            if not found:
                file.write(f"{self.__username}:{self.__password}\n")
            else:
                print("Your password has been taken, please generate a new password. \n")
                self.resetVars()
                self.generatePassword()

#Replace the first parameter of password_gen with your database textfile or csv

if __name__ == "__main__":
    passwordGenerator = password_gen("Python\TextFiles\passwordDatabase.txt")
    passwordGenerator.promptUsername()
    passwordGenerator.generatePassword()
    
