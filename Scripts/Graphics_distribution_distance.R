library(ggplot2)
library(tidyr)
path_data <- "../Output/"
path_graphics <- "../Graphics/"
file_data <- "Hourly_mean_distance.csv"
file_graphic <- "distribution_distance.png"
data <- read.csv(paste(
    path_data,
    file_data,
    sep = ""
))
data$names <- row.names(data)
data <- data %>% gather(data, value, -names, -Date)
data$value[data$value == 0] <- NA
ggplot(
    data = data,
    aes(value, fill = value)
) +
    geom_histogram(
        aes(y = ..count..),
        alpha = 0.5,
        bins = 100,
        fill = "#52b69a"
    ) +
    theme(
        panel.background = element_rect(
            fill = "white",
            colour = "black"
        ),
        panel.grid.major = element_line(
            colour = "lightgray",
            linetype = "dashed"
        )
    ) +
    scale_x_continuous(
        breaks = seq(0, 3, 0.2),
        limits = c(0, 3)
    ) +
    scale_y_continuous(
        breaks = seq(0, 1500, 100),
        limits = c(0, 1500)
    ) +
    labs(
        title = paste(
            "Distribución de las distancias recorridas en cada viaje"
        ),
        x = "Distancia (km)",
        y = ""
    )
ggsave(paste(path_graphics,
    file_graphic,
    sep = ""
),
height = 1200,
width = 2793,
limitsize = FALSE,
units = "px"
)