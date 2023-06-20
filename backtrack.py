# learnign backtrack algorithm

class backtrack:
    def __init__(self):
        pass

    def backtrack(self, a, k, input):
        c = [0] * 2
        ncandidates = 2

        if k == input:
            self.process_solution(a, k)
        else:
            k += 1
            ncandidates = self.construct_candidates(a, k, input, c, ncandidates)
            for i in range(ncandidates):
                a[k] = c[i]
                self.backtrack(a, k, input)

    def construct_candidates(self, a, k, input, c, ncandidates):
        c[0] = True
        c[1] = False
        return ncandidates
    
    def process_solution(self, a, k):
        for i in range(1, k + 1):
            if a[i]:
                print('a[{}] = {}'.format(i, a[i]), end=' ')
        print()

if __name__ == '__main__':
    backtrack().backtrack([0] * 4, 0, 3)
    