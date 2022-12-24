#!/usr/bin/env python
# coding: utf-8

# In[8]:


pip install tensorflow


# In[9]:


pip install keras


# In[12]:


pip install Pillow


# In[29]:


pip install matplotlib


# In[2]:


import matplotlib.pyplot as plt
import PIL
from PIL import ImageTk, ImageDraw, Image
from tkinter import *
from keras.preprocessing import image
from tensorflow.keras.utils import load_img, img_to_array 
import os
import keras


# In[4]:


def create_new_image():
    width = 400
    height = 256
    center = height // 2
    white = (255, 255, 255)
    green = (0, 128, 0)
    
    def save():
        filename = 'C:/Users/mdasr/OneDrive/Desktop/Project_need/BanglaLekha-Isolated/Image_draw/image.jpg'
        image.save(filename)
        
    def paint(event):
        x1, y1 = (event.x - 1), (event.y - 1)
        x2, y2 = (event.x + 1), (event.y + 1)
        cv.create_oval(x1, y1, x2, y2, fill = 'black', width = 30)
        draw.line([x1, y1, x2, y2], fill = 'black', width = 30)
        
    root = Tk()
    root.title('GUI for Handwritten Character')
    
    cv = Canvas(root, width = width, height = height, bg = 'cyan')
    cv.pack()
    
    image = PIL.Image.new('RGB', (width, height),white)
    draw = ImageDraw.Draw(image)
    
    cv.pack(expand = YES, fill = BOTH)
    cv.bind("<B1-Motion>", paint)
    
    button = Button(text = 'Save character', command = save,bg='white',font='sans 16 bold')
    button.pack()
    
    root.mainloop()


# In[52]:


create_new_image()


# In[53]:


test_img = keras.utils.load_img('C:/Users/mdasr/OneDrive/Desktop/Project_need/BanglaLekha-Isolated/Image_draw/image.jpg', target_size = (64, 64, 3))
#test_img=keras.utils.load_img('path_to_image', target_size=(img_size, img_size))
plt.imshow(test_img)

