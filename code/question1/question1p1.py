import pandas as pd

# gets file path and an amount of rows that should be in each chunk.
def split_logs(file_path, x=100000):
    
    df = pd.read_excel(file_path, header=None, names=["RawData"])#reads the excell data into a data frame
    array_size = df.shape[0]/x #gets the size of the array
    print("array_size", array_size)
    error_arr = [{} for _ in range(int(array_size))]#for each chunk creat an empty dictionary
    index =0
    for i in range(0, len(df), x):
        chunk = df.iloc[i:i+x].copy()#creates a chunk of x rows
       
        chunk[["Timestamp", "Error"]] = (
            chunk["RawData"]
            .str.replace("Timestamp: ", "", regex=False) #takes of "Timestamp: "
            .str.replace("Error: ", "", regex=False) #takes of "Error: "
            .str.split(", ", expand=True) #splits it tp 2 columns
        )
        chunk.drop(columns=["RawData"], inplace=True) #drops the raw data column
        print("chunk", chunk[:5],type(chunk))

        #sets the dictionary with 0s
        keys = chunk["Error"].unique() # gets the unique keys from the chunk
        print("keys", keys)
        for key in keys:
            error_arr[index][str(key)] = 0 #adds the keys to the dictionary of dictionaries

        print("error_arr[i] before", error_arr[index])
        for j in chunk.iterrows():
            error_arr[index][str(j[1]["Error"])] += 1 #adds 1 to the error count in the chunks place
        print("error_arr[i] after", error_arr[index])
        index+=1
    return error_arr

#gets an array of errors and returns the top N error in the array
def top_errors(error_arr, N=10):
    sum_dict = {}
    for i in error_arr:#goes through the array
        for error, count in i.items():#within each dictionary goes through the errors
            if error not in sum_dict: #if the error is a new error add it to the dictionary keys
                sum_dict[error] = 0
            sum_dict[error] += count
    sum_dict = sorted(sum_dict.items(), key=lambda x: x[1], reverse=True)#sorts the dictionary by the count of errors in descending order
    print("sum_dict", sum_dict)#prints the top N errors in the dictionary   
    return sum_dict[:N]#returns the top N errors

log_file = "./question1/logs.txt.xlsx"  # input file
N = 3  # number of errors to return
x=100000 #number of rows for each chunk
error_arr_full = split_logs(log_file, x) #retursns an array with dictionaries with their sums per chunk
print("error_arr_full", error_arr_full[:2])
final_arr = top_errors(error_arr_full, N=N)
print(f"top {N} errors {final_arr}")#prints the top N errors

#error arr is an array of dictionaries [{error3: 0, error6: 4}, {error1: 0, error2: 0}, {error4: 0, error5: 0}]

"""
example output for N=3:
sum_dict [('WARN_101', 200098), ('ERR_404', 200094), ('ERR_400', 200069), ('INFO_200', 199931), ('ERR_500', 199808)]
top 3 errors [('WARN_101', 200098), ('ERR_404', 200094), ('ERR_400', 200069)]
"""

"""
ניתוח זמן ריצה :
m=number of rows in the log file
x= the number of rows per chunk
e= the number of uniqu errors in the file

split_logs: O(m) 
top_errors: O(m/x *e) = number of chunks * the number of errors in the chunk. 


ניתוח מקום:
depends on the size of the chunks and the number of errors in the file.
split_logs: m + m/x reads the whole file into a data frame, and creat a chunk the size of m/x.
top_errors: sum_dict is the size of the amount of unique errors there is in the input file.
"""