birth=input().split("/")
current=input().split("/")
list1=[]
monthsanddays={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
if int(birth[1])==2:
     if int(birth[2])%4==0:
        days=(29-int(birth[0])) + int(current[0])
        months=(12-int(birth[1]))+  int(current[1])
        years=int(current[2])-int(birth[2])
else:
    days=(monthsanddays[int(birth[0])]-int(birth[0]))+int(current[0])
    months=(12-int(birth[1]))+ int(current[1])
    years=int(current[2])-int(birth[2])

if days>=monthsanddays[int(birth[0])]:
    days=days-monthsanddays[int(birth[0])]
if months>=12:
    months=months-12
print(years,"Y"," ",months,"M"," ",days,"D")
