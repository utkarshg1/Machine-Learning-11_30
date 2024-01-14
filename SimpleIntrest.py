#This is a example code for Simple Intrest
P = float(input('Please enter the Principal in INR : '))
N = float(input('Please enter Period in Years : '))
R = float(input('Please enter Rate of Intrest in %p.a. : '))

# Calculate Simple Intrest and Amount
I = (P*N*R)/100
A = P + I 

# Print the result
print(f'Simple Intrest : {I:.2f} INR')
print(f'Amount : {A:.2f} INR')