dir <- getSrcDirectory(function(x) {x})
wdir <- sub("Scripts", "Data", dir)

setwd(wdir)

df = data.frame(Date=c(), Count=c())
for( datafile in list.files()) {
     counts <- c()
    data <- read.csv(datafile, header = TRUE)
    
    dates <- as.Date(unique(gsub("( ).*", "", unlist(data["Inicio_del_viaje"]))))
    data_list <- as.Date(gsub("( ).*", "",unlist(data["Inicio_del_viaje"])))
    
    for(i in 1:length(dates)) {
      counts[i] <- length(data_list[data_list==dates[i]])
    }
    if(!exists("df")) {
      df <- data.frame(Date=dates, Count = counts)
    } else {
      tmp <- data.frame(Date=dates, Count = counts)
      df <- rbind(df, tmp)
      rm(tmp)
    }
    rm(data)
    rm(dates)
    rm(data_list)
}
write.table(df, file="../Output/Daily_count.csv", sep=",", row.names = FALSE, quote = FALSE)