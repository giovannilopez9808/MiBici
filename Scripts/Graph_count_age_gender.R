library(ggplot2)
library(latex2exp)
path_data <- "../Output/"
file_data <- "Age_gender_users.csv"
path_graphics <- "../Graphics/"
file_graphics <- "age_gender_distribution.png"
dframe <- read.csv(paste(path_data,
    file_data,
    sep = ""
))
colors <- c(
    "Female mean" = "#386641",
    "Male mean" = "#168aad"
)
# Edades
f_age <- unlist(dframe[dframe$Genero == "F", "Edad"])
m_age <- unlist(dframe[dframe$Genero == "M", "Edad"])
# media
f_mean <- mean(f_age)
m_mean <- mean(m_age)
message("Edad promedio femenino ", f_mean)
message("Edad promedio masculino ", m_mean)
# Graficacion con ggplot
rm(f_age)
rm(m_age)
p <- ggplot(
    dframe,
    aes(Edad, fill = Genero)
) +
    geom_density(aes(y = ..count..),
        alpha = 0.2
    ) +
    # M
    geom_vline(aes(
        xintercept = m_mean,
        color = "Male mean",
    ),
    linetype = "dashed",
    size = 0.9
    ) +
    # F
    geom_vline(aes(
        xintercept = f_mean,
        color = "Female mean",
    ),
    linetype = "dashed",
    size = 0.9
    ) +
    ##
    scale_y_continuous(
        breaks = seq(0, 3200, 200),
    ) +
    scale_x_continuous(
        breaks = seq(16, 80, 2),
        limits = c(16, 80)
    ) +
    scale_fill_manual(
        values = c(
            "#b5179e",
            "#4361ee"
        )
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
    # annotate("text",
    #     x = f_mean + 10,
    #     y = 1700,
    #     label = TeX(paste("$\\mu_F =$", round(f_mean, 2)))
    # ) +
    # annotate("text",
    #     x = m_mean + 10,
    #     y = 1900,
    #     label = TeX(paste("$\\mu_M =$", round(m_mean, 2)))
    # ) +
    labs(
        title = paste(
            "Número de usuarios por edad y género en el periodo 2015-2018"
        ),
        x = "Edad",
        y = "Número de usuarios"
    ) +
    scale_color_manual(values = colors)
ggsave(paste(
    path_graphics,
    file_graphics,
    sep = ""
),
height = 2043,
width = 2793,
limitsize = FALSE,
units = "px"
)