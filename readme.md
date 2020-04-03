Skripty pro stažení polohy meteorologických stanic [Českého hydrometeorologického ústavu](http://portal.chmi.cz/). Tato data lze spárovat z daty naměřených hodnot na jednotlivých stanicích, které ČHMÚ nyní poskytuje veřejnosti ([Počasí, věc veřejná. Meteorologové po letech sporů začali poskytovat historické záznamy](https://www.irozhlas.cz/zpravy-domov/chmu-pocasi-data-historicke-zaznamy-o-pocasi-pravo-na-informace_2003260832_elev)). Jak tato data vypadají, a jak o ně požádat najdete na [https://github.com/datastory/chmu-historicka-data](https://github.com/datastory/chmu-historicka-data).

## Vytvoření `GPKG`/`CSV`

Skript vytvoří dva soubory - body podle typu stanice `stanice` a podle měřených prvků `staniceElement`. Dále se vytvoří soubor s metadaty `stanice_info.txt`, kde je legenda ke stanicím. 

### Python
Zapíše data do `.csv` (viz [GeoPandas nezapíše GPKG pod Win](https://github.com/kalab-oto/chmu-poloha-stanic/issues/2))

- `chmu_stanice.py`
```
python3 chmu_stanice.py
```
závislosti: `geopandas`

### R
Zapíše data do `.gpkg`
- `chmu_stanice.R`
```
Rscript chmu_stanice.R
```

závislosti: `sf`


## Načtení bodů do QGIS pomocí Python konzole

- `chmu_stanice_QGIS.py`

Po spuštění skriptu v QGIS Python konzoli, načte všechny body (stanice podle typu i prvku) do projektu (bez legendy ke stanicím).

## Zdroj dat

[Metorologické stanice ČHMÚ](http://portal.chmi.cz/files/portal/docs/poboc/OS/stanice/ShowStations_CZ.html)
