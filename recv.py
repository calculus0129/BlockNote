import socket
import os
import uuid
import filecmp
import sys

class member:
    name = '(unknown)'
    ip = ''
m = list()
addressBook = [    
    ['bjh', '192.168.0.8'],
    ['amn','192.168.0.9'],
    ['kdy', '192.168.0.10']
    ]#["220.73.19.248","220.73.19.248"]


dirname4 = ['server', 'recv', 'send']
host = ""
port = 13426
#port = 32367
path = [os.getcwd()+"/"+dirname4[0]+"/"+dirname4[1]+"/", os.getcwd()+"/"+dirname4[0]+"/"+dirname4[2]+"/"]
if not os.path.isdir(path[0]): os.makedirs(path[0])

mySocket = socket.socket()
mySocket.bind((host, port))

for i in range(len(addressBook)):
    m.append(member())
    #m[i].name = ?
    m[i].ip = addressBook[i]

def eraseTempFile() :
    #path = os.getcwd() + '/vote/'
    files = os.listdir(path[0])
    
    fileToSave = fileCheck()
    
    if fileToSave == [] : pass
    else :
        files.remove(fileToSave)
        for file in files :
            os.remove(path[0] + file)

'''def eraseAllLegacyFiles() :
    #path = os.getcwd() + '/vote/'
    files = os.listdir(path)
    
    for file in files :
        os.remove(path + file)

def checkHashFileFromMiner() :  #literally, ...(something). Note: This code is useless right now. Do not Use!(It's function is just to check files)
    files = os.listdir(path)
    #files.remove('newMine')
    
    errorFlag = 0
    
    for file in files :
        with open(path + file, 'r') as f, open(path + 'newMine/' + file, 'r') as g :
            while True :
                orgByte = f.read(1)
                newByte = g.read(1)
                if newByte == '' :
                    # wrong hash file from Miner
                    errorFlag = 2
                    break
                if orgByte == '' :
                    errorFlag = 0
                    break
                if orgByte != newByte :
                    errorFlag = 1
                    break
    
    if errorFlag == 0 :
        os.rename(path + 'newmine/', path + createFileName())   #especially this
'''
def fileCheck() :   #check files in 'path' if some files are double(if then, one of the file is included in the returning list).
    #path = os.getcwd() + '/vote/'
    files = os.listdir(path[0])
    
    print("existing files in: "+path[0]+":")
    for i in range(len(files)):
        print(files[i])

    dfiles = []
    for i in range(len(files)):
        for j in range(i + 1, len(files)):
            if filecmp.cmp(path[0] + files[i], path[0] + files[j], shallow=False) :
                print("\nSame Hash Files: ")
                print(files[i])
                print(files[j])
                
                dfiles.append(files[i])
                """Compare the files named f1 and f2, returning True if they seem equal, False otherwise.
                If shallow is true, files with identical os.stat() signatures are taken to be equal. Otherwise, the contents of the files are compared.
                Note that no external programs are called from this function, giving it portability and efficiency."""
    
    return dfiles

'''def createFileName() :  #returns random hexdemical number
    return str(uuid.uuid4().hex)
'''
def main():
    while True :
        print("\nServer Waiting ..\n")
        
        try :
            mySocket.listen(1)
            conn, addr = mySocket.accept()
            k=0
            # message from other member
            sys.stdout.write("Connection from: " + str(addr) + " ")
            for i in range(len(addressBook)):
                for j in range(len(addr)):
                    if m[i].ip == addr[j]:
                        sys.stdout.write("member No."+str(i)+" Name: ")
                        print(m[i].name)
                        k=1
                        break
                if k == 1: break
            #if not os.isdir(path): os.makedirs(path)
            #fileName = createFileName()
            files = os.listdir(path[0])
            #fileName = 'recv'+str(len(files))
            #f = open(path[0]+fileName+".txt", 'a')
            data=''
            #data receiving part
            '''while True:
                data = conn.recv(1024)
                if not data:
                    break
                else :
                    f.write((data).decode())'''
            while True:
                d = (conn.recv(1024)).decode('utf-8')
                if not d: break
                else: data+=d
            for i in range(len(data.split('*'))):   #you can't input '^' or '*' in sending file. If then, the received data will be incorrect, or an error would occur.
                d = (data.split('*')[i]).split('?') # 보낸 i번째 파일의 제목 그리고 내용
                #f = open(path[0]+d[0]+".txt", 'w')
                f = open(path[0]+'.'.join(d[0].split(':')), 'w')
                f.write('?'.join(d[1:]))
                f.flush()
                f.close()
            #f.close()
            conn.close()
            
            #eraseTempFile()   
        except socket.error as expr :
            conn.close()
            print(expr)
            pass
            #print("Program Terminated!")
            #quit()

main()
