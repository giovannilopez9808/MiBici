library(hash)
source("Functions.R")
source_path <- getwd()
source_path <- sub(
    "Scripts",
    "",
    source_path
)
parameters <- hash()
parameters["file information"] <- paste(
    source_path,
    "Information/",
    "nomenclatura.csv",
    sep = ""
)
parameters["file output"] <- paste(
    source_path,
    "Output/",
    "Distance_between.csv",
    sep = ""
)
stations_data <- read.csv(parameters[["file information"]])
rownames(stations_data) <- stations_data$id
ndata <- nrow(stations_data)
stations_distance <- data.frame(matrix(0, nrow = ndata + 1, ncol = ndata + 1))
for (index_i in 1:ndata) {
    id <- stations_data[index_i, 1]
    stations_distance[1, index_i + 1] <- id
}
for (index_i in 1:ndata) {
    index_j <- index_i + 1
    id_i <- stations_data[index_i, 1]
    stations_distance[index_i + 1, 1] <- id_i
    lon_i <- stations_data[index_i, 6]
    lat_i <- stations_data[index_i, 5]
    while (index_j <= ndata) {
        lon_j <- stations_data[index_j, 6]
        lat_j <- stations_data[index_j, 5]
        distance <- obtain_distance_between_points(
            lat_i,
            lon_i,
            lat_j,
            lon_j
        )
        stations_distance[index_j + 1, index_i + 1] <- distance
        stations_distance[index_i + 1, index_j + 1] <- distance
        index_j <- index_j + 1
    }
}
write.table(stations_distance,
    parameters[["file output"]],
    sep = ",",
    row.names = FALSE,
    col.names = FALSE,
)