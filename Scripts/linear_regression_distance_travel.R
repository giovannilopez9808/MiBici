path_data <- "../Output/"
file_data <- "Yearly_mean_distance.csv"
data <- read.csv(paste(
    path_data,
    file_data,
    sep = ""
))
reg <- lm(Mean.distance ~ rownames(data), data = data)
summary(reg)
plot(rownames(data), data$Mean.distance)
abline(reg)
plot(reg)