#!/usr/bin/env python
# coding: utf-8

# # Ex. List Comprehensions

# #### Q1.	
# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.
# 
# Hints: Consider use range(begin, end) method

# In[1]:


div = list()
[div.append(i) for i in range(2000, 3201) if i%7==0 and i%5 != 0]
#7로 나눌 때 나머지가 0이고 5로 나눌 때 나머지가 0이 아닌 i를 div list에 append
print(div)


# #### Q2.	
# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program:
# ```
# 34, 67, 55, 33, 12, 98
# ```
# Then, the output should be:
# ```
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')
# ``` 
# Hints: In case of input data being supplied to the question, it should be assumed to be a console input. tuple() method can convert list to tuple
# 

# In[5]:


numL = input().split(',')
numT = tuple(numL)
print(numL, numT, sep = '\n')


# #### Q3.	
# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j. Note: i=0,1.., X-1; j=0,1,∼Y-1.
# 
# Suppose the following inputs are given to the program:
# ```
# 3,5
# ```
# Then, the output of the program should be:
# ```
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
# ```
# Hints: Note: In case of input data being supplied to the question, it should be assumed to be a console input in a comma-separated form.

# In[6]:


num = input().split(',')
x, y = int(num[0]), int(num[1])

xy = [[i*j for i in range(y)] for j in range(x)]
print(xy)


# #### Q4.	
# Write a program that accepts a sentence and calculate the number of letters and digits.
# 
# Suppose the following input is supplied to the program:
# ```Python
# hello world! 123
# ```
# 
# Then, the output should be:
# ```Python
# LETTERS 10
# DIGITS 3
# ```
# Hints: In case of input data being supplied to the question, it should be assumed to be a console input.
# 

# In[7]:


stc = input()

sCount = [i for i in range (len(stc)) if stc[i].isalpha()]
dCount = [i for i in range (len(stc)) if stc[i].isdigit()]
print('LETTERS {}'.format(len(sCount)), 'DIGITS {}'.format(len(dCount)), sep = '\n')


# #### Q5.	
# Write a program which can filter even numbers in a list by using range() for loops and list.append(). 
# 
# The list is: 
# ```
# [1,2,3,4,5,6,7,8,9,10]
# ```
# Hint: Use range() for loops.
# Use list.append() to add values into a list.

# In[8]:


num = [1,2,3,4,5,6,7,8,9,10]
even = list()

for i in range(1, len(num)+1):
    if i%2 == 0:
        even.append(i)
print(even)


# #### Q6.	
# Write a program which can filter even numbers in a list by using list comprehension. The list is: 
# ```
# [1,2,3,4,5,6,7,8,9,10]
# ```
# Hint: Use list comprehension

# In[9]:


even = [i for i in [1,2,3,4,5,6,7,8,9,10] if i%2 == 0]
print(even)


# #### Q7.	
# With two given lists `[1,3,6,78,35,55]` and `[12,24,35,24,88,120,155]`, write a program to make a list whose elements are intersection of the above given lists.
# 
# Hints: Use `set()` and `&=` to do set intersection operation.
# 

# In[6]:


set1, set2 = set([1,3,6,78,35,55]), set([12,24,35,24,88,120,155])
set1 &= set2
print(set1)


# #### Q8.	
# Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
# 
# Suppose the following input is supplied to the program:
# ```
# hello world and practice makes perfect and hello world again
# ```
# 
# Then, the output should be:
# ```again and hello makes perfect practice world
# ```
# Hints: In case of input data being supplied to the question, it should be assumed to be a console input. We use set container to remove duplicated data automatically and then use sorted() to sort the data.

# In[11]:


words = sorted(set(input().split(' ')))
print(words)

