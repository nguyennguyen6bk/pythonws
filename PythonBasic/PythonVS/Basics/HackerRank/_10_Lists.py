import numpy as np

N = int(input())
list = []

for i in range(N):
    line = input()
    s = line.split()
    cmd = s[0]
    args =  s[1:]
    print(args)
    # if len(s) > 1 :
    #     cmd += "(" + ",".join(args) + ")"
    #     eval("list." + cmd)
    # elif len(s) == 1 and s[0] != "print": 
    #     cmd += "()"
    #     eval("list." + cmd)
    # else :
    #     print(list)


l = [   ["insert", 2, 3], ["insert", 3, 5], 
        ["print"], ["sort"], ["remove", 5], 
        ["append", 6], ["print"], ["reverse"],
        ["print"],["pop"],["print"]
    ]
# list = []
# for s in l :
#     cmd  = s[0]
#     args = s[1:]
#     print(args)
#     if cmd == "print" :
#         print(list)
#     else : 
        
#         print( "(" + ",".join(args) + ")" )
#         # eval("list." + cmd)
        


