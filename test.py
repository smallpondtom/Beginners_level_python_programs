machine_num, candy_num = input().split()
machine_num = int(machine_num)
candy_num = int(candy_num)

candy_div = []
for x in range(machine_num):
    a = input()
    candy_div.append(int(a))

div = -1
mod = 1000000
opt_robot = -1
ct = 1
for y in candy_div:
    if y < candy_num/2:
        div_i = y
        mod_i = candy_num % y
    else:
        div_i = y
        mod_i = candy_num - y
    if mod_i == mod:
        if div_i > div:
            mod = mod_i
            div = div_i
            opt_robot = ct
    elif mod_i < mod:
        mod = mod_i
        div = div_i
        opt_robot = ct
    else:
        pass
    ct += 1

print(opt_robot)

# ! to do 
# ? I am not sure about this comment
# * I love this comment divider
# TODO: 