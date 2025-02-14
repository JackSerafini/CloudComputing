import pandas as pd
import numpy as np

def average_iperf_csv(input_csv, output_csv):
    df = pd.read_csv(input_csv)
    # Convert the start time to a numeric type and floor it to get the lower second.
    df['start'] = pd.to_numeric(df['start'], errors='coerce')
    df['second'] = np.floor(df['start']).astype(int)

    # Extract the numeric value from the transfer and bitrate columns.
    # This regex extracts the first group of digits and dots.
    df['transfer_num'] = pd.to_numeric(df['transfer'].str.extract(r'([\d.]+)')[0], errors='coerce')
    df['bitrate_num'] = pd.to_numeric(df['bitrate'].str.extract(r'([\d.]+)')[0], errors='coerce')

    # Group by the floored second and compute the average for transfer and bitrate
    avg_df = df.groupby('second', as_index=False)[['transfer_num', 'bitrate_num']].mean().round(2)

    # Rename the columns to indicate these are averages
    avg_df = avg_df.rename(columns={'transfer_num': 'transfer', 'bitrate_num': 'bitrate'})

    # Write the result to a new CSV file
    avg_df.to_csv(output_csv, index=False)
    print(f"Averaged results saved to {output_csv}")