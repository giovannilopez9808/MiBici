# Script que realiza el conteo de los usuarios dentro de un periodo
# Crea una grafica de la disribucion de las edades de los usuarios
# y un archivo con las frecuencias de cada edad encontrada

library(ggplot2)
library(stringr)
library(plyr)
source("Functions.R")
theme_set(theme_classic())
# Ruta de los datos
path_data <- "../Data/"
# Ruta del archivo de salida
path_output <- "../Output/"
# Ruta de la grafica
path_graphics <- "../Graphics/"
# Nombre de la grafica
file_graphic <- "edades_c.png"
# Nombre del archivo de salida
file_output <- "Age_frecuency.csv"
# Lista de archivos a analizar
files <- list.files(path_data)
# Inicializacion del dataframer que guardara a las edades de cada usuario
dframe <- data.frame(Usuario_Id = c(), age = c())
for (filename in files) {
  message(paste(
    "Analizando archivo",
    filename
  ))
  # Lectura de los datos
  data <- read.csv(paste(
    path_data,
    filename,
    sep = ""
  ))
  # Obtiene el año a partir del nombre del archivo
  year <- as.integer(substring(filename, 1, 4))
  # Usuarios unicos
  usrs <- unique(data["Usuario_Id"])
  # Calculo de la edad del usuario
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
# Frecuencia de las edades
frecuency <- count(age, "age")
colnames(frecuency) <- c(
  "Age",
  "Frecuency"
)
# Escritura del archivo de salida con las frecuencias
write.table(frecuency,
  paste(path_output,
    file_output,
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
frecuency <- table(df)
print(max(frecuency))
p <- ggplot(
  df,
  aes(edad)
) +
  geom_histogram(
    bins = 80 - 16 + 1,
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
  labs(
    title = paste(
      "Frecuencia de usuarios por edades en el periodo 2015-2018"
    ),
    x = "Edad",
    y = "Número de usuarios"
  ) +
  scale_y_continuous(breaks = seq(0, 3400, 100)) +
  scale_x_continuous(breaks = seq(16, 80, 4)) +
  annotate("text",
    x = mu + 16,
    y = max(frecuency),
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