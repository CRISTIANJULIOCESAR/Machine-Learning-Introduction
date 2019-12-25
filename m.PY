#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.datasets import  load_iris
iris = load_iris()

print(iris)


# In[2]:


"""
en si el listado de iris es un diccionario

keys y elemento

el elemento en este caso es un arreglo de listas de listas 
o sea un numpy array 
"""


# In[3]:


iris["target_names"]


# In[4]:


iris["feature_names"]


# In[5]:


type(iris)


# In[6]:


type(iris["data"])


# In[7]:


iris["data"]


# In[8]:


iris["data"].shape


# In[9]:


#un total de 150 flores o muestras
#con 4 features


# In[10]:


type(iris["target"])


# In[69]:


iris["target"]

type (iris["target"])


# In[12]:


"""
target means flower species
0 setosa
1 versicolor
2 virginica

"""


# # Training and testing data

# The part of the data is used to build our machine learning model, and is called the training data or trainning set. 
# 
# The rest of the data will be used to access how well the model works and is called test data, test set or hold-out set.
# 
# Scikit-learn contains a functaion that shuffles the dataset and splits it for you, the function:
# 
# train_test_split 
# 
# 
# 

# In[13]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(iris["data"],iris["target"]
                                                   , random_state = 0)


# In[35]:


X_train.shape
#see the number of instances and attributes  of Train data 
X_train


# In[153]:


X_test.shape
#see the number of instances and attributes  of Test data

print(y_train)
print()
y_train


# In[164]:


import matplotlib.pyplot as plt

fig, ax = plt.subplots(3, 3, figsize=(15,15))
plt.suptitle("iris_pairplot")

for j in range(3):
    for i in range(3):
    
        print("i=",i,"j=",j,"i +1=",i+1)
        ax[i, j].scatter(X_train[:,j], X_train[:, i +1 ], c=y_train, s=70)
        
        print("------------------------------------------------------------------------------------------------")
        print("X_train[:,j] =",X_train[:,j])
        print()
        print("X_train[:, i +1 ]=",X_train[:, i +1 ])
        print("------------------------------------------------------------------------------------------------")
        ax[i, j].set_xticks(())
        ax[i, j].set_yticks(())
        if i == 2:
            ax[i, j].set_xlabel(iris["feature_names"][j])
        if j == 0:
            ax[i, j].set_ylabel(iris["feature_names"][i +1])
        if j > i:
            ax[i, j].set_visible(False)
    
    
print(y_train)


# As you can see, without using a Machine Learning algorithm  you determined that there are certain ways to determine if your data can be classified for example plotting the data first, you can that there are attributes that reflect very well iris' classifications 

# matplotlib.pyplot.subplots
# 
# matplotlib.pyplot.subplots(nrows=1, ncols=1, sharex=False, sharey=False, squeeze=True, subplot_kw=None, gridspec_kw=None, **fig_kw)
# 

# In[152]:


y_train


# In[170]:


y_train.size


# In[171]:


X_train.size


# In[38]:


X_test


# In[52]:


{x= 0
for i in range(3):
    print("a")
    for j in range(3):
        print (i, j)
        x = x +1


# In[186]:


lol = np.array([[2,3,5,560] , [266,56,14,23], [22,35,14, 2],[2,33,18,56]])
print(lol)
maria = np.array([1, 2, 2, 0])
feature = np.array(["john", "luis", "2", "0"])


# In[187]:


import matplotlib.pyplot as plt

fig, ax = plt.subplots(3, 3, figsize=(15,15))
plt.suptitle("prueba")

for j in range(3):
    for i in range(3):
        ax[i, j].scatter(lol[:,j], lol[:, i +1 ], c=maria , s=70)
        print("i=",i,"j=",j,"  i+1=",i+1)
        print(lol[:,j])
        print(lol[:, i +1 ])
        print(".....")
        ax[i, j].set_xticks(())
        ax[i, j].set_yticks(())
        if i == 2:
            ax[i, j].set_xlabel(feature[j])
        if j == 0:
            ax[i, j].set_ylabel(feature[i +1])
        if j > i:
            ax[i, j].set_visible(False) 
        


# In[ ]:





# In[ ]:


