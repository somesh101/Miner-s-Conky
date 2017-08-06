import subprocess

fin=open("mac")
tac={}
for each in fin:
    each=each.strip('\n')
    x=each.split(" ")
    tac[x[0]]=x[1]
#print tac
#print(tac)

r = subprocess.check_output(["arp", "-na"])
r=str(r).split('?')
#print(r)
#print(len(r))
out=" "
for each in r:
    #print(each)
    each=each.split(" ")
    #print(each[3])
    try:
        if each[3] in tac:
            out+=tac[each[3]]+"\n "
        elif(each[3]=="<incomplete>"):
            continue    
        else : out+=each[3]+"\n "
    except:
        { }
print(out)
fin.close()
