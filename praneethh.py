class Asset:
    def __init__(self,asset_id,asset_holder_name,asset_type,asset_location,asset_status):
        self.asset_id=asset_id
        self.asset_holder_name=asset_holder_name
        self.asset_type=asset_type
        self.asset_location=asset_location
        self.asset_status=asset_status

class AssetManager:
    def __init__(self,asset_list):
        self.asset_list=asset_list

    def counttypes(self):
        newdict={}
        list2=[]
        for i in self.asset_list:
             if i.asset_type not in list2:
                 newdict[i.asset_type]=1
                 list2.append(i.asset_type)
             else:
                newdict[i.asset_type]+=1
        for i in newdict:
            print(i," : ",newdict[i])
    def allocateasset(self,location):
        count=0
        for i in self.asset_list:
             if i.asset_status=="unallocated":
                 if location in i.asset_location:
                     i.asset_status="allocated"
                     count+=1
        if count==0:
            print("No asset found with given location")
        else:
            print("Count of records updated:"," ",count)
            for i in self.asset_list:
                print(i.asset_id," ",i.asset_status)



if __name__=="__main__":
    n= int(input())
    list1=[]
    for i in range(n):
        a_id=input()
        a_holder=input()
        atype=input().capitalize()
        aloc=input()
        astat=input()
        list1.append(Asset(a_id,a_holder,atype,aloc,astat))
    loc=input()
    p= AssetManager(list1)
    p.counttypes()
    p.allocateasset(loc)
    
                     
        
        
        
