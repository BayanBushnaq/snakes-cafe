from typing import Counter
#from operator import countOf


def start_view():
    print("*******************************************")
    print("** \t Welcome to Snakes Cafe! \t **")
    print("** \t Please see our menu below. \t **")
    print("**")
    print("** \t To quit at any time,type \"quit\" **")
    print("*******************************************")
    menu = {'Appetizers': ["Wings", "Cookies", "Spring Rolls"],
            'Entress': ["Salmon", "Steak", "Meat Tornado", "A Literal Garden"],
            'Desserts': ["Ice cream", "Cake", "Pie"],
            'Drinks': ["Coffee", "Tea", "Unicorn Tears"]}

    for key in menu:
        print(key)
        print("----------")
        # print(menu[key])
        for i in menu[key]:
            print(i)
        print("\n")

    print("*******************************************")
    print("**\tWhat would you like to order? \t**")
    print("*******************************************")
    print(">", end=' ')
    Counter = 0
    user_oreder = input()
   
    

    # if user_oreder not in menu.values() and user_oreder != "quit":
           # print("please enter dish from this menu!")
    list = ["Wings", "Cookies", "Spring Rolls","Salmon", "Steak", "Meat Tornado", "A Literal Garden","Ice cream", "Cake", "Pie","Coffee", "Tea", "Unicorn Tears"]
    
    """
    while True :
        user_oreder = input()

        #if user_oreder not in menu.values() and user_oreder != "quit":
            #print("please enter dish from this menu!")
            #user_oreder=input() 
        re="quit"
        list.append(user_oreder)
        if re in list:
         list.remove(re)
        for item in menu.values():
             if user_oreder in item:
                Counter +=1
                if Counter >= 1:
                    print(f"** 1 order of {user_oreder} have been added to your meal **")
                   
                #elif Counter > 1:
                    #print(f"** {Counter} orders of {user_oreder} have been added to your meal **")
                #elif user_oreder not in item and user_oreder != "quit":
                 #print("please enter dish from this menu!")



        if user_oreder == "quit":
         break

    print("Summary of your orders is: ")
    print(*list, sep = "\n")  
    """

    #while True:
        #print(menu.values())
    re = "quit"
    summary_list=[]
    for item in range(len(list)):
        if user_oreder == "quit":
            if len(summary_list) == 0 :
                print("Your ordered list is empty")
                break
            else:
             print("Summary of your orders is: ")
             print(*summary_list, sep = "\n")
            break 
        if user_oreder in list:
            summary_list.append(user_oreder)
            x = summary_list.count(user_oreder)
            if x == 1 :
             print(f"**{x} order of {user_oreder} has been added to your meal**")
            else:
                print(f"**{x} orders of {user_oreder} have been added to your meal**")

            
            for a in range(len(summary_list)):
                if re in summary_list:
                    summary_list.remove(re)
            user_oreder = input()
            continue
        else:
            print("your order not in our menu, plz try again!")
            user_oreder = input()
            
             






start_view()


