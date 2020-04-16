#!/usr/bin/env python
# coding: utf-8

# ## Word Frequency
# 임의의 text file에 있는 word들의 빈도수를 구하려 한다. word는 대소문자 구분없고 숫자, 특수 문자들은 단어에서 배제된다.
# 따라서, word들의 list를 만들기 전에 file을 읽고 난 후
# - 대문자는 소문자로 변환
# - 숫자, 특수문자는 `' '` 로 변환해야 할 것이다.
# 
# #### Hint:
# 주어진 text를 한 번 scan으로 효율적으로 변환해 주는 string method를 사용하면 될 것이다.
# `maketrans` method는 변환시키는 dictionany를 정의해 주고, `translate` method는 이를 가지고 변환한 새로운 string을 generate한다.

# In[1]:


the_text = '"Well, I never!", said Alice.'
my_substitutions = the_text.maketrans(
  # If you find any of these
  "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&()*+,-./:;<=>?@[]^_`{|}~'\\",
  # Replace them by these
  "abcdefghijklmnopqrstuvwxyz                                          ")

# Translate the text now.
cleaned_text = the_text.translate(my_substitutions)
print(cleaned_text)


# #### Input: 
# 인터넷에 있는 *Alice in Wonderland* 동화책 내용을 다음과 같이 fetch한다.

# In[2]:


import urllib

url = "http://openbookproject.net/thinkcs/python/english3e/_downloads/alice_in_wonderland.txt" 
with urllib.request.urlopen(url) as f:
    contents = f.read().decode()
    
my_substitutions = contents.maketrans(
  # If you find any of these
  "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&()*+,-./:;<=>?@[]^_`{|}~'\\",
  # Replace them by these
  "abcdefghijklmnopqrstuvwxyz                                          ")

# Translate the text now.
contents = contents.translate(my_substitutions)

#Q3 파일
child = "http://openbookproject.net/thinkcs/python/english3e/_downloads/vocab.txt" 
with urllib.request.urlopen(child) as f:
    easyWords = f.read().decode()
    
easyW = easyWords.maketrans(
  # If you find any of these
  "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&()*+,-./:;<=>?@[]^_`{|}~'\\",
  # Replace them by these
  "abcdefghijklmnopqrstuvwxyz                                          ")

# Translate the text now.
easyWords = easyWords.translate(easyW)

contents = contents.split()
easyWords = easyWords.split()
words = {}
level = list()

i = 0
num=len(contents)

while i < num:
    if contents[i] == 's':
        contents[i-1] += "'s"
        del contents[i]
        num -= 1
    elif contents[i] == 't':
        contents[i-1] += "'t"
        del contents[i]
        num -= 1
    elif contents[i] == 're':
        contents[i-1] += "'re"
        del contents[i]
        num -= 1
    elif contents[i] == 'd':
        contents[i-1] += "'d"
        del contents[i]
        num -= 1
    elif contents[i] == 'm':
        contents[i-1] += "'m"
        del contents[i]
        num -= 1
    elif contents[i] == 've':
        contents[i-1] += "'ve"
        del contents[i]
        num -= 1
    i += 1
    
for j in contents:
    if j in words: words[j] += 1
    else: words[j] = 1
     
print(len(words)) #Q1 답

#Q2답
q2 = sorted(words.items(), key = (lambda x:x[1]), reverse = True)
for i in range(0,20):
    print(q2[i]) 

#Q3답
for key in words:
    if not key in easyWords:
        if not "'s" in key:
            level.append(key)
print(level)


# #### Q1. How many different words are used in the *Alice in Wonderland*?

# In[ ]:


2620


# #### Q2. List top 20 frequently used words and their frequencies in the *Alice in Wonderland*.

# In[ ]:


('the', 1642)
('and', 871)
('to', 729)
('a', 631)
('she', 544)
('it', 538)
('of', 514)
('said', 462)
('i', 441)
('alice', 386)
('you', 371)
('in', 369)
('was', 357)
('that', 281)
('as', 263)
('her', 248)
('at', 212)
('on', 193)
('all', 182)
('with', 180)


# #### Q3. 
# As children learn to read, there are expectations that their vocabulary will grow. So a child of age 14 is expected to know more words than a child of age 8. When prescribing reading books for a grade, an important question might be “which words in this book are not in the expected vocabulary at this level?”
# 
# Find the words in the book *Alice in the Wonderland* are not in the vocabulary given in the file  http://openbookproject.net/thinkcs/python/english3e/_downloads/vocab.txt.
# 
# (어린이가 수준 이상이 되는 단어들을 찾아내는 문제다. 적절한 수준의 단어들로 채워진 단어장에 없으면 적정 수준을 초과한 어려운 단어라는 의미다.)

# 참고사항)
# is 와 are가 다른 단어 인거 처럼 daisy와 daisies도 다른 단어로 취급하겠습니다. 단수,복수 구분해주세요 
# 
# "'s" 는 예외가 많습니다. (it has/ it is/ 소유격)
# - 따라서, it's 를 그냥 새로운 한 단어로 생각해서 풀어주세요.
# 가령 girls' 라고 하면 이것도 새로운 한 단어라고 생각해주세요.
# - Alice랑 Alice's 각각 새로운 한단어라고 생각하시면 됩니다. 만약, there's 와 there is 가 나왔으면 전자는 1단어 후자는 2단어 입니다.
