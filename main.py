import file_scraper
from file_scraper import the_file_scraper
import linear_reg
from linear_reg import linear_regression_model
import pandas as pd
import datetime as dt


file_data = the_file_scraper("battery-report.html")
charges = the_file_scraper.return_charge()
dates = the_file_scraper.return_date()

# Creates Data Frame for Linear Regression
columns = list(zip(dates, charges))
df = pd.DataFrame(columns, columns=['Dates','Charge Capacity(mwh)'])
df['Dates'] = pd.to_datetime(df['Dates'])
df['Dates'] = df['Dates'].map(dt.datetime.toordinal)#Lin. Regression doesn't work with string year month time lol
model = linear_regression_model(df)


file = open("out.txt", "w")
file.write(f"RMSE of Model :{model.return_RMSE()}\n")

final_day = df.get("Dates").iloc[-1]

for i in range(12):
    file.write(f"Predicted Battery Charge {i+1} week after: {model.prediction(final_day+i*7)}\n")
    


