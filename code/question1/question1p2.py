
import pandas as pd
import os

#gets a file and cleans it by removing duplicate rows and makes sure the dates are real dates and makes sure the value is a number
def preprocessing(file_path,processed_file):
    df = pd.read_excel(file_path, sheet_name=None)
    df= df['time_series']
    print( df.head())

    df.drop_duplicates(subset=['timestamp'],inplace=True) #drops duplicates
    df.dropna(subset=['value'],inplace=True) #drops rows with NaN or empty values
    
    for line in df.index.copy(): #goes through all the lines (copy of the original indexis)
        
        val = df["value"][line] #get the value of the line
        print("type of line", line, type(val), val) #print the type of the value

        if type(val) is not float and type(val) is not int: #check if the value is not a float or int
           print("not a float or int line", line, val)
           df.drop(line,axis=0, inplace=True) #drops the row if the value is not a float or int

        else:
            
            try:
                print(df["timestamp"][line])
                df.loc[line, "timestamp"] = pd.to_datetime(df["timestamp"][line], format='%m/%d/%Y %H:%M')
                print(df["timestamp"][line])
            except ValueError:
                print("droped line", line)
                df.drop(line, inplace=True)
            
    print(df.head())
    df.to_excel(processed_file, index=False, header=True) #savea the data to a new excel file

#gets a file and calculates the meand per hour of the values, and puts the results in mean_file
def average_hour_long_way(file_path, mean_file):
    df = pd.read_excel(file_path, sheet_name=None)
    df= df['Sheet1']
    print(type(df["timestamp"][0]), df["timestamp"][0])
    
    df["timestamp"] = pd.to_datetime(df["timestamp"], format='%m/%d/%Y %H:%M')# converts the timestamp column to datetime
    
    # sets the timestamp column as the index
    df.set_index("timestamp", inplace=True)
    print(df.head())

    hourly_data = df.resample("h").mean().dropna() #resample the data to hourly data and then does mean and drops the rows that there is no mean- empty
    print(hourly_data.head())

    hourly_data.to_csv(mean_file, index=True, header=True) #save the data to a csv file



# gets a big file and splits it to smaller files by day.
def split_byDay(file_path):
    chunk_size =10
    file_size = 300 #the file has 300 rows
    for start_row in range(0, file_size, chunk_size):
        # reads a chunk of rows from the file, nrows at a time
        chunk = pd.read_excel(file_path, sheet_name="Sheet1", skiprows=range(1, start_row), nrows=chunk_size)
        print(chunk.head()) 
        len = chunk.shape[0] #gets the length of the chunk
        print("length of the chunk", len)
        
        chunk['timestamp'] = pd.to_datetime(chunk['timestamp'])

        for line in chunk.index:
            # Extract the day (format it as 'YYYY-MM-DD')
            day = chunk["timestamp"][line].strftime("%Y-%m-%d")
            print("day:", day)

            check_file = f"byDay_{day}.xlsx"
            #checks if the file already exists. if it does then appends to the end of it if not then creats a new file
            if os.path.exists(check_file):
                #appends
                with pd.ExcelWriter(check_file, mode="a", engine="openpyxl", if_sheet_exists="overlay") as writer:
                    chunk.iloc[[line]].to_excel(writer, index=False, header=True, sheet_name="Sheet1")
            else:
                # creats a new file
                with pd.ExcelWriter(check_file, mode="w", engine="openpyxl") as writer:
                    chunk.iloc[[line]][["timestamp", "value"]].to_excel(writer, index=False, header=True, sheet_name="Sheet1")

            print(f"Processed row {line} for {day}")

#claculates the mean for each file per hour
def calc_mean_byDay():
    print("in calc_mean_byDay")
    files = os.listdir(".") #gets all the files in this directory
    
    byDay_files = [f for f in files if f.startswith("byDay_") and f.endswith(".xlsx")] #finds all the byDay files
    print("byDay_files", byDay_files)
    
    #goes through all the mean files and calculates the mean for each file per hour
    for file in byDay_files:
        file_path = file.replace(".xlsx", ".csv")  # changes the file extention to .csv
        file_path = f"mean_{file_path}"  # adds mean to the begging of the file name
        average_hour_long_way(file, file_path)  # calls the function from the long way that works on small data

#finds all the mean files and combines them into one file
def combine_all_byDay_files ():
     print("in combine_all_byDay_files")
     files = os.listdir(".") #gets all the files in this directory
     for file in files:
        if file.startswith("mean_byDay_") and file.endswith(".csv"): #finds all the mean files
            df = pd.read_csv(file)
            df.to_csv("mean_all.csv", mode="a", index=False, header=False) #appends the mean to the end of the combined file


#calculates the mean per hour using chunks
def average_hour_short(processed_file):
    print(" in average_hour_short")

    split_byDay(processed_file) #creats the byDay files
    calc_mean_byDay() #creates the mean files
    combine_all_byDay_files() #combines all the mean files into one file

def convert_to_excel(parquet_file, excel_file):
   
    df = pd.read_parquet(parquet_file) #reads the Parquet file into a DataFrame

    print(df.head())
    
    df = df[["timestamp", "mean_value"]] #takes only these 2 columns 
    print(df.head())

    df.to_excel(excel_file, index=False, engine='openpyxl')#saves the file in an excell format

    print(f"{parquet_file} has bean converted to {excel_file}")


log_file = "time_series_small.xlsx" #question1/time_series.xlsx"  # input file
processed_file = "time_series_small_preprocessed.xlsx"


parquet_file = 'time_series (4).parquet'  
excel_file = 'converted_time_series.xlsx'  
convert_to_excel(parquet_file, excel_file)



# # clean the data and save it to a new file
# preprocessing(log_file, processed_file)

# #calculates the mean per hour using the long way
# average_hour_long_way(processed_file)

# #calculates the mean per hour using the short way meant for bigdata
# average_hour_short(processed_file)

"""
the the data was coming as a stream that means getting a row at a time i would open the mean_all file
find the matching day and time and do sum with the mean and devide by 2. and write the value back to the file.
if im getting a few "rows " by stream then upload the file do all the changes and then write back to the file after all the changes.
"""

"""
.parquet format is a file format that is good for storing big data. it stores the data column based and not row based like csv format.
it works good when you would want to do stuff on the column like find the mean of the column. so it doesnt need to read the whole file just that colums.
its compressed and takes less space.
its faster to read and write than csv format.
"""
