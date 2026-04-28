"""Data related utility functions."""

__author__ = ["", ""]

from csv import DictReader


def get_keys(
    input_dict: (
        dict[str, list[str]]
        | dict[str, list[int]]
        | dict[str, list[str | int]]
        | dict[str, int]
        | dict[str, str]
    ),
) -> list[str]:
    result: list[str] = []
    for key in input_dict:
        result.append(key)

    return result


def convert_columns_to_int(
    data: dict[str, list[str]], columns_conv: list[str]
) -> dict[str, list[str | int]]:
    """Convert the data in the selected columns to be of type int."""
    # Create new table to store converted data
    data_converted: dict[str, list[int | str]] = {}

    # Iterate through column names (keys of the dictionary)
    for col_name in data:
        # Create new list to append converted values to
        data_converted[col_name] = []

        # Declare the converted value with a type of either int or str
        converted_value: int | str

        # Iterate through data values in the column
        for value in data[col_name]:
            # If this column is in the list of columns to be converted,
            # cast it to an int
            if col_name in columns_conv:
                converted_value = int(value)
            else:
                converted_value = value

            # Add it to the new column of values, the list we created
            # that we have a reference to at data_converted[col_name]
            data_converted[col_name].append(converted_value)

    return data_converted

"""These are the functions we wrote/will write in class!"""
def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a CSV into a 'table'."""
    result: list[dict[str, str]] = []

    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")

    # Prepare to read the data file as a CSV rather than just strings.
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)

    # Close the file when done, to free its resources.
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []

    for row in table:
        item: str = row[column]
        result.append(item)

    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result

def head(table: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Produce a new column-oriented table with only the first n rows of data."""
    result: dict[str, list[str]] = {}
    
    # Iterate over the keys (columns) in the input table
    for column in table:
        # Create an empty list to store the first n values
        first_n_values: list[str] = []
        # Get the list of values for the current column
        column_values: list[str] = table[column]
        
        # Ensure we don't try to take more rows than exist
        limit = n
        if n > len(column_values):
            limit = len(column_values)
            
        # Append the first n values to our list
        for i in range(limit):
            first_n_values.append(column_values[i])
            
        # Assign the list of first n values to the column name in result
        result[column] = first_n_values
        
    return result


def select(table: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Produce a new column-oriented table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}
    
    # Iterate over the names of the columns we want to select
    for name in names:
        # Copy the list of values from the original table to the new one
        result[name] = table[name]
        
    return result


def concat(table1: dict[str, list[str]], table2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-oriented table that is the two tables combined."""
    result: dict[str, list[str]] = {}
    
    # Add all columns from table1 to the result
    for column in table1:
        result[column] = table1[column]
        
    # For each column in table2, if it's already in result, append values.
    # If it's not, add it (though usually concat assumes matching schemas).
    for column in table2:
        if column in result:
            # We need to create a NEW list so we don't mutate table1's list
            combined_list: list[str] = []
            for val in result[column]:
                combined_list.append(val)
            for val in table2[column]:
                combined_list.append(val)
            result[column] = combined_list
        else:
            result[column] = table2[column]
            
    return result


def count(values: list[str]) -> dict[str, int]:
    """Given a list, produce a dictionary where keys are unique values and values are their frequencies."""
    result: dict[str, int] = {}
    
    for item in values:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
            
    return result