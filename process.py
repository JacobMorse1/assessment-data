# This line is opening the .txt file and setting it
# equal the variable log_file. This allows us to work with the info 
# stored in the .txt file in process.py

log_file = open("um-server-01.txt") 

# This line is a function called sales_reports that takes in the log_file 
# as a parameter

def sales_reports(log_file):
    # This line is a for loop where we are looping over log_file
    for line in log_file:
        # This line is removing any space on the right side of the string
        line = line.rstrip()
        # This line is setting the variable 'day' equal to every 3rd index 
        # starting from the 0 index
        day = line[0:3]
        # This conditional states that if the value of the above indicated index
        # contains the specified string then print the full line
        if day == "Mon":
            print(line)

# Here the function is called and log_file is passed in as a param
sales_reports(log_file)

def greater_ten(log_file):
    for line in log_file:
        line = line.rstrip("/n").split(",")
        # print(line)
        for quantity in line:
            quantity = quantity.rstrip("").split(",")
            print(quantity)
        # amount = line[0::2]
        # if amount >= 10:
        #     print(line)

greater_ten(log_file)