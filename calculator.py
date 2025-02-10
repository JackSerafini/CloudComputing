import glob
import os
import numpy as np
import pandas as pd

class Average():
    def __init__(self, path):
        self.path = path

    def iozone(self):
        path = os.path.join(self.path, "Iozone - OK")
        # 1 - Master
        path_M = os.path.join(path, "Master")
        file_paths = glob.glob(os.path.join(path_M, "*.txt"))

        # Adding the first row with column titles
        # column_titles = ["KB", "Reclen", "Write", "Rewrite", "Read", "Reread", "Random Read", "Random Write"]
        # avg_array = np.array([column_titles])
        # avg_array = np.append(avg_array, np.zeros((len(file_paths), len(column_titles) - 1)), axis=1)
        # print(avg_array)
        avg_dataframe = pd.DataFrame(columns=["KB", "Reclen", "Write", "Rewrite", "Read", "Reread", "Random Read", "Random Write"])
        print(avg_dataframe)

        for file_path in file_paths:
            with open(file_path, "r") as file:
                for line in file:
                    line = line.strip()
                    if not line:
                        continue
                    tokens = line.split()
                    try:
                        float(tokens[0])
                    except ValueError:
                        continue
                    # So right now we should have that the line starts with a number
                    avg_dataframe = avg_dataframe._append(pd.Series(tokens, index=avg_dataframe.columns), ignore_index=True)
        print(avg_dataframe)
                