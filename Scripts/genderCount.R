library(ggplot2)
library(scales)
library(dplyr)

dir <- getSrcDirectory(function(x) {x})
wdir <- sub("Scripts", "Data", dir)
setwd(wdir)

yr_in <- 2015
yr_f <-2018
mes_inicial <- 1
mes_final <- 12
meses <- c("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", 
          "Julio","Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

dframe <- data.frame(Usuario_Id=c(), age=c())

# Multiples archivos
for(yr in yr_in:yr_f){
  for(i in mes_inicial:mes_final) {
    if(i < 10) { # Nombre del archivo
      file <- paste(yr,"_", 0, i, ".csv", sep="")
    } else {
      file <- paste(yr,"_", i, ".csv", sep="")
    }
    data <- read.csv(file)
    # Datos para usuarios unicos
    usrs <- unique(data["Usuario_Id"])
    gen <-data[as.numeric(row.names(unique(data["Usuario_Id"]))), "Genero"]
  
    dff <- data.frame(usrs, gen)
    rm(data)
    rm(usrs)
    tmp <- dframe
    # union de datos previos y nuevos
    dframe <- unique(rbind(tmp, dff))
    rm(tmp)
    rm(dff)
    rm(gen)
    
  }
}
res <- summary(dframe$gen)
dframe <- dframe[dframe['gen'] == 'M' | dframe['gen'] == 'F',]
p <- ggplot(dframe, aes(gen)) + 
  geom_bar( aes(x=gen, y=..count.., fill=gen), colour="black", alpha=0.5) + 
  labs(title=paste("Número de usuarios por género de",
                   meses[mes_inicial],yr_in, "a", 
                   meses[mes_final], yr_f),
       x="Género", y = "Número de usuarios") +
  scale_y_continuous(
    breaks = seq(0, 36000, 2000),
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
  )+
  geom_text(aes(y = ((..count..)/sum(..count..)),
                label = scales::percent((..count..)/sum(..count..))),
            stat = "count", 
            vjust = -0.5)

ggsave("../Graphics/genderProp.png")
