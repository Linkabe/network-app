import os
from tkinter import scrolledtext, ttk
from tkinter import *
from datetime import datetime
from config import ReportStatsLocation, ReportARPLocation, ReportRoutingLocation, ReportDeviceLocation, ReportDiagLocation

button = [8, "green", "white", 1, 14, 5, .2, .4, "Aerial Bold"]
buttonName = ["NETWORK SCANNER", "SNMP", "Alerts", "Exit"]
rowx = [.2, .4, .6, .8]


def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func


def scanneropen():
    scanner()


def snmpopen():
    snmpwindow()


def alertsopen():
    alertswindow()


def runcreatewindow():
    createwindow()

##function to create main window
def createwindow():
    main = Tk()
    main.title("Network Management TNP")
    main.geometry('800x400')

    b1 = Button(main, text=buttonName[0], font=(button[8], button[0]), borderwidth=button[4], bg=button[1], fg=button[2], height=button[3], width=button[4],command=combine_funcs(lambda: main.destroy(), scanneropen))
    b1.place(relx=rowx[0], rely=button[7], anchor=CENTER)
    b1 = Button(main, text=buttonName[1], font=(button[8], button[0]), borderwidth=button[4], bg=button[1], fg=button[2], height=button[3], width=button[4],command=combine_funcs(lambda: main.destroy(), snmpopen))
    b1.place(relx=rowx[1], rely=button[7], anchor=CENTER)
    b1 = Button(main, text=buttonName[2], font=(button[8], button[0]), borderwidth=button[4], bg=button[1], fg=button[2], height=button[3], width=button[4],command=combine_funcs(lambda: main.destroy(), alertsopen))
    b1.place(relx=rowx[2], rely=button[7], anchor=CENTER)
    b1 = Button(main, text=buttonName[3], font=(button[8], button[0]), borderwidth=button[4], bg=button[1], fg=button[2], height=button[3], width=button[4],command=lambda: main.destroy())
    b1.place(relx=rowx[3], rely=button[7], anchor=CENTER)

    main.mainloop()

def scanner():
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

    def openmain():
        createwindow()

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
    btnBack = Button(f1, text="Back", font=("Arial Bold", 12), bg="Red", fg="black", command=combine_funcs(lambda: window.destroy(), openmain))
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
    btnBack = Button(f2, text="Back", font=("Arial Bold", 14), bg="Red", fg="black", command=combine_funcs(lambda: window.destroy(), openmain))
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
    btnBack = Button(f3, text="Back", font=("Arial Bold", 14), bg="Red", fg="black", command=combine_funcs(lambda: window.destroy(), openmain))
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
    btnBack = Button(f4, text="Back", font=("Arial Bold", 14), bg="Red", fg="black", command=combine_funcs(lambda: window.destroy(), openmain))
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
    btnBack = Button(f5, text="Back", font=("Arial Bold", 14), bg="Red", fg="black", command=combine_funcs(lambda: window.destroy(), openmain))
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

def snmpwindow():
    def raise_frame(frame):
        frame.tkraise()

    snmp = Tk()
    snmp.title("Network Management TNP")
    snmp.geometry('1000x450')

    f6 = Frame(snmp)
    f7 = Frame(snmp)
    f8 = Frame(snmp)

    DNow = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    for frame in (f6, f7, f8):
        frame.place(width=1000, height=450)

    def openmain2():
        snmp.destroy()
        createwindow()

    def openmain1():
        createwindow()

    def closesnmp():
        snmp.destroy()

    def getbulktemp():
        f = os.popen('snmpwalk -c public -v 1 localhost .1.3.6.1.4.1.30503.1')
        for line in f:
            line = line.strip()
            if line:
                txt8.insert("end", line + "\n")
            txt8.bind("<Return>", sysContact)
        f.close()

    def gettemp():
        f = os.popen('python C:/Users/niall/Documents/College/NetworkManagment/SNMP-Revised/graph.py')
        f.close()

    def getprocess():
        f = os.popen('python C:/Users/niall/Documents/College/NetworkManagment/SNMP-Revised/graph2.py')
        f.close()

    def sysUp():
        f = os.popen('snmpget -c public -v 1 localhost .1.3.6.1.2.1.1.3.0')
        for line in f:
            line = line.strip()
            if line:
                txt6.insert("end", line + "\n")
            txt6.bind("<Return>", sysUp)
        f.close()

    def sysDesc():
        f = os.popen('snmpget -c public -v 1 localhost .1.3.6.1.2.1.1.1.0')
        for line in f:
            line = line.strip()
            if line:
                txt6.insert("end", line + "\n")
            txt6.bind("<Return>", sysDesc)
        f.close()

    def sysContact():
        f = os.popen('snmpget -c public -v 1 localhost .1.3.6.1.2.1.1.4.0')
        for line in f:
            line = line.strip()
            if line:
                txt6.insert("end", line + "\n")
            txt6.bind("<Return>", sysContact)
        f.close()

    def sysName():
        f = os.popen('snmpget -c public -v 1 localhost .1.3.6.1.2.1.1.5.0')
        for line in f:
            line = line.strip()
            if line:
                txt6.insert("end", line + "\n")
            txt6.bind("<Return>", sysName)
        f.close()

    def sysBulk():
        f = os.popen('snmpbulkget -c public -v 2c localhost .1.3.6.1.2.1.1.0')
        for line in f:
            line = line.strip()
            if line:
                txt6.insert("end", line + "\n")
            txt6.bind("<Return>", sysBulk)
        f.close()

    def sysCPU():
        f = os.popen('snmpwalk -v 2c -c public localhost .1.3.6.1.2.1.25.3.3.1.2')
        for line in f:
            line = line.strip()
            if line:
                txt6.insert("end", line + "\n")
            txt6.bind("<Return>", sysCPU)
        f.close()

    def sysCPUSuse():
        f = os.popen('snmpbulkget -v2c -cpublic localhost .1.3.6.1.2.1.25.5.1.1.1')
        for line in f:
            line = line.strip()
            if line:
                txt6.insert("end", line + "\n")
            txt6.bind("<Return>", sysCPUSuse)
        f.close()

    def sysRAM():
        f = os.popen('snmpget -v 2c -c public localhost .1.3.6.1.2.1.25.2.2.0')
        for line in f:
            line = line.strip()
            if line:
                txt6.insert("end", line + "\n")
            txt6.bind("<Return>", sysRAM)
        f.close()

    def sysRAMuse():
        f = os.popen('snmpwalk -v1 -cpublic localhost 1.3.6.1.2.1.25.2.3.1.4')
        for line in f:
            line = line.strip()
            if line:
                txt6.insert("end", line + "\n")
            txt6.bind("<Return>", sysRAMuse)
        f.close()

    def sysStore():
        f = os.popen('snmpwalk -v1 -cpublic localhost .1.3.6.1.4.1.2021.9.1.9.1')
        for line in f:
            line = line.strip()
            if line:
                txt6.insert("end", line + "\n")
            txt6.bind("<Return>", sysStore)
        f.close()

    def sysStoreUs():
        f = os.popen('snmpwalk -v1 -cpublic localhost 1.3.6.1.2.1.25.2.3.1.5')
        for line in f:
            line = line.strip()
            if line:
                txt6.insert("end", line + "\n")
            txt6.bind("<Return>", sysStoreUs)
        f.close()

    def sysStoreBulk():
        f = os.popen('snmpbulkget -v2c -cpublic localhost 1.3.6.1.2.1.25.2.3.1.4')
        for line in f:
            line = line.strip()
            if line:
                txt6.insert("end", line + "\n")
            txt6.bind("<Return>", sysStoreBulk)
        f.close()

    def btnhelp():
        f = open('./Help.txt', 'r')
        for line in f:
            line = line.strip()
            if line:
                txt7.insert("end", line + "\n")
            txt7.bind("<Return>", sysStoreBulk)
        f.close()
        txt7.insert(INSERT, "Your help options Have been printed to the console!!")

    def snmpget():
        snmpAgent = e1A.get()
        snmpVersion = e3V.get()
        snmpOp = e4Op.get()
        snmpName = e1N.get()
        snmpOID = e5OID.get()
        f = os.popen('snmpget -v' + snmpVersion + ' -' + snmpOp + ' ' + snmpName + ' ' + snmpAgent + ' ' + snmpOID)
        for line in f:
            line = line.strip()
            if line:
                txt7.insert("end", line + "\n")
            txt7.bind("<Return>", snmpgetbulk)
        f.close()

    def snmpwalk():
        snmpAgent = e1A.get()
        snmpVersion = e3V.get()
        snmpOp = e4Op.get()
        snmpName = e1N.get()
        snmpOID = e5OID.get()
        f = os.popen('snmpwalk -v' + snmpVersion + ' -' + snmpOp + ' ' + snmpName + ' ' + snmpAgent + ' ' + snmpOID)
        for line in f:
            line = line.strip()
            if line:
                txt7.insert("end", line + "\n")
            txt7.bind("<Return>", snmpgetbulk)
        f.close()

    def snmpgetbulk():
        snmpAgent = e1A.get()
        snmpVersion = e3V.get()
        snmpOp = e4Op.get()
        snmpName = e1N.get()
        snmpOID = e5OID.get()
        f = os.popen('snmpbulkget -v' + snmpVersion + ' -' + snmpOp + ' ' + snmpName + ' ' + snmpAgent + ' ' + snmpOID)
        for line in f:
            line = line.strip()
            if line:
                txt7.insert("end", line + "\n")
            txt7.bind("<Return>", snmpgetbulk)
        f.close()

    def clearbtn():
        txt6.delete(1.0, END)
        txt7.delete(1.0, END)

    def printdiag():
        Diag = txt6.get("1.0", "end-1c")
        f = open("./MIB-Printout.txt", "w")
        f.write("Print Out of Your Information in: " + DNow + "\n" + "\n" + Diag)
        f.close()
        clearbtn()
        txt6.insert(INSERT,
                    "Your Network Information has been Writen" + "\n" + "  MIB-Printout.txt" + "\n" + "Located: ./MIB-Printout.txt")

    def closeWindowProcess():
        f = os.popen('taskkill /IM "python.exe" /F')
        f.close()


    txt6 = scrolledtext.ScrolledText(f6, width=86, height=10)
    txt6.place(x=60, y=80)
    Button(f6, text='SNMP System Requests', font=("Arial Bold", 10), borderwidth=5, command=lambda: raise_frame(f6)).place(x=10, y=2)
    Button(f6, text='SNPM MIB Browser', font=("Arial", 8), borderwidth=5, command=lambda: raise_frame(f7)).place(x=200,                                                                                                          y=2)
    Button(f6, text='SNMP Graph', font=("Arial", 10), borderwidth=5, command=combine_funcs(lambda: raise_frame(f8), getbulktemp)).place(x=340, y=2)
    Label(f6, text="SNMP System Requests", font=("Arial", 20)).place(relx=0.5, rely=0.13, anchor=CENTER)
    btnPrint = Button(f6, text="Print", font=("Arial Bold", 12), bg="Blue", fg="white", height=1, width=15,borderwidth=5, command=printdiag)
    btnPrint.place(x=900, y=335, anchor=CENTER)
    btnDesc = Button(f6, text="System Description", font=("Arial", 12), bg="Green", fg="black", height=1, width=15,borderwidth=5, command=sysDesc)
    btnDesc.place(x=130, y=280, anchor=CENTER)
    btnDesc = Button(f6, text="Get Bulk System", font=("Arial", 12), bg="Green", fg="black", height=1, width=15,borderwidth=5, command=sysBulk)
    btnDesc.place(x=130, y=335, anchor=CENTER)
    btnSBulk = Button(f6, text="Get Bulk Storage", font=("Arial", 12), bg="Green", fg="black", height=1, width=15,borderwidth=5, command=sysStoreBulk)
    btnSBulk.place(x=130, y=385, anchor=CENTER)
    btnContact = Button(f6, text="System Contact", font=("Arial", 12), bg="Green", fg="black", height=1, width=15,borderwidth=5, command=sysContact)
    btnContact.place(x=320, y=280, anchor=CENTER)
    btnDesc = Button(f6, text="CPU Temp", font=("Arial", 12), bg="Green", fg="black", height=1, width=15, borderwidth=5,command=sysCPU)
    btnDesc.place(x=320, y=385, anchor=CENTER)
    btnDesc = Button(f6, text="CPU Speed & Use", font=("Arial", 12), bg="Green", fg="black", height=1, width=15,borderwidth=5, command=sysCPUSuse)
    btnDesc.place(x=320, y=335, anchor=CENTER)
    btnName = Button(f6, text="System Name", font=("Arial", 12), bg="Green", fg="black", height=1, width=15,borderwidth=5, command=sysName)
    btnName.place(x=510, y=280, anchor=CENTER)
    btnRAM = Button(f6, text="RAM Size", font=("Arial", 12), bg="Green", fg="black", height=1, width=15, borderwidth=5,command=sysRAM)
    btnRAM.place(x=510, y=335, anchor=CENTER)
    btnRAMUS = Button(f6, text="RAM Use", font=("Arial", 12), bg="Green", fg="black", height=1, width=15, borderwidth=5,command=sysRAMuse)
    btnRAMUS.place(x=510, y=385, anchor=CENTER)
    btnUptime = Button(f6, text="System Uptime", font=("Arial", 12), bg="Green", fg="black", height=1, width=15,borderwidth=5, command=sysUp)
    btnUptime.place(x=700, y=280, anchor=CENTER)
    btnStore = Button(f6, text="Storage Size", font=("Arial", 12), bg="Green", fg="black", height=1, width=15,borderwidth=5, command=sysStore)
    btnStore.place(x=700, y=335, anchor=CENTER)
    btnStoreUs = Button(f6, text="Storage Used", font=("Arial", 12), bg="Green", fg="black", height=1, width=15,borderwidth=5, command=sysStoreUs)
    btnStoreUs.place(x=700, y=385, anchor=CENTER)
    btnClear = Button(f6, text="Clear", font=("Arial Bold", 12), bg="Red", fg="white", height=1, width=15,borderwidth=5, command=clearbtn)
    btnClear.place(x=900, y=280, anchor=CENTER)
    btnExit = Button(f6, text="Back", font=("Arial Bold", 12), bg="black", fg="white", height=1, width=15,borderwidth=5, command=combine_funcs(lambda: snmp.destroy(), openmain1))
    btnExit.place(x=900, y=385, anchor=CENTER)

    txt7 = scrolledtext.ScrolledText(f7, width=100, height=10)
    txt7.place(x=60, y=80)
    Button(f7, text='SNMP System Requests', font=("Arial", 10), borderwidth=5, command=lambda: raise_frame(f6)).place(x=10, y=2)
    Button(f7, text='SNMP MIB Browser', font=("Arial Bold", 10), borderwidth=5, command=lambda: raise_frame(f7)).place(x=200, y=2)
    Button(f7, text='SNMP Graph', font=("Arial", 10), borderwidth=5, command=combine_funcs(lambda: raise_frame(f8), getbulktemp)).place(x=370, y=2)
    Label(f7, text="SNMP MIB Browser", font=("Arial Bold", 20)).place(relx=0.5, rely=0.13, anchor=CENTER)
    btnGet = Button(f7, text="SNMP  Get", font=("Arial", 12), bg="Green", fg="black", height=1, width=12, borderwidth=5,command=snmpget)
    btnGet.place(x=368, y=330, anchor=CENTER)
    btnWalk = Button(f7, text="SNMP Walk", font=("Arial", 12), bg="Green", fg="black", height=1, width=12,borderwidth=5, command=snmpwalk)
    btnWalk.place(x=630, y=330, anchor=CENTER)
    btnBulk = Button(f7, text="SNMP Bulk Get", font=("Arial", 12), bg="Green", fg="black", height=1, width=12,borderwidth=5, command=snmpgetbulk)
    btnBulk.place(x=500, y=330, anchor=CENTER)
    btnHelp = Button(f7, text="Help", font=("Arial Bold", 12), bg="gold", fg="black", height=1, width=8, borderwidth=5,command=btnhelp)
    btnHelp.place(x=770, y=330, anchor=CENTER)
    btnClear = Button(f7, text="Clear", font=("Arial Bold", 12), bg="Red", fg="black", height=1, width=8, borderwidth=5,command=clearbtn)
    btnClear.place(x=770, y=390, anchor=CENTER)
    btnPrint = Button(f7, text="Print", font=("Arial", 12), bg="Blue", fg="white", height=1, width=8, borderwidth=5,command=printdiag)
    btnPrint.place(x=900, y=330, anchor=CENTER)
    btnExit = Button(f7, text="Exit", font=("Arial Bold", 12), bg="black", fg="white", height=1, width=8, borderwidth=5,command=combine_funcs(lambda: snmp.destroy(), openmain1))
    btnExit.place(x=900, y=390, anchor=CENTER)
    Label(f7, text="Configuration", font=("Arial Bold", 9)).place(x=80, y=250)
    Label(f7, text="Profile Name:", font=("Arial", 8)).place(x=90, y=270)
    e1N = Entry(f7, width=10)
    e1N.insert(0, 'public')
    e1N.place(x=170, y=270)
    Label(f7, text="Agent Address or Name:", font=("Arial", 8)).place(x=40, y=360)
    e1A = Entry(f7, width=10)
    e1A.insert(0, 'localhost')
    e1A.place(x=170, y=360)
    Label(f7, text="Options:", font=("Arial", 8)).place(x=90, y=330)
    e4Op = Entry(f7, width=10)
    e4Op.insert(0, 'c')
    e4Op.place(x=170, y=330)

    Label(f7, text="Version [1/2c/3]:", font=("Arial", 8)).place(x=70, y=300)
    e3V = Entry(f7, width=10)
    e3V.insert(0, '2c')
    e3V.place(x=170, y=300)
    Label(f7, text="Enter Your OID:", font=("Arial Bold", 12)).place(x=370, y=250)
    e5OID = Entry(f7, width=64)
    e5OID.insert(0, '')
    e5OID.place(x=305, y=275)

    txt8 = scrolledtext.ScrolledText(f8, width=70, height=15)
    txt8.place(x=60, y=100)
    Button(f8, text='SNMP System Requests', font=("Arial", 10), borderwidth=5, command=lambda: raise_frame(f6)).place(x=10, y=2)
    Button(f8, text='SNMP MIB Browser', font=("Arial", 10), borderwidth=5, command=lambda: raise_frame(f7)).place(x=200,y=2)
    Button(f8, text='SNMP Graph', font=("Arial Bold", 10), borderwidth=5, command=combine_funcs(lambda: raise_frame(f8), getbulktemp)).place(x=370,y=2)
    Label(f8, text="SNMP Graphs", font=("Arial Bold", 20)).place(x=350, y=80, anchor=CENTER)
    btnGet = Button(f8, text="CPU Temp", font=("Arial", 12), bg="Green", fg="black", height=1, width=12, borderwidth=5,command=gettemp)
    btnGet.place(x=218, y=400, anchor=CENTER)
    btnWalk = Button(f8, text="CPU Processes", font=("Arial", 12), bg="Green", fg="black", height=1, width=12,borderwidth=5, command=getprocess)
    btnWalk.place(x=480, y=400, anchor=CENTER)
    btnBulk = Button(f8, text="Memory Graph", font=("Arial", 12), bg="Green", fg="black", height=1, width=12,borderwidth=5, command=gettemp)
    btnBulk.place(x=350, y=400, anchor=CENTER)
    btnHelp = Button(f8, text="Help", font=("Arial Bold", 12), bg="gold", fg="black", height=1, width=8, borderwidth=5,command=btnhelp)
    btnHelp.place(x=770, y=180, anchor=CENTER)
    btnClear = Button(f8, text="Clear", font=("Arial Bold", 12), bg="Red", fg="black", height=1, width=8, borderwidth=5,command=clearbtn)
    btnClear.place(x=770, y=240, anchor=CENTER)
    btnPrint = Button(f8, text="Print", font=("Arial", 12), bg="Blue", fg="white", height=1, width=8, borderwidth=5,command=printdiag)
    btnPrint.place(x=900, y=180, anchor=CENTER)
    btnExit = Button(f8, text="Exit", font=("Arial Bold", 12), bg="black", fg="white", height=1, width=8, borderwidth=5,command=combine_funcs(lambda: closeWindowProcess, openmain2))
    btnExit.place(x=900, y=240, anchor=CENTER)

    raise_frame(f6)
    snmp.mainloop()

def alertswindow():
    def raise_frame(frame):
        frame.tkraise()

    alerts = Tk()
    alerts.title("Network Management TNP")
    alerts.geometry('1000x450')

    DNow = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    f9 = Frame(alerts).place(width=1000, height=450)

    def clearbtn():
        txt9.delete(1.0, END)

    def openmain3():
        createwindow()

    def printalerts():
        Stats = txt9.get("1.0", "end-1c")
        f = open(ReportStatsLocation, "w+")
        f.write("Print Out of Your Network Status on: " + DNow + "\n" + "\n" + Stats)
        f.close()
        clearbtn()
        txt9.insert(INSERT, "Your Notifications have been Writen to File Alerts.txt" + "\n" + "Located: " + ReportStatsLocation)

    txt9 = scrolledtext.ScrolledText(f9, width=86, height=10)
    txt9.place(x=60, y=80)
    Label(f9, text="Alerts", font=("Arial", 20)).place(relx=0.5, rely=0.13, anchor=CENTER)
    btnPrint = Button(f9, text="Print", font=("Arial Bold", 12), bg="Blue", fg="white", height=1, width=15,borderwidth=5, command=printalerts)
    btnPrint.place(x=900, y=335, anchor=CENTER)
    btnClear = Button(f9, text="Clear", font=("Arial Bold", 12), bg="Red", fg="white", height=1, width=15,borderwidth=5, command=clearbtn)
    btnClear.place(x=900, y=280, anchor=CENTER)
    btnExit = Button(f9, text="Back", font=("Arial Bold", 12), bg="black", fg="white", height=1, width=15,borderwidth=5, command=combine_funcs(lambda: alerts.destroy(), openmain3))
    btnExit.place(x=900, y=385, anchor=CENTER)

    alerts.mainloop()


if __name__ == '__main__':
    createwindow()

