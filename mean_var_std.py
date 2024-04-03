import numpy as np

def calculate(dataList):
    if len(dataList) != 9
        raise ValueError('List must contain nine numbers.')
    reshapedData = np.reshape(np.array(dataList), (3,3))
    calculations = {}
    calculations['mean'] = [np.mean(reshapedData, axis=0).tolist(), np.mean(reshapedData, axis=1).tolist(), np.mean(reshapedData.flatten()).tolist()]
    calculations['variance'] = [np.var(reshapedData, axis=0).tolist(), np.var(reshapedData, axis=1).tolist(), np.var(reshapedData.flatten()).tolist()]
    calculations['standard deviation'] = [np.std(reshapedData, axis=0).tolist(), np.std(reshapedData, axis=1).tolist(), np.std(reshapedData.flatten()).tolist()]
    calculations['max'] = [np.max(reshapedData, axis=0).tolist(), np.max(reshapedData, axis=1).tolist(), np.max(reshapedData.flatten()).tolist()]
    calculations['min'] = [np.min(reshapedData, axis=0).tolist(), np.min(reshapedData, axis=1).tolist(), np.min(reshapedData.flatten()).tolist()]
    calculations['sum'] = [np.sum(reshapedData, axis=0).tolist(), np.sum(reshapedData, axis=1).tolist(), np.sum(reshapedData.flatten()).tolist()]
    return calculations
