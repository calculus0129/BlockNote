# The main Program
import sys, os
from RSA import rsa

# note: .txt파일로 할 수도 있음

u = []
fdn = ['src', 'lib']
#fn = ['users.bin']

# 파일로 input하는 코드

class user:
    name = ''
    #pw = ''
    key = rsa()
    ts = ''
    #IsT = False
    stake = 10 # a default stake. Temporary Stake for all Users: 10
    #vrs = [] # verification records. 사용자 인증 기록
#epws = [] # pw encrypted text of name. contains all users' epw.

class blockchain():
    admin = ''
    ts = ''
    key = rsa()
    

#class note:
'''
def adduser():
    print('new user!\n')
    tmp = user()
    n = input("\tinput your name: ")
    p = input("\tinput your password: ")
    I = input("\tR U A Teacher? (yes: 1, no: else): ") == '1'

    tmp.name = n, tmp.pw = p, tmp.IsT = I
    u.append(tmp)
    
    print('welcome!')
'''
'''def main():
    print('hi')

'''
def create_new_blockchain():
    input("Administrator's name: ")
