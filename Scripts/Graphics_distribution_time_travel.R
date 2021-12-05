library(ggplot2)
library(tidyr)
path_data <- "../Output/"
path_graphics <- "../Graphics/"
file_data <- "Hourly_mean_time_travel.csv"
file_graphic <- "distribution_time_travel.png"
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
    geom_density(
        aes(y = ..count..),
        alpha = 0.5,
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
        breaks = seq(0, 20, 2),
        limits = c(0, 20)
    ) +
    scale_y_continuous(
        breaks = seq(0, 8000, 500),
        limits = c(0, 8000)
    ) +
    labs(
        title = paste(
            "Distribución de los tiempos de uso de una bicicleta en el periodo 2015-2018"
        ),
        x = "Tiempo (min)",
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