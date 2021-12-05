library(ggplot2)
path_data <- "../Output/"
file_data <- "Age_frecuency.csv"
path_graphics <- "../Graphics/"
file_graphic <- "age_distribution.png"
mu <- 31.68
data <- read.csv(paste(path_data,
    file_data,
    sep = ""
))
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
            "Frecuencia de usuarios por edad en el periodo 2015-2018"
        ),
        x = "Edad",
        y = "Número de usuarios"
    ) +
    scale_y_continuous(
        breaks = seq(0, 3200, 200),
    ) +
    scale_x_continuous(
        breaks = seq(16, 80, 2),
        limits = c(16, 80)
    ) +
     annotate("label",
         x = mu + 4,
         y = 3100,
         label = paste(
             "Mean:", round(mu, 2)
         ),
         size=3
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