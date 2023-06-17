from doctest import OutputChecker
import heapq
import sys
import time

###fromat (link id ,ups ,downs)

ALL_count=[]

link={}
count=1
index=0

for line in sys.stdin:
    nums={"Link_id":"","ups":0,"downs":0}
    line = line.strip()
    line=line.split("\t")
   
    
    link_id,up,down =line[0],line[1],line[2]
    up=int(up)
    down=int(down)
    
    if link_id in link:
        ind=link[link_id ]
        ALL_count[ind]["downs"]+=down
        ALL_count[ind]["ups"]+=up

    else:
        link[link_id]=index   
        nums["Link_id"]=link_id
        nums["downs"]+=down
        nums["ups"]+=up
        ALL_count.append(nums)
        index+=1

max=0
max_vote=""
downvote=""
min=0
maxlist=[0,0]
maxkeys=[-1,-1]
minlist=[0,0]

minkeys=[-1,-1]
####sorting the highest 20 subreddit 
for i in range(len(ALL_count)):
    flag1=1
    flag2=1
    data=ALL_count[i]
    for j in range(len(maxlist)):
        if data["ups"] >maxlist[j] and flag1:
            maxlist.insert(j,data["ups"])
            maxlist.pop(len(maxlist)-1)
            maxkeys.insert(j,i)
            maxkeys.pop(len(maxkeys)-1)
            flag1=0
        if data["downs"] <minlist[j] and flag2:
            minlist.insert(j,data["downs"])
            minlist.pop(len(minlist)-1)
            minkeys.insert(j,i)
            minkeys.pop(len(minkeys)-1)
        if not flag1 or not flag2:
            break



# for i in range(len(ALL_count)):
#     data=ALL_count[i]
#     if data["ups"]>max:
#         max=data["ups"]
#         max_vote=data['link_id']
#     if data["ups"]<min:
#          min=data["downs"]
#          downvote=data['link_id']
   
for i in range(len(maxkeys)):
    max_ind=maxkeys[i]
    min=minkeys[i]
    data=ALL_count[max_ind]
    print("{}\t{}".format((ALL_count[max_ind])['Link_id'],maxlist[i]))
    print("{}\t{}".format((ALL_count[min])['Link_id'],minlist[i]))

