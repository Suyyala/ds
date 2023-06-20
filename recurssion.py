# learning recurssion in python

# factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
# fibonacci
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
# power
def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent - 1)

# permute
def permute(s):
    out = []
    
    # base case
    if len(s) == 1:
        out = [s]
    else:
        # for every letter in string
        for i, let in enumerate(s):
            # for every permutation resulting from step 2 and 3
            for perm in permute(s[:i] + s[i + 1:]):
                # add it to output
                out += [let + perm]
    
    return out

# coin change
def coin_change(target, coins):
    min_coins = target
    
    if target in coins:
        return 1
    else:
        for i in [c for c in coins if c <= target]:
            num_coins = 1 + coin_change(target - i, coins)
            if num_coins < min_coins:
                min_coins = num_coins
    
    return min_coins

# reverse string
def reverse(s):
    if len(s) <= 1:
        return s
    else:
        return reverse(s[1:]) + s[0]
    
# string combination
def combination(s):
    out = []
    
    # base case
    if len(s) == 1:
        out = [s]
    else:
        # for every letter in string
        for i, let in enumerate(s):
            # for every combination resulting from step 2 and 3
            for comb in combination(s[:i] + s[i + 1:]):
                # add it to output
                out += [let + comb]
    
    return out