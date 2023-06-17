import json
import sys

for line in sys.stdin:
        
        line=json.loads(line)
        parent_id=line["parent_id"]
        contra=line["score"]
        link=line["link_id"]
        print("{}\t{}\t{}\t1".format(parent_id,contra,link))
        
        