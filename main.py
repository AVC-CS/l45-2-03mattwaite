import random


def main():
    total = 0
    numbers = []
    """
    ########################################
    Code Your Program here
    ########################################
    """
    while total <= 100 :
        random_numbers = random.randint(1, 10)
        if total + random_numbers > 100: 
            break
        numbers.append(random_numbers)
        total += random_numbers
        
    last_random_num = random.randint(1, 10)
    numbers.append(last_random_num)
    total += last_random_num
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
