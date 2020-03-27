Skripty pro stažení polohy meteorologických stanic [Českého hydrometeorologického ústavu](http://portal.chmi.cz/). Tato data lze spárovat z daty naměřených hodnot na jednotlivých stanicích, které ČHMÚ nyní poskytuje veřejnosti ([Počasí, věc veřejná. Meteorologové po letech sporů začali poskytovat historické záznamy ](https://www.irozhlas.cz/zpravy-domov/chmu-pocasi-data-historicke-zaznamy-o-pocasi-pravo-na-informace_2003260832_elev). Jak tato data vypadají, a jak o ně požádat najdete na [https://github.com/datastory/chmu-historicka-data](https://github.com/datastory/chmu-historicka-data).

## Vytvoření `GPKG` pomocí R nebo Python

- `chmu_stanice.py`

    python3 chmu_stanice.py

nebo

- `chmu_stanice.R`

    Rscript chmu_stanice.R

Skript vytvoří dva soubory [geopackage](https://www.geopackage.org/) - body podle typu stanice `stanice.gpkg` a podle měřených prvků `staniceElement.gpkg`. Dále se vytvoří soubor s metadaty `stanice_info.txt`, kde je legenda ke stanicím. 

## Načtení bodů do QGIS pomocí Python konzole

- `chmu_stanice_QGIS.py`

Po spuštění skriptu v QGIS Python konzoli, načte všechny body (stanice podle typu i prvku) do projektu (bez legendy ke stanicím).

## Zdroj dat

[Metorologické stanice ČHMÚ](http://portal.chmi.cz/files/portal/docs/poboc/OS/stanice/ShowStations_CZ.html)
