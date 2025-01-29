str = input()

cro_list = ["dz=", "c=", "c-", "d-", "lj", "nj", "s=", "z="]

for c in cro_list :
    str = str.replace(c, "*")

print(len(str))