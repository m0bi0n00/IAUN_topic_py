from methods import *

# 1️ capitalize
print(my_capitalize("hello WORLD"))

# 2️ casefold
print(my_casefold("HeLLo PYTHON")) 

# 3️ count
print(my_count("banana", "na")) 

# 4️ endswith
print(my_endswith("hello.py", ".py"))

# 5️ find
print(my_find("python", "th")) 

# 6️ index
print(my_index("python", "on"))

# 7️ isdigit
print(my_isdigit("12345"))  
print(my_isdigit("123a")) 

# 8️ islower
print(my_islower("hello")) 
print(my_islower("Hello")) 

# 9️ isupper
print(my_isupper("WORLD"))  
print( my_isupper("WorLD"))  

#  strip
print(f"'{my_strip('   hello world   ')}'")

# 1️1️ replace
print(my_replace("python python", "python", "java")) 

# 1️2️ rsplit
print( my_rsplit("a,b,c", ",")) 

# 1️3️ lsplit
print(my_lsplit("a,b,c", ",")) 

# 1️4️ swapcase
print(my_swapcase("PyThOn Is CoOl")) 
