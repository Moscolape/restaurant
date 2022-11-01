import re
import json


class MainApp():
    def __init__(self):
        print("Please Enter 1 for Sign Up")
        print("Please Enter 2 for Sign In")
        print("Please enter 3 for Quit")
        self.input = input(":") 


class SignUP():
    def __init__(self):
        self.user_data = {}
        self.name = input("Please enter your full name:")
        self.user_data["name"] = self.name
        self.number = input("Please enter your contact number:")
        self.user_data["number"] = self.number
        if len(self.number) == 10 and self.number.startswith("0"):
            pass
        else:
            print("You have entered an incorrect number!!\n")
            self.number = input("Please enter your contact number:")
            self.user_data["number"] = self.number

        self.password = input("Please enter your password:")
        self.confirm_pass = input("Password confirmation:")
        self.patterns = "[A-Za-z][@|&][0-9]*$"
        if re.match(self.patterns, self.password):
            pass
        else:
            print("Your password doesn't follow the required pattern please enter a valid password!! Please Restart")
            sign_up = SignUP()
        
        if self.password == self.confirm_pass:
            self.user_data["password"] = self.confirm_pass
        elif self.password != self.confirm_pass:
            print("Your passwords are not matching please start again")
            self.password = input("Please enter your password:")
            self.confirm_pass = input("Password confirmation:")
            self.user_data["password"] = self.password

        self.date_of_birth = input("Please enter your date of birth in the format dd/mm/yyyy:")
        match = "(0[1-9]|[12][0-9]|3[01])[/](0[1-9]|1[012])[/]\d{4}"
        if re.match(match, self.date_of_birth):
            self.split_D0B = self.date_of_birth.split("/")
            self.birth_year = self.split_D0B[2]
            age = 2021 - int(self.birth_year)
            if age >= 21:
                with open(f"{self.number}.json", "w") as file:
                    json.dump(self.user_data, file)
                print("You have successfully Signed up!!")
            else:
                print("You are too young to Sign up!")

        else:
            print("You have the entered the Date of Birth in invalid format.\nPlease start again\n:")
            self.date_of_birth = input("Please enter your date of birth in the format DD/MM/YYYY (No Space):")
  

class SignIn():
    def __init__(self):
        self.count = 0
        self.username = input("Please enter your username (Mobile Number):")
        try:
            with open(f"{self.username}.json", "r") as file:
                self.loaded_data = json.load(file)
                self.password = input("Please enter your password:")
                if self.loaded_data["password"] == self.password:
                    print("You have successfully signed in.")
                else:
                        print(f"You have entered the wrong Password\nPlease try again!{self.count}")
                        login = SignIn()
                print(f"Welcome {self.loaded_data['name']}")
            print("Please enter 1 for Resetting the Password")
            print("Please enter 2 for Signout")
            self.input = input(":")
            if self.input == "1":
                self.username = input("Please enter your username (Mobile Number):")
                self.Oldpassword = input("Please enter your old password:")
                self.Newpassword = input("Please enter your new password:")
                self.loaded_data["password"] = self.Newpassword
                print("Your password has been reset successfully!!")
                with open(f"{self.username}.json", "w") as file:
                    json.dump(self.loaded_data, file)
            elif self.input == "2":
                pass
        except:
            print("You have not Signed up with this Contact Number, Please Sign up first.")        


while True:
    app = MainApp()
    if app.input == "3":
        print("Thank You for using the application.")
        break
    if app.input == "1":
        sign_up = SignUP()
    if app.input == "2":
        login = SignIn()
    
