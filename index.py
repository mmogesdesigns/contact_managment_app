# # Welcome to the Contact Management System!

# Menu:
# 1. Add a new contact
# 2. Edit an existing contact
# 3. Delete a contact
# 4. Search for a contact
# 5. Display all contacts
# 6. Export contacts to a text file
# 7. Quit

# Name
# Phone number
# Email address
# Additional information (e.g., address, notes).

contacts={}

while True:
    choice = int(input("Welcome to the Contact Management System!\nMenu:\n1. Add a new contact\n2. Edit an existing contact\n3. Delete a contact\n4. Search for a contact\n5. Display all contacts\n6. Export contacts to a text file\n7. Quit\n "))
    
    if choice==1:
        name= input("Enter the contact name: ")
        number=input("Enter the phone number: ")
        email=input('Enter the email address: ')
        additional_info=input("Enter any additional information: ")
        contacts[number]={
            "name": name,
            "email":email,
            "additional info":additional_info}
        print("contact added successfully! :)")

        continue_or_quit=input("Would you like to add another contact? (yes/no):")
        if continue_or_quit != "yes":
            print("Returning to main menu. ")
            continue
       
    elif choice==2:
        contact_to_edit=int(input("Enter the phone number of the contact you would like to edit. "))
        if contact_to_edit not in contacts:
            print("Invalid response. Please enter a phone number that exsists in the phonebook. ")
        else:
            contact_details=contacts[contact_to_edit]
           # display current contacts dets
            print("Current Contact Information:")
            print(f"Name: {contact_details['name']} ")
            print(f"Phone Number: {contact_details} ")
            print(f"Email: {contact_details['email']} ")
            print(f"Additional Information: {contact_to_edit['additional_info']} ")

            # input()updates_name,email,additional info
            updated_name =input("Enter the updated name: ")
            updated_email =input("Enter the updated email: ")
            updated_additional_info =input("Enter the updated additional information: ")

            # update the new info in dicitionar (contacts)
            contacts[contact_to_edit]['name']=updated_name
            contacts[contact_to_edit]['email']=updated_email
            contacts[contact_to_edit]['additional_info']=updated_additional_info

            print("Contact details updated successfully! ")


    elif choice==3:
        delete_contact=input("Enter the phone number of the contact you would like to delete: ")
        if delete_contact not in contacts:
            print("Invalid response. Please enter a phone number that exists in the phonebook. ")
        else:
            confirm = input(f"Are you sure you want to delete this contact? (yes/no)")
            if confirm =="yes":
                contacts.pop(delete_contact)
                print("Contact details updated successfully! ")
                continue



    elif choice==4:
        search_for_contact = input("Enter the phone number of the contact you want to search for: ")
        if search_for_contact not in contacts:
            print("Invalid response. Please enter a phone number that exists in the phonebook. ")   
        else: 
            contact_details = contacts[search_for_contact]
            print("Contact Information: ")
            print(f"Name: {contact_details['name']}")
            print(f"Phone Number: {contact_details['phone']}")
            print(f"Email: {contact_details[email]}")
            print(f"Additional Information: {contact_to_edit['additional_info']}")
            
    elif choice==5:
        if contacts:
            print("All Contacts: ")  
            for contact_number in contacts:
                contact_details= contacts[contact_number]
                print(f"Name: {contact_details['name']}, Phone Number: {contact_details['phone']}, Email: {contact_details['email']}, Additional Information: {contact_details['additional_info']}")  
        else: 
            print("There are currently no contacts.\n ")
    
    elif choice==6:
        try:
            filename = input("Enter the filename to export contacts to (e.g contacts.txt): ") 
            with open(filename,'w') as file:
                if contacts: 
                    for contact_number in contacts:
                        contact_details = contacts[contact_number]
                        file.write(f"Name: {contact_details['name']}, Phone Number: {contact_number}, Email: {contact_details['email']}, Additional Information: {contact_details['additional info']}\n")
                    print(f"All contacts have been exported to {filename}")
                else:
                    print("There are currently no contacts to export. ")
        except IOError as e:
            print(f"An error occurred while writing to the file: {e}")

    elif choice==7:
        break
    else:
        print("Invalid choice. Please select a number between 1 and 7.")

