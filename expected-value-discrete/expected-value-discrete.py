import numpy as np

def expected_value_discrete(x: list, p: list) -> float:
    a=np.array(x,dtype=float)
    b=np.array(p,dtype=float)
    prod=  np.dot(a,b)
    return float(prod)
        
    