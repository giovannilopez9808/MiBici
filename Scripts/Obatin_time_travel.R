suppressPackageStartupMessages({
    library(dplyr)
})
source("Functions.R")

fill_time <- function(data) {
    data$Inicio_del_viaje <- as.POSIXlt(data$Inicio_del_viaje)
    data$Fin_del_viaje <- as.POSIXlt(data$Fin_del_viaje)
    data$Time <- (data$Fin_del_viaje - data$Inicio_del_viaje) / 3600
    return(data)
}
path_data <- "../Data/with_distances/"
path_output <- "../Data/with_distances_and_time/"
files <- list.files(path_data)
for (file in files) {
    message(paste("Analizando archivo", file))
    filename <- paste(path_data,
        file,
        sep = ""
    )
    data <- read.csv(filename)
    data <- fill_time(data)
    filename <- paste(path_output,
        file,
        sep = ""
    )
    write.table(data,
        filename,
        sep = ",",
        quote = FALSE,
        row.names = FALSE
    )
    rm(data)
}