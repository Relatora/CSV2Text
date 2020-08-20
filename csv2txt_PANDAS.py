"""csv2txt.py - Converts Employees csv table to a text table
                after applying new rate
"""
import pandas

def convertPandaPy():
    txtFile = "Employees_Panda.txt"     ## Declare destination txt file path
    
    if exists:
        df = pd.read_csv(csvFile, header=None, names=['Employee_id', 'first_name','last_name','hire_date', 'old_rate','new_rate'],engine='python')
        df = df.drop(df.index[0])
        
        df['new_rate']= df['old_rate']* NEW_RATE
        print(df['new_rate'])
    else:
        print("Employees.csv does not exist") ## if source file doe not exist, the user gets alerted
        
## Calls Functions
if __name__=="__main__":            
    ##convertNormalPy()
    convertPandaPy()
