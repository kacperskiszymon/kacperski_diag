def get_suggestions(system,network):

    tips=[]

    if network.get("Internet")=="FAIL":

        tips.append("Check router connection")

        tips.append("Restart network adapter")

        tips.append("Run ipconfig /release and /renew")

        tips.append("Check DNS configuration")


    if "Ping latency" in network:

        try:

            latency=int(network["Ping latency"].replace(" ms",""))

            if latency>100:

                tips.append("Network latency high – check WIFI signal")

        except:
            pass


    if "CPU usage" in system:

        cpu=float(system["CPU usage"].replace(" %",""))

        if cpu>80:

            tips.append("High CPU usage – check Task Manager")


    if "RAM usage" in system:

        ram=float(system["RAM usage"].replace(" %",""))

        if ram>85:

            tips.append("High RAM usage – close unused applications")


    if "Disk free" in system:

        disk=int(system["Disk free"].replace(" GB",""))

        if disk<10:

            tips.append("Low disk space – clean temp files")


    if len(tips)==0:

        tips.append("No major issues detected")


    return tips