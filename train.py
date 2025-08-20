import h5py 
import pandas as pd
import os

csd_path = r"F:\EVERYTHING\arjun folder\college files\4 fourth year\SEM 7\major_project(batch25)\datasets\CMU-MOSEI\CMU_MOSEI_Labels.csd"
output_dir = "data"
os.makedirs(output_dir, exist_ok=True)

with h5py.File(csd_path, "r") as f:
    key=f.keys()
    print(f"keys : {list(key)}")
    label_group = f['All Labels']
    print(f"glove_vectors_group keys : {list(label_group.keys())}")
    data_group = label_group['data']
    print(f"data_group keys : {list(data_group.keys())}")