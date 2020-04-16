#!/usr/bin/env python
# coding: utf-8

# # Exercise. my range function
# Unit test를 위해 `test` function이 다음과 같이 주어져 있고, 각 문제마다 적어도 제공된 test case들을 통과해야 한다.

# In[9]:


import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


# Q1. list를 return하는 `lrange1()` function을 작성하고 시험하라.

# In[7]:


def lrange1(start, stop, step):
    if step == 0:   # Cause ValueError exception
        raise ValueError('step must be non-zero') 
    return [i for i in range(start, stop, step)]
        
    
print(lrange1(0, 4, 1))
test(lrange1(-1, 7, 2) == [-1, 1, 3, 5])
test(lrange1(10, 1, -2) == [10, 8, 6, 4, 2])


# Q2. list를 return하되, 다만, 다음과 같은 형식으로 argument를 받을 수 있는 함수 lrange(start, stop, step)를 작성하라.
# - lrange(start, stop): 3번째 argument가 생략되면 step=1
# - lrange(stop): 2번째 3번째 argument가 생략되면, start=0, step=1
#   - Hint: parameter stop이 생략되면 `None`이 되게 해보자.

# In[27]:


def lrange(start = None, stop = None , step = None):
    if stop is None and step is None:
        stop = start
        start = 0
        step = 1
    elif step is None and stop is not None:
        step = 1
        
    return [i for i in range(start, stop, step)]

    
print(lrange(4))
test(lrange(4) == [0, 1, 2, 3])
test(sum(i for i in lrange(1, 11)) == 55)
test(lrange(-1, 7, 2) == list(range(-1, 7, 2)))
test(lrange(10, 1, -2) == list(range(10, 1, -2)))


# Q3. Q2와 동일하지만 generator로 구현한 `xrange()`  함수를 작성하라.

# In[32]:


def xrange(start = None, stop = None , step = None):
    if stop is None and step is None:
        stop = start
        start = 0
        step = 1
    elif step is None and stop is not None:
        step = 1
    
    for i in range(start, stop, step):
        yield i

print(xrange(4))
test(list(xrange(4)) == [0, 1, 2, 3])
test(list(xrange(4)) == list(range(4)))
test(sum(i for i in xrange(1, 11)) == 55)
test(list(xrange(-1, 7, 2)) == list(range(-1, 7, 2)))
test(list(xrange(10, 1, -2)) == list(range(10, 1, -2)))

