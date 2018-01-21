# https://www.hackerrank.com/challenges/s10-weighted-mean/problem

N = input()
X = input()
W = input()

N = int(N)
X = X.split(' ')
X = [int(x) for x in X]
W = W.split(' ')
W = [int(w) for w in W]

X_weighted = [x*w for x,w in zip(X,W)]
w_mean = round(sum(X_weighted)/sum(W), 1)

print(w_mean)
