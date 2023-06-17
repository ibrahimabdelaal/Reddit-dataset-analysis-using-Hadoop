###format (sub,1,link,author)
from doctest import OutputChecker
import heapq
import sys
import time
All_data=[]

suball={}
subcount={}
count=1
index=0


for line in sys.stdin:
    subreddit={"sub":"","count":0,"links":{}}
    line = line.strip()
    line=line.split("\t")
    sub,c,link=line[0],line[1],line[2]
    c=int(c)
    if sub in suball:
        
        value=suball[sub]  
        All_data[value]["count"]+=c
        if link in All_data[value]["links"]:
            (All_data[value]["links"])[link]+=1
        else:
            (All_data[value]["links"])[link]=1


    else:
        
        suball[sub]=index   
        subreddit["sub"]=sub
        subreddit["count"]=1
        subreddit["links"][link]=1
        All_data.append(subreddit)
        index+=1

for subredd in All_data:
    print("{}\t{}\t{}".format(subredd["sub"], subredd["count"],subredd["links"]))
    