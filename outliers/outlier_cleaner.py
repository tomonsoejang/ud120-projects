#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    errors = net_worths - predictions
    
    ### create a list of tuples
    data = zip(ages, net_worths, errors)
    
    ### get the number of elements for 10% of the overall data
    tenth_percent_of_total_elements = int(0.1 *len(data))
    
    ### sort the data by errors descending order and slice out the first 10% of the data.
    cleaned_data = sorted(data, key=lambda x: x[2])[tenth_percent_of_total_elements:]
    
  
    return cleaned_data

