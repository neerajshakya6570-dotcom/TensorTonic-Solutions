import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    # Write code here
    s= np.var(x,ddof=1)
    sd= np.sqrt(s)
    return{
        "variance": float(s),
        "standard_deviation": float(sd)
    }
        
    