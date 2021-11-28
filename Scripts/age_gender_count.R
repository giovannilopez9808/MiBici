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

f_dframe <- data.frame(Usuario_Id=c(), age=c())
m_dframe <- data.frame(Usuario_Id=c(), age=c())

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
   f_usrs <- usrs[usrs$Genero == "F",]
   m_usrs <- usrs[usrs$Genero == "M",]
   rm(usrs)
   
   f_age <- yr - f_usrs["Año_de_nacimiento"]
   m_age <- yr - m_usrs["Año_de_nacimiento"]
   
   f_df <- data.frame(f_usrs$Usuario_Id, f_age)
   m_df <- data.frame(m_usrs$Usuario_Id, m_age)
   
   rm(data)
   rm(f_usrs)
   rm(m_usrs)
   #Femenino
   tmp <- f_dframe
   # union de datos previos y nuevos
   f_dframe <- unique(rbind(tmp, f_df))
   
   rm(f_df)
   #Masculino
   tmp <- m_dframe
   # union de datos previos y nuevos
   m_dframe <- unique(rbind(tmp, m_df))
   
   rm(m_df) 
   rm(tmp)
   
  }
}
rm(f_age)
rm(m_age)
colnames(f_dframe) <- c("Usuario_Id", "Edad")
colnames(m_dframe) <- c("Usuario_Id", "Edad")
# Edades
f_age <- unlist(f_dframe[!is.na(f_dframe["Edad"]), "Edad"])
m_age <- unlist(m_dframe[!is.na(m_dframe["Edad"]), "Edad"])

rm(f_dframe)
rm(m_dframe)
# media
f_mean  <- mean(f_age)
m_mean <- mean(m_age)
# Graficacion con ggplot
f_df <- data.frame(edad=f_age[!is.na(f_age)])
m_df <- data.frame(edad=m_age[!is.na(m_age)])

p <- ggplot() +
  # M
  geom_density(data=m_df, aes(edad, y=..count..), colour="black", fill="#a687c1", alpha=0.7)+
  geom_vline(aes(xintercept=m_mean),
             color="#a687c1", linetype="dashed", size=0.9) +
  #F
  geom_density(data=f_df, aes(edad, y=..count..), colour="black", fill="#87c1ad", alpha=0.7)+
  geom_vline(aes(xintercept=f_mean),
              color="#87c190", linetype="dashed", size=0.9) +
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
      fill = "lightgray",
      colour = "black"
    ),
    panel.grid.major = element_line(
      colour = "white",
      linetype = "dashed"
    )
  ) +
  annotate("text", x = f_mean+10, y = 1900, label = paste("F_mean =", f_mean)) +
  annotate("text", x = m_mean+10, y = 1700, label = paste("M_mean =", m_mean)) +
  labs(title=paste("Número de usuarios por edad y género de",
                   meses[mes_inicial],yr_in, "a", 
                   meses[mes_final], yr_f),
       x="Edad",
       y = "Número de usuarios")

ggsave("../Graphics/age_gender_plot.png")
