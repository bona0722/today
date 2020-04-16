#!/usr/bin/env python
# coding: utf-8

# ## English Composition
# 
# 쇼핑 바구니에 쇼핑한 과일 종류별로 몇 개 있는지 묘사하는 완전한 영어 문장을 완성하여 return하는 함수 `sentence(basket)`을 작성하라. 
# 
# - 단수, 복수를 구분하여야 하고, 단수일 경우 'a'와 'an'을 영문법에 맞게 구분해야 한다. 
# - 갯수가 4개 이상이면 'many'로 표현하기로 한다.
# - 편의상, 사전식 순서를 따라 과일을 열거하기로 한다. (apple이 banana 보다 먼저)

# In[2]:


import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


# In[102]:


def sentence(basket):
    counter = {}
    plural = list()
    singular = list()
    
    for i in basket:
        if i in counter: counter[i] += 1
        else: counter[i] = 1
            
    for n in counter:
        if counter[n] == 1:
            if n[0] == 'a' or n[0] == 'e' or n[0] == 'i' or n[0] == 'o' or n[0] == 'u':
                counter[n] = 'an'
            else: counter[n] = 'a'
                
        elif counter[n] == 2: counter[n] = 'two'
        elif counter[n] == 3: counter[n] = 'three'
        else: counter[n] = 'many'
    
    for key, value in counter.items(): 
        if value == 'two' or value == 'three' or value == 'many': plural.append(key)
        else: singular.append(key)
    
    basket = sorted(plural + singular)
    
    for p in range(0,len(basket)): 
        
        if counter[basket[p]] == 'two': basket[p] = 'two '+ basket[p] +'s'
        elif counter[basket[p]] == 'three': basket[p] = 'three' + basket[p] +'s'
        elif counter[basket[p]] == 'many': basket[p] = 'many ' + basket[p] +'s'
        elif basket[p][0] == 'a' or basket[p][0] == 'e' or basket[p][0] == 'i' or basket[p][0] == 'o' or basket[p][0] == 'u' :
            basket[p] = 'an ' + basket[p]
        else: basket[p] = 'a ' + basket[p]
    
    basket[0] = 'There are ' + basket[0]
    basket[-1] = 'and ' + basket[-1] + ' in the basket.'

    basket = ', '.join(basket)
    
    return basket

    
fruits = ['orange', 'pear', 'pear', 'apple', 'orange', 'banana']
test(sentence(fruits) == 'There are an apple, a banana, two oranges, and two pears in the basket.')
many_oranges = ['apple', 'orange', 'orange', 'orange','pear', 'orange']
test(sentence(many_oranges) == 'There are an apple, many oranges, and a pear in the basket.')


# Hint:
# > - 종류 별로 count하자: dict 이용
# > - 먼저 과일들의 list를 만들자: ['an apple', 'a banana', 'two oranges', ... ]
# > - join method로 콤파를 삽입한다.
