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
path_output <- "../Output/"
distance_file <- paste(
    path_output,
    "Distance_between.csv",
    sep = ""
)
files <- list.files(path_data)
dates <- obtain_dates_consecutive(files)
daily_data <- data.frame(
    distance = matrix(0.01,
        nrow = length(dates)
    ),
    row.names = dates
)
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
    data$Inicio_del_viaje <- as.Date(data$Inicio_del_viaje)
    data <- data %>%
        group_by(Inicio_del_viaje) %>%
        dplyr::summarize(Mean = mean(distance))
    for (index in rownames(data)) {
        index <- as.integer(index)
        date <- as.Date(data$Inicio_del_viaje[index])
        distance <- data$Mean[index]
        index <- match(date, dates)
        daily_data$distance[index] <- distance
    }
}
daily_data <- na.omit(daily_data)
write.table(daily_data,
    "output.csv",
    sep = ",",
    quote = FALSE,
    col.names = "Date,Mean distance",
)