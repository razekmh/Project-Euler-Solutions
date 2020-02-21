even_list = []
even_accum = 0
current_val = 1
while current_val < 4000000:
    current_val =+ current_val
    if current_val % 2 == 0:
        even_accum += current_val
        even_list.append(current_val)

print (even_accum)
print(even_list)