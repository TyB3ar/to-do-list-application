to_do_list = {}     # Empty dicitonary to add tasks to 


def add_task():       # function to add task to to do list
    while True: 
        task = input("What task would you like to add to the list? ") 
        try: 
            if task.isalpha() == True:      # if input is alphabetical, run this 
                to_do_list[task.upper()] = "Incomplete" 
                print(f"{task.upper()} was added to your To-Do List as Incomplete")
                break
            else:   # if input is non alphabetical, run this 
                print("Error! Task must be a word to add to list.")
        except Exception as e: 
            print("Unexcpected error occured.")    


def view_task():      # function to view entire list of tasks to do and status
    print("Your current do to list: ") 
    for task in to_do_list: 
        print(task, "-",  to_do_list[task])  

def mark_complete():  # function to mark a task complete 
    try:    
        while True: 
            mark = input("Which task would you like to mark as complete?: ")   # ask user to input task to mark complete
            if mark.upper() in to_do_list:    # if task given is in To Do List
                to_do_list[mark.upper()] = "Complete"     # change value to "Complete" 
                print(f"{mark.upper()} marked as Complete.")
                break
            else:    # if task given or input is not in list at all 
                print("Task not found in To Do List.") 
    except Exception as e:
            print("Unexcpected error occured.")     
            
def delete_task():    # function to delete a task from list
    try:     
        while True:
            remove = input("Which task would you like to remove?: ")  # ask user to input task to remove
            if remove.upper() in to_do_list:   # if input given is in To Do List
                del to_do_list[remove.upper()]    # remove task from list
                print(f"{remove.upper()} has been removed from the To Do List.") 
                break
            else:    # if input given is not in our To Do List
                print("Task not found in To Do List.") 
    except Exception as e: 
        print("Unexcpected error occured.")
    
def quit_app():       # function to end application
    print("Thank you for using our To Do List Application! Have a nice day!") 
    
def to_do_app():      # function for the app itself, choosing options
    print("Welcome to the To-Do List Application!") 
    while True: 
        print('''Menu: 
    1. Add a task
    2. View tasks
    3. Mark a task as complete
    4. Delete a task
    5. Quit
    ''')
        menu_selection = input("What would you like to do? Enter 1/2/3/4/5: ")  
     
        try: 
            if menu_selection == '1': 
                add_task() 
            elif menu_selection == '2': 
                view_task() 
            elif menu_selection == '3': 
                mark_complete()
            elif menu_selection == '4': 
                delete_task() 
            elif menu_selection == '5': 
                quit_app() 
                break
            else: 
                print("Please select an option from the choices given.") 
        except Exception as e:
            print("Unexpected error occured.") 


to_do_app()   # call the app option to run app 
