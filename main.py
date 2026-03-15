from core.system_scan import get_system_info
from core.network_check import check_internet
from core.common_fixes import get_suggestions
from core.report_generator import generate_report

print("Kacperski IT Diagnostic Tool")

system = get_system_info()

network = check_internet()

tips = get_suggestions(network)

generate_report(system,network,tips)

print("Scan finished")

print("Report generated in reports folder")