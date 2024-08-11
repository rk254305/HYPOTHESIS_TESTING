import scipy.stats as st
import numpy as np
# H0 popolation_mean=150 Ha population_mean<150
# if population mean is not given then it become 0
# for single question
sample_mean=148
population_mean=150
standard_deviation_of_sample=5
no_of_sample=25
degree_of_freedom=no_of_sample-1
t_table=st.t.ppf(1-0.05,degree_of_freedom)
print(t_table)
t_cal=(sample_mean-population_mean)/((standard_deviation_of_sample)/np.sqrt(no_of_sample))
print(t_cal)
if t_table>t_cal:
    print("Ha is right")
else :
    print("H0 is right")

#hypothesis : if H0=VALUE and Ha>VALUE then right tailed test if Ha <VALUE left tailed test if Ha = VALUE two tailed test

'''
  for comparing two companies
 H0 population_mean_A=population_mean_B  , HA population_mean_A!=population_mean_Btwo tailed test take place
sam_a=80
sam_b=75
population_mean_A=0
population_mean_B=0
standard_deviation_of_sample_A=5
standard_deviation_of_sample_B=6
no_of_sample=20
degree_of_freedom=((no_of_sample+no_of_sample)-2) #2 because of different company
t_table=st.t.ppf(1-0.025,degree_of_freedom)
print(t_table)
#t_cal=(sam_a-sam_b)(-population_mean_A-population_mean_B)/np.sqrt((25/20)+(36/20))
print(t_cal)
'''