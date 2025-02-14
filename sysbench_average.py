import pandas as pd

def average_sysbench_csv(input_csv, output_csv):
    df = pd.read_csv(input_csv)
    # Convert columns that should be numeric.
    numeric_columns = [
        "CPU_events_per_sec", "CPU_total_time", "CPU_total_events",
        "CPU_latency_min", "CPU_latency_avg", "CPU_latency_max",
        "CPU_latency_95th", "CPU_latency_sum",
        "CPU_thread_fairness_events_avg", "CPU_thread_fairness_events_stddev",
        "CPU_thread_fairness_exec_avg", "CPU_thread_fairness_exec_stddev",
        "Memory_total_operations", "Memory_mib_transferred",
        "Memory_total_time", "Memory_total_events",
        "Memory_latency_min", "Memory_latency_avg", "Memory_latency_max",
        "Memory_latency_95th", "Memory_latency_sum",
        "Memory_thread_fairness_events_avg", "Memory_thread_fairness_events_stddev",
        "Memory_thread_fairness_exec_avg", "Memory_thread_fairness_exec_stddev"
    ]

    for col in numeric_columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # Compute the overall mean for each numeric column.
    avg_df = df[numeric_columns].mean().to_frame().T.round(2)

    # Compute the new metric: Memory_ops_per_sec.
    avg_df["Memory_ops_per_sec"] = (avg_df["Memory_total_operations"] / avg_df["Memory_total_time"]).round(2)

    # Drop CPU_total_time and Memory_total_time.
    avg_df = avg_df.drop(["CPU_total_time", "Memory_total_time"], axis=1)

    # Save the result.
    avg_df.to_csv(output_csv, index=False)
    print(f"Averaged results saved to {output_csv}")