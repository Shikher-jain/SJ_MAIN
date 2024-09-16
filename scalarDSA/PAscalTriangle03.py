# nCr =  n! / (r!(n−r)!)
# nC(r-1) =  n! / ((r-1)!(n−(r-1))!)
# nC(r-1) =  n! / ((r-1)!) (n−r+1)!
# nC(r-1) =  n! / ((r-1)!) (n−r+1)(n-r)!
# nCr =  n! / r*(r-1)! (n−r)!
# nCr / nC(r-1) =  (n−r+1)/r
# nCr = k . nC(r-1)
# k =  (n−r+1)/r
import BinomialCoefficient02 as BioCoeff

n=5

for i in range(n+1):
    curr =1
    
    for j in range(1,i+1):
        print(curr,end=" ")
        k=int((i-j+1)/j)
        curr = (curr * (i-j+1))//j
    print("1")

