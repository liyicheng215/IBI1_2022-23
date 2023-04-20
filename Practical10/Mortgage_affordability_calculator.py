def affordability(value, salary):
    if value <= 5 * salary:
        return 'Yes'
    else:
        return 'No'


# Example for test
test = affordability(180000, 35000)
print('Can the purchaser buy the house? ', test)  # Output: No
