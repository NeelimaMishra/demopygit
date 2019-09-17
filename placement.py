def func(input):
    index = 0
    output = []
    for i in input:
        if index == 0:
            output.append(0)
            index += 1
            continue
        curr_num = input[index]
        l2 = input[0:index]
        count = 0
        for j in l2:
            if j > curr_num:
                count += 1
        output.append(count)
        index += 1
    print(output)

func([1,2,4,3,9,19,10])

