library(ggplot2)
library(tidyr)
path_data <- "../Output/"
path_graphics <- "../Graphics/"
file_data <- "Hourly_count_travel.csv"
file_graphic <- "distribution_count_travel.png"
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
        bins = 81,
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
        breaks = seq(0, 80, 5),
        limits = c(0, 80)
    ) +
    scale_y_continuous(
        breaks = seq(0, 1200, 100),
        limits = c(0, 1200)
    ) +
    labs(
        title = paste(
            "Distribución del número de usuarios simultáneos en el periodo 2015-2018"
        ),
        x = "Número de viajes",
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
rm(data)
