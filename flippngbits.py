# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

def convert_to_base_two(num):
    num = int(num)
    num_list = []
    if num > 1:
        while num > 1:
            num_list.append(str(num % 2))
            num = num // 2
            if num == 1:
                num_list.append("1")
                break
        num_list.reverse()
        return "".join(num_list)
    else:
        return str(num)
        
# print(convert_to_base_two("2147483647"))

def convert_to_base_ten(num):
    num_list = list(num)
    num_list.reverse()
    i = 0
    sum = 0
    for i in range(0,len(num_list)):
        if num_list[i] != 0:
            sum += ((int(num_list[i])) * (2 ** i) )
    return sum

# print(convert_to_base_ten("1111111111111111111111111111111"))
def flipFunction(str_num):
    str_num = list(str_num)
    for i in range(len(str_num)):
        if str_num[i] == "1":
            str_num[i] = "0"
        elif str_num[i] == "0":
            str_num[i] = "1"
    return "".join(str_num)

# Main function
def flippingBits(n):
    n = str(n)  #turn n to string
    # converts to base two
    num = convert_to_base_two(n)
    # convert the num string to 32bits
    if len(num) < 32:
        num = "0" * (32 - len(num)) + num
    # flip the bits
    flipped_num = flipFunction(num)
    # convert to base 10
    return convert_to_base_ten(flipped_num)
print(flippingBits(0))