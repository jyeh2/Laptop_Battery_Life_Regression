from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np

class linear_regression_model:
    x_train = []
    x_test = []
    y_train = []
    y_test = []
    mse = 0
    rmse = 0
    def __init__(self,df):
        x = np.array(df.get("Dates")).reshape(-1, 1) 
        y = np.array(df.get("Charge Capacity(mwh)"))
        #Standard 80% training, 20% testing
        self.x_train, self.x_test, self.y_train\
            , self.y_test = train_test_split(x, y, test_size=0.2, random_state=42)

        #Create and train the linear regression model
        model = LinearRegression()
        model.fit(self.x_train, self.y_train)
        
        #Predict y from x
        y_predicted = model.predict(self.x_test)
        #plt.yticks(np.arange(np.min(self.y_train), np.max(self.y_train), 200))
        plt.scatter(self.x_test, self.y_test, label="Test Data", marker='x', s=10)
        
        plt.plot(self.x_test, y_predicted, color='red', label="Regression Line")

        plt.xlabel("Date(Ordinal)")
        plt.ylabel("Charge Capacity")
        plt.legend()
        plt.show()

        #RMSE
        linear_regression_model.mse = mean_squared_error(self.y_test, y_predicted)

        linear_regression_model.rmse = np.sqrt(self.mse)

        #1287 megawatt hours <- not bad


    
    @staticmethod
    def return_MSE():
        return linear_regression_model.mse
    @staticmethod
    def return_RMSE():
        return linear_regression_model.rmse

