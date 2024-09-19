
import re
import os 

# nested dictionary for storage of contacts and information
contacts = {}
# 'contacts' is initially empty, where user can enter in contact info to be added  
     
# function to add contacts and info:
def add_contact(contact_dict): 
   try:
       while True: # loop to enter and validate name entry
           name_input = input("Please enter the name of the new contact: ")
           
           if name_input.isalpha() == False:  # if input for name is not alphatbetical (digit or special character) 
               print("Error, not a valid name.")
           else: 
               contact_dict[name_input] = {} 
               print(f"{name_input} was added to the contact list.")
               break   
               
       while True:   # loop to validate phone number entry
            phone_input = input("Please enter the phone number for this contact, as xxx-xxx-xxxx: ") 
            
            if re.search(r"\d{3}-\d{3}-\d{4}", phone_input): # regex for phone number validation  
                contact_dict[name_input] = {'Phone' : phone_input} # creates sub dictinoary with key-value 'Phone' equal to entered phone number
                print(f"{phone_input} added under {name_input} to contact list.")
                break
            else:
                print("Error, invalid phone number.") 
            
       while True:   # loop to validate email entry 
            email_input = input(f"Enter the email you wish to add under this contact: ") 
            
            if re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9]+\.[A-Za-z0-9]{2,}", email_input):  # regex email validation
                contact_dict[name_input] = {'Phone' : phone_input, 'Email' : email_input}   # sets initial key 'name_input' to sub dictionary with key-value pair 'phone_input':'email_input' 
                print(f"{email_input} was added under {name_input} to contact list.")
                break
            else:
                print("Error, invalid email address.")
   except Exception as e:
       print(f"Error occured: {e}") 


# function to edit contact info:
def ammend_contact(contact_dict):
    try:
       while True: # loop to ask user to input contact to edit
           edit_name = input("Please enter the name of the contact you wish to edit: ")  # ask user to enter name of contact to edit
           if edit_name not in contact_dict:  # if name inputed is not in contact list
               print(f"Sorry, but {edit_name} was not found in your contact list.")
           else:  # else if name is found in contact list
               change_this = input("Would you like to change the name(1), phone number(2), or email(3) for this contact: ")
               # asking user whether they wish to change the name of contact, phone number, or email
               if change_this.isdigit() == False:   # if input is anything but a number
                   print("Sorry, please enter 1, 2, or 3 for the information to edit.")
               elif change_this == '1':
                    new_name = input("Please enter the new name for this contact: ")  # input for new contact name
                    
                    if new_name.isalpha() == False: # if new name given is anything but alphabetical
                        print("Invalid Name") 
                    else: 
                        contact_dict[new_name] = contact_dict[edit_name]
                        del contact_dict[edit_name] 
                        print(f"Contact name changed from {edit_name} to {new_name}") 
                        break 
               elif change_this == '2':
                   new_number = input("Please enter the new number for this contact, as xxx-xxx-xxxx: ") # input for new phone number to replace old
                   
                   if re.search(r"\d{3}-\d{3}-\d{4}", new_number): # validation if new number entered is a phone number
                       contact_dict[edit_name]['Phone'] = new_number # change value for 'Phone' to new number entered
                       print(f"{new_number} has been saved under {edit_name}") # tell user number has been changed
                       break # break the loop 
                   else:
                       print("Error, invalid phone number.")
                   break 
               elif change_this == '3':
                   new_email = input("Please enter the new email for this contact: ")
                   
                   if re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9]+\.[A-Za-z0-9]{2,}", new_email): # if input validates as an email 
                       contact_dict[edit_name]['Email'] = new_email # save the new email under the 'email' key
                       print(f"{new_email} has been saved under {edit_name}") # tell user email has been changed 
                       break # break the loop  
                   else: 
                       print("Error, invalid email.")
               else:   # if neither 1, 2, or 3 are entered
                   print("Sorry, please enter 1, 2, or 3 for the information to edit.")
    except Exception as e:
       print(f"Error occured: {e}") 


#function to delete contact from dictionary:
def remove_contact(contact_dict):
    try:
       while True:  # while loop for user input
           remove_this = input("Please enter the name of the contact you wish to delete: ")
           
           if remove_this.isalpha() == False:  # if user enters non alphabetical 
               print("Sorry, invalid name.")
           elif remove_this not in contact_dict: # if name entered is not found in dictnioary
               print(f"Sorry, {remove_this} not found in contact list.")
           else: 
               del contact_dict[remove_this]
               print(f"{remove_this} was removed from contact list.")
               break 
    except Exception as e:
       print(f"Error occured: {e}")  


# function to search for specific contact and info:
def search_contact(contact_dict):
    try:
        while True: 
            find_contact = input("Please enter the name of the contact you wish to find: ")
            
            if find_contact.isalpha() == True and find_contact in contact_dict: # if input is alphabetical and if input name is a key in main dictionary
                if isinstance(contact_dict[find_contact], dict): # if value of 'find_contact' is a dictinoary
                    print(f"{find_contact} found in contacts under: ")
                    print(f" - {find_contact}")
                    print(f"      Phone: {contact_dict[find_contact]['Phone']}, Email: {contact_dict[find_contact]['Email']}")    
                break 
            else: 
                print(f"Sorry, but {find_contact} was not found in contact list.")       
    except Exception as e:
       print(f"Error occured: {e}") 

        
# function to display list of all contacts:
def display_contacts(contact_dict):
    try:
       if contact_dict == {}:   # if contact list is empty 
           print("No Contacts found in Contact List.")  
       else:
           #print(contacts)     
           
           for name, items in contact_dict.items():
               print(f" - {name}:")
               print(f"      Phone: {contact_dict[name]['Phone']}, Email: {contact_dict[name]['Email']}")                                        
    except Exception as e:
       print(f"Error occured: {e}") 


# function to export contacts to txt file:
def export_contacts(contact_dict, file):
    try:
       with open(file, 'w+') as f:
            for name, items in contact_dict.items():
               f.write(f" - {name}:\n")
               f.write(f"      Phone: {contact_dict[name]['Phone']}, Email: {contact_dict[name]['Email']}\n")
    except Exception as e:
       print(f"Error occured: {e}") 


# function to import contacts from txt file:
def import_contacts(file):
    try:
        if os.path.exists(f):
            with open(file, 'r+') as f:
                contacts_file = f.read()
                print(contacts_file)   
        else: 
            print(f"Error, {f} not found.")            
    except Exception as e:
       print(f"Error occured: {e}") 
  

def main_menu():
    try:
        # Start menu with options for user to choose from
        print("Welcome to the Contact Management System!\n")

        while True:
            print("Menu:")
            print("1. Add a new contact")
            print("2. Edit an existing contact")
            print("3. Delete a contact")
            print("4. Search for a contact")
            print("5. Display all contacts")
            print("6. Export contacts to a text file")
            print("7. Import contacts from a text file")
            print("8. Quit\n")
            # user input value 
            user_option = input("Please enter the number of the option you would like to perform: ")
            
            if user_option.isdigit() == False:   # if user enters a non number character rather than a number from menu options
                print("Error, please enter a number for the option you wish to select.")
            elif user_option == '1':    # add new contact option 
                print("\nAdding a new contact.")
                add_contact(contacts)
            elif user_option == '2':    # edit contact option
                print("\nEditing Existing Contact:")
                ammend_contact(contacts)  
            elif user_option == '3':    # delete contact option
                print("\nRemoving Contact:") 
                remove_contact(contacts) 
            elif user_option == '4':    # search for specific contact option
                print("\nSearching for contact: ")
                search_contact(contacts) 
            elif user_option == '5':    # display all current contacts option
                print("\nCurrent Contact List:")
                display_contacts(contacts) 
            elif user_option == '6':    # export contacts to .txt file option
                export_contacts(contacts, 'contact_list.txt')
                print("Contacts exported to 'contact_list.txt' file.")  
            elif user_option == '7':    # import contacts from .txt file option
                print("Printing file imported:")
                import_contacts('contact_list.txt') 
            elif user_option == '8':    # quit service option
                print("\nThank you, have a great day!")
                break
            else:                       # else if option inputed by user is not on menu (number that is not 1-8) 
                print("Error, option selected not found in menu. ")
                
    except Exception as e:
        print(f"Error occured: {e}") 

main_menu()