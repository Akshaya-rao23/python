#!/usr/bin/env python
# coding: utf-8

# In[9]:


x=int(input('enter x number'))
y=int(input('enter y number'))
z=int(input('enter z number'))
if x>y & x>z:
    print("x is greatest")
elif y>x & y>z:
    print("y is greatest")
else:
    print("z is greatest")
 


# In[6]:


x=int(input("enter x number"))
y=int(input("enter y number"))
z=int(input("enter z number"))
if(x>y and x>z):
    print("x is greatest")
elif(y>x and y>z):
    print("y is greatest")
else:
    print("z is greatest")
 


# In[11]:


for i in range(1,6):
    for j in range (1,i+1):
        print(j,end=" ")
    print("\n")


# In[19]:


a=int(input("enter number"))
fact=1
for i in range(1,a+1):
    fact=fact*i
print(fact)


# In[13]:


#fibonaccci
a=0
b=1
n=int(input("enter range"))
print(a,end=" ")
print(b,end=" ")
for i in range(0,n):
    c=a+b
    print(c,end=" ")
    a=b
    b=c


# In[29]:


#average in list
my_list=[1,2,3,4,5]
sum=0
avg=0
for i in my_list:
    sum+=i
print("sum=",sum)
avg=sum/i
print(avg)
    


# In[21]:


#prime or not
int(input("enter a num:"))
flag =0 
for i in range(2,n):
    if(n%i==0):
        flag=0
        break
    else:
        flag=1
if(flag==1):
    print("is prime")
else:
    print("not prime")
          


# In[38]:


#toremove empty tuples
def Remove(tuples):
    for i in tuples:
        if(len(i) == 0):
            tuples.remove(i)
    return tuples
tuples = [(), ('akki', '15', '8'), (), ('pandu', 'sita'), ('krishna', 'akbar', '45'), ('', ''), ()]
print(Remove(tuples))


# In[48]:


list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
list.pop(5)
list.pop(4)
list.pop(0)
print(list) 


# In[52]:


tuples=[(),(1,2,3),()]
for i in tuples:
    if(len(i)==0):
        tuples.remove(i)
print(tuples)


# In[53]:


tuples=[(),(1,2,3),()]
for i in tuples:
    if(i==()):
        tuples.remove(i)
print(tuples)


# In[56]:


tuple=(1,2,3,4)
product=1
for i in tuple:
    product=product*i
print(product)


# In[67]:


string="akshayat"
if(string==4):
    print(rev(i))


# In[3]:


#monday(30-1-2023)
n = int(input())
arr=[]
for i in range(n):
    username = input("Username: ")
    password = input("Password: ")
    arr.append({username: password})
    
print(arr)


# In[9]:


n = int(input())
arr=[]
for i in range(n):
    username = input("Username: ")
    password = input("Password: ")
    arr.append({username: password})
    print(arr)

u1=input("Username: ")
p1=input("Password: ")
found = False
for obj in arr:
    try:
        password = obj[u1]
        found = True
        if p1 == password:
            print("Valid password")
        else:
            print("Invalid password")
    except:
        pass
if found == False:
    print("User not found")


# In[ ]:





# In[ ]:




