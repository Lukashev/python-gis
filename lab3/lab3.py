import geopandas as gpd
import matplotlib.pyplot as plt


fp = "./population/Vaestotietoruudukko_2015.shp"

pop = gpd.read_file(fp)

pop.crs = {'y_0': 0, 'no_defs': True, 'x_0': 25500000, 'k': 1, 'lat_0': 0,
'units': 'm', 'lon_0': 25, 'ellps': 'GRS80', 'proj': 'tmerc'}
#print(pop.head(5).to_string())

pop = pop.rename(columns={'ASUKKAITA': 'pop15'})

# print(pop.columns)

selected_cols = ['pop15', 'geometry']
pop = pop[selected_cols]

# print(pop.tail(2))


addr_fp = r"addresses_epsg3879.shp"
addresses = gpd.read_file(addr_fp)
addresses.crs = {'y_0': 0, 'no_defs': True, 'x_0': 25500000, 'k': 1, 'lat_0': 0,
'units': 'm', 'lon_0': 25, 'ellps': 'GRS80', 'proj': 'tmerc'}

# print(addresses.head(2))

join = gpd.sjoin(addresses, pop, how="inner", op="within")

# Output path
outfp = r"addresses_pop15_epsg3979.shp"
# Save to disk
join.to_file(outfp)

print(join.head())

join.plot(column='pop15', cmap="Reds", markersize=7, scheme='natural_breaks',
legend=True)

plt.title("Amount of inhabitants living close the the point")

plt.tight_layout()
plt.show()