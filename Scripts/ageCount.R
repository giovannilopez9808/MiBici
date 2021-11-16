library(ggplot2)
dir <- getSrcDirectory(function(x) {x})
wdir <- sub("Scripts", "Data", dir)
setwd(wdir)

# Parametros iniciales
yr <- 2019
mes_inicial <- 3
mes_final <- 5
dframe <- data.frame(Usuario_Id=c(), age=c())

# Multiples archivos
for(i in mes_inicial:mes_final) {
  if(i < 10) { # Nombre del archivo
    file <- paste(yr,"_", 0, i, ".csv", sep="")
  } else {
    file <- paste(yr,"_", i, ".csv", sep="")
  }
 data <- read.csv(file)
 # Datos para usuarios unicos
 usrs <- unique(data["Usuario_Id"])
 age <- yr - data[as.numeric(row.names(unique(data["Usuario_Id"]))), "Año_de_nacimiento"]
 
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
age <- unlist(dframe[!is.na(dframe["age"]), "age"])
rm(dframe)
# media
m  <- mean(age)
# Graficacion con ggplot
df <- data.frame(edad=age[!is.na(age)])
p <- ggplot(df, aes(edad)) + 
    geom_histogram(bins=20, aes(y=..count..), colour="black", fill="lightblue", alpha=0.5) + 
    geom_vline(aes(xintercept=m),
                color="red", linetype="dashed", size=0.9) + xlim(10, 80) +
  labs(title=paste("Número de usuarios por edad en meses",mes_inicial, "a", mes_final, "de", yr),x="Edad", y = "Número de usuarios") +
  annotate("text", x = m+10, y = 3000, label = paste("mean =", m))

ggsave("../Graphics/edades.png")

