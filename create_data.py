from sdv.metadata import MultiTableMetadata
from sdv.datasets.local import load_csvs
import plotly.io as pio
import numpy as np

FOLDER_NAME = 'input/'

metadata = MultiTableMetadata.load_from_json(
    filepath='Output/metadata.json')

datasets = load_csvs(folder_name=FOLDER_NAME, read_csv_parameters={'sep':'\t'})

# %%
from sdv.multi_table import HMASynthesizer

# Step 1: Create the synthesizer
synthesizer = HMASynthesizer(
    metadata,
    verbose=True)

# Step 2: Train the synthesizer
synthesizer.fit(datasets)

# Step 3: Generate synthetic data
synthetic_data = synthesizer.sample(1)

# %%
# Save a model
synthesizer.save('synthesizer.pkl')

# Save synthetic dataset
for table in synthetic_data:
    synthetic_data[table].to_csv(f'Output/{table}.csv', index=False, sep ='\t')


