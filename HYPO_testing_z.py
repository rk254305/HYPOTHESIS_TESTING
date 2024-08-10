import scipy.stats as st
import numpy as np
sample_of_mean=90
mean_of_population=82
standard_deviation_of_population=20
no_of_sample=81
Alpha=0.05

z_cal=(sample_of_mean-mean_of_population)/(standard_deviation_of_population/np.sqrt(no_of_sample))
print(z_cal)

z_table=st.norm.ppf(1-Alpha)
print(z_table)
if z_table<z_cal :
    print("Ha is right")
else :
    print("H0 is right")