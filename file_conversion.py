# Description: This program converts time from 12-hour to 24-hour format

def timeConversion(value):
    #checks if the last 2 characters of the value are string characters
    if value[-2:].isalpha():
        if value[-2:] == "AM":
            #if the last 2 characters are AM, return the value without the last 2 characters
            
        
            if value[:2] == "12":
                value = "00" + value[2:]


        elif value[-2:] == "PM":
            #if the last 2 characters are PM, return the value without the last 2 characters
            
            hours = int(value[:2])
            hours += 12
            value = "{:s}{:s}".format(str(hours), value[2:])
            

    return value[:-2]

#value to be checked
value = "01:45:54AM"
print(timeConversion(value))
