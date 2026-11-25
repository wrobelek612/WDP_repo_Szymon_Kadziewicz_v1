import geopandas as gpd
import matplotlib.pyplot as plt

powiaty = gpd.read_file("powiaty.shp")
print(powiaty.head())
print(powiaty.columns)
x = len(powiaty)
print(x)

print(powiaty["LUDNOSC"].sum())
print(powiaty["LUDNOSC"].mean())
print(powiaty["LUDNOSC"].min())
print(powiaty["LUDNOSC"].max())

print(powiaty.loc[powiaty["POW_KM2"].idxmax()])

powiaty["GESTOSC"] = powiaty["LUDNOSC"] / powiaty["POW_KM2"]

powiaty.plot(column="GESTOSC", legend=True)

plt.show()
print(powiaty.loc[powiaty["GESTOSC"].idxmin()])
print(powiaty.loc[powiaty["GESTOSC"].idxmax()])

powiaty.to_file("wynik.shp")
