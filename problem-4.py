def count_multiples(lst):
    result = {i: 0 for i in range(1, 10)}
    for num in lst:
        for i in result:
            if num % i == 0:
                result[i] += 1
    return result

if __name__ == "__main__":
    input_list = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
    print("Input List:", input_list)
    print("Output:", count_multiples(input_list))
