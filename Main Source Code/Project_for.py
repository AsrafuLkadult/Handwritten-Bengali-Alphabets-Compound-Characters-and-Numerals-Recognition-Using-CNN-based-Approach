#!/usr/bin/env python
# coding: utf-8

# In[1]:


from zipfile import ZipFile

file_name = "C:/Users/mdasr/OneDrive/Desktop/image/Ekush_dataset_Balanced.zip"

with ZipFile(file_name, 'r') as zip:
  zip.extractall()
  print("Successfully Unziped ")



# In[6]:


import os 
import warnings
warnings.filterwarnings('ignore')
# Get all the paths
data_dir_list = os.listdir('C:/Users/mdasr/OneDrive/Desktop/image/Ekush_dataset_Balanced/Validation')
data_dir_list.sort()
print(data_dir_list)
path, dirs, files = next(os.walk("C:/Users/mdasr/OneDrive/Desktop/image/Ekush_dataset_Balanced/Validation"))


# In[ ]:


import matplotlib.pyplot as plt
nimgs = {}
maximum =0
minimum=1e9
for i in data_dir_list:
    nimages = len(os.listdir('C:/Users/mdasr/OneDrive/Desktop/image/Ekush_dataset_Balanced/Validation/'+i+'/'))
    nimgs[i]=nimages
    maximum=max(maximum,nimages)
    minimum=min(minimum,nimages)
    print(f"{i} classes number of images :{nimages}\n")
print(f"Maximum value of particular class: {maximum}")
print(f"Minimum value of particular class: {minimum}")
plt.figure(figsize=(84, 5))
plt.bar(range(len(nimgs)), list(nimgs.values()),align ="center")
plt.xticks(range(len(nimgs)), list(nimgs.keys()))
plt.title('Distribution of different classes in Training Dataset')
plt.show()


# In[13]:


pip install split-folders


# In[16]:


pip install split-folders[full]


# In[18]:


#import splitfolders

#Train, val, test
# Split val/test with a fixed number of items, e.g. `(100, 100)`, for each set.
# To only split into training and validation set, use a single number to `fixed`, i.e., `10`.
# Set 3 values, e.g. `(300, 100, 100)`, to limit the number of training values.
#splitfolders.fixed("C:/Users/mdasr/OneDrive/Desktop/image/raw_image/male/male/", output="C:/Users/mdasr/OneDrive/Desktop/image/Ekush_dataset_Balanced",
    #seed=1337, fixed=(2100,450,450), oversample=False, group_prefix=None, move=False) # default values


# In[19]:


import matplotlib.pyplot as plt
nimgs = {}
maximum =0
minimum=1e9
for i in data_dir_list:
    nimages = len(os.listdir('C:/Users/mdasr/OneDrive/Desktop/image/Ekush_dataset_Balanced/train/'+i+'/'))
    nimgs[i]=nimages
    maximum=max(maximum,nimages)
    minimum=min(minimum,nimages)
    print(f"{i} classes number of images :{nimages}\n")
print(f"Maximum value of particular class: {maximum}")
print(f"Minimum value of particular class: {minimum}")
plt.figure(figsize=(84, 5))
plt.bar(range(len(nimgs)), list(nimgs.values()),align ="center")
plt.xticks(range(len(nimgs)), list(nimgs.keys()))
plt.title('Distribution of different classes in Training Dataset')
plt.show()


# In[21]:


import matplotlib.pyplot as plt
nimgs = {}
maximum =0
minimum=1e9
for i in data_dir_list:
    nimages = len(os.listdir('C:/Users/mdasr/OneDrive/Desktop/image/Ekush_dataset_Balanced/test/'+i+'/'))
    nimgs[i]=nimages
    maximum=max(maximum,nimages)
    minimum=min(minimum,nimages)
    print(f"{i} classes number of images :{nimages}\n")
print(f"Maximum value of particular class: {maximum}")
print(f"Minimum value of particular class: {minimum}")
plt.figure(figsize=(84, 5))
plt.bar(range(len(nimgs)), list(nimgs.values()),align ="center")
plt.xticks(range(len(nimgs)), list(nimgs.keys()))
plt.title('Distribution of different classes in Training Dataset')
plt.show()


# In[20]:


import matplotlib.pyplot as plt
nimgs = {}
maximum =0
minimum=1e9
for i in data_dir_list:
    nimages = len(os.listdir('C:/Users/mdasr/OneDrive/Desktop/image/Ekush_dataset_Balanced/val/'+i+'/'))
    nimgs[i]=nimages
    maximum=max(maximum,nimages)
    minimum=min(minimum,nimages)
    print(f"{i} classes number of images :{nimages}\n")
print(f"Maximum value of particular class: {maximum}")
print(f"Minimum value of particular class: {minimum}")
plt.figure(figsize=(84, 5))
plt.bar(range(len(nimgs)), list(nimgs.values()),align ="center")
plt.xticks(range(len(nimgs)), list(nimgs.keys()))
plt.title('Distribution of different classes in Training Dataset')
plt.show()

