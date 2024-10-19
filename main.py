n = int(input())
lst1 = [int(input())for i in range(n)]
lst2 = [int(input())for i in range(n)]

def summation(a = lst1, b = lst2):
    updated_list = [a[i] + b[i] for i  in range(n)]
    return updated_list

summed_list = summation(lst1,lst2)
print(summed_list)

def find_min_max(c = summed_list):
    return min(c), max(c)

print(find_min_max(summed_list))
