#import os

def write_to_file(n, e, d):
  '''
  path = [os.getcwd()+"/"+dirname[0]+"/"+dirname[1]+"/", os.getcwd()+"/"+dirname[0]+"/"+dirname[2]+"/"]
  if not os.path.isdir(path[0]): os.makedirs(path[0])
  if not os.path.isdir(path[1]): os.makedirs(path[1])

  filenumber = [len(os.listdir(path[0])), len(os.listdir(path[1]))]
  
  '''"""
  #Public Key
  try:
    print(p1+n1+'.txt')#debug
    f = open(p1+n1+'.txt', 'w')
    f.write('{0}\n{1}\n'.format(n,e))
    f.flush()
    f.close()
  #except AttributeError:
  except TypeError:
    if p1 == None: pass
    else: print('pub directory Error!')
  #Private Key
  try:
    print(p2+n2+'.txt')#debug
    f = open(p2+n2+'.txt', 'w')
    f.write('{0}\n{1}\n'.format(n,d))
    f.flush()
    f.close()
  #except AttributeError:
  except TypeError:
    if p1 == None: pass
    else: print('prv directory Error!')"""
  return [n, e, d]
#write_to_file(1, 2, 3, None, None, None, None)

#write_to_file(1, 2, 3)

'''

def write_to_file(n, e, d):
  dirname = ['keys', 'pub', 'prv']

  path = [os.getcwd()+"/"+dirname[0]+"/"+dirname[1]+"/", os.getcwd()+"/"+dirname[0]+"/"+dirname[2]+"/"]
  if not os.path.isdir(path[0]): os.makedirs(path[0])
  if not os.path.isdir(path[1]): os.makedirs(path[1])
  
  filenumber = [len(os.listdir(path[0])), len(os.listdir(path[1]))]
  
  with open (path[0]+'pukey'+str(filenumber[0])+'.txt', 'w') as f:
    f.write('{0}\n{1}\n'.format(n,e))
    f.flush()
    f.close()
    
  with open (path[1]+'prkey'+str(filenumber[1])+'.txt', 'w') as f:
    f.write('{0}\n{1}\n'.format(n,d))
    f.flush()
    f.close()
'''
