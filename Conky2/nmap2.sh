declare -A mac=(["4c:cc:6a:f9:ee:75"]="Somesh-Pc" ["e0:98:61:48:6e:2e"]="MotoG4plus" ["90:e7:c4:ab:42:8c"]="htc" ["90:48:9a:5b:da:f5"]="Shalupc" ["18:26:66:7a:2f:b5"]="Anshu" ["bc:d1:1f:5f:9b:98"]="Papaji" ["54:27:58:1e:c6:31"]="Vicky" ["d0:b3:3f:e3:b9:d8"]="Babita" ["54:b8:0a:0a:0a:3e"]="Router" ["78:02:f8:c7:a5:b3"]="Dimpu" ["50:8f:4c:95:92:25"]="Sonu" ["90:e7:c4:ab:42:8c"]="Bittu" ["04:c2:3e:a1:37:29"]="Papal" ["ec:88:92:a8:14:b4"]="Kirti" ["64:db:43:a7:e5:3b"]="Guddi")
list=$(arp -na)
IFS=$'\n'
for item in $list;
do 
    #echo $item
    user=$(awk '{split($0,a," ");print a[4];}'<<<$item)
    if [[ -v "${mac[$user]}" ]]; then
        echo "${mac[$user]}"   
    else echo "$user" 
    fi
done
