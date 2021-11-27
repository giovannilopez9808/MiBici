library(ggplot2)
library(stringr)
library(plyr)
source("Functions.R")
theme_set(theme_classic())
path_data <- "../Data/"
path_output <- "../Output/"
path_graphics <- "../Graphics/"
files <- list.files(path_data)
dframe <- data.frame(Usuario_Id = c(), age = c())
for (filename in files) {
  message(paste(
    "Analizando archivo",
    filename
  ))
  data <- read.csv(paste(
    path_data,
    filename,
    sep = ""
  ))
  year <- as.integer(substring(filename, 1, 4))
  # Usuarios unicos
  usrs <- unique(data["Usuario_Id"])
  age <- year - data[
    as.numeric(row.names(unique(data["Usuario_Id"]))),
    "Año_de_nacimiento"
  ]
  dff <- data.frame(
    usrs,
    age
  )
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
frecuency <- count(age, "age")
colnames(frecuency) <- c(
  "Age",
  "Frecuency"
)
write.table(frecuency,
  paste(path_output,
    "Age_frecuency.csv",
    sep = ""
  ),
  sep = ",",
  quote = FALSE,
  row.names = FALSE
)
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
    bins = 70,
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
      "Número de usuarios"
    ),
    x = "Edad",
    y = "Número de usuarios"
  ) #+
# annotate("text",
#   x = mu + 10,
#   y = max(df),
#   label = paste(
#     "mean =",
#     round(mu, 4)
#   )
# )
ggsave(paste(path_graphics,
  "edades_c.png",
  sep = ""
),
height = 2043,
width = 2793,
limitsize = FALSE,
units = "px"
)