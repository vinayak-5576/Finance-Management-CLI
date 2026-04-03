import json
import pandas as pd
with open ("Categories.json","r") as file:
    data = json.load(file)
with open ("budget_planning.json","r") as file:
    budget_data = json.load(file)


def save_data():
    with open ("Categories.json","w") as file:
        json.dump(data,file,indent=4)

        
assign_category = ['Travel','College','Fun','Food','College event','Necessities', 'My stuff']
def add_money():
    try:
        Money = int(input('Enter the Amount: '))
    except:
        print("Please enter valid number")
        return
            
    if  Money <=0:
        print('Invalid')
        return
        
    else:
    
        print("Enter the Serial Number: \n 1.Travel  2.College  3.Fun  4.Food \n 5.College event  6.Necessities  7.My stuff") 
        try:
            Category = int(input("Category: "))
        except:
            print("Please enter valid catgeory number")
            return
            
        Category = Category-1
    
        if 0 <= Category < len(assign_category):
            data[assign_category[Category]].append(Money)
            save_data()
            Total_Category_expense = sum(data[assign_category[Category]])
            print(Total_Category_expense)
    
        else:
            print('Category not found')
        
def show_expense():
    print("Do you want expense on specific categories: \n 1.Travel  2.College  3.Fun  4.Food \n 5.College event  6.Necessities  7.My stuff  8.total")
    try:
        analysis = int(input('enter from (1-8): '))
      
    except:
        print('please enter valid category number')
        return

    analysis =analysis- 1
    net_Expense =0

    if 0 <= analysis <= 7:
    
        if analysis ==7:
            for cat in data:
                net_Expense += sum(data[cat]) 
            print(net_Expense)
        
        else:
            SUM = sum(data[assign_category[analysis]])
            print(SUM)        
    else:
        print('invalid')


def budget_planning():
    print("Enter the Serial Number: \n 1.Travel  2.College  3.Fun  4.Food \n 5.College event  6.Necessities  7.My stuff")
    try:
        Category = int(input('Category: '))
    except:
        print('Invalid category')
        return
    Category = Category-1
    
    if 0<= Category < len(assign_category):
        
        cat = assign_category[Category]
        
        if cat not in budget_data:
            print(f"The {Category} doesn't exist in {budget_data} collection")
            return
        
        max_budget = budget_data[cat]["max"]
        min_budget = budget_data[cat]["min"]
        actual = sum(data[cat])
        
        if max_budget == 0:
            print("Please check the max Budget you have set")
            return
        usage = (actual/ max_budget)*100
        
        if actual > max_budget :
            print(f'Your Budget for {cat} has exceeded by: {actual - max_budget}')
            print(f'You have used {usage:.2f}% of your total budget for {cat}')
        elif actual < max_budget:
            print(f'It\'s within budget and the differnce of the remaining amount is: {max_budget - actual}')
            print(f'You have used {usage:.2f}% of your total budget for {cat}')
            if usage >=80 and usage <100:
                print(f"Your budget for this {cat} is about to finish.. Spend wisely")
            if min_budget> actual:
                print("Your expense way less than minimal expense.. Good job!")      
        else:
            print(f'Your Budget for {cat} is finsihed...')
    else:
        print('Invalid choice')
        return
    
def show_table():
    row =[]
    for item in data:
        Actual = sum(data[item])
    
        if item in budget_data:
            min_budget = budget_data[item]["min"]
            max_budget = budget_data[item]["max"]
            if max_budget !=0:
                usage = (Actual/max_budget)*100
                usage2 = round(usage,2)
            else:
                usage2 = 0
        else:
            min_budget = 0
            max_budget = 0
            usage2 = 0
        
        row.append({
            "Category" : item,
            "Minimum" : min_budget,
            "Maximum": max_budget,
            "Actual" : Actual,
            "Usage (%)" : usage2,
            "Difference" : Actual - max_budget
            })
    df= pd.DataFrame(row)
    print(df)
    

        
while True:
    print('1.Add expense \n2.Check expense \n3.Budget planning \n4.Show table \n5.Exit')
    try:
        USER_WISH = int(input('Wt are Wishing to go for?'))
    except:
        print('INVALID CHOICE')
        continue
    
    if USER_WISH == 1:
        add_money()
    elif USER_WISH == 2:
        show_expense()
    elif USER_WISH == 3:
        budget_planning()
    elif USER_WISH == 4:
        show_table()
    elif USER_WISH == 5:
        break
    
print('Done')