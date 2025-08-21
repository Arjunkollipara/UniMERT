import os
import pandas as pd

input_dir = r"F:\EVERYTHING\arjun folder\college files\4 fourth year\SEM 7\major_project(batch25)\project\data\audio"
output_file = os.path.join(input_dir, "audio.csv")

# Create output file if it doesn't exist
if not os.path.exists(output_file):
    pd.DataFrame().to_csv(output_file, index=False)  # start with empty CSV

all_files = [f for f in os.listdir(input_dir) if f.endswith(".csv") and f != "audio_merged.csv"]

print(f"Found {len(all_files)} files to merge...")

for i, file in enumerate(all_files, start=1):
    utt_id = os.path.splitext(file)[0]
    file_path = os.path.join(input_dir, file)
    
    df = pd.read_csv(file_path)
    df['utterance_id'] = utt_id

    # Append directly to CSV file
    df.to_csv(output_file, mode='a', index=False, header=not os.path.getsize(output_file))

    print(f"[{i}/{len(all_files)}] Merged: {file}")

print(f"\nAll files merged into: {output_file}")
