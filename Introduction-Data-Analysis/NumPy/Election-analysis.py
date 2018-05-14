import codecademylib
import numpy as np
from matplotlib import pyplot as plt

survey_responses = ['Ceballos', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos','Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos']

#Calculate the number of people who answered 'Ceballos' 
total_ceballos = sum([1 for n in survey_responses if n == 'Ceballos'])
print total_ceballos

#Calculate the percentage of people in the survey who voted for Ceballos
percentage_ceballos = total_ceballos / float(len(survey_responses))
print percentage_ceballos

#Generate a binomial distribution that takes the number of total survey responses, the actual success rate, and the size of the town's population as its parameters
possible_surveys = np.random.binomial(len(survey_responses), 0.54, size=10000) / float(len(survey_responses))
#print possible_surveys

#Calculate the percentage of surveys that could have an outcome of Ceballos receiving less than 50% of the vote
ceballos_loss_surveys = np.mean(possible_surveys < 0.5)
print ceballos_loss_surveys


#Plot a histogram of possible_surveys with a range of 0-1 and 20 bins
plt.hist(possible_surveys, range=(0,1), bins=20)
plt.show()

#Generate another binomial distribution, but this time, see what would happen if you had instead surveyed 7,000 people
large_survey = np.random.binomial(7000, 0.54, size=10000) / 7000.
#print large_survey

#recalculate the percentage of surveys that would have an outcome of Ceballos losing 
ceballos_loss_new = np.mean(large_survey < 0.5)
print ceballos_loss_new
