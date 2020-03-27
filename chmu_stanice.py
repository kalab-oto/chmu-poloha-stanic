import geopandas as gpd
from urllib.request import urlopen

js_names = ["staniceElement","stanice"]

for file_nam in js_names:
    str_data = urlopen("http://portal.chmi.cz/files/portal/docs/poboc/OS/stanice/js/" + file_nam + ".js").readlines()
    for l in range(1,len(str_data)-1):
        lay_nam = str(str_data[l].split(b"=")[0][4:-1], 'utf-8')
        geojs = str(str_data[l].split(b"=")[1], 'utf-8')
        points = gpd.read_file(geojs)
        points.to_file(file_nam+".gpkg", layer=lay_nam, driver="GPKG")
        
meta = urlopen("http://portal.chmi.cz/files/portal/docs/poboc/OS/stanice/js/messages.js").readlines()

for line in range(0,len(meta)):
    meta[line] = str(meta[line],"utf-8")
    meta[line] = meta[line][8:]
    meta[line] = meta[line].replace("<H4>","") 
    meta[line] = meta[line].replace("</H4>","") 
    meta[line] = meta[line].replace(";","") 

meta = "\n".join(meta)

with open("stanice_info.txt", "w") as f: 
    f.write(meta) 

