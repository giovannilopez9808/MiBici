source("Functions.R")
path_data <- "../Data/"
path_output <- "../Output/"
file_output <- "Age_gender_users.csv"
# Lista de archivos a analizar
files <- list.files(path_data)
# Parametros iniciales
dframe <- data.frame(
  Usuario_Id = c(),
  age = c(),
  gender = c()
)
meses <- c(
  "Enero",
  "Febrero",
  "Marzo",
  "Abril",
  "Mayo",
  "Junio",
  "Julio",
  "Agosto",
  "Septiembre",
  "Octubre",
  "Noviembre",
  "Diciembre"
)
# Multiples archivos
for (file in files) {
  message(paste("Analizando archivo", file))
  data <- read.csv(paste(path_data,
    file,
    sep = ""
  ))
  # Obtiene el año a partir del nombre del archivo
  year <- as.integer(substring(file, 1, 4))
  # Datos para usuarios unicos
  usrs <- data[as.numeric(row.names(unique(data["Usuario_Id"]))), ]
  df <- data.frame(
    usrs$Usuario_Id,
    year - usrs["Año_de_nacimiento"],
    usrs$Genero
  )
  rm(data)
  rm(usrs)
  # Femenino
  tmp <- dframe
  # union de datos previos y nuevos
  dframe <- unique(rbind(
    tmp,
    df
  ))
  rm(df)
  rm(tmp)
}
colnames(dframe) <- c(
  "Usuario_Id",
  "Edad",
  "Genero"
)
dframe <- dframe[!is.na(dframe["Edad"]), ]
dframe <- dframe[dframe$Genero == "M" | dframe$Genero == "F", ]
rm(dframe)