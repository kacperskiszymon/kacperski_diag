import tkinter as tk
from tkinter import messagebox
import os
import webbrowser

from core.system_scan import get_system_info
from core.network_check import check_network
from core.ticket_notes import generate_ticket
from core.report_generator import generate_report
from core.common_fixes import get_suggestions


def run_scan():

    incident=incident_entry.get()

    if incident=="":
        messagebox.showwarning("Warning","Enter incident description")
        return

    status_label.config(text="Scanning system...")

    root.update()

    system=get_system_info()

    network=check_network()

    suggestions=get_suggestions(system,network)

    ticket=generate_ticket(system,network,incident)

    generate_report(system,network,ticket,incident,suggestions)

    ticket_box.delete("1.0",tk.END)

    ticket_box.insert(tk.END,ticket)

    status_label.config(text="Scan completed")

    messagebox.showinfo("Done","Diagnostic report generated")


def copy_notes():

    root.clipboard_clear()

    root.clipboard_append(ticket_box.get("1.0",tk.END))

    messagebox.showinfo("Copied","Ticket notes copied")


def export_txt():

    file=open("reports/ticket.txt","w",encoding="utf-8")

    file.write(ticket_box.get("1.0",tk.END))

    file.close()

    messagebox.showinfo("Saved","Ticket exported")


def open_report():

    path=os.path.abspath("reports/report.html")

    webbrowser.open(path)


root=tk.Tk()

root.title("Kacperski Diagnostic Tool")

root.geometry("750x650")

root.resizable(False,False)


title=tk.Label(root,
text="Kacperski Diagnostic Tool",
font=("Segoe UI",20,"bold"))

title.pack(pady=10)


incident_label=tk.Label(root,
text="Incident description")

incident_label.pack()


incident_entry=tk.Entry(root,
width=90)

incident_entry.pack(pady=5)


button_frame=tk.Frame(root)

button_frame.pack(pady=10)


scan_button=tk.Button(button_frame,
text="Run Scan",
width=15,
command=run_scan)

scan_button.grid(row=0,column=0,padx=5)


copy_button=tk.Button(button_frame,
text="Copy Notes",
width=15,
command=copy_notes)

copy_button.grid(row=0,column=1,padx=5)


txt_button=tk.Button(button_frame,
text="Export TXT",
width=15,
command=export_txt)

txt_button.grid(row=0,column=2,padx=5)


open_button=tk.Button(button_frame,
text="Open Report",
width=15,
command=open_report)

open_button.grid(row=0,column=3,padx=5)


ticket_box=tk.Text(root,
height=25,
width=90)

ticket_box.pack(pady=10)


status_label=tk.Label(root,
text="Ready",
fg="gray")

status_label.pack()


root.mainloop()