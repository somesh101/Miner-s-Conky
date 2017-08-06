import subprocess
import json
import datetime
out1=subprocess.check_output(["curl","https://api.cryptonator.com/api/ticker/btc-usd"])
out2=subprocess.check_output(["curl","https://api.cryptonator.com/api/ticker/zec-usd"])
out3=subprocess.check_output(["curl","https://api.cryptonator.com/api/ticker/eth-usd"])
out4=subprocess.check_output(["curl","https://api.nanopool.org/v1/zec/user/t1RL3nmwnLhBpX9n1ZrRKgZXac4Pp7aCvYB"])
out5=subprocess.check_output(["curl","http://api.fixer.io/latest?base=USD"])


out1=json.loads(out1)
out2=json.loads(out2)
out3=json.loads(out3)
out4=json.loads(out4)
out5=json.loads(out5)

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

