from random import randint

try:
    f=open('file','r')
    #number of characters in one line
    width=38

    feed=f.read().split('\n')
    f.close()

    feed=[each for each in feed if len(each)>5]
    r=randint(0,len(feed)-1)


    feed=feed[r]
    author=feed.split('-')[0]
    feed=feed.split("-")[1].split(" ")#[:width]
    x=0
    res=str()
    temp=str()
    #aligning text
    for each in feed:
        if len(each)+x>=width:#feed[width+1]!=' ':
            temp= " "*int(((width-x)/2))+temp[:-1]+'\n'       
            res+=temp
            temp=each+" "
            x=len(each)+1
        else :
            temp+=each+" "
            x+=len(each)+1
            
    if x<width:
        temp= " "*int(((width-x)/2))+temp[:-1]
        res+=temp+'\n'
    res+= " "*int(((width-len(author))/2))+'- '+author
    print(res)
except:
    print("failed to execute the script")
