suppressPackageStartupMessages({
    library(dplyr)
})
source("Functions.R")

path_data <- "../Data/with_distances/"
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
files <- c("2014_12.csv")
for (file in files) {
    print(paste("Analizando archivo", file))
    filename <- paste(path_data,
        file,
        sep = ""
    )
    data <- read.csv(filename)
    data <- clean_data(data, id_list)
    data <- subset(data, distance != 0)
    data$Inicio_del_viaje <- as.Date(data$Inicio_del_viaje)
    mean <- data %>%
        group_by(Inicio_del_viaje) %>%
        dplyr::summarize(Mean = mean(distance))
    mean$Inicio_del_viaje <- as.Date(mean$Inicio_del_viaje)
    for (index in rownames(mean)) {
        index <- as.integer(index)
        date <- mean$Inicio_del_viaje[index]
        distance <- mean$Mean[index]
        index <- match(date, dates)
        daily_data$distance[index] <- distance
    }
    rm(data)
}
daily_data <- na.omit(daily_data)
write.table(daily_data,
    "output.csv",
    sep = ",",
    quote = FALSE,
    col.names = "Date,Mean distance",
)