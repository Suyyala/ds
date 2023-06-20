# learning dynamic programming in python

class fib:
    def __init__(self):
        self.memo = {}
    
    def fib(self, n):
        if n < 0:
            raise ValueError('n must be positive')
        elif n <= 1:
            return n
        elif n in self.memo:
            return self.memo[n]
        else:
            result = self.fib(n - 1) + self.fib(n - 2)
            self.memo[n] = result
            return result

class grid:
    def __init__(self):
        self.memo = {}
    
    def grid(self, m, n):
        key = str(m) + ',' + str(n)
        if m == 1 and n == 1:
            return 1
        elif m == 0 or n == 0:
            return 0
        elif key in self.memo:
            return self.memo[key]
        else:
            result = self.grid(m - 1, n) + self.grid(m, n - 1)
            self.memo[key] = result
            return result
        
class can_sum:
    def __init__(self):
        self.memo = {}
    
    def can_sum(self, target_sum, numbers):
        if target_sum == 0:
            return True
        elif target_sum < 0:
            return False
        elif target_sum in self.memo:
            return self.memo[target_sum]
        else:
            for num in numbers:
                remainder = target_sum - num
                if self.can_sum(remainder, numbers):
                    self.memo[target_sum] = True
                    return True
            
            self.memo[target_sum] = False
            return False
        
class how_sum:
    def __init__(self):
        self.memo = {}
    
    def how_sum(self, target_sum, numbers):
        if target_sum == 0:
            return []
        elif target_sum < 0:
            return None
        elif target_sum in self.memo:
            return self.memo[target_sum]
        else:
            for num in numbers:
                remainder = target_sum - num
                remainder_result = self.how_sum(remainder, numbers)
                if remainder_result is not None:
                    remainder_result.append(num)
                    self.memo[target_sum] = remainder_result
                    return remainder_result
            
            self.memo[target_sum] = None
            return None
        
class best_sum:
    def __init__(self):
        self.memo = {}

    def best_sum(self, target_sum, numbers):
        if target_sum == 0:
            return []
        elif target_sum < 0:
            return None
        elif target_sum in self.memo:
            return self.memo[target_sum]
        else:
            shortest_combination = None
            for num in numbers:
                remainder = target_sum - num
                remainder_result = self.best_sum(remainder, numbers)
                if remainder_result is not None:
                    combination = remainder_result.copy()
                    combination.append(num)
                    if shortest_combination is None or len(combination) < len(shortest_combination):
                        shortest_combination = combination
            
            self.memo[target_sum] = shortest_combination
            return shortest_combination
        
class can_construct:
    def __init__(self):
        self.memo = {}
    
    def can_construct(self, target, word_bank):
        if target == '':
            return True
        elif target in self.memo:
            return self.memo[target]
        else:
            for word in word_bank:
                if target.startswith(word):
                    suffix = target[len(word):]
                    if self.can_construct(suffix, word_bank):
                        self.memo[target] = True
                        return True
            
            self.memo[target] = False
            return False
        
class count_construct:
    def __init__(self):
        self.memo = {}
    
    def count_construct(self, target, word_bank):
        if target == '':
            return 1
        elif target in self.memo:
            return self.memo[target]
        else:
            total_count = 0
            for word in word_bank:
                if target.startswith(word):
                    suffix = target[len(word):]
                    num_ways_for_rest = self.count_construct(suffix, word_bank)
                    total_count += num_ways_for_rest
            
            self.memo[target] = total_count
            return total_count
        
class all_construct:
    def __init__(self):
        self.memo = {}
    
    def all_construct(self, target, word_bank):
        if target == '':
            return [[]]
        elif target in self.memo:
            return self.memo[target]
        else:
            result = []
            for word in word_bank:
                if target.startswith(word):
                    suffix = target[len(word):]
                    suffix_ways = self.all_construct(suffix, word_bank)
                    target_ways = list(map(lambda way: [word] + way, suffix_ways))
                    result.extend(target_ways)
            
            self.memo[target] = result
            return result
    
if __name__ == '__main__':
    print('fibonacci')
    f = fib()
    print(f.fib(6))

    print('grid')
    g = grid()
    print(g.grid(3, 3))

    print('can_sum')
    c = can_sum()
    print(c.can_sum(7, [2, 3]))

    print('how_sum')
    h = how_sum()
    print(h.how_sum(7, [2, 3]))

    print('best_sum')
    b = best_sum()
    print(b.best_sum(7, [5, 3, 4, 7]))

    print('can_construct')
    c = can_construct()
    print(c.can_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))

    print('count_construct')
    c = count_construct()
    print(c.count_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))

    print('all_construct')
    a = all_construct()
    print(a.all_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))


    
