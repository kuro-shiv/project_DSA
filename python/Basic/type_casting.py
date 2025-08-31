# Type Casting in Python
# Type casting is converting one data type into another data type.

# Integer to Float
num_int = 10
num_float = float(num_int)  # converts integer to float
print(num_float)  # 10.0
print(type(num_float))  # <class 'float'>

# Float to Integer
num_float2 = 9.8
num_int2 = int(num_float2)  # converts float to integer (truncates decimal)
print(num_int2)  # 9
print(type(num_int2))  # <class 'int'>

# Integer to String
num = 100
num_str = str(num)  # converts integer to string
print(num_str)  # '100'
print(type(num_str))  # <class 'str'>

# String to Integer
str_num = "50"
int_num = int(str_num)  # converts string to integer
print(int_num)  # 50
print(type(int_num))  # <class 'int'>

# String to Float
str_float = "25.5"
float_num = float(str_float)  # converts string to float
print(float_num)  # 25.5
print(type(float_num))  # <class 'float'>

# Integer to Boolean
num_bool = bool(1)  # 0 becomes False, any non-zero becomes True
print(num_bool)  # True
print(type(num_bool))  # <class 'bool'>

# Float to Boolean
float_bool = bool(0.0)  # 0.0 is False, other values True
print(float_bool)  # False
print(type(float_bool))  # <class 'bool'>
