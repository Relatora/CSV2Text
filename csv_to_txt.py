"""
    csv2txt.py - Converts Employees csv table to text table after
                 appending new rate and modifying table headers accordingly
                
    @author     Amr Abdallah
    @id         C0744378
    @date ISO   2019/06/15 
"""
## -----------------------------------------------------------------
import os   ## Imports os library
from datetime import date
from datetime import datetime
## -----------------------------------------------------------------
## Global variables are declared here beacuase I was attempting
## a solution with pandas
csvFile = "Employees.csv"           ## Declare source CSV file path
exists = os.path.isfile(csvFile)    ## Boolean flag for csv file existance
NEW_RATE = 1.0385                   ## New Rate

## ---------------------------------------------------------------------------------------------------
## This Function Converts a CSV file to a properly formated Text file
## Uses normal python to to make conversion
def convertCSV2TXT():
    txtFile = "Employees.txt"    ## Declare destination txt file path
    
    if exists:                          ## Uses exist boolean var to see if the source file exists
        rfile=open(csvFile,'r')         ## opens source file for reading after confirming it's existance
        wfile = open(txtFile,'w+')      ## opens detination file for writing
        firstline=[]                    ## Initializes an Empty list for first line
        lineList = [line.rstrip('\n') for line in rfile ]   ## loops through source file getting it's lines 
        firstLine = lineList[0].split(",")      ## Splits First line to list items
        firstLine.append("New_rate")            ## adds new_rate to firstLine list
        firstLine.pop(0)                        ## removes Employee ID
        firstLine.pop(0)                        ## removes First_name
        firstLine.pop(0)                        ## removes Last_name
        firstLine.insert(0,"Employee name")     ## insert Employee name
        firstLine.pop(2)                        ## removes hire_rate
        firstLine.pop(1)                        ## removes hire date
        firstLine.insert(1,"Hire date")         ## change character casing of hire date
        firstLine.insert(2,"Old_rate")          ## replaces hire_rate by old_rate
        lineList.pop(0)                         ## removes old table headers from non-table header list
        lineList.insert(0,firstLine)            ## replaces with new table headers
        lineList.insert(1,["-------------","----------","---------","---------"])
        lineCounter = 0                         ## Intialize Line Counter
        lineItems=[]                            ## Intialize lineItems list
        
        for line in lineList:                   ## sifts through line list updating it's value to assginment requirments
            if lineCounter > 1 and lineCounter < len(lineList):                 ## Skips first two lines (table header)
                lineItems = lineList[lineCounter].split(",")                    ## Splits each line to seperate items for parsing
                lineItems.pop(0)                                                ## Removes Employee ID value
                lineItems.insert(0,(lineItems[0].strip() + " " +
                                    lineItems[1].strip()))                      ## Concat first and last name into Employee Name
                lineItems.pop(1)                                                ## Removes first_name value
                lineItems.pop(1)                                                ## Removes last_name value
                hireDate = datetime.strptime(lineItems[1].strip(),"%Y-%m-%d")   ## datetime object created from hire_date
                lineItems.pop(1)                                                ## Removes hire_date old format 
                lineItems.insert(1, hireDate.strftime("%m-%d-%Y"))              ## Inserts New rate format
                oldRate = lineItems[2]                                          ## stores old rate in a variable
                lineItems.pop(2)                                                ## removes old date
                lineItems.insert(2,('{:.2f}'.format(float(oldRate))))           ## formats old date to 2 decimal places
                lineItems.append(str(round(float(lineItems[2])* NEW_RATE,2)))   ## Adds calculated new rate at the end of the list
                lineList.pop(lineCounter)                   ## removes line based on line counter
                lineList.insert(lineCounter,lineItems)      ## replaces line based on new_rate
              
            lineCounter = lineCounter + 1   ## Accumulator
            
        wfile.write("Output using new rate as old rate * 1.0385\n\n\n")             ## Inserts text file header
        wfile.write("Employee Salary Estimates \n-------------------------\n\n\n")  ## Inserts text file header
        
        for x in lineList:                  ## loop to format table cells
            for i in x:
                row = "{:14}" .format(i)    ## character padding
                wfile.write(row)            ## write to file
            wfile.write("\n")               ## Add line ending
            
        rfile.close     ## Closes csv file
        wfile.close     ## closes txt file
    else:
        print("Employees.csv does not exist") ## if source file doe not exist, the user gets alerted
## -----------------------------------------------------------------------------------------------------------------------
           
## Invokes convertCSV2TXT method
if __name__ == "__main__":
    convertCSV2TXT()



