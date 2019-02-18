import os
from tkinter import scrolledtext, ttk
from tkinter import *
from datetime import datetime
from config import ReportStatsLocation, ReportARPLocation, ReportRoutingLocation, ReportDeviceLocation, ReportDiagLocation


def raise_frame(frame):
    frame.tkraise()

window = Tk()
window.title("Network Management TNP")
window.geometry('800x400')

f1 = Frame(window)
f2 = Frame(window)
f3 = Frame(window)
f4 = Frame(window)
f5 = Frame(window)

DNow = datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def pathping():
    txt5.insert(INSERT, "Warning PathPing Takes Some Time to Produce Results!!" + "\n")
    pathaddress = e2.get()
    f = os.popen('pathping ' + str(pathaddress))
    for line in f:
        line = line.strip()
        if line:
            txt5.insert("end", line + "\n")
        txt5.bind("<Return>", pathping)
    f.close()


def traceroute():
    txt5.insert(INSERT, "Warning Trace Route Takes Some Time to Produce Results!!" + "\n")
    traceaddress = e1.get()
    f = os.popen('tracert ' + str(traceaddress))
    for line in f:
        line = line.strip()
        if line:
            txt5.insert("end", line + "\n")
        txt5.bind("<Return>", traceroute)
    f.close()


def nslookup():
    dnsaddress = e3.get()
    f = os.popen('tracert ' + str(dnsaddress))
    for line in f:
        line = line.strip()
        if line:
            txt5.insert("end", line + "\n")
        txt5.bind("<Return>", traceroute)
    f.close()


def wirelessinfo():
    f = os.popen('netsh wlan show interfaces')
    for line in f:
        line = line.strip()
        if line:
            txt4.insert("end", line + "\n")
        txt4.bind("<Return>", wirelessinfo)
    f.close()


def deviceinfo():
    f = os.popen('systeminfo')
    for line in f:
        line = line.strip()
        if line:
            txt4.insert("end", line + "\n")
        txt4.bind("<Return>", deviceinfo)
    f.close()


def routingtable():
    f = os.popen('route print -4')
    for line in f:
        line = line.strip()
        if line:
            txt3.insert("end", line + "\n")
        txt3.bind("<Return>", routingtable)
    f.close()


def ifconfig():
    f = os.popen('ipconfig /all')
    for line in f:
        line = line.strip()
        if line:
            txt1.insert("end", line + "\n")
        txt1.bind("<Return>", ifconfig)
    f.close()


def ipscan():
    network = e4.get()
    rangefrom = e5.get()
    rangeto = e6.get()
    f = os.popen('FOR /L %i IN ('+rangefrom+',1,'+rangeto+') DO ping -n 1 ' + network + '%i | FIND "TTL="')
    for line in f:
        line = line.strip('(venv) C:/Users/niall\Documents\College\Scripting/Networkscanner>ping -n 1 192.168.0.1   | FIND "TTL="')
        if line:
            txt1.insert("end", line + "\n")
        txt1.bind("<Return>", ifconfig)
    f.close()


def netscanner():
    f = os.popen('arp -a')
    for line in f:
        line = line.strip()
        if line:
            txt2.insert("end", line + "\n")
        txt2.bind("<Return>", netscanner)
    f.close()



def printnetstat():
    Stats = txt1.get("1.0", "end-1c")
    f = open(ReportStatsLocation, "w+")
    f.write("Print Out of Your Network Status on: " + DNow + "\n" + "\n" + Stats)
    f.close()
    clearbtn()
    txt1.insert(INSERT, "Your Network Information has been Writen to File NetStats.txt" + "\n" + "Located: " + ReportStatsLocation)


def printrouting():
    Routes = txt3.get("1.0", "end-1c")
    f = open(ReportRoutingLocation, "w+")
    f.write("Print Out of Your Routing info on: " + DNow + "\n" + "\n" + Routes)
    f.close()
    clearbtn()
    txt3.insert(INSERT, "Your Network Information has been Writen" + "\n" + "  to File Routing.txt" + "\n" + "Located: " + ReportRoutingLocation)


def printarp():
    ARP = txt2.get("1.0", "end-1c")
    f = open("./ARPDetail.txt", "w+")
    f.write("Print Out of Your ARP Information on: " + DNow + "\n" + "\n" + ARP)
    f.close()
    clearbtn()
    txt2.insert(INSERT, "Your Network Information has been Writen" + "\n" + " to File ARPDetails.txt" + "\n" + "Located: " + ReportARPLocation)


def printdiag():
    Diag = txt5.get("1.0", "end-1c")
    f = open("./Diag.txt", "w+")
    f.write("Print Out of Your Diagnositic Trace Route & Path Ping Information in: " + DNow + "\n" + "\n" + Diag)
    f.close()
    clearbtn()
    txt5.insert(INSERT, "Your Network Information has been Writen" + "\n" + "  to File Diag.txt" + "\n" + "Located: " + ReportDiagLocation)

def printdevice():
    device = txt4.get("1.0", "end-1c")
    f = open("./DeviceInfo.txt", "w+")
    f.write("PrintOut of Your Device Information on: " + DNow + "\n" + "\n" + device)
    f.close()
    clearbtn()
    txt4.insert(INSERT, "Your Network Information has been Writen" + "\n" + "  to File DeviceInfo.txt" + "\n" + "Located: " + ReportDeviceLocation)


def routeprint():
    f = os.popen('route print')
    for line in f:
        line = line.strip()
        if line:
            txt3.insert("end", line + "\n")
        txt3.bind("<Return>", routeprint)
    f.close()


def deletearp():
    f = os.popen('arp -d -a')
    for line in f:
        line = line.strip()
        if line:
            txt2.insert("end", line + "\n")
        txt2.bind("<Return>", deletearp)
    f.close()


def clearbtn():
    txt1.delete(1.0, END)
    txt2.delete(1.0, END)
    txt3.delete(1.0, END)
    txt4.delete(1.0, END)
    txt5.delete(1.0, END)



def netstatus():
    f = os.popen('netstat -n')
    for line in f:
        line = line.strip()
        if line:
            txt1.insert("end", line + "\n")
        txt1.bind("<Return>", netstatus)
    f.close()


for frame in (f1, f2, f3, f4, f5):
    frame.place(width=800, height=400)


pgBar = ttk.Progressbar(f1, orient=HORIZONTAL, length=300, mode="determinate")
pgBar.place(x=250, y=75)
txt1 = scrolledtext.ScrolledText(f1, width=80, height=10)
txt1.place(x=400, y=180, anchor=CENTER)
Button(f1, text='ARP Scanner', font=("Arial", 10), command=lambda:raise_frame(f2)).place(x=332, y=2)
Button(f1, text='Routing Tables', font=("Arial", 10), command=lambda:raise_frame(f3)).place(x=116, y=2)
Button(f1, text='Device Information', font=("Arial", 10), command=lambda:raise_frame(f4)).place(x=214, y=2)
Button(f1, text='Network Status', font=("Arial Bold", 10), command=lambda:raise_frame(f1)).place(x=10, y=2)
Button(f1, text='Network Diagnostics', font=("Arial", 10), command=lambda:raise_frame(f5)).place(x=423, y=2)
Label(f1, text="IP & Net-Status", font=("Arial Bold", 25)).place(relx=0.5, rely=0.13, anchor=CENTER)
btnStart = Button(f1, text="Get Status", font=("Arial Bold", 12), bg="Green", fg="black", command=netstatus)
btnStart.place(x=115, y=70, anchor=CENTER)
btnIP = Button(f1, text="IP Details", font=("Arial Bold", 14), bg="Green", fg="black", command=ifconfig)
btnIP.place(x=300, y=360, anchor=CENTER)
Label(f1, text="Enter the Network Your Wist to Scan:", font=("Arial", 11)).place(x=390, y=280, anchor=CENTER)
btnScan = Button(f1, text="Scan All IPs", font=("Arial Bold", 14), bg="Green", fg="black", command=ipscan)
btnScan.place(x=440, y=360, anchor=CENTER)
btnPrint = Button(f1, text="Print", font=("Arial Bold", 14), bg="Blue", fg="black", command=printnetstat)
btnPrint.place(x=690, y=70, anchor=CENTER)
btnClear = Button(f1, text="Clear", font=("Arial Bold", 12), bg="Red", fg="black", command=clearbtn)
btnClear.place(x=690, y=310, anchor=CENTER)
btnBack = Button(f1, text="Back", font=("Arial Bold", 12), bg="Red", fg="black", command=netstatus)
btnBack.place(x=690, y=350, anchor=CENTER)
e4 = Entry(f1, width=30)
e4.insert(0, 'Eg: 192.168.0.')
e4.place(x=295, y=290)
Label(f1, text="Enter Range From/To:", font=("Arial", 8)).place(x=320, y=318, anchor=CENTER)
e5 = Entry(f1, width=5)
e5.insert(0, '')
e5.place(x=390, y=308)
Label(f1, text="/", font=("Arial Bold", 10)).place(x=435, y=316, anchor=CENTER)
e6 = Entry(f1, width=5)
e6.insert(0, '')
e6.place(x=445, y=308)


pgBar = ttk.Progressbar(f2, orient = HORIZONTAL, length=300, mode = "determinate")
pgBar.place(x=250, y=80)
txt2 = scrolledtext.ScrolledText(f2, width=90, height=10)
txt2.place(relx=0.5, rely=0.5, anchor=CENTER)
Button(f2, text='ARP Scanner', font=("Arial Bold", 10), command=lambda:raise_frame(f2)).place(x=327, y=2)
Button(f2, text='Routing Tables', font=("Arial", 10), command=lambda:raise_frame(f3)).place(x=110, y=2)
Button(f2, text='Device Information', font=("Arial", 10), command=lambda:raise_frame(f4)).place(x=209, y=2)
Button(f2, text='Network Status', font=("Arial", 10), command=lambda:raise_frame(f1)).place(x=10, y=2)
Button(f2, text='Network Diagnostics', font=("Arial", 10), command=lambda:raise_frame(f5)).place(x=423, y=2)
Label(f2, text="Arp Tables", font=("Arial Bold", 25)).place(relx=0.5, rely=0.13, anchor=CENTER)
btnArp = Button(f2, text="Start Scan", font=("Arial Bold", 14), bg="Green", fg="black", command=netscanner)
btnArp.place(x=85, y=320, anchor=CENTER)
btnPrint = Button(f2, text="Print", font=("Arial Bold", 14), bg="Blue", fg="black", command=printarp)
btnPrint.place(x=730, y=80, anchor=CENTER)
btnDelArp = Button(f2, text="Flush Tables", font=("Arial Bold", 14), bg="Green", fg="black", command=deletearp)
btnDelArp.place(x=230, y=320, anchor=CENTER)
btnClear = Button(f2, text="Clear", font=("Arial Bold", 14), bg="Red", fg="black", command=clearbtn)
btnClear.place(x=650, y=320, anchor=CENTER)
btnBack = Button(f2, text="Back", font=("Arial Bold", 14), bg="Red", fg="black", command=netstatus)
btnBack.place(x=730, y=320, anchor=CENTER)


pgBar = ttk.Progressbar(f3, orient=HORIZONTAL, length=300, mode="determinate")
pgBar.place(x=250, y=80)
txt3 = scrolledtext.ScrolledText(f3, width=90, height=10)
txt3.place(relx=0.5, rely=0.5, anchor=CENTER)
Button(f3, text='ARP Scanner', font=("Arial", 10), command=lambda:raise_frame(f2)).place(x=338, y=2)
Button(f3, text='Routing Tables', font=("Arial Bold", 10), command=lambda:raise_frame(f3)).place(x=112, y=2)
Button(f3, text='Device Information', font=("Arial", 10), command=lambda:raise_frame(f4)).place(x=220, y=2)
Button(f3, text='Network Status', font=("Arial", 10), command=lambda:raise_frame(f1)).place(x=10, y=2)
Button(f3, text='Network Diagnostics', font=("Arial", 10), command=lambda:raise_frame(f5)).place(x=430, y=2)
Label(f3, text="Routing Tables", font=("Arial Bold", 25)).place(relx=0.5, rely=0.13, anchor=CENTER)
btnRoute = Button(f3, text="Routing TBL", font=("Arial Bold", 14), bg="Green", fg="black", command=routingtable)
btnRoute.place(x=100, y=320, anchor=CENTER)
btnPrint = Button(f3, text="Print", font=("Arial Bold", 14), bg="Blue", fg="black", command=printrouting)
btnPrint.place(x=730, y=80, anchor=CENTER)
btnPrintRoute = Button(f3, text="All Routing Details", font=("Arial Bold", 14), bg="Green", fg="black", command=routeprint)
btnPrintRoute.place(x=280, y=320, anchor=CENTER)
btnClear = Button(f3, text="Clear", font=("Arial Bold", 14), bg="Red", fg="black", command=clearbtn)
btnClear.place(x=650, y=320, anchor=CENTER)
btnBack = Button(f3, text="Back", font=("Arial Bold", 14), bg="Red", fg="black", command=netstatus)
btnBack.place(x=730, y=320, anchor=CENTER)

pgBar = ttk.Progressbar(f4, orient=HORIZONTAL, length=300, mode="determinate")
pgBar.place(x=250, y=80)
txt4 = scrolledtext.ScrolledText(f4, width=90, height=10)
txt4.place(relx=0.5, rely=0.5, anchor=CENTER)
Button(f4, text='ARP Scanner', font=("Arial", 10), command=lambda:raise_frame(f2)).place(x=345, y=2)
Button(f4, text='Routing Tables', font=("Arial", 10), command=lambda:raise_frame(f3)).place(x=113, y=2)
Button(f4, text='Device Information', font=("Arial Bold", 10), command=lambda:raise_frame(f4)).place(x=212, y=2)
Button(f4, text='Network Status', font=("Arial", 10), command=lambda:raise_frame(f1)).place(x=10, y=2)
Button(f4, text='Network Diagnostics', font=("Arial", 10), command=lambda:raise_frame(f5)).place(x=437, y=2)
Label(f4, text="Device Information", font=("Arial Bold", 25)).place(relx=0.5, rely=0.13, anchor=CENTER)
btnWiFi = Button(f4, text="WiFi Info", font=("Arial Bold", 14), bg="Green", fg="black", command=wirelessinfo)
btnWiFi.place(x=85, y=320, anchor=CENTER)
btnPrint = Button(f4, text="Print", font=("Arial Bold", 14), bg="Blue", fg="black", command=printdevice)
btnPrint.place(x=730, y=80, anchor=CENTER)
btnDevice = Button(f4, text="Device Info", font=("Arial Bold", 14), bg="Green", fg="black", command=deviceinfo)
btnDevice.place(x=210, y=320, anchor=CENTER)
btnClear = Button(f4, text="Clear", font=("Arial Bold", 14), bg="Red", fg="black", command=clearbtn)
btnClear.place(x=650, y=320, anchor=CENTER)
btnBack = Button(f4, text="Back", font=("Arial Bold", 14), bg="Red", fg="black", command=netstatus)
btnBack.place(x=730, y=320, anchor=CENTER)


txt5 = scrolledtext.ScrolledText(f5, width=50, height=18)
txt5.place(x=30, y=80)
Button(f5, text='ARP Scanner', font=("Arial", 10), command=lambda:raise_frame(f2)).place(x=330, y=2)
Button(f5, text='Routing Tables', font=("Arial", 10), command=lambda:raise_frame(f3)).place(x=113, y=2)
Button(f5, text='Device Information', font=("Arial", 10), command=lambda:raise_frame(f4)).place(x=212, y=2)
Button(f5, text='Network Status', font=("Arial", 10), command=lambda:raise_frame(f1)).place(x=10, y=2)
Button(f5, text='Network Diagnostics', font=("Arial Bold", 10), command=lambda:raise_frame(f5)).place(x=422, y=2)
Label(f5, text="Network Diagnoistic", font=("Arial Bold", 25)).place(relx=0.5, rely=0.13, anchor=CENTER)
btnTrace = Button(f5, text="Trace Route", font=("Arial", 12), bg="Green", fg="black", command=traceroute)
btnTrace.place(x=730, y=145, anchor=CENTER)
btnPrint = Button(f5, text="Print", font=("Arial", 14), bg="Blue", fg="black", command=printdiag)
btnPrint.place(x=60, y=57, anchor=CENTER)
btnPath = Button(f5, text="Ping Path", font=("Arial", 12), bg="Green", fg="black", command=pathping)
btnPath.place(x=730, y=210, anchor=CENTER)
btnNS = Button(f5, text="DNS Lookup", font=("Arial", 10), bg="Green", fg="black", command=nslookup)
btnNS.place(x=730, y=270, anchor=CENTER)
btnClear = Button(f5, text="Clear", font=("Arial Bold", 14), bg="Red", fg="black", command=clearbtn)
btnClear.place(x=650, y=320, anchor=CENTER)
btnBack = Button(f5, text="Back", font=("Arial Bold", 14), bg="Red", fg="black", command=netstatus)
btnBack.place(x=730, y=320, anchor=CENTER)
Label(f5, text="Please Enter Trace IP Address:", font=("Arial", 10)).place(x=450, y=114)
Label(f5, text="Please Enter IP Address To Ping:", font=("Arial", 10)).place(x=450, y=180)
Label(f5, text="Enter IP Address or Blank For Local DNS:", font=("Arial", 9)).place(x=438, y=237)
Label(f5, text="Eg:", font=("Arial", 9)).place(x=450, y=131)
e1 = Entry(f5, width=25)
e1.insert(0, '8.8.8.8')
e1.place(x=470, y=133)
Label(f5, text="Eg:", font=("Arial", 9)).place(x=450, y=201)
e2 = Entry(f5, width=25)
e2.insert(0, '8.8.8.8')
e2.place(x=470, y=203)
Label(f5, text="Eg:", font=("Arial", 9)).place(x=450, y=263)
e3 = Entry(f5, width=25)
e3.insert(0, '8.8.8.8')
e3.place(x=470, y=265)

raise_frame(f1)
window.mainloop()

