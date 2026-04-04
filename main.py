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
assign_month = ['January', 'February', 'March','April','May','June','July','August','September','October','November','December']

def choose_month():  
    print("Please enter the month (1-12): \n1.January 2.February 3.March 4.April 5.May 6.June \n7.July 8.August 9.September 10.October 11.November 12.December")
    try:
        Month = int(input('Month: '))
    except:
        print('INVALID CHOICE')
        return choose_month()
    if 0<Month<=12:
        Month = Month -1
        return Month 
    else:
        print('Please enter a Number from Valid range')
        return choose_month()
    
        
    

def add_money(month_I):
    m=assign_month[month_I]
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
            data[m][assign_category[Category]].append(Money)
            save_data()
            Total_Category_expense = sum(data[m][assign_category[Category]])
            print(Total_Category_expense)
    
        else:
            print('Category not found')
        
def show_expense(month_I):
    print("Do you want expense on specific categories: \n 1.Travel  2.College  3.Fun  4.Food \n 5.College event  6.Necessities  7.My stuff  8.total")
    m=assign_month[month_I]
    try:
        analysis = int(input('enter from (1-8): '))
      
    except:
        print('please enter valid category number')
        return

    analysis =analysis- 1
    net_Expense =0

    if 0 <= analysis <= 7:
    
        if analysis ==7:
            for cat in data[m]:
                net_Expense += sum(data[m][cat]) 
            print(net_Expense)
        
        else:
            SUM = sum(data[m][assign_category[analysis]])
            print(SUM)        
    else:
        print('invalid')


def budget_planning(month_I):
    m=assign_month[month_I]
    print("Enter the Serial Number: \n 1.Travel  2.College  3.Fun  4.Food \n 5.College event  6.Necessities  7.My stuff")
    try:
        Category = int(input('Category: '))
    except:
        print('Invalid category')
        return
    Category = Category-1
    
    if 0<= Category < len(assign_category):
        
        cat = assign_category[Category]
        
        if cat not in budget_data[m]:
            print(f"The {Category} doesn't exist in {budget_data} collection")
            return
        
        max_budget = budget_data[m][cat]["max"]
        min_budget = budget_data[m][cat]["min"]
        actual = sum(data[m][cat])
        
        if max_budget == 0:
            print("Please check the max Budget you have set")
            return
        usage = (actual/ max_budget)*100
        
        if actual > max_budget :
            print(f'Your Budget for {cat} in this month {m} has exceeded by: {actual - max_budget}')
            print(f'You have used {usage:.2f}% of your total budget for {cat}')
        elif actual < max_budget:
            print(f'It\'s within budget for this {m} and the differnce of the remaining amount is: {max_budget - actual}')
            print(f'You have used {usage:.2f}% of your total budget for {cat}')
            if usage >=80 and usage <100:
                print(f"Your budget for this {cat} in this {m} onth is about to finish.. Spend wisely")
            if min_budget> actual:
                print("Your expense way less than minimal expense.. Good job!")      
        else:
            print(f'Your Budget for {cat} in this {m} month is finsihed...')
    else:
        print('Invalid choice')
        return
    
def show_table(month_I):
    m=assign_month[month_I]
    row =[]
    if m in data:
        for category in data[m]:
            Actual = sum(data[m][category])
            
            if category not in budget_data[m]:
                print(f'{category} not found in Budget Data')
                continue
    
            if category in budget_data[m]:
                min_budget = budget_data[m][category]["min"]
                max_budget = budget_data[m][category]["max"]
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
                "Category" : category,
                "Minimum" : min_budget,
                "Maximum": max_budget,
                "Actual" : Actual,
                "Usage (%)" : usage2,
                "Difference" : Actual - max_budget
                })
        df= pd.DataFrame(row)
        print(f'{m} Month expenses')
        print(df)


    
    
while True:
    print('1.Add expense \n2.Check expense \n3.Budget planning \n4.Show table \n5.Exit')
    try:
        USER_WISH = int(input('Wt are Wishing to go for?'))
    except:
        print('INVALID CHOICE')
        continue
    
    
    if USER_WISH == 1:
        month_I=choose_month()
        add_money(month_I)
    elif USER_WISH == 2:
        month_I=choose_month()
        show_expense(month_I)
    elif USER_WISH == 3:
        month_I=choose_month()
        budget_planning(month_I)
    elif USER_WISH == 4:
        month_I=choose_month()
        show_table(month_I)
    elif USER_WISH == 5:
        break
    
print('Done')