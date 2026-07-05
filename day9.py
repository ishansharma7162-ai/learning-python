string_num1 = "18" # yeh abhi string hai
string_num2 = "7" # yeh bhi string hai 
# int() func ka use karke string ko num banaya
real_num1 = int( string_num1)
real_num2 = int(string_num2)
print(real_num1 + real_num2) # output aayega:22 ek dum perfect
string_num3 = "2025" 
string_num4 = "2704"
real_num3 = int(string_num3)
real_num4 = int(string_num4)
print(real_num3 + real_num4)
string_num5 = "51" 
string_num6 = "49"
real_num5 = int(string_num5)
real_num6 = int(string_num6)
print(real_num5 + real_num6)
a = 7  # yeh ek integer hai 
b = 3.5 # yeh ek float hai 
c = a + b # yeh dono k sum hai 
print(c) 
print(type(c)) # output aayega: <class 'float'>
# Explicit typecasting ki practice 
x = 50 
y = 40
# x ko int mein badla tabhi y k sath judega
sum_result = int(x) + y 
print(sum_result) 
# implicit typecasting ki practice 
p = 10 
q = 1.5 
print("implicit sum:", p + q)
