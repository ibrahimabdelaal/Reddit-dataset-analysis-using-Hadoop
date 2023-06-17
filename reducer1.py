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
     
maxlist=[0,0,0,0,0]
maxkeys=[-1,-1,-1,-1,-1]
max=0
####sorting the highest 20 subreddit 
for i in range(len(All_data)):
    data=All_data[i]
    for j in range(len(maxlist)):
        if data["count"] >maxlist[j]:
            maxlist.insert(j,data["count"])
            maxlist.pop(len(maxlist)-1)
            maxkeys.insert(j,i)
            maxkeys.pop(len(maxkeys)-1)
            break
            

 
    

#####Choosing the first #10 discussed subreddit 
t=[]
d=0
for i in range(len(maxkeys)):
    ind=maxkeys[i]
    if ind!=-1:
        data=All_data[ind]
        topics=data["links"]
        dic2=list(dict(sorted(topics.items(),key= lambda x:x[1])))
        #print(dic2)
        
        print("{}\t{}\t{}\t{}".format(data["sub"], int(data["count"]),dic2[len(dic2)-3:len(dic2)-1],[topics[dic2[len(dic2)-3]],topics[dic2[len(dic2)-2]]]))
        
    
    


####Refere to this link to be aple to pull first (highest )N record from the output without code
    #https://stackoverflow.com/questions/20583211/top-n-values-by-hadoop-map-reduce-code
    ##So I think with cat command we can put the first max 15 reddit directly to some file to next stage

