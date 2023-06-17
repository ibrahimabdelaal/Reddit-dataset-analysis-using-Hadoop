import json
import sys
for line in sys.stdin:

    line=json.loads(line)

    subred=line["subreddit_id"]
    author=line["author"]
    print("{}\t{}\t1".format(subred, author))
       
    