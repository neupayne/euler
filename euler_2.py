def fibo(limit):
    fibo_list = [1, 2]
    while True:
        last_element = fibo_list[-1]
        sondan_ikinci = fibo_list[-2]
        if last_element > limit:
            break
        fibo_list.append(last_element + sondan_ikinci)
    return fibo_list


def sum_even_numbers(fibo_list):
    """
    Returns sum of even numbers in a list.
    """
    sum = 0
    for i in fibo_list:
        if isinstance(i, int) and i % 2 == 0:
            sum += i
    return sum

if __name__ == "__main__":
    limit = 4000000
    fibo_list = fibo(limit)
    print(sum_even_numbers(fibo_list))
    x = sum_even_numbers(['bir', 'iki'])
    print(x)