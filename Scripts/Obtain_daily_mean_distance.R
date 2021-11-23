source("Functions.R")
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
    distance = matrix(0.0, nrow = length(dates)),
    row.names = dates
)
distance_data <- read.csv(distance_file)
for (file in files) {
    filename <- paste(path_data,
        file,
        sep = ""
    )
    data <- read.csv(filename)
}