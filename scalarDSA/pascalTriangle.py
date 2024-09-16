# 1_
# 1_2_1_
# 1_3_3_1_
# 1_4_6_4_1_
# 1_5_10_10_5_1_

# import Binomial_Coefficient01 as BioCoeff
import BinomialCoefficient02 as BioCoeff
n=5
for i in  range(n+1):
    for j in range(i):
        print(BioCoeff.binomial_coefficient(i,j),end=" ")
    print()
