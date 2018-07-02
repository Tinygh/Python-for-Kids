import sys
weight = 0
def moon_weight(weight,rate,years):    
    print("Please enter your current Earth weight:")
    weight = int(sys.stdin.readline())
    print("Please enter the amount your weight might increase each year:")
    increase = int(sys.stdin.readline())
    print("Please enter the number of years:")  
    years = int(sys.stdin.readline())
    rate = 0.25
    for x in range(1,years):
        print(x,weight*rate)
        weight=weight+increase
