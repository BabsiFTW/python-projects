"""You work in marketing for a food company YummyCorps, which is developing a new kind of tasty, 
wholesome cereal called CrunchieMunchies. You want to demonstrate to consumers how healthy your cereal is in comparison 
to other leading brands, so you've dug up nutritional data on several different competitors. 
Your task is to use NumPy statistical calculations to analyze this data and prove that your  CrunchieMunchies cereal 
is the healthiest choice for consumers."""

import numpy as np

#Load the CSV-file 'cereal.csv'
calorie_stats = np.genfromtxt('cereal.csv', delimiter=',')

#Calculate the average
average_calories = np.mean(calorie_stats)
#print average_calories

#Calculate the median
calorie_stats_sorted = np.sort(calorie_stats)
print calorie_stats_sorted
median_calories = np.median(calorie_stats_sorted)
#print median_calories

#Calculate the first and third quartile
first_quarter = np.percentile(calorie_stats_sorted, 25)
print first_quarter
third_quarter = np.percentile(calorie_stats_sorted, 75)
print third_quarter

#Calculate the interquartile range
interquartile_range = third_quarter - first_quarter
print interquartile_range

#find the lowest percentile that is greater than 60 calories
nth_percentile = np.percentile(calorie_stats_sorted, 4)
print nth_percentile

#calculate the percentage of cereals that have more than 60 calories per serving
more_calories = np.mean(calorie_stats_sorted > 60)
print more_calories

#Calculate the amount of variation by finding the standard deviation
calorie_std = np.std(calorie_stats_sorted)
print calorie_std
