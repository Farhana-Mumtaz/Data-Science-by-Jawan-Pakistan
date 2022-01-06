#!/usr/bin/env python
# coding: utf-8

# # PROGRAM TO GET THE PYTHON VERSION YOU ARE USING:

# In[2]:


import sys
print("python version")
print(sys.version)
print("Version Info")
print(sys.version_info)


# # TASK 1

# In[ ]:


print("Twinkle,twinkle,little star,")
print("         How I wonder what you are!")
print("                 Up above the world so high,")
print("                 Like a diamond in the sky.")
print("Twinkle,twinkle,little star,")
print("         How I wonder what you are!")


# # TASK 3
# # write a program to display the current date and time.

# In[13]:


import datetime
now=datetime.datetime.now()
print("Print Current Date And Time : ")
print(now.strftime("%Y-%m-%d %H:%M:%S"))


# # TASK 4
# # Write a program which accepts the radius of a circle from the user and compute the area.

# In[6]:


from math import pi
r=float(input("Enter Radius value : "))
print("The Area Of Circle with radius  = "+str(r)+" is ="+str(pi*r**2))


# # TASK 5
# # Write a program which accepts the user first and last name and print them in reverse order with a space between them.

# In[6]:


first_name=input("Input First Name :")
last_name=input("Input Last Name :")

for char in range(len(first_name) -1,-1,-1):
    print(first_name[char],end=" ") 
for char in range(len(last_name) -1,-1,-1):
    print(last_name[char],end=" ")
  


# # TASK 6
# # Write a python program which takes two inputs from user and print them addition

# In[12]:


val=int(input("Enter value one ="))
val2=int(input("Enter Value two ="))     
print("Addition is = "+str(val+val2))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




