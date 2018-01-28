# https://www.hackerrank.com/challenges/s10-spearman-rank-correlation-coefficient/problem

#Task
# Given two -element data sets X and Y,
# calculate the value of Spearman's rank correlation coefficient.


#https://codereview.stackexchange.com/questions/65031/creating-a-list-containing-the-rank-of-the-elements-in-the-original-list
def get_rank_list(X):
    seq = sorted(X)
    index = [seq.index(x) for x in X]
    index = [i+1 for i in index]
    return index

N = input()
X = input()
Y = input()

N = int(N)
X = X.strip().split(' ')
X = [float(x) for x in X]
Y = Y.strip().split(' ')
Y = [float(y) for y in Y]

rank_X = get_rank_list(X)
rank_Y = get_rank_list(Y)

d = [(r_x - r_y)**2 for r_x, r_y in zip(rank_X, rank_Y)]

r_xy = 1 - (6*sum(d) / (N*(N**2-1)))

print(round(r_xy, 3))





