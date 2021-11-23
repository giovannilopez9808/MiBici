obtain_distance_between_points <- function(lat1, lon1, lat2, lon2) {
    R <- 6372.795477598
    rad <- pi / 180
    dlat <- lat2 - lat1
    dlon <- lon2 - lon1
    a <- (sin(rad * dlat / 2))**2
    a <- a + cos(rad * lat1) * cos(rad * lat2) * (sin(rad * dlon / 2))**2
    distancia <- 2 * R * asin(sqrt(a))
    return(c(distancia))
}

period_from_filenames <- function(filenames) {
    n_file <- length(filenames)
    file_i <- filenames[1]
    file_f <- filenames[n_file]
    date_i <- year_month_from_filename(file_i)
    date_f <- year_month_from_filename(file_f)
    month <- as.integer(substring(date_f, 6, 7))
    if (month %in% c(12, 1, 3, 5, 7, 8, 10)) {
        day <- 31
    }
    if (month %in% c(2, 4, 6, 9, 11)) {
        day <- 30
    }
    date_i <- as.Date(paste(date_i, "01", sep = "-"))
    date_f <- as.Date(paste(date_f, day, sep = "-"))
    return(c(date_i, date_f))
}

year_month_from_filename <- function(filename) {
    year <- substring(filename, 1, 4)
    month <- substring(filename, 6, 7)
    date <- paste(year, month, sep = "-")
    return(date)
}

obtain_dates_consecutive <- function(files) {
    period <- period_from_filenames(files)
    dates <- seq(period[1], period[2], by = "days")
    return(dates)
}