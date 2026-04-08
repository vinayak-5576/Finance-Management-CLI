import json
import pandas as pd
import matplotlib.pyplot as plt
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
            print(f"The {cat} doesn't exist in {budget_data} collection")
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
                print(f"Your budget for this {cat} in this {m} month is about to finish.. Spend wisely")
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
                min_budget = 0
                max_budget = 0
    
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
        
def graph():
    print("Please enter the month (1-12): \n1.January 2.February 3.March 4.April 5.May 6.June \n7.July 8.August 9.September 10.October 11.November 12.December")
    months_choice_list = []
    while True:
        try:
            Months_choice_input = int(input('Enter the serial no(1-12)[enter 0 for end]: '))
            if Months_choice_input ==0 and len(months_choice_list) == 0:
                print("Select at least one month")
                continue 
            elif Months_choice_input ==0 and len(months_choice_list) > 0:
                break
            
            elif Months_choice_input >12 or Months_choice_input < 0:
                print("Please enter a number from the valid range...")
                continue
            Months_choice_input = Months_choice_input - 1
            if assign_month[Months_choice_input] in months_choice_list:
                print("Duplicate value")
                continue
            months_choice_list.append(assign_month[Months_choice_input])
            
            
        except:
            print("Enter a valid number... ")
            continue
    print(months_choice_list, 'these are Your selected months')
    try:
        print("Category options: \n 1.Travel  2.College  3.Fun  4.Food \n 5.College event  6.Necessities  7.My stuff") 
        cat_choice_input = int(input("Enter the Serial Number: ")) 
        if cat_choice_input<1 or cat_choice_input > 7:
            print('Invalid choice')
            return
        cat_choice_input = cat_choice_input -1
        
    except:
        print("Enter a valid number... ")
        return
    months_choice_list.sort(key = lambda x : assign_month.index(x))
    Y = [] 
    for items in months_choice_list:
        if assign_category[cat_choice_input] in data[items]:
            total = sum(data[items][assign_category[cat_choice_input]])
            Y.append(total)
        else:
            print('Data isnt Available so i have taken 0')
            Y.append(0)
    print("Graph Choice:\n1.Line graph \n2.Bar graph")
    try:
        Graph_choice = int(input("Enter you graph choice:\n"))     
    except:
        print("Enter a valid Number")
        return
    try:
        if Graph_choice == 1:
            plt.figure(figsize=(8,5))
            plt.plot(months_choice_list,Y, marker = 'o',linestyle = '-')
            plt.title(f'Expenses on {assign_category[cat_choice_input]} in these months')
            plt.xlabel("Months")
            plt.ylabel("Expenses")
            plt.grid(True)
            plt.show()
        elif Graph_choice == 2 :
            plt.figure(figsize=(8,5))
            plt.bar(months_choice_list,Y)
            plt.title(f'Expenses on {assign_category[cat_choice_input]} in these months')
            plt.xlabel("Months")
            plt.ylabel("Expenses")
            plt.xticks(rotation=30)
            plt.tight_layout()
            plt.show()
        
        else:
            print("Invalid choice")
    except:
        print("Invalid Input")
        return 
                  
while True:
    print('1.Add expense \n2.Check expense \n3.Budget planning \n4.Show table \n5.Show graph \n6.Exit')
    try:
        USER_WISH = int(input('Wt are Wishing to go for?\n'))
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
        graph()
    elif USER_WISH == 6:
        break
    
print('Done')