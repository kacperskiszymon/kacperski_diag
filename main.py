from core.system_scan import get_system_info
from core.network_check import check_network
from core.ticket_notes import generate_ticket
from core.report_generator import generate_report
from core.common_fixes import get_suggestions
from gui.interface import *

print("Kacperski Diagnostic Tool")

incident=input("Describe user problem: ")

system=get_system_info()

network=check_network()

suggestions=get_suggestions(system,network)

ticket=generate_ticket(system,network,incident)

generate_report(system,network,ticket,incident,suggestions)

print("Report ready")