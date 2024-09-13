''' Final Submission

Module: Stancil Solutions - Reusable Module for My Data Analytics Projects

This module provides a simple, reusable foundation for my analytics projects. 
When we work hard to write useful code, we want it to be reusable.
A good byline could be used in every Python analytics project we do.
'''
#####################################
# Declare a global variable named byline.
#####################################

byline: str = 'Stancil Solutions: The Absolute Best'

import statistics

#Declare Global Variables 

#Boolean variable for hybrid workplace
has_hybrid_workplace: bool = True

#Int variable for years in operation
years_in_operation: int = 9

#String List for employee characteristics
employee_characteristics: list = ["Timely", "Personable", "Respectful"]

#Float list for customer satisfaction scores
customer_satisfaction_scores: list = [9.8, 7.8, 8.4, 10, 9.1]

#Calculate basic stats using built in functions min(), max() and statistics modules functions mean() and stdev()
min_score: float = min(customer_satisfaction_scores)
max_score: float = max(customer_satisfaction_scores)
mean_score: float = statistics.mean(customer_satisfaction_scores)
stdev_score: float = statistics.stdev(customer_satisfaction_scores)


byline: str = f"""
-------------------------------------
Stancil Solutions: The Absolute Best
-------------------------------------
Has Hybrid Workplace: {has_hybrid_workplace}
Years in Operation: {years_in_operation}
Employee Characteristics: {employee_characteristics}
Customer Satisfaction Scores: {customer_satisfaction_scores}
Minimum Satisfaction Score: {min_score}
Maximum Satisfaction Score: {max_score}
Average Satisfaction Score: {mean_score}
Standard Deviation Satisfaction Score: {stdev_score}
"""


#####################################
# Define the get_byline() Function
#####################################

def get_byline() -> str:
    '''Return a byline for my analytics projects.'''
    return byline

#####################################
# Define a main() function for this module.
#####################################

# The function now calls get_byline() to retrieve the byline.

def main() -> None:
    '''Print the byline to the console when this function is called.'''
    print(get_byline())

#####################################
# Conditional Execution - Only call main() when executing this module as a script.
#####################################

if __name__ == '__main__':
    main()
