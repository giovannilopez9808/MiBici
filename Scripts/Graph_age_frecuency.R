library(ggplot2)
path_data <- "../Output/"
file_data <- "Age_frecuency.csv"
path_graphics <- "../Graphics/"
file_graphic <- "edades.png"
mu <- 33.62
data <- read.csv(paste(path_data,
    file_data,
    sep = ""
))
theme_set(theme_classic())
ggplot(
    data = data,
    aes(x = Age, y = Frecuency)
) +
    geom_bar(
        stat = "identity",
        color = "black",
        fill = "grey"
    ) +
    geom_vline(aes(xintercept = mu),
        color = "red",
        linetype = "dashed",
        size = 0.9
    ) +
    labs(
        title = paste(
            "Frecuencia de usuarios por edades en el periodo 2015-2018"
        ),
        x = "Edad",
        y = "Número de usuarios"
    ) +
    scale_y_continuous(breaks = seq(0, 3300, 200)) +
    scale_x_continuous(
        breaks = seq(16, 80, 4),
        limits = c(16, 80)
    ) +
    annotate("text",
        x = mu + 16,
        y = 3300,
        label = paste(
            "mean =",
            round(mu, 2)
        )
    )
ggsave(paste(path_graphics,
    file_graphic,
    sep = ""
),
height = 2043,
width = 2793,
limitsize = FALSE,
units = "px"
)