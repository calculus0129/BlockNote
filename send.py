import socket
import os
import sys
import time

addressBook = [
    ['bjh', '192.168.0.8'],
    ['amn','192.168.0.9'],
    ['kdy', '192.168.0.10']
    ]

dirname4 = ['server', 'recv', 'send']
host = ""
port = 13426
#port = 32367
path = [os.getcwd()+"/"+dirname4[0]+"/"+dirname4[1]+"/", os.getcwd()+"/"+dirname4[0]+"/"+dirname4[2]+"/"]
if not os.path.isdir(path[1]): os.makedirs(path[1])

memberNumber = len(addressBook) - 1 


'''files = os.listdir(path[1])
for i in range(len(files)):
    f = open(path[1] + files[i], 'r')
    print((files[i].split('.')[0]+':'+files[i].split('.')[1]+'?').encode())
    print("\n내용: \n")
    l = f.read(1024)
    while (l) :# 내용 확인
        print(l.encode())
        l = f.read(1024)
    print(("*").encode())'''

while True :
    #get ip from address book
    if memberNumber < 0 :
        memberNumber = len(addressBook) - 1
    
    host = addressBook[memberNumber][1]
    if host == socket.gethostbyname(socket.gethostname()) :
        memberNumber = memberNumber - 1
        continue
            
    memberNumber = memberNumber - 1
    
    print("\Sending Hash File To : " + host)

    try :
        #establish network connection
        mySocket = socket.socket()
        mySocket.settimeout(1)
        mySocket.connect((host, port))
        
        print("\nServer Connected ...\n")
        
        files = os.listdir(path[1])
        
        print("\nSending File ... \n")
        # file transfer form: f1_name:f1_form?f1_content*f2_name...
        for i in range(len(files)): #you can't input ':' or '?' or '*' in sending file. If then, the received data will be incorrect, or an error would occur.
            #open the hash file
            sys.stdout.write(" Send File: "+path[1] + files[i]+" ... ")
            f = open(path[1] + files[i], 'r')
            #sys.stdout.write("\n내용: \n" + f.read()) # 내용 확인
            mySocket.send((files[i].split('.')[0]+':'+files[i].split('.')[1]+'?').encode('utf-8')) # 파일 제목 보내기
            l = f.read(1024)
            while (l) :
                mySocket.send(l.encode('utf-8'))
                l = f.read(1024)
            mySocket.send(("✐").encode('utf-8'))
            print("Completed!")
            f.close()
        if len(files) == 0: print("No File to Send")
        mySocket.close()
    
    except socket.error as i : 
        print('\nConnection Error\n' + str(i))
    
    time.sleep(3)

