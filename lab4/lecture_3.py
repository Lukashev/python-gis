import geopandas as gpd
import matplotlib.pyplot as plt

# File path
fp = "data/Corine2012_Uusimaa.shp"
data = gpd.read_file(fp)

# print(data.head(2))

selected_cols = ['Level1', 'Level1Eng', 'Level2', 'Level2Eng', 'Level3', 'Level3Eng',
                 'Luokka3', 'geometry']

data = data[selected_cols]

# print(data.columns)

# data.plot(column='Level3', linewidth=0.05)

# plt.tight_layout()
# plt.show()

# print(list(data['Level3Eng'].unique()))

lakes = data.loc[data['Level3Eng'] == 'Water bodies'].copy()

# print(lakes.head(2).to_string())

lakes['area'] = lakes.area

lakes['area_km2'] = lakes['area'] / 1000000

l_mean_size = lakes['area_km2'].mean()


# print(l_mean_size)

def binaryClassifier(row, source_col, output_col, threshold):
    # If area of input geometry is lower that the threshold value
    if row[source_col] < threshold:
        # Update the output column with value 0
        row[output_col] = 0
        # If area of input geometry is higher than the threshold value update with value 1
    else:
        row[output_col] = 1
        # Return the updated row
    return row


lakes['small_big'] = None

lakes = lakes.apply(binaryClassifier, source_col='area_km2', output_col='small_big',
                    threshold=l_mean_size, axis=1)

# lakes.plot(column='small_big', linewidth=0.05, cmap="seismic")

# plt.tight_layout()
# plt.show()

lakes['small_big_alt'] = None
lakes.loc[lakes['area_km2'] < l_mean_size, 'small_big_alt'] = 0
lakes.loc[lakes['area_km2'] >= l_mean_size, 'small_big_alt'] = 1


def customClassifier2(row, src_col1, src_col2, threshold1, threshold2, output_col):
    # 1. If the value in src_col1 is LOWER than the threshold1 value
    # 2. AND the value in src_col2 is HIGHER than the threshold2 value, give value 1,
    if row[src_col1] < threshold1 and row[src_col2] > threshold2:
        # Update the output column with value 0
        row[output_col] = 1
        # If area of input geometry is higher than the threshold value update with value 1
    else:
        row[output_col] = 0
    # Return the


fp = r"data/TravelTimes_to_5975375_RailwayStation_Helsinki.geojson"
# Read the GeoJSON file similarly as Shapefile
acc = gpd.read_file(fp)

acc = acc.loc[acc['pt_r_tt'] >= 0]

# acc.plot(column="pt_r_tt", scheme="Fisher_Jenks", k=9, cmap="RdYlBu", linewidth=0)

# plt.tight_layout()
# plt.show()
acc['Suitable_area'] = ""
acc.apply(customClassifier2, src_col1='pt_r_tt', src_col2='walk_d',
          threshold1=20, threshold2=4000, output_col="Suitable_area", axis=1)

# acc.plot(column="Suitable_area", linewidth=0)
# plt.tight_layout()
# plt.show()

import pysal.viz.mapclassify as mc

n_classes = 9

classifier = mc.NaturalBreaks.make(k=n_classes)

classifications = acc[['pt_r_tt']].apply(classifier)

# print(classifications.head())

classifications.columns = ['nb_pt_r_tt']

acc = acc.join(classifications)

acc.plot(column="nb_pt_r_tt", linewidth=0, legend=True)

plt.tight_layout()
plt.savefig('demo.png')

