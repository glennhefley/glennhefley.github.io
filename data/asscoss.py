import pandas as pd
# pip install pandas
# Load the SWOW-EN dataset
assoc_df = pd.read_csv("strength.SWOW-EN.R123.csv", delimiter='\t')

# Function to get top associations
def get_top_associations(cues, top_n=10):
    results = {}
    for cue in cues:
        filtered = assoc_df[assoc_df['cue'] == cue].sort_values(by='R123.Strength', ascending=False)
        top_assoc = filtered.head(top_n)[['response', 'R123.Strength']].reset_index(drop=True)
        results[cue] = top_assoc
    return results

# Example usage
cues = ["chaos", "war", "peace"]
top_associations = get_top_associations(cues, top_n=10)

# Display results
for cue, assoc in top_associations.items():
    print(f"\nTop associations for '{cue}':\n{assoc}")
