import sys
weight = 0
def moon_weight(weight,rate):    
#    print("What is your weight?")
#    weight = int(sys.stdin.readline())
    rate = 0.25
    increase = 1
    for x in range(1,16):
        print(x,weight*rate)
        weight=weight+increase
