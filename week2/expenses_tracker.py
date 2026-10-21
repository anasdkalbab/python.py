import csv

import sys


expenses=[]


try:
    with open("expense.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            expenses.append({"describtion": row["describtion"], "cost":row["cost"], "category":row["category"]})

except FileNotFoundError:
    with open("expense.csv","w")as file:
        writer = csv.DictWriter(file,fieldnames=["describtion" ,"cost" ,"category"])
        writer.writeheader()
  

def new_item():
    while True:
            try:
                describtion = input("What did you pay for? ")
                cost = float((input("How did that expense cost? ")))
                while cost < 0:
                    cost = float(input("cost must be a positiv number? "))
                category = input(f"what is {describtion}s category ? ")
                expenses.append({"describtion":describtion,"cost":cost , "category":category})
                
                with open ("expense.csv","a") as file:
                    writer = csv.DictWriter(file,fieldnames=["describtion","cost","category"])
                    writer.writerow({"describtion":describtion,"cost":cost, "category":category})
                    break

            except ValueError:
                print("The cost and amount both need to be Numbers. ")


def view_all_expenses():   
    for item in expenses:
        for category, amount in item.items():
            print(f"{category} : {amount} /",end="")
        print()

def get_spending():
    price = 0
    for item in expenses:
        price += float(item["cost"]) 

    return price

def view_category():
    category = input("What category do you want to see? ")
    for expense in expenses:
        if expense["category"] == category:
            print(expense)





def main():
    while True:
        do = input("What do you want to do (add a new expense, view all expenses, get total spendings, or view a category.)")
        if do == "add a new expense":
            new_item()
        elif do == "view all expenses":
            view_all_expenses()
        elif do == "get total spendings":
            print(get_spending())
        elif do == "view category":
            view_category()
        elif do == "quit":
            sys.exit()        
        else:
            print("Please choose one of what i said? ")

    
if __name__ =="__main__":
    main()
    
