from classes import *

s = Child() 

print(s.get_super_public_var())
print(s.get_super_protected_var())
# print(s.get_super_private_var())
print(s.call_super_public_method())
print(s.call_super_protected_method())
# print(s.call_super_private_method())