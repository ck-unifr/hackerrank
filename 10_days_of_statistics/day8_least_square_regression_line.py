#https://www.hackerrank.com/challenges/s10-least-square-regression-line/problem

# Task
# A group of five students enrolls in Statistics immediately after taking a Math aptitude test.
# Each student's Math aptitude test score x, and Statistics course grade y, can be expressed as the following list of points (x, y):
# 1. (95, 85)
# 2. (85, 95)
# ...

# If a student scored an 80 on the Math aptitude test, what grade would we expect them to achieve in Statistics?
# Determine the equation of the best-fit line using the least squares method, then compute and print the value of y when x=8.


#Input Format

#There are five lines of input;
# each line contains two space-separated integers describing a student's respective  and  grades:
# 95 85
# 85 95
# 80 70
# 70 65
# 60 70
# If you do not wish to read this information from stdin, you can hard-code it into your program.

X = [95, 85, 80, 70, 60]
Y = [85, 95, 70, 65, 70]


# solution 1
import statistics as st

mean_x = st.mean(X)
mean_y = st.mean(Y)

X_squared = sum([x ** 2 for x in X])
XY = sum([x*y for x, y in zip(X, Y)])

b = (len(X) * XY - sum(X) * sum(Y)) / (len(X) * X_squared - (sum(X) ** 2))
a = mean_y - b * mean_x

print (round(a + 80 * b, 3))

# solution 2
from sklearn import linear_model
import numpy as np

X = np.asarray(X).reshape(-1, 1)

lm = linear_model.LinearRegression()
lm.fit(X, Y)

# print(lm.intercept_)
# print(lm.coef_[0])
#print(lm.coef_[0]*8 + lm.intercept_)

print(round(lm.predict(80)[0], 3))


