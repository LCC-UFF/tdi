from scipy import stats
import matplotlib.pyplot as plt
import numpy as np

mD = 180
sD = 38
distrib_D = stats.norm(loc=mD,scale=sD)
mC = 400
sC = 28
distrib_C = stats.norm(loc=mC,scale=sC)

n = 1000000
sample_D = distrib_D.rvs(size=n)
sample_C = distrib_C.rvs(size=n)
plt.hist(sample_D,bins=100)
plt.hist(sample_C,bins=100)
plt.show()

min_D = 80
max_D = 280
values_D = np.linspace(min_D,max_D,num=1000)
min_C = 220
max_C = 420
values_C = np.linspace(min_C,max_C,num=1000)

probab_D = distrib_D.pdf(x=values_D)
probab_C = distrib_C.pdf(x=values_C)
plt.plot(values_D,probab_D)
plt.plot(values_C,probab_C)
plt.show()

# Monte Carlo
NF = 0
for i in range(n):
    if sample_D[i] > sample_C[i]:
        NF += 1
print(".PF = ",NF/n)


