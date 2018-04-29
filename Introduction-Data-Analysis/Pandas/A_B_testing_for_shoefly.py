import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')
#print ad_clicks.head()

#create a variable which consists of the amount of views for each utm-source
popular_plattform = ad_clicks.groupby('utm_source').user_id.count().reset_index()

#Create a new column called is_click, which is True if ad_click_timestamp is not null and False otherwise
ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()

#Create a variable which consists of the amount of people who clicked on ads from each utm_source
clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click']).user_id.count().reset_index()
#print clicks_by_source.head()

clicks_pivot = clicks_by_source.pivot(
  columns='is_click',
  index='utm_source',
  values='user_id'
).reset_index()
#print clicks_pivot

clicks_pivot['percent_clicked'] = clicks_pivot[True] / (clicks_pivot[True] + clicks_pivot[False])
#print clicks_pivot
#print ad_clicks.head()

#create a dataframe where it is shown how many people saw ad a and how many saw ad b
distribution_AB_test = ad_clicks.groupby('experimental_group').user_id.count().reset_index()
#print distribution_AB_test

#create a dataframe where it is shown how many percent of the people clicked at ad a and how many percent of them clicked on ad b
percentage_AB_test = ad_clicks.groupby(['experimental_group', 'is_click']).user_id.count().reset_index()
#print percentage_AB_test

percentage_pivot = percentage_AB_test.pivot(
  columns='is_click',
  #index='utm_source',
  index='experimental_group',
  #values='is_click'
  values='user_id'
).reset_index()

percentage_pivot['percent_clicked'] = percentage_pivot[True] / (percentage_pivot[True] + percentage_pivot[False])
#print percentage_pivot

#Start by creating two DataFrames: a_clicks and b_clicks, which contain only the results for A group and B group, respectively.
a_clicks = ad_clicks[ad_clicks.experimental_group == 'A'].reset_index()
b_clicks = ad_clicks[ad_clicks.experimental_group == 'B'].reset_index()


#calculate the percent of users who clicked on the ad by day for 'a_clicks'
percent_by_day_a = a_clicks.groupby(['day', 'is_click']).user_id.count().reset_index()

percent_by_day_a_pivot = percent_by_day_a.pivot(
  columns='is_click',
  index='day',
  values='user_id'
).reset_index()

percent_by_day_a_pivot['percent_clicked_a'] = percent_by_day_a_pivot[True] / (percent_by_day_a_pivot[True] + percent_by_day_a_pivot[False])
#print percent_by_day_a_pivot

#calculate the percent of users who clicked on the ad by day for 'b_clicks'
percent_by_day_b = b_clicks.groupby(['day', 'is_click']).user_id.count().reset_index()

percent_by_day_b_pivot = percent_by_day_b.pivot(
  columns='is_click',
  index='day',
  values='user_id'
).reset_index()

percent_by_day_b_pivot['percent_clicked_b'] = percent_by_day_b_pivot[True] / (percent_by_day_b_pivot[True] + percent_by_day_b_pivot[False])
#print percent_by_day_b_pivot

#Compare the results for A and B
comparison_ad_a_b = percent_by_day_a_pivot.append(percent_by_day_b_pivot)
print comparison_ad_a_b
