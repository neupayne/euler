x = 1000
output_list = list()
for i in range(0, x):
    if i % 3 == 0 or i % 5 == 0:
        output_list.append(i)

output_sum = sum(output_list)
print(output_sum)
