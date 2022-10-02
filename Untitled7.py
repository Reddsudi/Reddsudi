#!/usr/bin/env python
# coding: utf-8

# In[295]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
import glob
import os

r=requests.get('https://web.saumag.edu/directory/')
info = []
soup = BeautifulSoup(r.content,'html5lib')
x_all = soup.find_all('ul', attrs={'class':'alpha-list'})



# In[296]:


soup2 = BeautifulSoup(r.content,'html5lib')
k = soup2.find('li', attrs={'id':'letter-a'})
link_all=k.find_all( href = True)
info = []  
name_ar = []
email_ar = []
URL_ar = []
org_ar = []
title_ar = []
for link in link_all:
  print (link.get('href'))
  URL_ar.append(link.get('href'))
    
    
  re=requests.get(link.get('href')) 
  soup = BeautifulSoup(re.content,'html5lib')
  name_all = soup.find_all('h1', attrs={'class':'name fn'})
  org_all = soup.find_all('p', attrs={'class':'organization organization-unit'})
  title_all = soup.find_all('h2', attrs={'class':'title'})
  email_all = soup.find_all('p', attrs={'class':'email'})
  
  for name in name_all:
    print(name.text)  
    name_ar.append(name.text.strip())  
   
    
  for title in title_all:
    print(title.text)    
    title_ar.append(title.text.strip())  
  
  
  for org in org_all:
    print(org.text)    
    org_ar.append(org.text.strip())  
  

    
    
  for email in email_all:
    print(email.text)
    email_ar.append(email.text.strip())  
    
info = {'Name': name_ar,'Link': URL_ar,
        'email': email_ar,'title':title_ar,'org':org_ar}
  
# Create DataFrame
df = pd.DataFrame(info)
  
# Save the output.
df.to_csv('professors1.csv',index = False)
 
 


# In[222]:


soup2 = BeautifulSoup(r.content,'html5lib')
k = soup2.find('li', attrs={'id':'letter-b'})
link_all=k.find_all( href = True)
info = []  
name_ar = []
email_ar = []
URL_ar = []
org_ar = []
title_ar = []
for link in link_all:
  print (link.get('href'))
  URL_ar.append(link.get('href'))
    
    
  re=requests.get(link.get('href')) 
  soup = BeautifulSoup(re.content,'html5lib')
  name_all = soup.find_all('h1', attrs={'class':'name fn'})
  org_all = soup.find_all('p', attrs={'class':'organization organization-unit'})
  title_all = soup.find_all('h2', attrs={'class':'title'})
  email_all = soup.find_all('p', attrs={'class':'email'})
  
  for name in name_all:
    print(name.text)  
    name_ar.append(name.text.strip())  
   
    
  for title in title_all:
    print(title.text)    
    title_ar.append(title.text.strip())  
  
  
  for org in org_all:
    print(org.text)    
    org_ar.append(org.text.strip())  
  

    
    
  for email in email_all:
    print(email.text)
    email_ar.append(email.text.strip())  
    
info = {'Name': name_ar,'Link': URL_ar,
        'email': email_ar,'title':title_ar,'org':org_ar}
  
# Create DataFrame
df = pd.DataFrame(info)
  
# Save the output.
df.to_csv('professors1.csv',mode = 'a',index = False)
 
 


# In[223]:


soup2 = BeautifulSoup(r.content,'html5lib')
k = soup2.find('li', attrs={'id':'letter-c'})
link_all=k.find_all( href = True)
info = []  
name_ar = []
email_ar = []
URL_ar = []
org_ar = []
title_ar = []
for link in link_all:
  print (link.get('href'))
  URL_ar.append(link.get('href'))
    
    
  re=requests.get(link.get('href')) 
  soup = BeautifulSoup(re.content,'html5lib')
  name_all = soup.find_all('h1', attrs={'class':'name fn'})
  org_all = soup.find_all('p', attrs={'class':'organization organization-unit'})
  title_all = soup.find_all('h2', attrs={'class':'title'})
  email_all = soup.find_all('p', attrs={'class':'email'})
  
  for name in name_all:
    print(name.text)  
    name_ar.append(name.text.strip())  
   
    
  for title in title_all:
    print(title.text)    
    title_ar.append(title.text.strip())  
  
  
  for org in org_all:
    print(org.text)    
    org_ar.append(org.text.strip())  
  

    
    
  for email in email_all:
    print(email.text)
    email_ar.append(email.text.strip())  
    
info = {'Name': name_ar,'Link': URL_ar,
        'email': email_ar,'title':title_ar,'org':org_ar}
  
# Create DataFrame
df = pd.DataFrame(info)
  
# Save the output.
df.to_csv('professors1.csv',mode = 'a',index = False) 
 


# In[224]:


soup2 = BeautifulSoup(r.content,'html5lib')
k = soup2.find('li', attrs={'id':'letter-d'})
link_all=k.find_all( href = True)
info = []  
name_ar = []
email_ar = []
URL_ar = []
org_ar = []
title_ar = []
for link in link_all:
  print (link.get('href'))
  URL_ar.append(link.get('href'))
    
    
  re=requests.get(link.get('href')) 
  soup = BeautifulSoup(re.content,'html5lib')
  name_all = soup.find_all('h1', attrs={'class':'name fn'})
  org_all = soup.find_all('p', attrs={'class':'organization organization-unit'})
  title_all = soup.find_all('h2', attrs={'class':'title'})
  email_all = soup.find_all('p', attrs={'class':'email'})
  
  for name in name_all:
    print(name.text)  
    name_ar.append(name.text.strip())  
   
    
  for title in title_all:
    print(title.text)    
    title_ar.append(title.text.strip())  
  
  
  for org in org_all:
    print(org.text)    
    org_ar.append(org.text.strip())  
  

    
    
  for email in email_all:
    print(email.text)
    email_ar.append(email.text.strip())  
    
info = {'Name': name_ar,'Link': URL_ar,
        'email': email_ar,'title':title_ar,'org':org_ar}
  
# Create DataFrame
df = pd.DataFrame(info)
  
# Save the output.
df.to_csv('professors1.csv',mode = 'a',index = False) 
 


# In[225]:


soup2 = BeautifulSoup(r.content,'html5lib')
k = soup2.find('li', attrs={'id':'letter-e'})
link_all=k.find_all( href = True)
info = []  
name_ar = []
email_ar = []
URL_ar = []
org_ar = []
title_ar = []
for link in link_all:
  print (link.get('href'))
  URL_ar.append(link.get('href'))
    
    
  re=requests.get(link.get('href')) 
  soup = BeautifulSoup(re.content,'html5lib')
  name_all = soup.find_all('h1', attrs={'class':'name fn'})
  org_all = soup.find_all('p', attrs={'class':'organization organization-unit'})
  title_all = soup.find_all('h2', attrs={'class':'title'})
  email_all = soup.find_all('p', attrs={'class':'email'})
  
  for name in name_all:
    print(name.text)  
    name_ar.append(name.text.strip())  
   
    
  for title in title_all:
    print(title.text)    
    title_ar.append(title.text.strip())  
  
  
  for org in org_all:
    print(org.text)    
    org_ar.append(org.text.strip())  
  

    
    
  for email in email_all:
    print(email.text)
    email_ar.append(email.text.strip())  
    
info = {'Name': name_ar,'Link': URL_ar,
        'email': email_ar,'title':title_ar,'org':org_ar}
  
# Create DataFrame
df = pd.DataFrame(info)
  
# Save the output.
df.to_csv('professors1.csv',mode = 'a',index = False) 
 


# In[226]:


soup2 = BeautifulSoup(r.content,'html5lib')
k = soup2.find('li', attrs={'id':'letter-f'})
link_all=k.find_all( href = True)
info = []  
name_ar = []
email_ar = []
URL_ar = []
org_ar = []
title_ar = []
for link in link_all:
  print (link.get('href'))
  URL_ar.append(link.get('href'))
    
    
  re=requests.get(link.get('href')) 
  soup = BeautifulSoup(re.content,'html5lib')
  name_all = soup.find_all('h1', attrs={'class':'name fn'})
  org_all = soup.find_all('p', attrs={'class':'organization organization-unit'})
  title_all = soup.find_all('h2', attrs={'class':'title'})
  email_all = soup.find_all('p', attrs={'class':'email'})
  
  for name in name_all:
    print(name.text)  
    name_ar.append(name.text.strip())  
   
    
  for title in title_all:
    print(title.text)    
    title_ar.append(title.text.strip())  
  
  
  for org in org_all:
    print(org.text)    
    org_ar.append(org.text.strip())  
  

    
    
  for email in email_all:
    print(email.text)
    email_ar.append(email.text.strip())  
    
info = {'Name': name_ar,'Link': URL_ar,
        'email': email_ar,'title':title_ar,'org':org_ar}
  
# Create DataFrame
df = pd.DataFrame(info)
  
# Save the output.
df.to_csv('professors1.csv',mode = 'a',index = False) 
 


# In[297]:


soup2 = BeautifulSoup(r.content,'html5lib')
k = soup2.find('li', attrs={'id':'letter-g'})
link_all=k.find_all( href = True)
info = []  
name_ar = []
email_ar = []
URL_ar = []
org_ar = []
title_ar = []
for link in link_all:
  print (link.get('href'))
  URL_ar.append(link.get('href'))
    
    
  re=requests.get(link.get('href')) 
  soup = BeautifulSoup(re.content,'html5lib')
  name_all = soup.find_all('h1', attrs={'class':'name fn'})
  org_all = soup.find_all('p', attrs={'class':'organization organization-unit'})
  title_all = soup.find_all('h2', attrs={'class':'title'})
  email_all = soup.find_all('p', attrs={'class':'email'})
  
  for name in name_all:
    print(name.text)  
    name_ar.append(name.text.strip())  
   
    
  for title in title_all:
    print(title.text)    
    title_ar.append(title.text.strip())  
  
  
  for org in org_all:
    print(org.text)    
    org_ar.append(org.text.strip())  
  

    
    
  for email in email_all:
    print(email.text)
    email_ar.append(email.text.strip())  
    
info = {'Name': name_ar,'Link': URL_ar,
        'email': email_ar,'title':title_ar,'org':org_ar}
  
# Create DataFrame
df = pd.DataFrame(info)
  
# Save the output.
df.to_csv('professors1.csv',mode = 'a',index = False) 
 


# In[294]:


soup2 = BeautifulSoup(r.content,'html5lib')
k = soup2.find('li', attrs={'id':'letter-h'})
link_all=k.find_all( href = True)
info = []  
name_ar = []
email_ar = []
URL_ar = []
org_ar = []
title_ar = []
for link in link_all:
  print (link.get('href'))
  URL_ar.append(link.get('href'))
    
    
  re=requests.get(link.get('href')) 
  soup = BeautifulSoup(re.content,'html5lib')
  name_all = soup.find_all('h1', attrs={'class':'name fn'})
  org_all = soup.find_all('p', attrs={'class':'organization organization-unit'})
  title_all = soup.find_all('h2', attrs={'class':'title'})
  email_all = soup.find_all('p', attrs={'class':'email'})
  
  for name in name_all:
    print(name.text)  
    name_ar.append(name.text.strip())  
   
    
  for title in title_all:
    print(title.text)    
    title_ar.append(title.text.strip())  
  
  
  for org in org_all:
    print(org.text)    
    org_ar.append(org.text.strip())  
  

    
    
  for email in email_all:
    print(email.text)
    email_ar.append(email.text.strip())  
    
info = {'Name': name_ar,'Link': URL_ar,
        'email': email_ar,'title':title_ar,'org':org_ar}
  
# Create DataFrame
df = pd.DataFrame(info)
  
# Save the output.
df.to_csv('professors1.csv',mode = 'a',index = False) 
 


# In[298]:


soup2 = BeautifulSoup(r.content,'html5lib')
k = soup2.find('li', attrs={'id':'letter-i'})
link_all=k.find_all( href = True)
info = []  
name_ar = []
email_ar = []
URL_ar = []
org_ar = []
title_ar = []
for link in link_all:
  print (link.get('href'))
  URL_ar.append(link.get('href'))
    
    
  re=requests.get(link.get('href')) 
  soup = BeautifulSoup(re.content,'html5lib')
  name_all = soup.find_all('h1', attrs={'class':'name fn'})
  org_all = soup.find_all('p', attrs={'class':'organization organization-unit'})
  title_all = soup.find_all('h2', attrs={'class':'title'})
  email_all = soup.find_all('p', attrs={'class':'email'})
  
  for name in name_all:
    print(name.text)  
    name_ar.append(name.text.strip())  
   
    
  for title in title_all:
    print(title.text)    
    title_ar.append(title.text.strip())  
  
  
  for org in org_all:
    print(org.text)    
    org_ar.append(org.text.strip())  
  

    
    
  for email in email_all:
    print(email.text)
    email_ar.append(email.text.strip())  
    
info = {'Name': name_ar,'Link': URL_ar,
        'email': email_ar,'title':title_ar,'org':org_ar}
  
# Create DataFrame
df = pd.DataFrame(info)
  
# Save the output.
df.to_csv('professors1.csv',mode = 'a',index = False) 
 


# In[299]:


soup2 = BeautifulSoup(r.content,'html5lib')
k = soup2.find('li', attrs={'id':'letter-j'})
link_all=k.find_all( href = True)
info = []  
name_ar = []
email_ar = []
URL_ar = []
org_ar = []
title_ar = []
for link in link_all:
  print (link.get('href'))
  URL_ar.append(link.get('href'))
    
    
  re=requests.get(link.get('href')) 
  soup = BeautifulSoup(re.content,'html5lib')
  name_all = soup.find_all('h1', attrs={'class':'name fn'})
  org_all = soup.find_all('p', attrs={'class':'organization organization-unit'})
  title_all = soup.find_all('h2', attrs={'class':'title'})
  email_all = soup.find_all('p', attrs={'class':'email'})
  
  for name in name_all:
    print(name.text)  
    name_ar.append(name.text.strip())  
   
    
  for title in title_all:
    print(title.text)    
    title_ar.append(title.text.strip())  
  
  
  for org in org_all:
    print(org.text)    
    org_ar.append(org.text.strip())  
  

    
    
  for email in email_all:
    print(email.text)
    email_ar.append(email.text.strip())  
    
info = {'Name': name_ar,'Link': URL_ar,
        'email': email_ar,'title':title_ar,'org':org_ar}
  
# Create DataFrame
df = pd.DataFrame(info)
  
# Save the output.
df.to_csv('professors1.csv',mode = 'a',index = False) 
 


# In[300]:


soup2 = BeautifulSoup(r.content,'html5lib')
k = soup2.find('li', attrs={'id':'letter-k'})
link_all=k.find_all( href = True)
info = []  
name_ar = []
email_ar = []
URL_ar = []
org_ar = []
title_ar = []
for link in link_all:
  print (link.get('href'))
  URL_ar.append(link.get('href'))
    
    
  re=requests.get(link.get('href')) 
  soup = BeautifulSoup(re.content,'html5lib')
  name_all = soup.find_all('h1', attrs={'class':'name fn'})
  org_all = soup.find_all('p', attrs={'class':'organization organization-unit'})
  title_all = soup.find_all('h2', attrs={'class':'title'})
  email_all = soup.find_all('p', attrs={'class':'email'})
  
  for name in name_all:
    print(name.text)  
    name_ar.append(name.text.strip())  
   
    
  for title in title_all:
    print(title.text)    
    title_ar.append(title.text.strip())  
  
  
  for org in org_all:
    print(org.text)    
    org_ar.append(org.text.strip())  
  

    
    
  for email in email_all:
    print(email.text)
    email_ar.append(email.text.strip())  
    
info = {'Name': name_ar,'Link': URL_ar,
        'email': email_ar,'title':title_ar,'org':org_ar}
  
# Create DataFrame
df = pd.DataFrame(info)
  
# Save the output.
df.to_csv('professors1.csv',mode = 'a',index = False) 
 


# In[301]:


soup2 = BeautifulSoup(r.content,'html5lib')
k = soup2.find('li', attrs={'id':'letter-l'})
link_all=k.find_all( href = True)
info = []  
name_ar = []
email_ar = []
URL_ar = []
org_ar = []
title_ar = []
for link in link_all:
  print (link.get('href'))
  URL_ar.append(link.get('href'))
    
    
  re=requests.get(link.get('href')) 
  soup = BeautifulSoup(re.content,'html5lib')
  name_all = soup.find_all('h1', attrs={'class':'name fn'})
  org_all = soup.find_all('p', attrs={'class':'organization organization-unit'})
  title_all = soup.find_all('h2', attrs={'class':'title'})
  email_all = soup.find_all('p', attrs={'class':'email'})
  
  for name in name_all:
    print(name.text)  
    name_ar.append(name.text.strip())  
   
    
  for title in title_all:
    print(title.text)    
    title_ar.append(title.text.strip())  
  
  
  for org in org_all:
    print(org.text)    
    org_ar.append(org.text.strip())  
  

    
    
  for email in email_all:
    print(email.text)
    email_ar.append(email.text.strip())  
    
info = {'Name': name_ar,'Link': URL_ar,
        'email': email_ar,'title':title_ar,'org':org_ar}
  
# Create DataFrame
df = pd.DataFrame(info)
  
# Save the output.
df.to_csv('professors1.csv',mode = 'a',index = False) 
 


# In[302]:


soup2 = BeautifulSoup(r.content,'html5lib')
k = soup2.find('li', attrs={'id':'letter-m'})
link_all=k.find_all( href = True)
info = []  
name_ar = []
email_ar = []
URL_ar = []
org_ar = []
title_ar = []
for link in link_all:
  print (link.get('href'))
  URL_ar.append(link.get('href'))
    
    
  re=requests.get(link.get('href')) 
  soup = BeautifulSoup(re.content,'html5lib')
  name_all = soup.find_all('h1', attrs={'class':'name fn'})
  org_all = soup.find_all('p', attrs={'class':'organization organization-unit'})
  title_all = soup.find_all('h2', attrs={'class':'title'})
  email_all = soup.find_all('p', attrs={'class':'email'})
  
  for name in name_all:
    print(name.text)  
    name_ar.append(name.text.strip())  
   
    
  for title in title_all:
    print(title.text)    
    title_ar.append(title.text.strip())  
  
  
  for org in org_all:
    print(org.text)    
    org_ar.append(org.text.strip())  
  

    
    
  for email in email_all:
    print(email.text)
    email_ar.append(email.text.strip())  
    
info = {'Name': name_ar,'Link': URL_ar,
        'email': email_ar,'title':title_ar,'org':org_ar}
  
# Create DataFrame
df = pd.DataFrame(info)
  
# Save the output.
df.to_csv('professors1.csv',mode = 'a',index = False) 
 


# In[303]:


soup2 = BeautifulSoup(r.content,'html5lib')
k = soup2.find('li', attrs={'id':'letter-n'})
link_all=k.find_all( href = True)
info = []  
name_ar = []
email_ar = []
URL_ar = []
org_ar = []
title_ar = []
for link in link_all:
  print (link.get('href'))
  URL_ar.append(link.get('href'))
    
    
  re=requests.get(link.get('href')) 
  soup = BeautifulSoup(re.content,'html5lib')
  name_all = soup.find_all('h1', attrs={'class':'name fn'})
  org_all = soup.find_all('p', attrs={'class':'organization organization-unit'})
  title_all = soup.find_all('h2', attrs={'class':'title'})
  email_all = soup.find_all('p', attrs={'class':'email'})
  
  for name in name_all:
    print(name.text)  
    name_ar.append(name.text.strip())  
   
    
  for title in title_all:
    print(title.text)    
    title_ar.append(title.text.strip())  
  
  
  for org in org_all:
    print(org.text)    
    org_ar.append(org.text.strip())  
  

    
    
  for email in email_all:
    print(email.text)
    email_ar.append(email.text.strip())  
    
info = {'Name': name_ar,'Link': URL_ar,
        'email': email_ar,'title':title_ar,'org':org_ar}
  
# Create DataFrame
df = pd.DataFrame(info)
  
# Save the output.
df.to_csv('professors1.csv',mode = 'a',index = False) 
 


# In[304]:


soup2 = BeautifulSoup(r.content,'html5lib')
k = soup2.find('li', attrs={'id':'letter-o'})
link_all=k.find_all( href = True)
info = []  
name_ar = []
email_ar = []
URL_ar = []
org_ar = []
title_ar = []
for link in link_all:
  print (link.get('href'))
  URL_ar.append(link.get('href'))
    
    
  re=requests.get(link.get('href')) 
  soup = BeautifulSoup(re.content,'html5lib')
  name_all = soup.find_all('h1', attrs={'class':'name fn'})
  org_all = soup.find_all('p', attrs={'class':'organization organization-unit'})
  title_all = soup.find_all('h2', attrs={'class':'title'})
  email_all = soup.find_all('p', attrs={'class':'email'})
  
  for name in name_all:
    print(name.text)  
    name_ar.append(name.text.strip())  
   
    
  for title in title_all:
    print(title.text)    
    title_ar.append(title.text.strip())  
  
  
  for org in org_all:
    print(org.text)    
    org_ar.append(org.text.strip())  
  

    
    
  for email in email_all:
    print(email.text)
    email_ar.append(email.text.strip())  
    
info = {'Name': name_ar,'Link': URL_ar,
        'email': email_ar,'title':title_ar,'org':org_ar}
  
# Create DataFrame
df = pd.DataFrame(info)
  
# Save the output.
df.to_csv('professors1.csv',mode = 'a',index = False) 
 


# In[305]:


soup2 = BeautifulSoup(r.content,'html5lib')
k = soup2.find('li', attrs={'id':'letter-p'})
link_all=k.find_all( href = True)
info = []  
name_ar = []
email_ar = []
URL_ar = []
org_ar = []
title_ar = []
for link in link_all:
  print (link.get('href'))
  URL_ar.append(link.get('href'))
    
    
  re=requests.get(link.get('href')) 
  soup = BeautifulSoup(re.content,'html5lib')
  name_all = soup.find_all('h1', attrs={'class':'name fn'})
  org_all = soup.find_all('p', attrs={'class':'organization organization-unit'})
  title_all = soup.find_all('h2', attrs={'class':'title'})
  email_all = soup.find_all('p', attrs={'class':'email'})
  
  for name in name_all:
    print(name.text)  
    name_ar.append(name.text.strip())  
   
    
  for title in title_all:
    print(title.text)    
    title_ar.append(title.text.strip())  
  
  
  for org in org_all:
    print(org.text)    
    org_ar.append(org.text.strip())  
  

    
    
  for email in email_all:
    print(email.text)
    email_ar.append(email.text.strip())  
    
info = {'Name': name_ar,'Link': URL_ar,
        'email': email_ar,'title':title_ar,'org':org_ar}
  
# Create DataFrame
df = pd.DataFrame(info)
  
# Save the output.
df.to_csv('professors1.csv',mode = 'a',index = False) 
 


# In[306]:


soup2 = BeautifulSoup(r.content,'html5lib')
k = soup2.find('li', attrs={'id':'letter-q'})
link_all=k.find_all( href = True)
info = []  
name_ar = []
email_ar = []
URL_ar = []
org_ar = []
title_ar = []
for link in link_all:
  print (link.get('href'))
  URL_ar.append(link.get('href'))
    
    
  re=requests.get(link.get('href')) 
  soup = BeautifulSoup(re.content,'html5lib')
  name_all = soup.find_all('h1', attrs={'class':'name fn'})
  org_all = soup.find_all('p', attrs={'class':'organization organization-unit'})
  title_all = soup.find_all('h2', attrs={'class':'title'})
  email_all = soup.find_all('p', attrs={'class':'email'})
  
  for name in name_all:
    print(name.text)  
    name_ar.append(name.text.strip())  
   
    
  for title in title_all:
    print(title.text)    
    title_ar.append(title.text.strip())  
  
  
  for org in org_all:
    print(org.text)    
    org_ar.append(org.text.strip())  
  

    
    
  for email in email_all:
    print(email.text)
    email_ar.append(email.text.strip())  
    
info = {'Name': name_ar,'Link': URL_ar,
        'email': email_ar,'title':title_ar,'org':org_ar}
  
# Create DataFrame
df = pd.DataFrame(info)
  
# Save the output.
df.to_csv('professors1.csv',mode = 'a',index = False) 
 


# In[307]:


soup2 = BeautifulSoup(r.content,'html5lib')
k = soup2.find('li', attrs={'id':'letter-r'})
link_all=k.find_all( href = True)
info = []  
name_ar = []
email_ar = []
URL_ar = []
org_ar = []
title_ar = []
for link in link_all:
  print (link.get('href'))
  URL_ar.append(link.get('href'))
    
    
  re=requests.get(link.get('href')) 
  soup = BeautifulSoup(re.content,'html5lib')
  name_all = soup.find_all('h1', attrs={'class':'name fn'})
  org_all = soup.find_all('p', attrs={'class':'organization organization-unit'})
  title_all = soup.find_all('h2', attrs={'class':'title'})
  email_all = soup.find_all('p', attrs={'class':'email'})
  
  for name in name_all:
    print(name.text)  
    name_ar.append(name.text.strip())  
   
    
  for title in title_all:
    print(title.text)    
    title_ar.append(title.text.strip())  
  
  
  for org in org_all:
    print(org.text)    
    org_ar.append(org.text.strip())  
  

    
    
  for email in email_all:
    print(email.text)
    email_ar.append(email.text.strip())  
    
info = {'Name': name_ar,'Link': URL_ar,
        'email': email_ar,'title':title_ar,'org':org_ar}
  
# Create DataFrame
df = pd.DataFrame(info)
  
# Save the output.
df.to_csv('professors1.csv',mode = 'a',index = False) 
 


# In[ ]:


soup2 = BeautifulSoup(r.content,'html5lib')
k = soup2.find('li', attrs={'id':'letter-s'})
link_all=k.find_all( href = True)
info = []  
name_ar = []
email_ar = []
URL_ar = []
org_ar = []
title_ar = []
for link in link_all:
  print (link.get('href'))
  URL_ar.append(link.get('href'))
    
    
  re=requests.get(link.get('href')) 
  soup = BeautifulSoup(re.content,'html5lib')
  name_all = soup.find_all('h1', attrs={'class':'name fn'})
  org_all = soup.find_all('p', attrs={'class':'organization organization-unit'})
  title_all = soup.find_all('h2', attrs={'class':'title'})
  email_all = soup.find_all('p', attrs={'class':'email'})
  
  for name in name_all:
    print(name.text)  
    name_ar.append(name.text.strip())  
   
    
  for title in title_all:
    print(title.text)    
    title_ar.append(title.text.strip())  
  
  
  for org in org_all:
    print(org.text)    
    org_ar.append(org.text.strip())  
  

    
    
  for email in email_all:
    print(email.text)
    email_ar.append(email.text.strip())  
    
info = {'Name': name_ar,'Link': URL_ar,
        'email': email_ar,'title':title_ar,'org':org_ar}
  
# Create DataFrame
df = pd.DataFrame(info)
  
# Save the output.
df.to_csv('professors1.csv',mode = 'a',index = False) 
 


# In[ ]:


soup2 = BeautifulSoup(r.content,'html5lib')
k = soup2.find('li', attrs={'id':'letter-t'})
link_all=k.find_all( href = True)
info = []  
name_ar = []
email_ar = []
URL_ar = []
org_ar = []
title_ar = []
for link in link_all:
  print (link.get('href'))
  URL_ar.append(link.get('href'))
    
    
  re=requests.get(link.get('href')) 
  soup = BeautifulSoup(re.content,'html5lib')
  name_all = soup.find_all('h1', attrs={'class':'name fn'})
  org_all = soup.find_all('p', attrs={'class':'organization organization-unit'})
  title_all = soup.find_all('h2', attrs={'class':'title'})
  email_all = soup.find_all('p', attrs={'class':'email'})
  
  for name in name_all:
    print(name.text)  
    name_ar.append(name.text.strip())  
   
    
  for title in title_all:
    print(title.text)    
    title_ar.append(title.text.strip())  
  
  
  for org in org_all:
    print(org.text)    
    org_ar.append(org.text.strip())  
  

    
    
  for email in email_all:
    print(email.text)
    email_ar.append(email.text.strip())  
    
info = {'Name': name_ar,'Link': URL_ar,
        'email': email_ar,'title':title_ar,'org':org_ar}
  
# Create DataFrame
df = pd.DataFrame(info)
  
# Save the output.
df.to_csv('professors1.csv',mode = 'a',index = False) 
 


# In[308]:


soup2 = BeautifulSoup(r.content,'html5lib')
k = soup2.find('li', attrs={'id':'letter-u'})
link_all=k.find_all( href = True)
info = []  
name_ar = []
email_ar = []
URL_ar = []
org_ar = []
title_ar = []
for link in link_all:
  print (link.get('href'))
  URL_ar.append(link.get('href'))
    
    
  re=requests.get(link.get('href')) 
  soup = BeautifulSoup(re.content,'html5lib')
  name_all = soup.find_all('h1', attrs={'class':'name fn'})
  org_all = soup.find_all('p', attrs={'class':'organization organization-unit'})
  title_all = soup.find_all('h2', attrs={'class':'title'})
  email_all = soup.find_all('p', attrs={'class':'email'})
  
  for name in name_all:
    print(name.text)  
    name_ar.append(name.text.strip())  
   
    
  for title in title_all:
    print(title.text)    
    title_ar.append(title.text.strip())  
  
  
  for org in org_all:
    print(org.text)    
    org_ar.append(org.text.strip())  
  

    
    
  for email in email_all:
    print(email.text)
    email_ar.append(email.text.strip())  
    
info = {'Name': name_ar,'Link': URL_ar,
        'email': email_ar,'title':title_ar,'org':org_ar}
  
# Create DataFrame
df = pd.DataFrame(info)
  
# Save the output.
df.to_csv('professors1.csv',mode = 'a',index = False) 
 


# In[309]:


soup2 = BeautifulSoup(r.content,'html5lib')
k = soup2.find('li', attrs={'id':'letter-v'})
link_all=k.find_all( href = True)
info = []  
name_ar = []
email_ar = []
URL_ar = []
org_ar = []
title_ar = []
for link in link_all:
  print (link.get('href'))
  URL_ar.append(link.get('href'))
    
    
  re=requests.get(link.get('href')) 
  soup = BeautifulSoup(re.content,'html5lib')
  name_all = soup.find_all('h1', attrs={'class':'name fn'})
  org_all = soup.find_all('p', attrs={'class':'organization organization-unit'})
  title_all = soup.find_all('h2', attrs={'class':'title'})
  email_all = soup.find_all('p', attrs={'class':'email'})
  
  for name in name_all:
    print(name.text)  
    name_ar.append(name.text.strip())  
   
    
  for title in title_all:
    print(title.text)    
    title_ar.append(title.text.strip())  
  
  
  for org in org_all:
    print(org.text)    
    org_ar.append(org.text.strip())  
  

    
    
  for email in email_all:
    print(email.text)
    email_ar.append(email.text.strip())  
    
info = {'Name': name_ar,'Link': URL_ar,
        'email': email_ar,'title':title_ar,'org':org_ar}
  
# Create DataFrame
df = pd.DataFrame(info)
  
# Save the output.
df.to_csv('professors1.csv',mode = 'a',index = False) 
 


# In[310]:


soup2 = BeautifulSoup(r.content,'html5lib')
k = soup2.find('li', attrs={'id':'letter-w'})
link_all=k.find_all( href = True)
info = []  
name_ar = []
email_ar = []
URL_ar = []
org_ar = []
title_ar = []
for link in link_all:
  print (link.get('href'))
  URL_ar.append(link.get('href'))
    
    
  re=requests.get(link.get('href')) 
  soup = BeautifulSoup(re.content,'html5lib')
  name_all = soup.find_all('h1', attrs={'class':'name fn'})
  org_all = soup.find_all('p', attrs={'class':'organization organization-unit'})
  title_all = soup.find_all('h2', attrs={'class':'title'})
  email_all = soup.find_all('p', attrs={'class':'email'})
  
  for name in name_all:
    print(name.text)  
    name_ar.append(name.text.strip())  
   
    
  for title in title_all:
    print(title.text)    
    title_ar.append(title.text.strip())  
  
  
  for org in org_all:
    print(org.text)    
    org_ar.append(org.text.strip())  
  

    
    
  for email in email_all:
    print(email.text)
    email_ar.append(email.text.strip())  
    
info = {'Name': name_ar,'Link': URL_ar,
        'email': email_ar,'title':title_ar,'org':org_ar}
  
# Create DataFrame
df = pd.DataFrame(info)
  
# Save the output.
df.to_csv('professors1.csv',mode = 'a',index = False) 
 


# In[ ]:



 


# In[ ]:


soup2 = BeautifulSoup(r.content,'html5lib')
k = soup2.find('li', attrs={'id':'letter-y'})
link_all=k.find_all( href = True)
info = []  
name_ar = []
email_ar = []
URL_ar = []
org_ar = []
title_ar = []
for link in link_all:
  print (link.get('href'))
  URL_ar.append(link.get('href'))
    
    
  re=requests.get(link.get('href')) 
  soup = BeautifulSoup(re.content,'html5lib')
  name_all = soup.find_all('h1', attrs={'class':'name fn'})
  org_all = soup.find_all('p', attrs={'class':'organization organization-unit'})
  title_all = soup.find_all('h2', attrs={'class':'title'})
  email_all = soup.find_all('p', attrs={'class':'email'})
  
  for name in name_all:
    print(name.text)  
    name_ar.append(name.text.strip())  
   
    
  for title in title_all:
    print(title.text)    
    title_ar.append(title.text.strip())  
  
  
  for org in org_all:
    print(org.text)    
    org_ar.append(org.text.strip())  
  

    
    
  for email in email_all:
    print(email.text)
    email_ar.append(email.text.strip())  
    
info = {'Name': name_ar,'Link': URL_ar,
        'email': email_ar,'title':title_ar,'org':org_ar}
  
# Create DataFrame
df = pd.DataFrame(info)
  
# Save the output.
df.to_csv('professors1.csv',mode = 'a',index = False) 
 


# In[311]:


soup2 = BeautifulSoup(r.content,'html5lib')
k = soup2.find('li', attrs={'id':'letter-z'})
link_all=k.find_all( href = True)
info = []  
name_ar = []
email_ar = []
URL_ar = []
org_ar = []
title_ar = []
for link in link_all:
  print (link.get('href'))
  URL_ar.append(link.get('href'))
    
    
  re=requests.get(link.get('href')) 
  soup = BeautifulSoup(re.content,'html5lib')
  name_all = soup.find_all('h1', attrs={'class':'name fn'})
  org_all = soup.find_all('p', attrs={'class':'organization organization-unit'})
  title_all = soup.find_all('h2', attrs={'class':'title'})
  email_all = soup.find_all('p', attrs={'class':'email'})
  
  for name in name_all:
    print(name.text)  
    name_ar.append(name.text.strip())  
   
    
  for title in title_all:
    print(title.text)    
    title_ar.append(title.text.strip())  
  
  
  for org in org_all:
    print(org.text)    
    org_ar.append(org.text.strip())  
  

    
    
  for email in email_all:
    print(email.text)
    email_ar.append(email.text.strip())  
    
info = {'Name': name_ar,'Link': URL_ar,
        'email': email_ar,'title':title_ar,'org':org_ar}
  
# Create DataFrame
df = pd.DataFrame(info)
  
# Save the output.
df.to_csv('professors1.csv',mode = 'a',index = False) 
 


# In[ ]:





# In[312]:


## bar graph

import matplotlib.pyplot as plt
r=requests.get('https://web.saumag.edu/directory/depts/')
info = []
soup = BeautifulSoup(r.content,'html5lib')


depts = soup.find('ul',attrs = {'class':'department-list',})
link_all=depts.find_all('a', href = True)
l=[]
i=0
for link in link_all:
    l.append(i)
    print(l)
    print(link.get('href'))
    re=requests.get(link.get('href')) 
    soup2 = BeautifulSoup(re.content,'html5lib')
    names = soup2.find_all('span',attrs = {'class':'m-name'})
    i=0
    for x in names:
        
        print(x.text)
        i=i+1
        print(i)


# In[313]:


l.sort()
print(l)
     


# In[314]:


#from above we can say that top 10 numbers are

top_10 = [18, 20, 20, 24, 33, 33, 37, 54, 73, 109]
top_depts = ["financial_services","Academic_affairs","Maths&computers","College_of_bussiness","Physical_plant2","College_of_education","athletics","liberal_arts","College_of_science&tech","Student_affairs"]


plt.barh(top_depts, top_10, color ='red',
        )

plt.xlabel("count")
plt.ylabel("organisation")
plt.title("top ten organisations with most employees")
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




