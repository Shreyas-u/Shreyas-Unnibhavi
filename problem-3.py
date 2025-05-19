def generate_conditional_series(a):
    count = a if a % 2 != 0 else a - 1
    result = []
    num = 1
    while len(result) < count:
        result.append(num)
        num += 2
    return result

if __name__ == "__main__":
    a = int(input("Enter a: "))
    print("Output:", generate_conditional_series(a))
