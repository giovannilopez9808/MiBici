suppressPackageStartupMessages({
    library(dplyr)
})
source("Functions.R")

fill_distance <- function(data, header, id_list, distance_data) {
    for (index in rownames(data)) {
        index <- as.integer(index)
        origen_id <- data$Origen_Id[index]
        destino_id <- data$Destino_Id[index]
        origen_id <- paste("X", origen_id, sep = "")
        origen_id <- match(origen_id, header)
        destino_id <- match(destino_id, id_list)
        if (!is.na(origen_id) & !is.na(destino_id)) {
            distance <- distance_data[destino_id, origen_id]
            data[index, "distance"] <- distance
        }
    }
    return(data)
}

path_data <- "../Data/"
path_distance <- "../Output/"
path_output <- "../Data/with_distances/"
distance_file <- paste(
    path_distance,
    "Distance_between.csv",
    sep = ""
)
files <- list.files(path_data)
distance_data <- read.csv(distance_file)
header <- colnames(distance_data)
id_list <- distance_data$X0
for (file in files) {
    print(paste("Analizando archivo", file))
    filename <- paste(path_data,
        file,
        sep = ""
    )
    data <- read.csv(filename)
    data <- clean_data(data, id_list)
    data$distance <- NA
    data <- fill_distance(
        data,
        header,
        id_list,
        distance_data
    )
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