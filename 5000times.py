import numpy as np
nwalks = 5000
nsteps = 1000
mat = np.random.randint(0,2,size=(nwalks, nsteps))
steps = np.where(mat>0,1,-1)
walks = steps.cumsum(1)
print(walks)
