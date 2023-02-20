import is_prime as ip


def prime_numbers(number):
    list = [i for i in range(2, number+1) if ip.is_prime(i)]
    # list = []
    # for i in range(2, number+1):
    #     if ip.is_prime(i):
    #         list.append(i)
    return list


if __name__ == '__main__':
    try:
        num = int(input("enter:"))
    except:
        pass

    prime_numbers(num)
