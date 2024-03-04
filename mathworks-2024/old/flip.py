import pandas as pd

def flip_rows_and_columns(input_file, output_file):
    # Read the input CSV file using pandas
    df = pd.read_csv(input_file)

    # Flip rows and columns
    flipped_df = df.transpose()

    # Write the result to the output CSV file
    flipped_df.to_csv(output_file, index=False)

    print(f"Flipped rows and columns successfully. Result saved to {output_file}")

# Example usage
input_csv_file = 'andrew-seattle.csv'
output_csv_file = 'seattle.csv'
flip_rows_and_columns(input_csv_file, output_csv_file)
