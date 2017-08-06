#sudo cp /proc/kallsyms /boot/system.map-`uname-r`;
#sudo make install
#sudo modprobe nct6775

x=$(wc -l < file)
x=$(($x-1))
x=$(( ( RANDOM % $x )+1))
sed "${x}q;d" file | fold -sw 40
