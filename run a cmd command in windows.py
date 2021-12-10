#!/usr/bin/env python
# coding: utf-8

# In[38]:


cmd="ipconfig"
#Perform a command on windows cmd line
from subprocess import PIPE,Popen
import sys
import time 

def run(cmd):
    obj=Popen(cmd,stdout=PIPE,stderr=PIPE,shell=True)
    res,err=obj.communicate()
    if err:
        return(str(err,'utf-8'))
    else:
        return(str(res,'utf-8'))

start=time.time()
print(run(cmd))
end=time.time()
print("Execution Time: {}".format(end-start))


# In[ ]:




