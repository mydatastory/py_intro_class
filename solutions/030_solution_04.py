# We want the minimum number of surveys that reaches everyone once, whoch is the 
# rounded up value of num_nubjects / num_per_survey. This is equivalent to 
# performing an integer division with // and adding 1.

num_subjects = 600
num_per_survey = 42
num_surveys = num_subjects // num_per_survey + 1

print(num_subjects, 'subjects,', num_per_survey, 'per survey:', num_surveys)