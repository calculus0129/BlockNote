#directories

d0 = ['srcs']
d1 = ['blockchain', 'history']
d2 = ['base', 'block', 'newblock', 'verify']
p = [d0[0]+'/'+d1[0]+'/'+d2[1]+'/', d0[0]+'/'+d1[0]+'/'+d2[2], d0[0]+'/'+d1[0]+'/'+d2[3]+'/'] # 

'''dn = {'srcs':
      [{'blockchain':
        [{'base':None},
         {'block':None},
         {'newblock':None}
         ]},
       {'history':None}
       ]
      }
'''
#if not isdirs...
'''
#test
print(dn, dn['srcs'], dn['srcs'][0], dn['srcs'][0]['blockchain'], sep = '\n')
'''
