import pandas as pd

def average_hpl_csv(input_csv, output_csv):
    df = pd.read_csv(input_csv)
    # Define the columns that remain constant (grouping keys)
    group_cols = ["T/V", "N", "NB", "P", "Q"]

    # Group by these columns and average the GFLOPs column
    avg_df = df.groupby(group_cols, as_index=False)["Gflops"].mean().round(2)

    # Save the result to a new CSV file
    avg_df.to_csv(output_csv, index=False)
    print(f"Averaged results saved to {output_csv}")