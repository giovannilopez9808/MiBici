library(ggplot2)
dir <- getSrcDirectory(function(x) {x})
wdir <- sub("Scripts", "Data", dir)
setwd(wdir)

yr <- 2019
mes <- 12


data <- read.csv(paste(yr,"_", mes,".csv", sep=""))
# Usuarios unicos
# usrs <- unique(data["Usuario_Id"])
# Edad de cada usuario
age <- 2020 - data[as.numeric(row.names(unique(data["Usuario_Id"]))), "Año_de_nacimiento"]


# media
m  <- mean(age[!is.na(age)])
# Graficacion con ggplot
df <- data.frame(edad=age[!is.na(age)])
p <- ggplot(df, aes(edad)) + 
    geom_histogram(bins=20, aes(y=..count..), colour="black", fill="lightblue", alpha=0.5) + 
    geom_vline(aes(xintercept=mean(age[!is.na(age)])),
                color="red", linetype="dashed", size=0.9) + xlim(10, 80) +
  labs(title="Número de usuarios por edad",x="Edad", y = "Número de usuarios") +
  annotate("text", x = m+10, y = 3000, label = paste("mean =", m))
ggsave("../Graphics/edades.png")

