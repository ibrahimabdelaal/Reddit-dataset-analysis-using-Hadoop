import json
import sys
for line in sys.stdin:

     line=json.loads(line)

     subred=line["subreddit_id"]
     link_id=line["link_id"]
     print("{}\t1\t{}".format(subred, link_id))
    
          
  
        



















