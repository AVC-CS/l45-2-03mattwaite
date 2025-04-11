import random


def main():
    import random
    total = 0
    numbers = []
    """
    ########################################
    Code Your Program here
    ########################################
    """
    while total<= 100 :
        random_number = random.randint(1,10)
        numbers.append(random_number)
        total += random_number
    
    last_random_num = numbers.pop()
    
    sum_excluding_last = total - last_random_num
    
    
    print("Sum exlcluding last number:",sum_excluding_last)
    print(f'The random values are {numbers}')
    print(f'The total is {total}')

    ########################################
    # Do not delete the return statement
    ########################################
    return numbers, total


if __name__ == '__main__':
    main()
