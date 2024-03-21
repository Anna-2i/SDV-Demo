# LOADING DATA

from sdv.datasets.local import load_csvs

datasets = load_csvs("input/")

# CREATING METADATA

from sdv.metadata import MultiTableMetadata

#metadata is loaded and detected
metadata = MultiTableMetadata()

metadata.detect_from_dataframes(
    datasets
)

# MODIFY METADATA

#Access metadata dictionary (metadata is represented as a dict or SDV object, here we do dict)
metadata_dict = metadata.to_dict()

# we need to make sure keys that are related as primary-foreign are the same data type in order to establish the relationship
# Modify the data type of 'id' in the 'pokemon' table to 'id'


#  Update columns with Unknown types
metadata.update_column(table_name="pokemon", column_name="pokemon", sdtype="categorical")
metadata.update_column(table_name="pokemon", column_name="pokemon_order", sdtype="id")
metadata.update_column(table_name="types", column_name="type_name", sdtype="categorical")

#print(metadata_dict.get('type_id'))

# VISUALISE METADATA

metadata.visualize()
metadata.save_to_json(filepath='Output/metadata.json')




