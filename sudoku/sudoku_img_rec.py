from tensorflow.keras import datasets
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import Activation
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Dropout

(X_train, y_train), (X_test,
                     y_test) = datasets.mnist.load_data(path="mnist.npz")

X_train = X_train / 255
X_test = X_test / 255
