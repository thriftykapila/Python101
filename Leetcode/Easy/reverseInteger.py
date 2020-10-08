
# Solution 1 - Working
# def reverse(x):
#     y = ""
#     if int(x) <= -1:y="-";x = int(x)*-1
#     output =  int(y+str(x)[::-1])
#     if output >= -2**31 and output <= 2**31 - 1:return output
#     else: return 0

# print(reverse(-123))

# Solution 2 - working

# def reverse(x: int):
#         n = 0
#         s = 0
#         if x < 0:
#             s = 1
#             x = abs(x)
#         while x != 0:
#             m = 0
#             m = x%10
#             n = n*10 + m
#             x = int(x/10)
#         if s == 1:
#             n *= -1
#         if n >= -2**31 and n<= 2**31:
#         # if n >= -2147483648 and n<= 2147483647:
#             return n
#         else:
#             return 0

# print(reverse(-129834567))

# Solution to convert positive number using reverse method of list

# def reverse( x: int):
#   res = [int(i) for i in str(x)]
#   res.reverse()
#   s = [str(i) for i in res]
#   out = int("".join(s))
#   return out
# print(reverse(321))

# Solution to convert positive number using slice method of string

# def reverse( x: int):
#   inputstring = str(x)
#   return int(inputstring[::-1])
# print(reverse(3213))
