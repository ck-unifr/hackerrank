#https://www.hackerrank.com/challenges/s10-standard-deviation/problem


if __name__ == "__main__":
    import math

    N = input()
    X = input()

    N = int(N)
    X = X.split(' ')
    X = [int(x) for x in X]

    mean = sum(X) / len(X)

    sd = math.sqrt(sum([math.pow(x - mean, 2) for x in X]) / len(X))

    print(round(sd, 1))
