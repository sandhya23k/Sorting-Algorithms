import csv
import time
import json
import pandas as pd

"""
Note : For test cases 7-10, you need to extract the required data (filter on conditions mentioned above)
and rename it to appropriate name as mentioned in the test case descriptions. You need to write the code
to perform this extraction and renaming, at the start of the skeleton file.
"""

column_names= ['tconst', 'primaryTitle', 'originalTitle', 'startYear',
               'runtimeMinutes', 'genres', 'averageRating', 'numVotes', 'ordering',
               'category', 'job', 'seasonNumber', 'episodeNumber', 'primaryName', 'birthYear',
               'deathYear', 'primaryProfession']


#############################################################################################################
# Data Filtering
#############################################################################################################
def data_filtering(filelocation, num):
    """
    Data Filtering is for the test cases from 7 to 10.
    filelocation: imdb_dataset.csv location
    num: if num == 1 -> filter data based on years (years in range 1941 to 1955)
         if num == 2 -> filter data based on genres (genres are either ‘Adventure’ or ‘Drama’)
         if num == 3 -> filter data based on primaryProfession (if primaryProfession column contains substrings
                        {‘assistant_director’, ‘casting_director’, ‘art_director’, ‘cinematographer’} )
         if num == 4 -> filter data based on primary Names which start with vowel character.

    """
    df = pd.read_csv(filelocation)
    if(num==1):
        #NEED TO CODE
        #Implement your logic here for Filtering data based on years (years in range 1941 to 1955)
        df_year = df[(df['startYear'] >= 1941) & (df['startYear'] <= 1955)]
        df_year.reset_index(drop=True).to_csv("imdb_years_df.csv", index=False)

    if(num==2):
        #NEED TO CODE
        #Implement your logic here for Filtering data based on genres (genres are either ‘Adventure’ or ‘Drama’)
        df_genres = df[df['genres'].isin(['Adventure', 'Drama'])]
        df_genres.reset_index(drop=True).to_csv("imdb_genres_df.csv", index=False)
    if(num==3):
        #NEED TO CODE
        #Implement your logic here for Filtering data based on primaryProfession (if primaryProfession column contains
        #substrings {‘assistant_director’, ‘casting_director’, ‘art_director’, ‘cinematographer’} )
        professions_to_include = ['assistant_director', 
                                  'casting_director', 
                                  'art_director',
                                  'cinematographer']
        df_professions = df[df['primaryProfession'].str.contains('|'.join(professions_to_include))]
        df_professions.reset_index(drop=True).to_csv("imdb_professions_df.csv", index=False)
    if(num==4):
        #NEED TO CODE
        #Implement your logic here for Filtering data based on primary Names which start with vowel character.
        df_vowels = df[((df['primaryName'].str[0]) == 'a') |
                       ((df['primaryName'].str[0]) == 'e') |
                       ((df['primaryName'].str[0]) == 'i') |
                       ((df['primaryName'].str[0]) == 'o') |
                       ((df['primaryName'].str[0]) == 'u') |
                       ((df['primaryName'].str[0]) == 'A') |
                       ((df['primaryName'].str[0]) == 'E') |
                       ((df['primaryName'].str[0]) == 'I') |
                       ((df['primaryName'].str[0]) == 'O') |
                       ((df['primaryName'].str[0]) == 'U') ]
        df_vowels.reset_index(drop=True).to_csv("imdb_vowel_names_df.csv", index=False)


#############################################################################################################
#Quick Sort
#############################################################################################################
def pivot_element(arr):
    # Select the middle element as the pivot
    p_value = len(arr) // 2
    return arr[p_value]

def quicksort(arr, columns):
    """
    The function performs the QuickSort algorithm on a 2D array (list of lists), where
    the sorting is based on specific columns of the 2D array. The function takes two parameters:

    arr: a list of lists representing the 2D array to be sorted
    columns: a list of integers representing the columns to sort the 2D array on

    The function first checks if the length of the input array is less than or equal to 1,
    in which case it returns the array as is. Otherwise, it selects the middle element of
    the array as the pivot, and splits the array into three parts: left, middle, right.

    Finally, the function calls itself recursively on the left and right sub-arrays, concatenates
    the result of the recursive calls with the middle sub-array, and returns the final sorted 2D array.
    """
    if len(arr) <= 1:
        return arr
    pi_pivot = pivot_element(arr)
    Arrayleft, Arraymiddle, Arrayright = [], [], []
    for loop_i in range(len(arr)):
        r_arrRow = arr[loop_i]
        v_code = r_arrRow[1:]
        if v_code < pi_pivot[1:]:
            Arrayleft.append(r_arrRow)
        elif v_code == pi_pivot[1:]:
            Arraymiddle.append(r_arrRow)
        else:
            Arrayright.append(r_arrRow)
    sortedLeft = quicksort(Arrayleft, columns)
    sortedRight = quicksort(Arrayright, columns)
    arr= sortedLeft + Arraymiddle + sortedRight
    return arr



    #Output Returning array should look like [['tconst','col1','col2'], ['tconst','col1','col2'], ['tconst','col1','col2'],.....]
    #column values in sublist must be according to the columns passed from the testcases.

#############################################################################################################
#Selection Sort
#############################################################################################################
def selection_sort(arr, columns):
    for loop_i in range(len(arr)):
        lowerIndex = loop_i
        for loop_j in range(loop_i+1, len(arr)):
            if arr[loop_j][1:] < arr[lowerIndex][1:]:
                lowerIndex = loop_j
        arr[loop_i], arr[lowerIndex] = arr[lowerIndex], arr[loop_i]
    return arr

    #Output Returning array should look like [['tconst','col1','col2'], ['tconst','col1','col2'], ['tconst','col1','col2'],.....]
    #column values in sublist must be according to the columns passed from the testcases.

#############################################################################################################
#Heap Sort
#############################################################################################################
def heap_sort(arr, columns):
    """
    The function performs the Heap Sort algorithm on a 2D array (list of lists), where
    the sorting is based on specific columns of the 2D array. The function takes two parameters:

    arr: a list of lists representing the 2D array to be sorted
    columns: a list of integers representing the columns to sort the 2D array on

    The function first builds a max heap from the input array. It then iterates over the
    length of the input array in reverse order, and for each iteration extracts the maximum
    element from the heap and places it at the end of the unsorted part of the array.

    Finally, the function returns the sorted 2D array.
    """
    lengthN = len(arr)

    # Build max heap
    build_max_heap(arr, lengthN, columns)

    # Extract elements one by one
    for loop_i in range(lengthN - 1, 0, -1):
        arr[loop_i], arr[0] = arr[0], arr[loop_i]  # swap
        max_heapify(arr, loop_i, 0, columns)

    return arr

def build_max_heap(arr, lengthN, columns):
    for loop_i in range(lengthN // 2 - 1, -1, -1):
        max_heapify(arr, lengthN, loop_i, columns)

def max_heapify(arr, lengthN, loop_i, columns):
    Arrayleft = 2 * loop_i + 1
    Arrayright = 2 * loop_i + 2
    largestValue = loop_i

    if Arrayleft < lengthN and arr[Arrayleft][1:] > arr[largestValue][1:]:
        largestValue = Arrayleft

    if Arrayright < lengthN and arr[Arrayright][1:] > arr[largestValue][1:]:
        largestValue = Arrayright

    if largestValue != loop_i:
        arr[loop_i], arr[largestValue] = arr[largestValue], arr[loop_i]
        max_heapify(arr, lengthN, largestValue, columns)

    #Output Returning array should look like [['tconst','col1','col2'], ['tconst','col1','col2'], ['tconst','col1','col2'],.....]
    #column values in sublist must be according to the columns passed from the testcases.

#############################################################################################################
#Shell Sort
#############################################################################################################
def shell_sort(arr, columns):
    lenghtN = len(arr)
    halfG = lenghtN // 2
    while halfG > 0:
        for loop_i in range(halfG, lenghtN):
            ValueT = arr[loop_i]
            loop_j = loop_i
            while loop_j >= halfG and arr[loop_j - halfG][1:] > ValueT[1:]:
                arr[loop_j] = arr[loop_j - halfG]
                loop_j -= halfG
            arr[loop_j] = ValueT
        halfG //= 2
    return arr

    #Output Returning array should look like [['tconst','col1','col2'], ['tconst','col1','col2'], ['tconst','col1','col2'],.....]
    #column values in sublist must be according to the columns passed from the testcases.

#############################################################################################################
#Merge Sort
#############################################################################################################

def merge(arrayLeft, arrayRight, columns):
    """
    left: a list of lists representing the left sub-array to be merged
    right: a list of lists representing the right sub-array to be merged
    columns: a list of integers representing the columns to sort the 2D array on

    Finally, after one of the sub-arrays is fully merged, the function extends the result
    with the remaining elements of the other sub-array and returns the result as the final
    sorted 2D array.
    """
    answer = []
    loop_i = loop_j = 0
    while loop_i < len(arrayLeft) and loop_j < len(arrayRight):
        if arrayLeft[loop_i][1:] <= arrayRight[loop_j][1:]:
            answer.append(arrayLeft[loop_i])
            loop_i += 1
        else:
            answer.append(arrayRight[loop_j])
            loop_j += 1
    answer.extend(arrayLeft[loop_i:])
    answer.extend(arrayRight[loop_j:])
    return answer

def merge_sort(data, columns):
    """
    data: a list of lists representing the 2D array to be sorted
    columns: a list of integers representing the columns to sort the 2D array on
    Finally, the function returns the result of the merge operation as the final sorted 2D array.
    """
    if len(data) <= 1:
        return data
    halfMid = len(data) // 2
    arrayLeft = data[:halfMid]
    arrayRight = data[halfMid:]
    arrayLeft = merge_sort(arrayLeft, columns)
    arrayRight = merge_sort(arrayRight, columns)
    return merge(arrayLeft, arrayRight, columns)

    #Output Returning array should look like [['tconst','col1','col2'], ['tconst','col1','col2'], ['tconst','col1','col2'],.....]
    #column values in sublist must be according to the columns passed from the testcases.

#############################################################################################################
#Insertion Sort
#############################################################################################################
def insertion_sort(arr, columns):
    for loop_i in range(1, len(arr)):
        loop_j = loop_i
        while loop_j > 0 and arr[loop_j][1:] < arr[loop_j-1][1:]:
            arr[loop_j], arr[loop_j-1] = arr[loop_j-1], arr[loop_j]
            loop_j -= 1
    return arr

    #Output Returning array should look like [['tconst','col1','col2'], ['tconst','col1','col2'], ['tconst','col1','col2'],.....]
    #column values in sublist must be according to the columns passed from the testcases.

#############################################################################################################
# Sorting Algorithms Function Calls
#############################################################################################################
def sorting_algorithms(file_path, columns, select):
    """
    # file_path: a string representing the path to the CSV file
    # columns: a list of strings representing the columns to sort the 2D array on
    # select: an integer representing the sorting algorithm to be used

    # colum_vals: is a list of integers representing the indices of the specified columns to be sorted.

    # data: is a 2D array of values representing the contents of the CSV file, with each row in
    the array corresponding to a row in the CSV file and each element in a row corresponding to a value
    in a specific column.

    More Detailed Description:

    df= #read imdb_dataset.csv data set using pandas library

    column_vals = convert the columns strings passed from the test cases in the form of indices according to
                  the imdb_dataset indices for example tconst column is in the index 0. Apart from the testcase
                  Columns provided you must also include 0 column in the first place of list in column_vals
                  for example if you have provided with columns {'startYear', 'primaryTitle'} which are in the
                  #indices {3,1}. So the column_vals should look like [0,3,1].

    data = #convert the dataframes into list of sublists, each sublist consists of values corresponds to
           #the particular columns which are passed from the test cases. In addition to these columns, each
           #sublist should consist of tconst values which are used to identify each column uniquely.
           #At the end of sorting all the rows in the dataset by using any algorithm you need to
           #Return : List of tconst strings which are obtained after sorting the dataset.
           #Example data looks like [['tconst string 1', 'startYear value 1', 'primaryTitle String 1'],
                                    #['tconst string 1', 'startYear value 1', 'primaryTitle String 1'],
                                    #................so on ]
                                    # NOTE : tconst string value must be in first position of every sublist and
                                    # the other provided column values with respect to columns from the provided
                                    # test cases must be after the tconst value in every sublist. Every sublist
                                    # Represents one record or row from the imdb_dataset.csv (sublist of values).
    """
    #NEED TO CODE
    #Read imdb_dataset.csv
    #write code here Inorder to read imdb_dataset
    df = pd.read_csv(file_path)
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

    column_vals = [0] + [df.columns.get_loc(col) for col in columns]

    # Convert the dataframe to a 2D array of values
    data = df.iloc[:, column_vals].values.tolist()
    column_vals = [df.columns.get_loc(col) for col in column_names]

#############################################################################################################
# Donot Modify Below Code
#############################################################################################################
    if(select==1):
        start_time = time.time()
        output_list = insertion_sort(data, column_vals)
        end_time = time.time()
        time_in_seconds = end_time - start_time
        return [time_in_seconds, list(map(lambda x: x[0], output_list))]
    if(select==2):
        start_time = time.time()
        output_list = selection_sort(data, column_vals)
        end_time = time.time()
        time_in_seconds = end_time - start_time
        return [time_in_seconds, list(map(lambda x: x[0], output_list))]
    if(select==3):
        start_time = time.time()
        output_list = quicksort(data, column_vals)
        end_time = time.time()
        time_in_seconds = end_time - start_time
        return [time_in_seconds, list(map(lambda x: x[0], output_list))]
    if(select==4):
        start_time = time.time()
        output_list = heap_sort(data, column_vals)
        end_time = time.time()
        time_in_seconds = end_time - start_time
        return [time_in_seconds, list(map(lambda x: x[0], output_list))]
    if(select==5):
        start_time = time.time()
        output_list = shell_sort(data, column_vals)
        end_time = time.time()
        time_in_seconds = end_time - start_time
        return [time_in_seconds, list(map(lambda x: x[0], output_list))]
    if(select==6):
        start_time = time.time()
        output_list = merge_sort(data, column_vals)
        end_time = time.time()
        time_in_seconds = end_time - start_time
        return [time_in_seconds, list(map(lambda x: x[0], output_list))]
