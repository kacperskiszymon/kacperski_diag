import platform
import psutil
import socket
import datetime

def get_system_info():

    info = {}

    info["Computer name"] = socket.gethostname()

    info["OS"] = platform.system() + " " + platform.release()

    info["Processor"] = platform.processor()

    info["RAM"] = str(round(psutil.virtual_memory().total / (1024**3))) + " GB"

    info["Disk space"] = str(round(psutil.disk_usage('/').free / (1024**3))) + " GB free"

    info["Boot time"] = datetime.datetime.fromtimestamp(
        psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")

    return info