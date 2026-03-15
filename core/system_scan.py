import platform
import psutil
import socket
import getpass

def get_system_info():

    info={}

    info["Computer name"]=socket.gethostname()

    info["Logged user"]=getpass.getuser()

    info["OS"]=platform.system()+" "+platform.release()

    info["OS version"]=platform.version()

    info["Processor"]=platform.processor()

    info["RAM"]=str(round(psutil.virtual_memory().total/(1024**3)))+" GB"

    info["RAM usage"]=str(psutil.virtual_memory().percent)+" %"

    info["Disk free"]=str(round(psutil.disk_usage('/').free/(1024**3)))+" GB"

    info["CPU usage"]=str(psutil.cpu_percent(interval=1))+" %"

    info["Processes"]=str(len(psutil.pids()))

    return info