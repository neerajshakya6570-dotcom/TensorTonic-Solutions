import numpy as np

def bernoulli_pmf_and_moments(x: list, p: float) -> dict:
    x=np.array(x,dtype=float)
    p=np.array(p,dtype=float)
    pmf= np.where(x==1,p,1.0-p)
    mean=float(p)
    var=float(p*(1.0-p))
    return {
        "pmf":pmf,
        "mean":mean,
        "variance":var
    }