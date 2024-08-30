#!/usr/bin/sh
IP1=`curl -s http://checkip.amazonaws.com`
IP2=`hostname -I | awk '{print $1}'`
echo "Updating $IP1 in settings file"
sed -i 's/ipPUB/'".iksaan.com\",\"$IP1"'/' elearning/settings.py
echo "Updating $IP2 in settings file"
sed -i 's/ipPRI/'"*.iksaan.com\",\"$IP2"'/' elearning/settings.py
