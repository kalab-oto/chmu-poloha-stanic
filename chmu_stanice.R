library(sf)
js_names <- c("staniceElement","stanice")

for (file_nam in js_names){
    str <- readLines(url(paste0("http://portal.chmi.cz/files/portal/docs/poboc/OS/stanice/js/",file_nam,".js")))
    for (l in 3:length(str)-1){
        lay_nam <- strsplit(str[l],"=")[[1]][1]
        lay_nam <- substring(lay_nam,5)
        geojs <- strsplit(str[l],"=")[[1]][2]
        points <- st_read(geojs)
        st_write(points, paste0(file_nam,".gpkg"), lay_nam, update = TRUE)
        }
    }

meta <- readLines(url("http://portal.chmi.cz/files/portal/docs/poboc/OS/stanice/js/messages.js"))

for (line in 1:length(meta)){
    meta[line] <- substring(meta[line],9)
    meta[line] <- gsub("<H4>", "", meta[line])
    meta[line] <- gsub("</H4>", "", meta[line])
    meta[line] <- gsub(";", "", meta[line])
}

meta <- paste(paste(meta,collapse="\n\n"))
write(meta, "stanice_info.txt")

