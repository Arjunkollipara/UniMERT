import os
import pandas as pd


input_dir = r"data/audio"  
output_file = r"data/audio.csv"  

# List all CSV files
all_files = [f for f in os.listdir(input_dir) if f.endswith(".csv")]

merged_df = pd.DataFrame()

for file in all_files:
    utt_id = os.path.splitext(file)[0]  
    file_path = os.path.join(input_dir, file)
    
    df = pd.read_csv(file_path)
    df['utterance_id'] = utt_id  
    
    merged_df = pd.concat([merged_df, df], ignore_index=True)

# Save final merged CSV
merged_df.to_csv(output_file, index=False)
print(f"Merged {len(all_files)} files into {output_file}")
