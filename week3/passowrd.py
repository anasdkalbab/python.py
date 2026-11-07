import re
import csv
import string
import random
import sys
import secrets

accounts = []


try:
    with open("password.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            accounts.append({"app": row["app"], "username":row["username"], "password":row["password"]})

except FileNotFoundError:
    with open("password.csv","w")as file:
        writer = csv.DictWriter(file,fieldnames=["app" ,"username" ,"password"])
        writer.writeheader()

def main():
    
    
    while True:
        print("\n===== PASSWORD MANAGER =====")
        print("1. Add account")
        print("2. View all accounts")
        print("3. Find an account")
        print("4. Delete an account")
        print("5. Edit an account")
        print("6. Generate a password")
        print("7. Exit")
        print("============================")
        choice = input("Choose an option: ")
        if choice == "1":
            add_account()
        elif choice == "2":
            view_accounts()
        elif choice == "3":
            find_account()
        elif choice == "4":
            username = input("Which username do you want to delete? ")
            delete(username)
        elif choice == "5":
            edit()
        elif choice == "6":
            try:
                length = int(input("How long do you want your password to be? "))
                print(f"This is a strong password from {length} charecters: {generate(length)}")
            except ValueError:
                print("Please enter a number. ")
        elif choice == "7":
            sys.exit()
        else:
            print("Please choose a number. ")
def add_account():
    
    while True:
        app = input("What is the app? ")
        username = input("What is your username? ")
        skip_to_while_start = False
        for account in accounts:
            if account["username"] == username and account["app"] == app:
                print("We already have the username you gave us. ")
                skip_to_while_start = True
                break 
        
        if skip_to_while_start:
            continue
        else:
            password = input("What is your password? ")
            accounts.append({"app":app,"username":username , "password":password})
            with open("password.csv","a") as file:
                writer = csv.DictWriter(file , fieldnames =["app","username","password"])
                writer.writerow({"username":username , "app":app, "password":password})
            break

def view_accounts():
    for account in accounts:
        print(f"{account['username']}  {account['app']}")

def find_account():
    name = input("What is your username or app? ")
    for account in accounts:
        if account["username"] == name or account["app"] == name:
            print(account)
            break
    else:
        print("We have no account or app with this name. ")

        
def delete(username):    
    deleted = False  
    found = False
    for account in accounts:
        if account["username"] == username:
            found = True    
            confirm = input(f"Are you sure you want to delete {username} ")
            if confirm == "yes":
                accounts.remove(account)
                deleted = True
            else:
                print("Deletion cancelled")
            break
                    
    if deleted:
        with open ("password.csv","w",newline="")as file:
            writer = csv.DictWriter(file,fieldnames=["app","username","password"])
            writer.writeheader()
            writer.writerows(accounts)
        print("account deleted succesfully")
    elif not found:
        print("their is no account with this username. ")

def edit():
    username = input("What is your username? ")
    for account in accounts:
        if account["username"] == username:
            choice = input("What do you want to change? ")
            if choice == "username":
                new_username = input("What is your new username? ")
                account["username"] = new_username
                with open("password.csv", "w", newline="") as file:
                    writer = csv.DictWriter(file,fieldnames=["app", "username", "password"])
                    writer.writeheader()
                    writer.writerows(accounts)
                print("Account updated succefully")
            elif choice == "password":
                new_password = input("What is your new password? ")
                account["password"] = new_password
                with open("password.csv", "w", newline="") as file:
                    writer = csv.DictWriter(file,fieldnames=["app", "username", "password"])
                    writer.writeheader()
                    writer.writerows(accounts)
                print("Account updated succefully")
            elif choice == "app":
                new_app = input("What is your new app? ")
                account["app"] = new_app 
                with open("password.csv", "w", newline="") as file:
                    writer = csv.DictWriter(file,fieldnames=["app", "username", "password"])
                    writer.writeheader()
                    writer.writerows(accounts)
                print("Account updated succefully")          
            else:
                print("invalid choice. ")
           
            break
    else:
        print("account not found.")

def generate(l):
    if l < 8:
        return "Password should at least be 8 letters. "
    pool = string.ascii_letters + string.digits + string.punctuation    
    word = ''.join(secrets.choice(pool) for _ in range(l))
    return word
            
                    
if __name__ == "__main__":
    main()