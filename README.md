# s24_project_financial
This is the repository for the group project for CMSE202 s24 group 0

by: Jose, Maximus, Nabi, and Insaan

 
 
 
Jose worked on Segment 5, which operates on a dictionary named states_w_cities, which maps states to lists of cities within those states. It first prints each state's name along with the list of cities associated with it. Then, for each city in each state, it calls a function regress() with three arguments: housing, the state, and the city. Insaan was tasked with comparing the different cities. Subsequently, there's a list named adjust_rs containing adjusted R-squared values for regression models associated with each city. After initializing a counter variable, the code iterates over each state and prints the state's name. For each city in the state, it prints the city's name along with its corresponding adjusted R-squared value from the adjust_rs list, using the counter variable as an index. The counter is then incremented to move to the next value in the adjust_rs list. The code essentially prints out information about cities within each state and their associated adjusted R-squared values, presumably for housing-related regression models. However, it doesn't handle missing or invalid data represented by "nan" values in the adjust_rs list, which might lead to errors if not addressed. Max mainly worked on the model. Surprisingly, bigger datasets don't necessarily equate to better models; in fact, they may even diminish accuracy. The crux lies in focusing on pertinent features rather than drowning in a sea of data. In this context, variables like the number of bedrooms and bathrooms, alongside house size and acreage, emerge as crucial predictors. Precision trumps volume; a focused, narrowed dataset has the potential to yield remarkably accurate models. Thus, the essence of effective modeling lies in the strategic selection and utilization of data points, rather than indiscriminate accumulation. By honing in on the most impactful features, real estate brokers can construct regression models that offer insightful predictions, guiding informed decisions in the dynamic property market landscape. It seemed to be very dependent on the location of the data. When we tried to use different datasets in which location was not a feature there seemed to be a very low r squared value. We chose to narrow down the data into locations that were similar. In order to make the project more applicable to us, we narrowed down the location to East Lansing, Michigan. This meant that we could create a model that predicted housing prices based on the data gathered. Narayana mainly worked on the simple web application that uses the model that predicts housing prices using the features that were most correlated. This application runs on Dash and has some simple callback functions that allow the user to input their own data into the application to see the predicted value of houses. 


How to run the project:

Open the CSV file. 
Run the ipynb file.
Run the app.py file.
Click on the local server link.
Input your features.
