import numpy as np
import scipy.stats as stats

#H0 says that there is no relation between tables1 and table2
#Ha says that there is a relationship between tables
#total_no_of_row=2
#total_no_of_column=4
#alpha=0.05 it is given in problem
#df=(total_no_of_row-1)*(total_no_of_column-1) for this case df=(2-1)*(4-1)=3
#alpha and df used to find value from chi table 
# Define the degrees of freedom and significance level
df = 3  # degrees of freedom
alpha = 0.05  # significance level

no_of_sample=235
row_1=np.array([40,45,25,10])
row_2=np.array([35,30,20,30])
#you can add number of rows and columns as well
sum_r1=np.sum(row_1)
sum_r2=np.sum(row_2)
sum_row=np.array([sum_r1,sum_r2])

#sum of column each element of array 1 with array 2
sum_col=row_1+row_2

#loop for multiply each for finding expected value
expected=[]
for i in sum_row :
    for j in sum_col :
        value=(i*j)/no_of_sample
        expected.append(value)
# concate both row 1 and row 2 for applying formula and getting accurate result
observed=np.concatenate((row_1,row_2))
#formula for calculating chi
chi_calculated=np.sum(np.square(observed-expected)/expected)
print(chi_calculated)


# Get value from chi table
chi_value = stats.chi2.ppf(1 - alpha, df)
print(chi_value)
if chi_value<chi_calculated :
    print("Ha is right")
else:
    print("H0 is right")

