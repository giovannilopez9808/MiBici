library(ggplot2)
library(stringr)
theme_set(theme_classic())
dir <- getwd()
path_data <- sub(
  "Scripts",
  "Data/",
  dir
)
path_graphics <- sub(
  "Scripts",
  "Graphics/",
  dir
)
yr <- 2019
initial_month <- 3
final_month <- 5
dframe <- data.frame(Usuario_Id = c(), age = c())

for (month in initial_month:final_month) {
  filename <- str_pad(month, 2, pad = "0")
  filename <- paste(yr, "_", filename, ".csv", sep = "")
  print(filename)
  data <- read.csv(paste(path_data, filename, sep = ""))
  # Usuarios unicos
  usrs <- unique(data["Usuario_Id"])
  age <- yr - data[
    as.numeric(row.names(unique(data["Usuario_Id"]))),
    "Año_de_nacimiento"
  ]
  dff <- data.frame(usrs, age)
  rm(data)
  rm(usrs)
  tmp <- dframe
  # union de datos previos y nuevos
  dframe <- unique(rbind(tmp, dff))
  rm(tmp)
  rm(dff)
}
rm(age)
# Edades
age <- unlist(dframe[
  !is.na(dframe["age"]),
  "age"
])
rm(dframe)
# media
mu <- mean(age)
# Graficacion con ggplot
df <- data.frame(edad = age[!is.na(age)])
p <- ggplot(
  df,
  aes(edad)
) +
  geom_histogram(
    bins = 20,
    aes(y = ..count..),
    colour = "black",
    fill = "lightblue",
    alpha = 0.5
  ) +
  geom_vline(aes(xintercept = mu),
    color = "red",
    linetype = "dashed",
    size = 0.9
  ) +
  xlim(10, 80) +
  labs(
    title = paste(
      "Número de usuarios por edad en meses",
      initial_month,
      "a",
      final_month,
      "de",
      yr
    ),
    x = "Edad",
    y = "Número de usuarios"
  ) +
  annotate("text",
    x = mu + 10,
    y = 3000,
    label = paste(
      "mean =",
      round(mu, 4)
    )
  )
ggsave(paste(path_graphics, "edades_c.png", sep = ""),
  height = 2043,
  width = 2793,
  limitsize = FALSE,
  units = "px"
)