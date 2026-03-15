def generate_report(system, network, tips):

    file = open("reports/report.html","w")

    file.write("<h1>Kacperski Diagnostic Report</h1>")

    file.write("<h2>System info</h2>")

    for key,value in system.items():

        file.write(f"<p>{key}: {value}</p>")

    file.write("<h2>Network</h2>")

    file.write(f"<p>Status: {network}</p>")

    file.write("<h2>Suggestions</h2>")

    for tip in tips:

        file.write(f"<p>{tip}</p>")

    file.close()