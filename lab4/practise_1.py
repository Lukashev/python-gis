import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt


# print first 5 rows of dataframe, geodataframe
def output(input_data):
    print(input_data.head(5).to_string())
    print(type(data))


def visual_by_time(input_data):
    input_data.plot(column='pt_r_tt', linewidth=0.05, )
    plt.title('Civilian')
    plt.tight_layout()
    plt.savefig('plots/visual_by_civilian_time')

    input_data.plot(column='car_r_t', linewidth=0.05)
    plt.title('Car')
    plt.tight_layout()

    plt.savefig('plots/visual_by_cars_time')


def binaryClassifier(row, source_col, output_col, threshold):
    if row[source_col] < threshold:
        row[output_col] = 0
    else:
        row[output_col] = 1
    return row


# set txt file path
filep = 'dataE4/TravelTimes_to_5878070_Jumbo.txt'
shapep = 'dataE4/MetropAccess_YKR_grid_EurefFIN.shp'

# create list of selected rows
dt_columns = ['pt_r_tt', 'car_r_t', 'from_id', 'to_id']

# read file with delimiter ';'
data = pd.read_csv(filep, delimiter=';')

gdata = gpd.read_file(shapep).to_crs(epsg=3879)

# create new df with selection
data = data[dt_columns]

data = gdata.join(data)

# output(data)
# visual_by_time(data)

pr_time = data['pt_r_tt']
pr_mean_time = pr_time.mean()

# print(pr_mean_time)

# detect suitable trip by using binary classifier

class_data = data.copy()

class_data['suitable_trip'] = None

class_data = class_data.apply(binaryClassifier, source_col='pt_r_tt', output_col='suitable_trip',
                    threshold=pr_mean_time, axis=1)

class_data.plot(column='suitable_trip', linewidth=0.05, cmap="seismic", legend=True)
plt.tight_layout()
plt.savefig('plots/suitable_trips')