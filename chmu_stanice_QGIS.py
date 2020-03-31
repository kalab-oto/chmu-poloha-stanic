from qgis.core import QgsVectorLayer
from urllib.request import urlopen

js_names = ["staniceElement","stanice"]

for file_nam in js_names:
    str_data = urlopen("http://portal.chmi.cz/files/portal/docs/poboc/OS/stanice/js/" + file_nam + ".js").readlines()
    for l in range(1,len(str_data)-1):
        lay_nam = str(str_data[l].split(b"=")[0][4:-1], 'utf-8')
        geojs = str(str_data[l].split(b"=")[1], 'utf-8')
        iface.addVectorLayer(geojs, lay_nam, "ogr")

# meta = urlopen("http://portal.chmi.cz/files/portal/docs/poboc/OS/stanice/js/messages.js").readlines()

# for line in range(0,len(meta)):
    # meta[line] = str(meta[line],"utf-8")
    # meta[line] = meta[line][8:]
    # meta[line] = meta[line].replace("<H4>","") 
    # meta[line] = meta[line].replace("</H4>","") 
    # meta[line] = meta[line].replace(";","") 

# iface.addVectorLayer(meta, "stanice_info", "ogr")
