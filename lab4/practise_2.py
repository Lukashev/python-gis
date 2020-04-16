import geopandas as gpd
import pandas as pd
import pysal.viz.mapclassify as mc
import matplotlib.pyplot as plt


# print first 5 rows of dataframe, geodataframe
def output(input_data, limit=5):
    print(input_data.head(limit).to_string())
    print(type(input_data))


filep_list = [
    'dataE4/TravelTimes_to_5878070_Jumbo.txt',
    'dataE4/TravelTimes_to_5878087_Dixi.txt',
    'dataE4/TravelTimes_to_5944003_Itis.txt'
]

shapep = 'dataE4/MetropAccess_YKR_grid_EurefFIN.shp'

gdata = gpd.read_file(shapep).to_crs(epsg=3879)

dt_columns = ['pt_r_tt', 'from_id', 'to_id']

column_list = []

for path in filep_list:
    # create list of selected rows
    # read file with delimiter ';'
    data = pd.read_csv(path, delimiter=';')
    column_name = dt_columns[0] + "_" + str(data["to_id"][0])
    column_list.append(column_name)
    gdata[column_name] = data["pt_r_tt"]

gdata["min_time_pt"] = gdata[column_list].min(axis=1)
gdata["dominant_service"] = gdata[column_list].idxmin(axis=1)

# output(gdata)

n_classes = 3

classifier = mc.NaturalBreaks.make(k=n_classes)

classifications = gdata[['min_time_pt']].apply(classifier)

# output(classifications)

classifications.columns = ['nb_min_pt_r_tt']

acc = gdata.join(classifications)

output(acc, 20)

acc.plot(column="nb_min_pt_r_tt", linewidth=0, legend=True)

plt.tight_layout()

# the best origin by time
plt.savefig('plots/min_time_pt.png')


acc.plot(column="dominant_service", linewidth=0, legend=True)
plt.tight_layout()

# the most visited service
plt.savefig('plots/dominant_service.png')