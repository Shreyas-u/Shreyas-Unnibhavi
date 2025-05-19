def generate_series(a):
    result = []
    num = 1
    while len(result) < a:
        result.append(num)
        num += 2
    return result

if __name__ == "__main__":
    a = int(input("Enter a: "))
    print("Output:", generate_series(a))
