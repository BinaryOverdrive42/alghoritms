import numpy as np
from sklearn.base import BaseEstimator
from sklearn.metrics import mean_squared_error

class SGDRegressor(BaseEstimator):
    def __init__(
        self, 
        eta: float=10 ** -3, 
        n_iter: int=10
    ):
        self.eta = eta
        self.n_iter = n_iter
        self.mse_ = []
        self.weights_ = []
        
    def fit(self, X: np.array, y: np.array):
        X = np.concatenate([np.ones((X.shape[0], 1)), X], axis=1)
        w = np.zeros(X.shape[1])
        for _ in range(self.n_iter):
            for index, item in enumerate(X):
                w[0] += 2 * self.eta * (y[index] - w.dot(item))
                for j in range(len(item)):
                    w[j] += 2 * self.eta * (y[index] - w.dot(item)) * item[j]
                    self.weights_.append(w.copy())
                    self.mse_.append(mean_squared_error(y, X.dot(w)))
        
        self.w_ = self.weights_[np.argmin(self.mse_)]
        
        return self

    def predict(self, X):
        X = np.concatenate([np.ones((X.shape[0], 1)), X], axis=1)
        
        return X.dot(self.w_)