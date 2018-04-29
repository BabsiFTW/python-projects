"""
Application should be able to analyze data which was gathered during the following process:
1. A user visits CoolTShirts.com
2. A user adds a t-shirt to their cart
3. A user clicks "checkout"
4. A user actually purchases a t-shirt
"""
import codecademylib
import pandas as pd

#load data
visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])

#print visits.head()
#print cart.head()
#print checkout.head()
#print purchase.head()

#merge dataframes "visits" and "cart"
visits_n_cart = pd.merge(
  visits,
  cart,
  how='left'
)
#print visits_n_cart
#print len(visits_n_cart)

#detect all missing timestamps at the 'cart_time'-column
missing_timestamp = visits_n_cart[~visits_n_cart.cart_time.isnull()]
#print len(missing_timestamp)

#calculate the percentage of how many visitors put an item in the cart
percentage_visits_n_cart = float(len(missing_timestamp)) / float(len(visits_n_cart))

#merge the dataframes 'cart' and 'checkout'
cart_n_checkout = pd.merge(
  cart,
  checkout,
  how='left'
)
#print len(cart_n_checkout)

#detect the missing timestamps within the "checkout_time"-column
missing_timestamp_2 = cart_n_checkout[~cart_n_checkout.checkout_time.isnull()]

#calculate the percentage of how many people added an item to the cart and checked out
percentage_cart_n_checkout = float(len(missing_timestamp_2)) / float(len(cart_n_checkout))

#merge all four dataframes "visits", "cart", "checkout" and "purchase"
all_data = visits.merge(cart, how='left').merge(checkout, how='left').merge(purchase, how='left')
#print all_data.head()

#detect all missing timestamps within the "purchase_time"-column
missing_timestamp_3 = all_data[~all_data.purchase_time.isnull()]

#calculate the percentage of how many people actually bought an item in the end who already checked out
percentage_checkout_n_purchase = float(len(missing_timestamp_3)) / float(len(~all_data.checkout_time.isnull()))

#compare the different percentages and define the stronges and the weakest step
print percentage_visits_n_cart
#weakest step of the process
print percentage_cart_n_checkout
#strongest step of the process
print percentage_checkout_n_purchase

#calculate the average time from initial visit to final purchase
all_data['time_to_purchase'] = all_data.purchase_time - all_data.visit_time
print all_data.time_to_purchase
print all_data.time_to_purchase.mean()
