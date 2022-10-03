from typing import Counter


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
    """
     for key in menu:
        print(key)
        print("----------")
        count = 0
        for value in menu.values():
         print(menu[key])
         count +=1
         if count > 0:
            break
    """

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
    # user_oreder = input()

    # if user_oreder not in menu.values() and user_oreder != "quit":
           # print("please enter dish from this menu!")
    list = []
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
                if Counter == 1:
                    print(f"** {Counter} one order of {user_oreder} have been added to your meal **")
                   
                elif Counter > 1:
                    print(f"** {Counter} orders of {user_oreder} have been added to your meal **")
                #elif user_oreder not in item and user_oreder != "quit":
                 #print("please enter dish from this menu!")



        if user_oreder == "quit":
         break
        """
        for menu_item in menu.values():
         for list_item in range(len(list)):
          if  list_item != menu_item:
            list.remove(list_item)
        """
    print("Summary of your orders is: ")
    print(*list, sep = "\n")  

           






start_view()


