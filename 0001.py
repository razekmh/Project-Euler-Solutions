# list_x = []
# val_x = 0 
# for i in range (1, 1000):
#     if (i % 5 ==0) or (i % 3 ==0):
#         list_x.append(i)
#         val_x += i
# print (list_x, val_x)


target = 999 
def sum_div_by(n):
    p = int(target / n)
    return int ((n * (p * ( p + 1))) / 2)

output = sum_div_by(3)+sum_div_by(5)-sum_div_by(15)
print(output)
