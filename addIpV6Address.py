import os
import sys
def main(addrPrefix):
    ipRange=["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
    for ip in ipRange:
        command="ip -6 addr add %s%s/64 dev eth0"%(addrPrefix,ip)
        print(command)
        os.system(command)

def getPrefixArgv():
    for arg in  sys.argv:
        print(arg)
        if("py" in arg):
            pass
        else:
            return arg
        
    raise Exception("error")


prefix=getPrefixArgv()

main(prefix)

#2604:a880:4:1d0::322:700

