nums = [i for i in range(1, 11)]
chotnie = [num for num in nums if num %2 == 0]
nechotnie = [num for num in nums if num %2 != 0]

print(chotnie, nechotnie)