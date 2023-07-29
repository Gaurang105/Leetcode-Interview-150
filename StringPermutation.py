def permute_string(input_str, permute_str=''):
    if len(input_str) == 0:
        print(permute_str)
    else:
        used_char = set()
        for i in range(len(input_str)):
            if input_str[i] not in used_char:
                used_char.add(input_str[i])
                remaining_str = input_str[:i] + input_str[i+1:]
                new_permute_str = permute_str + input_str[i]
                permute_string(remaining_str, new_permute_str)

input_str = "Start"
permute_string(input_str)
