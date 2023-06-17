from doctest import OutputChecker
import heapq
import sys
import time
All_data=[]

suball={}
#authors={}
count=1
index=0
for line in sys.stdin:
    subreddit={"sub":"","author":{}}
    line = line.strip()
    line=line.split("\t")
    sub,auth,c=line[0],line[1],line[2]
    c=int(c)
    if sub in suball:
        
        value=suball[sub]  
        #print(All_data[value])
        if auth in All_data[value]["author"]:
           All_data[value]["author"][auth]+=1
        else:
            All_data[value]["author"][auth]=1
           

    else:
        suball[sub]=index 
        subreddit["sub"]=sub
        subreddit["author"][auth]=1
        All_data.append(subreddit)
        index+=1

maxlist=[0,0,0,0,0]
maxkeys=[-1,-1,-1,-1,-1]
max=0
####getting max 3 authors foreach subreddit
for i in range(len(All_data)):
    data=All_data[i]
    authors=data["author"]
    for k in authors.keys():
        for j in range(len(maxlist)):
            if authors[k] >maxlist[j]:
                maxlist.insert(j,authors[k])
                maxlist.pop(len(maxlist)-1)
                maxkeys.insert(j,(i,k))
                maxkeys.pop(len(maxkeys)-1)
                break
print("{}\t{}\t{}".format("subreddit", "max author" ,"value"))            
for i in range(len(maxkeys)):
    ind,auth=maxkeys[i]
    if ind!=-1:
        data=All_data[ind]
        author=data["author"]
        
        print("{}\t{}\t{}".format(data["sub"], auth ,author[auth]))
        
    
    