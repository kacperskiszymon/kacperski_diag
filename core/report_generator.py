import os
import datetime

def generate_report(system,network,ticket,incident,suggestions):

    logo_path=os.path.abspath("assets/logo.png")

    logo_path=logo_path.replace("\\","/")

    scan_time=str(datetime.datetime.now())

    file=open("reports/report.html","w",encoding="utf-8")

    file.write("""

<html>

<head>

<style>

body{
font-family:Segoe UI;
background:white;
color:black;
padding:40px;
}

.logo{
display:block;
margin:auto;
width:220px;
margin-bottom:20px;
}

.box{
border:1px solid #dcdcdc;
padding:18px;
margin:18px;
border-radius:10px;
background:#fafafa;
}

.security{
background:#e8f5e9;
padding:18px;
border-radius:10px;
margin-top:25px;
}

.meta{
color:gray;
font-size:13px;
}

</style>

</head>

<body>

""")

    file.write(f"<img src='file:///{logo_path}' class='logo'>")

    file.write("<h1>Kacperski Diagnostic Tool</h1>")

    file.write("<h2>L1 Support Report</h2>")

    file.write(f"<div class='meta'>Scan time: {scan_time}</div>")


    file.write("<div class='box'>")

    file.write("<h3>Incident Description</h3>")

    file.write(f"<p>{incident}</p>")

    file.write("</div>")


    file.write("<div class='box'>")

    file.write("<h3>System Information</h3>")

    for k,v in system.items():

        file.write(f"<p><b>{k}</b>: {v}</p>")

    file.write("</div>")


    file.write("<div class='box'>")

    file.write("<h3>Network Information</h3>")

    for k,v in network.items():

        if k!="IPCONFIG":

            file.write(f"<p><b>{k}</b>: {v}</p>")

    file.write("</div>")


    file.write("<div class='box'>")

    file.write("<h3>Recommended L1 Actions</h3>")

    for tip in suggestions:

        file.write(f"<p>{tip}</p>")

    file.write("</div>")


    file.write("<div class='box'>")

    file.write("<h3>L1 Ticket Notes</h3>")

    file.write("<pre>"+ticket+"</pre>")

    file.write("</div>")


    file.write("""

<div class='security'>

<h3>Security Information</h3>

<p>Read only diagnostic tool.</p>

<p>No files modified.</p>

<p>No external connections except diagnostics.</p>

<p>Safe for enterprise troubleshooting.</p>

</div>

""")

    file.write("</body></html>")

    file.close()