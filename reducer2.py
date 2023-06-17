from doctest import OutputChecker
import heapq
import sys
import time

rate={}
contraver={}
listlinks={}

for line in sys.stdin:
    
    line = line.strip()
    line=line.split("\t")
   
    
    parent,contra,link,count =line[0],line[1],line[2],line[3]
    count=int(count)
    if link==parent :
        ##then its comment
  
        if (not(link in listlinks)) :
          listlinks[link]=1
        if not(link in contraver):
          contraver[link]=contra
        if not(link in rate):
              rate[link]=0
        
           
        
    elif link in rate:
        rate[link]+=count
    else:
        rate[link]=1
    


for L in listlinks.keys():
    #print(L)
    print("{}\t{}\t{}".format(L,rate[L],contraver[L]))




    


     

        
    