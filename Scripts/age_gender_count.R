library(ggplot2)
dir <- getSrcDirectory(function(x) {x})
wdir <- sub("Scripts", "Data", dir)
setwd(wdir)

# Parametros iniciales
yr_in <- 2015
yr_f <-2018
mes_inicial <- 1
mes_final <- 12
meses <- c("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", 
           "Julio","Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

dframe <- data.frame(Usuario_Id=c(), age=c(), gender=c())

# Multiples archivos
for(yr in yr_in:yr_f) {
  for(i in mes_inicial:mes_final) {
    if(i < 10) { # Nombre del archivo
      file <- paste(yr,"_", 0, i, ".csv", sep="")
    } else {
      file <- paste(yr,"_", i, ".csv", sep="")
    }
   data <- read.csv(file)
   # Datos para usuarios unicos
   usrs <- data[as.numeric(row.names(unique(data["Usuario_Id"]))), ]
   
   df <- data.frame(usrs$Usuario_Id, yr - usrs["Año_de_nacimiento"], usrs$Genero)
    
   rm(data)
   rm(usrs)
   #Femenino
   tmp <- dframe
   # union de datos previos y nuevos
   dframe <- unique(rbind(tmp, df))
   
   rm(df) 
   rm(tmp)
   
  }
}
colnames(dframe) <- c("Usuario_Id", "Edad", "Genero")
dframe <- dframe[!is.na(dframe["Edad"]),]
dframe <- dframe[dframe$Genero=="M" | dframe$Genero =="F",]
# Edades
f_age <- unlist(dframe[dframe$Genero=="F", "Edad"])
m_age <- unlist(dframe[dframe$Genero=="M", "Edad"])

# media
f_mean  <- mean(f_age)
m_mean <- mean(m_age)
# Graficacion con ggplot
rm(f_age)
rm(m_age)
p <- ggplot(dframe, aes(Edad, fill = Genero)) +
  geom_density(aes(y=..count..),alpha=0.2)+
  #M
  geom_vline(aes(xintercept=m_mean),
             color="blue", linetype="dashed", size=0.9) +
  #F
  geom_vline(aes(xintercept=f_mean),
              color="red", linetype="dashed", size=0.9) +
  ##
  scale_y_continuous(
    breaks = seq(0, 3200, 200),
  ) +
  scale_x_continuous(
    breaks = seq(16, 80, 2),
    limits = c(16, 80)
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
  annotate("text", x = f_mean+10, y = 1700, label = paste("F_mean =", f_mean)) +
  annotate("text", x = m_mean+10, y = 1900, label = paste("M_mean =", m_mean)) +
  labs(title=paste("Número de usuarios por edad y género de",
                   meses[mes_inicial],yr_in, "a", 
                   meses[mes_final], yr_f),
       x="Edad",
       y = "Número de usuarios")

ggsave("../Graphics/age_gender_plot.png")
rm(dframe)
