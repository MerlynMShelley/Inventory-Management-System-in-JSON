#!/usr/bin/env python
# coding: utf-8

# In[ ]:


record = {1001 : {'Name': "5-Star",  'Price': 10, 'Qn': 200}, 
          1002 : {'Name': "Cadbury", 'Price': 20, 'Qn':300}, 
          1003 : {'Name': "Perk",    'Price': 30, 'Qn':250}, 
          1004 : {'Name': "Treat",   'Price': 15, 'Qn':350},
          1005 : {'Name': "Munch",   'Price': 25, 'Qn':150},}


# In[ ]:


record


# In[33]:


import json
record = {1001 : {'Name': "5-Star",  'Price': 10, 'Qn': 200}, 
          1002 : {'Name': "Cadbury", 'Price': 20, 'Qn':300}, 
          1003 : {'Name': "Perk",    'Price': 30, 'Qn':250}, 
          1004 : {'Name': "Treat",   'Price': 15, 'Qn':350},
          1005 : {'Name': "Munch",   'Price': 25, 'Qn':150},}


print('------------Menu------------\n')
for key in record.keys():
    print(key, ":", record[key]['Name'], "|",record[key]['Price'], "|",record[key]['Qn'])
print('\n----------------------------\n')

ui_pr = int(input("Enter the product ID: "))
ui_qn = int(input("Enter the quantity  : "))

record[ui_pr]['Qn'] = record[ui_pr]['Qn'] - ui_qn

print('\n--------------Bill--------------\n')

print('Name of the product purchased:', record[ui_pr]['Name'])
print('Price of one quantity:', record[ui_pr]['Price'])
print('The quantity purchased:',ui_qn)

print('\n----------------------------\n')
print('The amount to be paid:', record[ui_pr]['Price'] * ui_qn)

print('\n----------------------------\n')


# ### Converting Dict to Str - dumps()

# In[ ]:


js = json.dumps(record)


# In[ ]:


fd = open("Record.json", 'w')
fd.write(js)
fd.close()


# In[ ]:


js


# In[ ]:


get_ipython().system('ls')


# In[51]:


import json

fd = open("Records.json", 'r')
js = fd.read()
fd.close


print('------------Menu------------\n')
for key in record.keys():
    print(key, ":", record[key]['Name'], "|",record[key]['Price'], "|",record[key]['Qn'])
print('\n----------------------------\n')

ui_pr = input("Enter the product ID: ")
ui_qn = int(input("Enter the quantity  : "))

record[ui_pr]['Qn'] = record[ui_pr]['Qn'] - ui_qn

print('\n--------------Bill--------------\n')

print('Name of the product purchased:', record[ui_pr]['Name'])
print('Price of one quantity:', record[ui_pr]['Price'])
print('The quantity purchased:',ui_qn)

print('\n----------------------------\n')
print('The amount to be paid:', record[ui_pr]['Price'] * ui_qn)

print('\n----------------------------\n')

js = json.dumps(record)
fd = open("Records.json", 'w')
fd.write(js)
fd.close()


# In[37]:


js


# ### Converting Str to Dict - load() 

# In[42]:


fd = open('Record.json', 'r')
js = fd. read()
fd.close()

record = json.loads(js)
# In[43]:


record


# In[49]:


import json

fd = open("Records.json", 'r')
js = fd.read()
fd.close()

record = json.loads(js)

print('------------Menu------------\n')
for key in record.keys():
    print(key, ":", record[key]['Name'], "|",record[key]['Price'], "|",record[key]['Qn'])
print('\n----------------------------\n')

ui_pr = input("Enter the product ID: ")
ui_qn = int(input("Enter the quantity  : "))

record[ui_pr]['Qn'] = int(record[ui_pr]['Qn'] - ui_qn)

print('\n--------------Bill--------------\n')

print('Name of the product purchased:', record[ui_pr]['Name'])
print('Price of one quantity:', record[ui_pr]['Price'])
print('The quantity purchased:',ui_qn)

print('\n----------------------------\n')
print('The amount to be paid:', record[ui_pr]['Price'] * ui_qn)

print('\n----------------------------\n')

js = json.dumps(record)
fd = open("Records.json", 'w')
fd.write(js)
fd.close()


# In[50]:


record


# ### Adding more functionalities

# In[62]:


import json

fd = open("Records.json", 'r')
js = fd.read()
fd.close()

record = json.loads(js)

print('------------Menu------------\n')
for key in record.keys():
    print(key, ":", record[key]['Name'], "|",record[key]['Price'], "|",record[key]['Qn'])
print('\n----------------------------\n')

ui_pr = str(input("Enter the product ID: "))
ui_qn = int(input("Enter the quantity  : "))

if(record[ui_pr]['Qn'] >= ui_qn):

    record[ui_pr]['Qn'] = int(record[ui_pr]['Qn'] - ui_qn)
    print('\n--------------Bill--------------\n')
    print('Name of the product purchased:', record[ui_pr]['Name'])
    print('Price of one quantity:', record[ui_pr]['Price'])
    print('The quantity purchased:',ui_qn)
    print('\n----------------------------\n')
    print('The amount to be paid:', record[ui_pr]['Price'] * ui_qn)
    print('\n----------------------------\n')

else:
    
    print("Sorry, we are not having enough quantity!")
    print("We only have", record[ui_pr]['Qn'], " qunatity in the inventory.")
    print('\n----------------------------\n')
    
    ch = str(input('Press Y/y to purchase:'))
    
    if(ch == 'Y' or ch == 'y'):
    
        print('\n--------------Bill--------------\n')
        print('Name of the product purchased:', record[ui_pr]['Name'])
        print('Price of one quantity:', record[ui_pr]['Price'])
        print('The quantity purchased:',record[ui_pr]['Qn'])
        print('\n----------------------------\n')
        print('The amount to be paid:', record[ui_pr]['Price'] * record[ui_pr]['Qn'])
        print('\n----------------------------\n')
        
        record[ui_pr]['Qn'] = 0
    else:

        print('Thanks!')

js = json.dumps(record)
fd = open("Records.json", 'w')
fd.write(js)
fd.close()


# In[63]:


record


# ### Generating Sales Structure

# In[74]:


import json
import time

fd = open("Records.json", 'r')
js = fd.read()
fd.close()

record = json.loads(js)

print('------------Menu------------\n')
for key in record.keys():
    print(key, ":", record[key]['Name'], "|",record[key]['Price'], "|",record[key]['Qn'])
print('\n----------------------------\n')

ui_name = str(input("Enter your Name:"))
ui_mail = str(input("Enter your Mail Id:"))
ui_phno = str(input("Enter your phone number:"))
ui_pr = str(input("Enter the product ID: "))
ui_qn = int(input("Enter the quantity  : "))

if(record[ui_pr]['Qn'] >= ui_qn):

    record[ui_pr]['Qn'] = int(record[ui_pr]['Qn'] - ui_qn)
    print('\n--------------Bill--------------\n')
    print('Name of the product purchased:', record[ui_pr]['Name'])
    print('Price of one quantity:', record[ui_pr]['Price'])
    print('The quantity purchased:',ui_qn)
    print('\n----------------------------\n')
    print('The amount to be paid:', record[ui_pr]['Price'] * ui_qn)
    print('\n----------------------------\n')
    
    sales = "1" + "," + ui_name + "," + ui_mail + "," + ui_phno + "," + ui_pr + "," + record[ui_pr]["Name"] + "," + str(record[ui_pr]["Price"]) + "," + str(ui_qn * record[ui_pr]["Price"]) + "," + time.ctime()

else:
    
    print("Sorry, we are not having enough quantity!")
    print("We only have", record[ui_pr]['Qn'], " qunatity in the inventory.")
    print('\n----------------------------\n')
    
    ch = str(input('Press Y/y to purchase:'))
    
    if(ch == 'Y' or ch == 'y'):
    
        print('\n--------------Bill--------------\n')
        print('Name of the product purchased:', record[ui_pr]['Name'])
        print('Price of one quantity:', record[ui_pr]['Price'])
        print('The quantity purchased:',record[ui_pr]['Qn'])
        print('\n----------------------------\n')
        print('The amount to be paid:', record[ui_pr]['Price'] * record[ui_pr]['Qn'])
        print('\n----------------------------\n')
        
        sales = "1" + "," + ui_name + "," + ui_mail + "," + ui_phno + "," + ui_pr + "," + record[ui_pr]["Name"] + "," + str(record[ui_pr]["Price"]) + "," + str(record[ui_pr]['Qn']*record[ui_pr]["Price"]) + "," + time.ctime()
        record[ui_pr]['Qn'] = 0
    else:

        print('Thanks!')

js = json.dumps(record)
fd = open("Records.json", 'w')
fd.write(js)
fd.close()


# In[70]:


import time
sales = "1" + "," + ui_name + "," + ui_mail + "," + ui_phno + "," + ui_pr + "," + record[ui_pr]["Name"] + "," + str(record[ui_pr]["Price"]) + "," + str(record[ui_pr]['Qn']*record[ui_pr]["Price"]) + "," + time.ctime()


# In[71]:


sales


# In[75]:


sales


# ### Generating Sales File and Saving them 

# In[97]:


import json
import time

fd = open("Records.json", 'r')
js = fd.read()
fd.close()

record = json.loads(js)

sales = " "

print('------------Menu------------\n')
for key in record.keys():
    print(key, ":", record[key]['Name'], "|",record[key]['Price'], "|",record[key]['Qn'])
print('\n----------------------------\n')

ui_name = str(input("Enter your Name:"))
ui_mail = str(input("Enter your Mail Id:"))
ui_phno = str(input("Enter your phone number:"))
ui_pr = str(input("Enter the product ID: "))
ui_qn = int(input("Enter the quantity  : "))

if(record[ui_pr]['Qn'] >= ui_qn):

    record[ui_pr]['Qn'] = int(record[ui_pr]['Qn'] - ui_qn)
    print('\n--------------Bill--------------\n')
    print('Name of the product purchased:', record[ui_pr]['Name'])
    print('Price of one quantity:', record[ui_pr]['Price'])
    print('The quantity purchased:',ui_qn)
    print('\n----------------------------\n')
    print('The amount to be paid:', record[ui_pr]['Price'] * ui_qn)
    print('\n----------------------------\n')
    
    sales = ui_name + "," + ui_mail + "," + ui_phno + "," + ui_pr + "," + record[ui_pr]["Name"] + "," + str(record[ui_pr]["Price"]) + "," + str(ui_qn * record[ui_pr]["Price"]) + "," + time.ctime()+ "\n"

else:
    
    print("Sorry, we are not having enough quantity!")
    print("We only have", record[ui_pr]['Qn'], " qunatity in the inventory.")
    print('\n----------------------------\n')
    
    ch = str(input('Press Y/y to purchase:'))
    
    if(ch == 'Y' or ch == 'y'):
    
        print('\n--------------Bill--------------\n')
        print('Name of the product purchased:', record[ui_pr]['Name'])
        print('Price of one quantity:', record[ui_pr]['Price'])
        print('The quantity purchased:',record[ui_pr]['Qn'])
        print('\n----------------------------\n')
        print('The amount to be paid:', record[ui_pr]['Price'] * record[ui_pr]['Qn'])
        print('\n----------------------------\n')
        
        sales = ui_name + "," + ui_mail + "," + ui_phno + "," + ui_pr + "," + record[ui_pr]["Name"] + "," + str(record[ui_pr]["Price"]) + "," + str(record[ui_pr]['Qn']*record[ui_pr]["Price"]) + "," + time.ctime()+ "\n"
        record[ui_pr]['Qn'] = 0
    else:

        print('Thanks!')

js = json.dumps(record)
fd = open("Records.json", 'w')
fd.write(js)
fd.close()

fd = open('Sales.txt', 'a')
fd.write(sales)
fd.close()

print("--------------------------------\n")
print("Thank you for purchasing! Inventory Updated.")
print("--------------------------------\n")


# In[92]:


fd = open('Sales.txt', 'a')
fd.write(sales)
fd.close()


# In[88]:


sales


# ### Final Code with Comments

# In[98]:


#Importing the Libraries
import json
import time

#Loading the Records from Inventory - JSON to String
fd = open("Records.json", 'r')
js = fd.read()
fd.close()

#Converting String Records to JSON?Dictionaries
record = json.loads(js)

#Initialising Variable for Generating Sales Data
sales = " "

#Displaying the Menu
print('------------Menu------------\n')
for key in record.keys():
    print(key, ":", record[key]['Name'], "|",record[key]['Price'], "|",record[key]['Qn'])
print('\n----------------------------\n')


#Taking inputs from the user on product requirements and user details
ui_name = str(input("Enter your Name:"))
ui_mail = str(input("Enter your Mail Id:"))
ui_phno = str(input("Enter your phone number:"))
ui_pr = str(input("Enter the product ID: "))
ui_qn = int(input("Enter the quantity  : "))

#If we are having more or equal quantity than user wants
if(record[ui_pr]['Qn'] >= ui_qn):

    #Purchase details
    print('\n--------------Bill--------------\n')
    print('Name of the product purchased:', record[ui_pr]['Name'])
    print('Price of one quantity:', record[ui_pr]['Price'])
    print('The quantity purchased:',ui_qn)
    print('\n----------------------------\n')
    print('The amount to be paid:', record[ui_pr]['Price'] * ui_qn)
    print('\n----------------------------\n')
    
    #Updating the inventory in Dictionary
    record[ui_pr]['Qn'] = int(record[ui_pr]['Qn'] - ui_qn)
    
    #Generating Sales Details and Saving in CSV
    sales = ui_name + "," + ui_mail + "," + ui_phno + "," + ui_pr + "," + record[ui_pr]["Name"] + "," + str(record[ui_pr]["Price"]) + "," + str(ui_qn * record[ui_pr]["Price"]) + "," + time.ctime()+ "\n"

# Not having enough quantity
else:
    
    #Displaying about the available quantity
    print("Sorry, we are not having enough quantity!")
    print("We only have", record[ui_pr]['Qn'], " qunatity in the inventory.")
    print('\n----------------------------\n')
    
    #If user wants to purchase the available quantity from the inventory
    ch = str(input('Press Y/y to purchase:'))
    
    if(ch == 'Y' or ch == 'y'):
        
        #Displaying Purchase Details
        print('\n--------------Bill--------------\n')
        print('Name of the product purchased:', record[ui_pr]['Name'])
        print('Price of one quantity:', record[ui_pr]['Price'])
        print('The quantity purchased:',record[ui_pr]['Qn'])
        print('\n----------------------------\n')
        print('The amount to be paid:', record[ui_pr]['Price'] * record[ui_pr]['Qn'])
        print('\n----------------------------\n')
        
        #Generating Sales Details and Saving in CSV
        sales = ui_name + "," + ui_mail + "," + ui_phno + "," + ui_pr + "," + record[ui_pr]["Name"] + "," + str(record[ui_pr]["Price"]) + "," + str(record[ui_pr]['Qn']*record[ui_pr]["Price"]) + "," + time.ctime()+ "\n"
        
        #Updating the inventory in Dictionary
        record[ui_pr]['Qn'] = 0
    else:
        print('Thanks!')
#Converting Dict to Str
js = json.dumps(record)

#Saving in JSON
fd = open("Records.json", 'w')
fd.write(js)
fd.close()

#Saving sales details
fd = open('Sales.txt', 'a')
fd.write(sales)
fd.close()

print("--------------------------------\n")
print("Thank you for purchasing! Inventory Updated.")
print("--------------------------------\n")


# In[99]:


sales


# In[ ]:




