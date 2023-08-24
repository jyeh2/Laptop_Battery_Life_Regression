from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error


class linear_regression_model:
    x_train = []
    x_test = []
    y_train = []
    y_test = []
    mse = 0
    rmse = 0
    def __init__(df):
        x = np.array(df.get("Dates")).reshape(-1, 1) 
        y = np.array(df.get("Charge Capacity(mwh)"))

        #Standard 80% training, 20% testing

        linear_regression_model.x_train, linear_regression_model.x_test, linear_regression_model.y_train\
            , linear_regression_model.y_test = train_test_split(x, y, test_size=0.2, random_state=42)

        #Create and train the linear regression model
        model = LinearRegression()
        model.fit(x_train, y_train)

        #Predict y from x
        y_predicted = model.predict(x_test)

        plt.scatter(x, y, label="Data")

        plt.plot(x_test, y_predicted, color='red', label="Regression Line")

        plt.xlabel("Date(Ordinal)")
        plt.ylabel("Charge Capacity")
        plt.legend()
        plt.show()

        #RMSE
        mse = mean_squared_error(y_test, y_predicted)

        rmse = np.sqrt(mse)

        #1287 megawatt hours <- not bad


    
    @staticmethod
    def return_MSE():
        return linear_regression_model.mse
    @staticmethod
    def return_RMSE():
        return linear_regression_model.rmse

