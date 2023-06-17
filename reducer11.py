from doctest import OutputChecker
import heapq
import sys
import time
import json

###format from combiner is (subreddit,count,dictionary of links)
All_data=[]

suball={}
subcount={}
count=1
index=0
maxlist=[0]*5
maxkeys=[""]*5    ###max subreddits
max=0
sub_links={}    ##to relate each subreddit with its links

for line in sys.stdin:
    
    line = line.strip()
    line=line.split("\t")
    sub,count,link=line[0],line[1],line[2]
    count=int(count)
   
    #print(link)
    sub_links[sub]=link



    ####getting the highest 5 subreddit 
    
    for j in range(len(maxlist)):
        if count >maxlist[j]:
            maxlist.insert(j,count)
            maxlist.pop(len(maxlist)-1)
            maxkeys.insert(j,sub)
            maxkeys.pop(len(maxkeys)-1)
            break
   

for i in range(len(maxkeys)):
    max_sub=maxkeys[i]
    if max_sub!="":
        
        
        topics=(sub_links[max_sub])
        
        json_data = topics.replace("'", '"')
        topics=json.loads(json_data)
        dic2=list(dict(sorted(topics.items(),key= lambda x:x[1])))
        print("{}\t{}\t{}\t{}".format(max_sub, maxlist[i],dic2[len(dic2)-3:len(dic2)-1],[topics[dic2[len(dic2)-3]],topics[dic2[len(dic2)-2]]]))
        
