import numpy as np

def calculate(list):
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")
    arr = np.array(list).reshape(3,3)
    np.mean.__name__ = 'mean'
    np.var.__name__ = 'variance'
    np.std.__name__ = 'standard deviation'
    np.min.__name__ = 'min'
    np.max.__name__ = 'max'
    np.sum.__name__ = 'sum'
    calculations = {fun.__name__: [fun(arr,axis=0).tolist(),fun(arr,axis=1).tolist(),fun(arr)] for fun in [np.mean, np.var, np.std, np.min, np.max, np.sum]}

    return calculations