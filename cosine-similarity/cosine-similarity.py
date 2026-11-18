import numpy as np

def cosine_similarity(a,b):
 x=np.array(a, dtype=float)
 y=np.array(b, dtype=float)
 mag_1=np.linalg.norm(x)
 mag_2=np.linalg.norm(y)
 denominator=(mag_1*mag_2)
 if denominator==0:
     return 0.0
  
 return float(np.dot(x,y)/(denominator))
 
    
