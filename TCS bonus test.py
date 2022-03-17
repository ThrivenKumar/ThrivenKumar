class Property:
    def __init__(self,property_type,property_value,max_bid_price):
        self.property_type=property_type
        self.property_value=property_value
        self.max_bid_price=max_bid_price
class Tender:
    def __init__(self,buyer_name,property_type,bid_price):
        self.property_type=property_type
        self.buyer_name=buyer_name
        self.bid_price=bid_price

def main():
    propcount=int(input())
    prop1=[]
    prop2=[]
    prop3=[]
    for i range(propcount):
        prop1.append(input())
        prop2.append(input())
        prop3.append(input())
    bidcount=int(input())
    bid1=[]
    bid2=[]
    bid3=[]
    for i range(bidcount):
        bid1.append(input())
        bid2.append(input())
        bid3.append(input())
def bidProperty(one,two):
    for i in range(len(two[1])):
        if not two[1][i] in one[0]:
            two[1].remove(two[1][i])
            two[0].remove(two[0][i])
            two[2].remove(two[2][i])
    for i in range(len(two[1])):
        for j in range(len(one[0])):
            if two[1][i]==one[0][j]:
                if two[2][i]>one[2][j]:
                    two[1].remove(two[1][i])
                    two[0].remove(two[0][i])
                    two[2].remove(two[2][i])
    for k in range(len(one[1])):
        proptype=one[0][k]
        for i in range(len(two[1])):
            maxbid=two[2][i]
            indexj=0
            for j in range(len(two[0])):
                if proptype==two[1][j]:
                    if maxbid> two[2][j]:
                        maxbid=two[2][j]
                        indexj=j
                    
                
if __name__=="__main__":
    main()
    
