# Laptop_Battery_Life_Regression
Small personal project of mine using linear regression(scikit-learn) to tackle when should laptop batteries should be changed 
This all-purpose project involves me experimenting with linear regression, using the battery life diagnostics generated through windows diagnostics. (Command prompt) -- which provides a HTML file with the same structure every time.

HOWEVER, the process of determining battery life of everyone else's is much more difficult -- as there are different factors that account into the degradation of batteries -- like the temperature the battery operates at(the higher the more damaging), which maybe an exponential factor, or maybe the installation of battery optimization systems that varies from manufactuer to manufacturer.
Not exactly a completely linear or exponential regression process.

The output files are included in the repositories, one including the graph of my linear regression model and the other the RMSE, and predictions for the following 12 weeks(after the last date on the bttery report)

Another future attempt maybe to simply incorporating additional actors without sacraficing the sake of parsimony(simpleness of this model). Like operating temperature, brightness... etc. Which makes it harder to predict(larger rooms for error)

Packages I used:
Matplotlib, ScikitLearn, BeautifulSoup, Pandas, Numpy

