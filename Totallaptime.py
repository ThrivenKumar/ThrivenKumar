def computerLapTime(laptimes):
    minutes=laptimes//60
    seconds=laptimes%60
    hours=minutes//60
    minutes=minutes%60
    if hours<10:
        print('0'+str(hours),end=":")
    else:
        print(str(hours),end=":")
    if minutes<10:
        print('0'+str(minutes),end=":")
    else:
        print(str(minutes),end=":")
    if seconds<10:
        print('0'+str(seconds))
    else:
        print(str(seconds))
    
    
def binaryToDecimal(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal

if __name__=='__main__':
    n=int(input())
    count=0
    for i in range(n):
        count=count+binaryToDecimal(int(input()))
    computerLapTime(count)
    
        
    
                     
