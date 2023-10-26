# Script to pull Parcel Fabric from BC Open Data, and save as .csv

import geopandas as gpd
import requests
import zipfile
import os

# Set Path for input output
f_path = str('Z:/shp_to_csv/')

# URL to download
dl_url = "https://pub.data.gov.bc.ca/datasets/4cf233c2-f020-4f7a-9b87-1923252fbc24/pmbc_parcel_fabric_poly_svw.zip"

# Download the zip file
response = requests.get(dl_url)
zip_file_path = os.path.join(f_path, "PARCEL_MAP_FABRIC.zip")

with open(zip_file_path, 'wb') as zip_file:
    zip_file.write(response.content)

# Unzip the downloaded file to the same folder
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(f_path)

# Read the geodatabase table into a GeoDataFrame
gdf = gpd.read_file(str(f_path+'pmbc_parcel_fabric_poly_svw.gdb'))

# Export the GeoDataFrame to a CSV file
gdf.to_csv('gdb_as_csv.csv', index=False)

