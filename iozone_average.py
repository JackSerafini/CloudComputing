import pandas as pd

def average_iozone_csv(input_csv, output_csv):
    df = pd.read_csv(input_csv)
    # Define the columns that remain constant (grouping keys)
    group_cols = ["Size (kB)", "Record Length"]
    
    # Define the performance columns to average
    perf_cols = [
        "Write (kB/s)", "Rewrite (kB/s)",
        "Read (kB/s)", "Reread (kB/s)",
        "Random Read (kB/s)", "Random Write (kB/s)"
    ]

    # Group by Size and Record Length and compute the average for each performance metric
    avg_df = df.groupby(group_cols, as_index=False)[perf_cols].mean().round(2)

    # Save the averaged results to a new CSV file
    avg_df.to_csv(output_csv, index=False)
    print(f"Averaged results saved to {output_csv}")