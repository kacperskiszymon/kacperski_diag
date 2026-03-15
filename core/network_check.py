import subprocess

def check_internet():

    try:

        subprocess.check_output("ping -n 1 google.com", shell=True)

        return "OK"

    except:

        return "NO CONNECTION"