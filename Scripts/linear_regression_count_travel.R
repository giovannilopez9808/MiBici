path_data <- "../Output/"
file_data <- "Monthly_mean_count_travel.csv"
data <- read.csv(paste(
    path_data,
    file_data,
    sep = ""
))
reg <- lm(rownames(data) ~ Count, data = data)
summary(reg)
plot(data$Count, rownames(data))
abline(reg)
plot(reg)