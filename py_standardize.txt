# Python : Data Scaling
def ZScaler(data) :
    from sklearn.preprocessing import StandardScaler
    z = StandardScaler()
    z.fit(data)
    zdata = z.transform(data)
    n = z.n_samples_seen_
    zdata = zdata * np.sqrt((n-1)/n)
    return zdata

def ZScaler_test(train_data, test_data) :
    from sklearn.preprocessing import StandardScaler
    z = StandardScaler()
    z.fit(train_data)
    zdata = z.transform(test_data)
    n = z.n_samples_seen_
    zdata = zdata * np.sqrt((n-1)/n)
    return zdata

def MinMaxScaler(data) :
    from sklearn.preprocessing import MinMaxScaler
    zm = MinMaxScaler()
    zm.fit(data)
    MinMaxData = zm.transform(data)
    return MinMaxData

def MinMaxScaler_test(train_data, test_data) :
    from sklearn.preprocessing import MinMaxScaler
    zm = MinMaxScaler()
    zm.fit(train_data)
    MinMaxData = zm.transform(test_data)
    return MinMaxData


from sklearn.model_selection import train_test_split
from sklearn import datasets 
iris = datasets.load_iris()
# iris : Bunch object (like dictionaries)
iris.keys()
X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(
     X, y, train_size=0.7, random_state=12345)
X_train.shape()  
X_test.shape()

ZX_train = ZScaler(X_train) 
ZX_test = ZScaler_test(X_train, X_test) 
ZX01_train = ZScaler(X_train) 
ZX01_test = ZScaler_test(X_train, X_test) 