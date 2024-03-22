# LOADING DATA

from sdv.datasets.local import load_csvs

datasets = load_csvs("input/", read_csv_parameters={'sep':'\t'})

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


#Update columns with Unknown types
#Update columns with Unknown types
metadata.update_column(table_name="Product", column_name="Product", sdtype="categorical")
metadata.update_column(table_name="Product", column_name="ProductKey", sdtype="id", regex_format="[2-6][0-9][0-9]")
metadata.update_column(table_name="Sales", column_name="ProductKey", sdtype="id", regex_format="[2-6][0-9][0-9]")
metadata.update_column(table_name="Product", column_name="Standard Cost", sdtype="numerical")
metadata.update_column(table_name="Reseller", column_name="Reseller", sdtype="categorical")
metadata.update_column(table_name="Reseller", column_name="City", sdtype="categorical")
metadata.update_column(table_name="Reseller", column_name="State-Province", sdtype="categorical")
metadata.update_column(table_name="Reseller", column_name="ResellerKey", sdtype="id")
metadata.update_column(table_name="Region", column_name="Region", sdtype="categorical")
metadata.update_column(table_name="Region", column_name="Country", sdtype="categorical")
metadata.update_column(table_name="Region", column_name="Group", sdtype="categorical")
metadata.update_column(table_name="Sales", column_name="ResellerKey", sdtype="id")
metadata.update_column(table_name="Sales", column_name="EmployeeKey", sdtype="categorical")

#print(metadata_dict.get('type_id'))

# VISUALISE METADATA

metadata.visualize()
metadata.save_to_json(filepath='Output/metadata.json')




