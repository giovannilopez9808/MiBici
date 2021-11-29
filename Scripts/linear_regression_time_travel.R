path_data <- "../Output/"
file_data <- "Monthly_mean_time_travel.csv"
data <- read.csv(paste(
    path_data,
    file_data,
    sep = ""
))
reg <- lm(Time ~ rownames(data), data = data)
summary(reg)
plot(rownames(data), data$Time)
abline(reg)
plot(reg)