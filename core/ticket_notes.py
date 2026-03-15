def generate_ticket(system,network,incident):

    note=""

    note+="INCIDENT SUMMARY\n\n"

    note+=incident+"\n\n"

    note+="COLLECTED DATA\n\n"

    note+="SYSTEM\n"

    for k,v in system.items():

        note+=k+": "+str(v)+"\n"


    note+="\nNETWORK\n"

    for k,v in network.items():

        if k!="IPCONFIG":

            note+=k+": "+str(v)+"\n"


    note+="\nL1 ACTIONS PERFORMED\n"

    note+="Diagnostic scan executed\n"

    note+="Network test completed\n"

    note+="System data collected\n"


    note+="\nRECOMMENDED NEXT STEP\n"

    note+="Review diagnostics\n"

    note+="Escalate if required\n"


    return note