from sdv.metadata import MultiTableMetadata

metadata = MultiTableMetadata.load_from_json(
    filepath='metadata2.json')


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
synthetic_data['pokemon'].to_csv('synth/pokemon.csv', index=False)
synthetic_data['pokemon_types'].to_csv('synth/pokemon_types.csv', index=False)
synthetic_data['types'].to_csv('synth/types.csv', index=False)


