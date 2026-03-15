import subprocess
import socket
import re

def check_network():

    data={}

    hostname=socket.gethostname()

    data["Hostname"]=hostname

    try:

        ip=socket.gethostbyname(hostname)

        data["Local IP"]=ip

    except:

        data["Local IP"]="unknown"


    try:

        ping=subprocess.check_output(
            "ping -n 1 google.com",
            shell=True
        ).decode()

        latency=re.search(r'time=(\d+)',ping)

        if latency:

            data["Ping latency"]=latency.group(1)+" ms"

        else:

            data["Ping latency"]="unknown"

        data["Internet"]="OK"

    except:

        data["Internet"]="FAIL"


    ipconfig=subprocess.check_output(
        "ipconfig /all",
        shell=True
    ).decode(errors="ignore")


    gateway=re.search(r'Default Gateway[ .:]*([\d\.]+)',ipconfig)

    if gateway:

        data["Default Gateway"]=gateway.group(1)


    dns=re.findall(r'DNS Servers[ .:]*([\d\.]+)',ipconfig)

    if dns:

        data["DNS"]=dns[0]


    mac=re.search(r'Physical Address[ .:]*([A-F0-9\-]+)',ipconfig)

    if mac:

        data["MAC Address"]=mac.group(1)


    data["IPCONFIG"]=ipconfig


    return data