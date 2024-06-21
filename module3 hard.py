def calculate_structure_sum2(*args):
    sum=0
    for i in args:
    #i стал листом
        for x in i:
            if isinstance(x, dict):
                sum=sum + calculate_structure_sum2(x.items())
            else:
                if isinstance(x, int):
                    sum=sum + x
                else:
                    if isinstance(x, str):
                        sum=sum + len(x)
                    else:
                        sum=sum + calculate_structure_sum2(x)
    return sum


data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum2(data_structure)
print(result)