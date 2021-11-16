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