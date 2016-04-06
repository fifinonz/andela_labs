#DS LAB
#Create a function manipulate_data that does the following

#Accepts as the first parameter a string specifying the data structure to be used "list", "set" or "dictionary"
#Accepts as the second parameter the data to be manipulated based on the data structure specified e.g [1, 4, 9, 16, 25] for a list data structure
#Based off the first parameter
#return the reverse of a list or
#add items `"ANDELA"`, `"TIA"` and `"AFRICA"` to the set and return the resulting set
#return the keys of a dictionary.

def manipulate_data(data_type=None, data=None):
    if data_type is 'list':
        return data[-1:: -1]
    if data_type == 'set':
        return set.union(data, ["ANDELA", "TIA", "AFRICA"])
    if data_type == 'dictionary':
        return [key for key, item in data.items()]