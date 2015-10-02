'''
Created on Dec 14, 2011

@author: pablocelayes
'''

import ContinuedFractions, Arithmetic, RSAvulnerableKeyGenerator


E1 = 0x1e4805a218009c7f779033e3378b07693f56b266786a295b32d7275ae2e2cd3449dac7468cdae9bb04f547ec759e560739e0d448ebba0ded244095fe1d9b900a885ae931ec760715dbdee4acddb6170b036753c8b572c8af9a02ef370d41a0f2009388bfa042b9f1d0d0847e2fd6fd7ac9e231b17cc95d1dec4540681262c919 

N1 = 0x323fada9cfa3c3037e0b907d2cea83b9ad3655092cb04aeed95500bca4e366a06cb4d215c65bb3d630b779d27bdc8dcd907d655acbdcef465e411beb1be3dddaaba20fb058e7850aa355ec1b89358602fde7f8be59d4150770cacc1b77b775f7caa358167b3226515f15fca8a4659fea2c4efb0360e31993dde4d1c199832b89

 

def hack_RSA(e,n):
    '''
    Finds d knowing (e,n)
    applying the Wiener continued fraction attack
    '''
    frac = ContinuedFractions.rational_to_contfrac(e, n)
    convergents = ContinuedFractions.convergents_from_contfrac(frac)
    
    for (k,d) in convergents:
        
        #check if d is actually the key
        if k!=0 and (e*d-1)%k == 0:
            phi = (e*d-1)//k
            s = n - phi + 1
            # check if the equation x^2 - s*x + n = 0
            # has integer roots
            discr = s*s - 4*n
            if(discr>=0):
                t = Arithmetic.is_perfect_square(discr)
                if t!=-1 and (s+t)%2==0:
                    print("Hacked!")
                    return d

# TEST functions

def test_hack_RSA():
    print("Testing Wiener Attack")
    times = 5
    
    while(times>0):
        e,n,d = RSAvulnerableKeyGenerator.generateKeys(1024)
        print("(e,n) is (", e, ", ", n, ")")
        print("d = ", d)
    
        hacked_d = hack_RSA(e, n)
    
        if d == hacked_d:
            print("Hack WORKED!")
        else:
            print("Hack FAILED")
        
        print("d = ", d, ", hacked_d = ", hacked_d)
        print("-------------------------")
        times -= 1
    
if __name__ == "__main__":
    #test_is_perfect_square()
    #print("-------------------------")
    #test_hack_RSA()
    print hack_RSA(E1, N1)
   


    


        
    
