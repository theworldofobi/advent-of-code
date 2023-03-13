with open("numbers.txt") as n:
    numbers = n.read()

### Part 1 ###
def find_total_fuel_reqs(numbers):
    """
    Solves Part 1 (see problem statement for more details)

    Parameter:
    - numbers (list of integers)

    Returns an integer
    """

    ### Replace with your code
    total = 0

    for n in numbers:
        n = (n // 3) - 2
        total += n
    
    return total

# find_total_fuel_reqs(numbers) --> 3331849

### Part 2 ###
def find_added_fuel_reqs(numbers):
    """
    Solves Part 2 (see problem statement for more details)

    Parameter:
    - numbers (list of integers)

    Returns an integer
    """

    ### Replace with your code
    total = 0

    for n in numbers:
        n_total = 0
        
        while n > 0:
            n = find_total_fuel_reqs([n])
            if n > 0:
                n_total += n
        
        total += n_total

    return total

# find_added_fuel_reqs(numbers) --> 4994898

pt1 = find_total_fuel_reqs(numbers)
pt2 = find_added_fuel_reqs(numbers)

print("The answer to part 1 is", pt1)
print("The answer to part 2 is", pt2)