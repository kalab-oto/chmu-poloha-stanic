# %%
import geopandas as gpd
from urllib.request import urlopen
import os

# %%
if not os.path.exists('./output/'):
    os.makedirs('./output/')

# %%
js_names = ['staniceElement', 'stanice']

for file_nam in js_names:
    str_data = urlopen('http://portal.chmi.cz/files/portal/docs/poboc/OS/stanice/js/' + file_nam + '.js').readlines()
    points = gpd.GeoDataFrame()
    for l in range(1,len(str_data)-1):
        geojs = str(str_data[l].split(b'=')[1], 'utf-8')
        tmp = gpd.read_file(geojs)
        points = points.append(tmp)
    points.to_csv('./output/' + file_nam + '.csv', encoding='utf-8', index=False)

meta = urlopen('http://portal.chmi.cz/files/portal/docs/poboc/OS/stanice/js/messages.js').readlines()

for line in range(0,len(meta)):
    meta[line] = str(meta[line],'utf-8')
    meta[line] = meta[line][8:]
    meta[line] = meta[line].replace('<H4>','') 
    meta[line] = meta[line].replace('</H4>','') 
    meta[line] = meta[line].replace(';','') 

meta = '\n'.join(meta)

with open('./output/stanice_info.txt', 'w', encoding='utf-8') as f: 
    f.write(meta) 

