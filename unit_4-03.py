#created by Matthew Walsh
#created on nov 2017
#created for ics3u
#adress program

def print_address(apt_number, st_address, city, province, postal_code):
    if apt_number == "": 
       print(st_address + ", " + city + ", " + province + ", " + postal_code)   
    elif apt_number == "redo":
       print("Please type 'yes' or 'no'")
       setup()
    else:
       print(apt_number + ", " + st_address + ", " + city + ", " + province + ", " + postal_code) 
def address():      
    apt_number = raw_input("Would you like to enter an apartment number (yes or no): ")
    if apt_number == "yes":
       apt_number = raw_input("Please enter your apartment number: ")
       st_address = raw_input("Please enter your street address: ")
       city = raw_input("Please enter the city you live in: ")
       province = raw_input("Please enter the province you live in: ")
       postal_code = raw_input("Please enter you postal code: ")
       print_address(apt_number, st_address, city, province, postal_code)
    elif apt_number == "no":
       apt_number = ""
       st_address = raw_input("Please enter your street address: ")
       city = raw_input("Please enter the city you live in: ")
       province = raw_input("Please enter the province you live in: ")
       postal_code = raw_input("Please enter you postal code: ")
       print_address(apt_number, st_address, city, province, postal_code)  
    else: 
       apt_number = "redo"
       st_address = ""
       city = ""
       province = ""
       postal_code = ""
       print_address(apt_number, st_address, city, province, postal_code)
       
address()
