"""
Find the answers for the following questions on the basis of the data collected in the "restaurant.csv"-file:
1. What cuisines does FoodWheel offer? Which areas should the company search for more restaurants to partner with?
2. How has the average order amount changed over time? What does this say about the trajectory of the company?
3. How much has each customer on FoodWheel spent over the past six months? What can this tell us about the average FoodWheel customer?
"""
import matplotlib as plt
import pandas as pd
import numpy

"""What cuisines does FoodWheel offer? Which areas should the company search for more restaurants to partner with?"""

#load csv-file into a dataframe called "restaurants"
restaurants = pd.read_csv('restaurants.csv')
print restaurants.head()

#save the amount of cuisine types in a new variable
cuisine_options_count = restaurants.cuisine.nunique()
print cuisine_options_count

#save the amount of restaurants with a specific cuisine type in a new dataframe called "cuisine_counts"
cuisine_counts = restaurants.groupby('cuisine').id.count().reset_index()
print cuisine_counts

#create a variable which containts the values from the column "cuisine" from "cuisine_counts"
cuisines = cuisine_counts['cuisine']
#create a variable which containts the values from the column "id" from "cuisine_counts"
counts = cuisine_counts['id']
#create a pie chart with the variable "counts" as foundation, "cuisines" as label, a title and percent labels
plt.pie(counts, labels=cuisines, autopct='%d%%')
plt.title('Distribution of cuisine types')
plt.axis('equal')
plt.show()

"""How has the average order amount changed over time? What does this say about the trajectory of the company?"""

#load the data from orders.csv into the DataFrame orders.
orders = pd.read_csv('orders.csv')
#print orders.head()

#create a new column which contains the month that the order was placed
orders['month'] = orders.date.apply(lambda x: x.split('-')[0])
print orders.head()

#create a new dataframe which contains the average order price in each month
avg_order = orders.groupby('month').price.mean().reset_index()
print avg_order

#create a new dataframe which contains the standard deviation for the average price of orders for each month
std_order = orders.groupby('month').price.std().reset_index()
print std_order

#create a set of axes
ax = plt.subplot()
#create a variable with the average prices
bar_heights = avg_order['price']
#create a variable with the standard deviation
bar_errors = std_order['price']

#Create a bar chart with the following attributes: bar_heights as the bar value, bar_errors as error bars, capsize of 5, the months as x-label, a y-label and a descriptive title
plt.bar(range(len(bar_heights)), bar_heights, yerr=bar_errors, capsize=5)
ax.set_xticks(range(len(avg_order)))
#ax.set_xticklabels(avg_order.month)
ax.set_xticklabels(["April", "May", "June", "July", "August", "September"])
plt.ylabel('price')
plt.title("Average amount spent on order for each month")
plt.show()

"""How much has each customer on FoodWheel spent over the past six months? What can this tell us about the average FoodWheel customer?"""

#Calculate the sum of price spent by each customer
customer_amount = orders.groupby('customer_id').price.sum().reset_index()
#print customer_amount.head()

#create a histogram of this data with the following attributes: range from 0 to 200, 40 bins, "Total spent" as x-axis, "Number of customers" as y-axis and an appropriate title
plt.hist(customer_amount.price.values, range=(0,200), bins=40)
plt.xlabel('Total Spent')
plt.ylabel('Number of Customers')
plt.title('Customer purchases over the past six months')
plt.show()
