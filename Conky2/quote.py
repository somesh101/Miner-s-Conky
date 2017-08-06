import feedparser
import sys
url=["http://feeds.feedburner.com/brainyquote/QUOTEFU","https://feeds.feedburner.com/brainyquote/QUOTEBR"]
f=open("file","w+")
for each in url:
    feed=feedparser.parse(each)
    for x in range(len(feed.entries)):
        f.write(feed.entries[x].description)
        f.write('\n')
f.close()
