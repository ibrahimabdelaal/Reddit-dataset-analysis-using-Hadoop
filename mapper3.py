import json
import sys
# with open("final_sample.txt") as xh:
#     lines=xh.readlines()
# with open('upout.txt','w') as o:
for line in sys.stdin:
        
            line=json.loads(line)
            link_id=line["link_id"]
            ups=line["ups"]
            downs=line["downs"]
            print("{}\t{}\t{}".format(link_id, ups,downs))
           