def get_suggestions(network_status):

    tips = []

    if network_status == "NO CONNECTION":

        tips.append("Restart router")

        tips.append("Check ethernet cable")

        tips.append("Run ipconfig /renew")

    return tips