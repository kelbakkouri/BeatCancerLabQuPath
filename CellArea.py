import pandas as pd
import os
import re
#This is only for sorting your CSV file if needed
def sort_order(value, category):
    """
    Custom sorting function to rank values in specific order based on category.
    """
    order_dict = {
        'A2780': 0, 'A2780cis': 1,  # First A2780 then A2780cis
        'untreated': 0, 'treated': 1,  # Then untreated before treated
        'Day1': 0, 'Day2': 1, 'Day3': 2, 'Day4': 3, 'Day5': 4, 'Day6': 5, 'Day7': 6, 'Day8': 7, 'Day10': 8
        # Day1 to Day10
    }

    if category == 'cell_line':
        # Sort A2780 first, then A2780cis
        if 'A2780' in value:
            return order_dict['A2780']
        return order_dict['A2780cis']
    elif category == 'treatment':
        # Sort untreated first, then treated
        if 'untreated' in value:
            return order_dict['untreated']
        return order_dict['treated']
    elif category == 'day':
        # Extract day information like 'Day1', 'Day2' etc.
        for day in range(1, 11):  # Allow for Day10
            if f'Day{day}' in value:
                return order_dict[f'Day{day}']
        return -1  # Default if no day is found
    elif category == 'group':
        # Extract group information like 'B4', 'B5', 'B6', 'D4', 'D5', 'D6'
        group_match = re.search(r'_(B|D)(\d)', value)
        if group_match:
            group_type = group_match.group(1)  # B or D
            group_number = int(group_match.group(2))  # Group number 1-6
            # Return tuple to ensure proper sorting:
            # B groups should come first (group_type='B'), then sorted by group number
            if group_type == 'B':
                return (0, group_number)  # B1 -> B2 -> B3 ... B6
            else:
                return (1, group_number)  # D1 -> D2 -> D3 ... D6
        return (2, 0)  # Default return value if no group is found

    return -1  # Default return value if category doesn't match

#THIS WILL CREATE THE COLUMNS OF DATA for CELL COUNTS, SAMPLE AVERAGE AND DAY AVERAGE
def process_csvData(input_file):
    df = pd.read_csv(input_file, header=None)  # No header

    # Create the Third Column: Column 2 (index 1) divided by 140
    df['Third Column'] = df[1] / 140 #140 was my cell size

    # Create the Fourth Column: Average of last 6 rows of the Third Column (only every 6th row) 
    df['Fourth Column'] = None  # Initialize the column as None
    for i in range(5, len(df)):  # Start from row 6 (index 5)
        if i % 6 == 5:  # Every 6th row (0-based index)
            df.at[i, 'Fourth Column'] = df['Third Column'][i - 5:i + 1].mean()

    # Create the Fifth Column: Average of last 3 values of the Fourth Column (only every 18th row)
    df['Fifth Column'] = None  # Initialize the column as None
    for i in range(17, len(df)):  # Start from row 18 (index 17)
        if i % 18 == 17:  # Every 18th row (0-based index)
            df.at[i, 'Fifth Column'] = df['Fourth Column'][i - 17:i + 1].mean()

    # Ensure directory exists before saving
    output_dir = os.path.dirname(input_file)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Save the result to a new CSV (only prepend processed_ to the file name, not the directory)
    output_file = os.path.join("Processed.csv")
    df.to_csv(output_file, index=False, header=False)  # Save without headers

    print(f"Processed data saved to {output_file}")

# Example Files
RFPFile = "D:/Research/A2780 Cell Line/Measurements/sorted_combinedRFP.csv"
CISFile = "D:/Research/A2780 Cell Line/Measurements/sorted_combinedCIS.csv"
#process_csvData(CISFile)
process_csvData(RFPFile)
print("Added needed columns")
