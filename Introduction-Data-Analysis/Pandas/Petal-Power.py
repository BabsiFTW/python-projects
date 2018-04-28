import pandas as pd

#Upload Csv-file which contains the required data and save it as dataframe
inventory = pd.read_csv("inventory.csv")

#show the first 10 lines of the dataframe "inventory"
print inventory.head(10)

#save the first 10 lines of the dataframe "inventory" in the variable "staten_island"
staten_island = inventory.head(10)

#save only the column "product_description" of the dataframe "product_request"
product_request = staten_island['product_description']
#product_request = staten_island.product_description

#save only the rows of the dataframe "inventory" where the entry for the "location"-column is "Brooklyn" and the entry for the "product_type"-column is "Seeds"
seed_request = inventory[(inventory.location == 'Brooklyn') & (inventory['product_type'] == 'seeds')]

#add the new column "in_stock" and add the entry "True" if the "quantity"-value is bigger than zero
inventory['in_stock'] = inventory.quantity.apply(lambda x: True if x > 0 else False)

#add the new column "total_value" and add the product of the "price" and "quantity"-value as entry
inventory['total_value'] = inventory.price * inventory.quantity

#add the new column "full_description" and add the string interpolation of the "product_type" and "product_description"-value as entry
inventory['full_description']= inventory.apply(lambda row: \
    '{} - {}'.format(row.product_type,
                     row.product_description), axis=1)
                     
print inventory
