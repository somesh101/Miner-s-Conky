#import subprocess
import json,requests
import datetime
out1=requests.get("https://api.cryptonator.com/api/ticker/btc-usd").json()
out2=requests.get("https://api.cryptonator.com/api/ticker/zec-usd").json()
out3=requests.get("https://api.cryptonator.com/api/ticker/eth-usd").json()
out4=requests.get("https://api.nanopool.org/v1/zec/user/t1RL3nmwnLhBpX9n1ZrRKgZXac4Pp7aCvYB").json()
out5=requests.get("http://api.fixer.io/latest?base=USD").json()


#out1=json.loads(out1)
#out2=json.loads(out2)
#out3=json.loads(out3)
#out4=json.loads(out4)
#out5=json.loads(out5)

res="1 USD       : INR "
res+=str(out5['rates']['INR'])+ '\n'
res+="1 BTC       : USD "
res+=out1['ticker']['price'] + '\n'
res+="1 ZEC       : USD "
res+=out2['ticker']['price'] + '\n'
res+="1 ETH       : USD "
res+=out3['ticker']['price'] + '\n'



res+="UnConfirmed : Z   "+ out4['data']['unconfirmed_balance'] + '\n'
res+="Balance     : Z   " + out4['data']['balance'] +'\n' 
res+="Hash Rate   : Sol/s " + out4['data']['hashrate']

fp=open("balance.log",'r+')

for each in fp:
    each=each.strip()

tail=each.split(',')
if(float(out4['data']['balance'])<float(tail[1])+float(tail[2])):
    fp.write("---- Flag -----")
fp.write('\n'+str(datetime.datetime.now())+','+str(out4['data']['balance'])+','+str(out4['data']['unconfirmed_balance']))
print res

