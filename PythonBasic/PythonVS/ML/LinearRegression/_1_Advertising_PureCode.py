import pandas as pd
import matplotlib.pyplot as plt


dataFrame = pd.read_csv("..\Advertising.csv")
X = dataFrame.values[:, 2]
Y = dataFrame.values[:, 4]

plt.scatter(X, Y, marker='o')
plt.show()


def predict(newRadio, w, b):
    return w * newRadio + b


def cost_function(X, Y, w, b):
    n = len(X)
    sumError = 0
    for i in range(n):
        sumError += (Y[i] - (w * X[i] + b)) ** 2
    return sumError / n


def update_weight(X, Y, w, b, lr):
    n = len(X)
    w_temp = 0.0
    b_temp = 0.0
    for i in range(n):
        w_temp += -2 * X[i] * (Y[i] - (w * X[i] + b))
        b_temp += -2 * (Y[i] - (w * X[i] + b))
    w -= lr * (w_temp / n)
    b -= lr * (b_temp / n)
    return w, b


def train(X, Y, w, b, lr, itr):
    cos_his = []
    for i in range(itr):
        w, b = update_weight(X, Y, w, b, lr)
        cost = cost_function(X, Y, w, b)
        cos_his.append(cost)

    return w, b, cos_his


w, b, cost = train(X, Y, 0.03, 0.0014, 0.001, 60)
print(w)
print(b)
print(predict(19, w, b))
solanlap = [i for i in range (60)]
plt.plot(solanlap, cost)
plt.show()
