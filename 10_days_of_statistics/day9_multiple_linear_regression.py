#https://www.hackerrank.com/challenges/s10-multiple-linear-regression/problem

#Input Format
#
# The first line contains 2 space-separated integers,  m (the number of observed features)
# and n (the number of feature sets Andrea studied), respectively.
# Each of the n subsequent lines contain m+1 space-separated decimals;
# the first m elements are features (f_1, f_2, ..., f_m),
# and the last element is the value of Y for the line's feature set.
# The next line contains a single integer, q , denoting the number of feature sets Andrea wants to query for.
# Each of the q subsequent lines contains m space-separated decimals describing the feature sets.

# Output Format
# For each of the q feature sets, print the value of Y on a new line (i.e., you must print a total of q lines).


mn = input()
mn = mn.strip().split(' ')

m = int(mn[0])
n = int(mn[1])

X = []
Y = []
for i in range(n):
    x = input()
    x = x.strip().split(' ')
    x = [float(a) for a in x]
    X.append(x[0:m])
    Y.append(x[m:])

q = input()
q = int(q.strip())

X_test = []
for i in range(q):
    x_test = input()
    x_test = x_test.strip().split(' ')
    x_test = [float(a) for a in x_test]
    X_test.append(x_test)


from sklearn import linear_model

lm = linear_model.LinearRegression()
lm.fit(X, Y)
a = lm.intercept_
b = lm.coef_

Y_test = lm.predict(X_test)
for y_test in Y_test:
    print(round(y_test[0], 2))