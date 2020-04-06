# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 19:48:26 2020

@author: Vladimir Petrov
"""

import pandas as pd
import geopandas as gpd
from pathlib import Path
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows

input_file ='Coordinates.xlsx'

world=gpd.read_file(gpd.datasets.get_path('naturalearth_lowres')) 

df_coord=pd.read_excel(input_file)
gdf_coord=gpd.GeoDataFrame(df_coord, geometry=gpd.points_from_xy(df_coord.Longitude, df_coord.Latitude))
df_countries=gpd.sjoin(gdf_coord, world, how='left')

result=df_countries[['Latitude', 'Longitude', 'name']]

output_file=Path.cwd() / "Coordintaes_Countries.xlsx"
wb=Workbook()
ws=wb.active

for r in dataframe_to_rows(result, index=False, header=True):
    ws.append(r)
    
wb.save(output_file)