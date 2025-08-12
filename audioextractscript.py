import h5py
import pandas as pd
import os

csd_path = r"F:\EVERYTHING\arjun folder\college files\4 fourth year\SEM 7\major_project(batch25)\datasets\CMU-MOSEI\CMU_MOSEI_OpenFace2.csd"
output_dir = "data"
os.makedirs(output_dir, exist_ok=True)

with h5py.File(csd_path, "r") as f:
    covarep_group = f['COVAREP']
    data_group = covarep_group['data']
    utterance_ids = list(data_group.keys())
    print(f"Total utterances: {len(utterance_ids)}")

    for utterance_id in utterance_ids:
        output_path = os.path.join(output_dir, f"{utterance_id}.csv")

        if os.path.exists(output_path):
            print(f"Skipping {utterance_id} (already extracted)")
            continue

        utterance_data = data_group[utterance_id]
        features = utterance_data['features'][:]
        intervals = utterance_data['intervals'][:]

        df = pd.DataFrame(features)
        for col in range(intervals.shape[1]):
            df[f"interval_{col}"] = intervals[:, col]

        df.to_csv(output_path, index=False)
        print(f"Saved extracted features to {output_path}")
