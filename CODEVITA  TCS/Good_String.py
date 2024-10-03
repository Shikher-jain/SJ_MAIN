def totalDist(name, GoodStr):
    Distance = 0
    PrevGood = GoodStr[0]

    for char in name:
        if char in GoodStr:
            PrevGood = char
            continue
        
        MDistance = float('inf')
        Best = None
        
        for Good in GoodStr:
            distance = abs(ord(char) - ord(Good))
            
            if distance < MDistance:
                MDistance = distance
                Best = Good
            elif distance == MDistance:
                if abs(ord(PrevGood) - ord(Good)) < abs(ord(PrevGood) - ord(Best)):
                    Best = Good
        
        Distance += MDistance
        PrevGood = Best
    return Distance

name = input()
GoodStr  = input()
# name = "Vyom"
# GoodStr  = "(@HR*i{kcQl" 
Distance = totalDist(name, GoodStr)
print(f"{Distance}")