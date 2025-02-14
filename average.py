from hpl_average import average_hpl_csv
from iozone_average import average_iozone_csv
from iperf_average import average_iperf_csv
from sysbench_average import average_sysbench_csv
import os

output_folder = "./avgs"
csv_folder = "./csv"

for filename in os.listdir(csv_folder):
    output_filename = filename.split('.')[0] + "_avg.csv"
    output_filename = output_filename.replace("test_", "")
    if filename.startswith("hpl_test"):
        average_hpl_csv(os.path.join(csv_folder, filename), os.path.join(output_folder, output_filename))
    elif filename.startswith("iozone_test"):
        average_iozone_csv(os.path.join(csv_folder, filename), os.path.join(output_folder, output_filename))
    elif filename.startswith("iperf_test"):
        average_iperf_csv(os.path.join(csv_folder, filename), os.path.join(output_folder, output_filename))
    elif filename.startswith("sysbench_test"):
        average_sysbench_csv(os.path.join(csv_folder, filename), os.path.join(output_folder, output_filename))
