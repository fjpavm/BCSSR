import math


class BCSSR:
    def __init__(self):
        # Algorithm parameter initialization and options

    
    # calculates significance level (adaptation of Numerical Recipes in C as implemented in https://github.com/stites/CSSR/blob/master/Test.cpp)
    def ProbKS(alam):
        EPS1 = 0.001
        EPS2 = 1.0e-8

        fac = 2.0
        sum = 0.0
        term_bf = 0.0

        a2 = -2.0*alam*alam
        for j in range(1, 100):
            term = fac*exp(a2*j*j)
            sum = sum + term
            if abs(term) <= EPS1 * term_bf or abs(term) <= EPS2 * sum:
                return sum
            fac = -fac
            term_bf = abs(term)
        return 1.0 # not converging

    # Uses the Kolmogorov-Smirnov test to determine the probability of wrongly rejecting 
    # the null hipothesis (two empirical distributions being from same distribution)
    def RunKSTest(dist1, count1, dist2, count2):
        
        sigLevel = 0.0

        # TODO: obtain comulative distributions
            cumDist1
            cumDist2
        
        # Calculate KS statistic (max difference between 2 values)
        KSstat = 0.0
        for i in range(len(cumDist1)):
            dist = math.fabs(cumDist1[i] - cumDist2[i])
            KSstat = max(KSstat, dist)
        
        # calculate significance level
        n1 = float(count1)
        n2 = float(count2)
        en = sqrt(n1*n2/(n1 + n2))
        magic = (en + 0.12 + 0.11/en) # magic numbers calculation to bultiply by distance (KSstat)
        sigLevel = ProbKS(magic*KSstat)
        return sigLevel # Probability of wrongly rejecting the null hipothesis (two empirical distributions being from same distribution)


# For use during developnet to test progress
if __name__ == '__main__':
