
 # import data set
hour <- read.csv("https://raw.githubusercontent.com/reddyprasade/Bicycle-sharing-system-in-US/master/hour.csv")
hour

ncol(hour)

nrow(hour)

### TASK 1

names(hour)

# define recode function for recoding values:
recodev <- function(original.vector, 
                    old.values, 
                    new.values) {
  new.vector <- original.vector
  for (i in 1:length(old.values)) {
    change.log <- original.vector == old.values[i] & 
      is.na(original.vector) == F
    new.vector[change.log] <- new.values[i] 
    
  }
  return(new.vector)
}
# apply the functiontion for recoding season values
hour$season <- recodev(original.vector = hour$season,
           old.values = c(1:4),
           new.values = c("spring","summer","fall",
                          "winter"))

### TASK 1

# rename columns
names(hour)[4:5] <- c("year","month")
# recode year values
hour$year <- recodev(original.vector = hour$year,
           old.values = c(0,1),
           new.values = c(2011,2012))
# check column names
names(hour)

### TASK 1

# rename columns
names(hour)[names(hour)=="hum"] <- "humidity"
names(hour)[names(hour)=="cnt"] <- "count"
names(hour)

### TASKS 10, 1

# create a function for denormalisartion
tconvert <- function(min, max, vector){
  result <- vector * (max - min) + min
  return (result)
}

# apply the function and denormalise the temperature values
hour$temp <- tconvert(-8, 39, hour$temp)
hour$atemp <- tconvert(-16, 50, hour$atemp)

### TASKS 2, 9

# calculate mean, st.dev and median for each season
# by aggregation with dplyr library
library(dplyr)
hour.agg <- hour %>%
  group_by(season) %>%
  summarise(
    temp.min = min(temp),
    temp.max = max(temp),
    temp.med = median(temp),
    temp.stdev = sd(temp),
    temp.mean = mean(temp), 
    count = n())
hour.agg

### TASK 8

# create a boxplot for temperature by season
boxplot(temp ~ season,
        data = hour,
        xlab = "Season",
        ylab = "Temperature",
        main = "Temperature by Season",
        col = "skyblue")

# check seasons and respective months
# fall months
unique(hour$month[hour$season=="fall"])

# winter months
unique(hour$month[hour$season=="winter"])

# spring months
unique(hour$month[hour$season=="spring"])

# summer months
unique(hour$month[hour$season=="summer"])

### TASK 8

# create a beanplot for number of bike rents per each weather condition
library("beanplot")
require("beanplot")
require("RColorBrewer")
bean.cols <- lapply(brewer.pal(6, "Set3"),
                    function(x){return(c(x, "black", "gray", "red"))})
beanplot(count ~ weathersit,
         data = hour,
         main = "Bike Rents by Weather Condition",
         xlab = "Weather Condition",
         ylab = "Number of rentals",
         col = bean.cols,
         lwd = 1,
         what = c (1,1,1,0),
         log = ""
         )

### TASK 11

# create a data frame
df <- data.frame(spring = rep(NA, 3),
                 winter = rep(NA, 3),
                 summer = rep(NA, 3),
                 fall = rep(NA, 3))
row.names(df) <- c("mean", "median", "sd")

# fill the data frame with corresponding mean, median and sd values
vec <- c ("mean","median","sd") 
for (n in vec){
  for (i in unique(hour$season)) {
    my.fun <- get(n)
    res <- my.fun(hour$count[hour$season == i])
    df[n,i] <- res
  }
}  
df

# statistics (analysis of variance model)
summary(aov(count ~ season, data = hour))

# pairwise comparison of means for seasons
# in order to identify any difference between two means that is greater than the expected standard error
TukeyHSD(aov(count ~ season, data = hour))

### TASK 8

# create a boxplot for count~season in order to reveal the most popular season
# for bike rentals

boxplot(count ~ season,
        data = hour,
        xlab = "Season",
        ylab = "Count",
        main = "Count by Season",
        col = "yellow3")

### TASK 4

# correlation test for count~atemp
t1 <- cor.test(hour$atemp[hour$year == 2011],
               hour$count[hour$year == 2011])
t1

t2 <- cor.test(hour$atemp[hour$year == 2012], 
               hour$count[hour$year == 2012])
t2

# apa format
library("yarrr")
apa(t1)

apa(t2)

### TASKS 5, 6

# plotting the results in a scatterplot with regression lines

# blank plot
plot(x = 1,
     xlab = "Temperature",
     ylab = "Number of Rents",
     xlim = c(-25,50),
     ylim = c(0,1000),
     main = "Temperature vs. Count")

# draw points for 2011 year
points(x = hour$atemp[hour$year == 2011],
       y = hour$count[hour$year == 2011],
       pch = 16,
       col = "red",
       cex = 0.5
       )
# draw points for 2012 year
points(x = hour$atemp[hour$year == 2012],
       y = hour$count[hour$year == 2012],
       pch = 16,
       col = "darkgreen",
       cex = 0.5
       )

# add regression lines for two ears
abline(lm(count~atemp, hour, subset = year == 2011),
       col = "darkgreen",
       lwd = 3)

abline(lm(count~atemp, hour, subset = year == 2012),
       col = "red",
       lwd = 3)

# add legend
legend("topleft",
       legend = c(2011, 2012),
       col = c("darkgreen","red"),
       pch = c(16, 16),
       bg = "white",
       cex = 1
)

### TASK 5 

# summary on linear model fitting
summary(lm(count~weathersit, hour))

summary(aov(count~weathersit, hour))

### TASK 9

# calculate min, max, mean, st.dev and median for each season
# by aggregation with dplyr library

w.agg <- hour %>%
  group_by(weathersit) %>%
  summarise(
    temp.min = min(temp),
    temp.max = max(temp),
    temp.mean = mean(temp),
    temp.stdev = sd(temp),
    temp.med = median(temp), 
    count = n())
w.agg

### TASKS 7, 11 

# create histograms for each weather condition
# to explore distribution of the bike rentals by 
# weather condition

# create a vector for histograms titles
vec <- c("Clear Weather", "Cloudy Weather", "Rainy Weather", "Thunderstorm Weather")

# parameters for plots combining
par(mfrow = c(2, 2))

# create 4 histograms with a loop
for (i in c(1:4)){
  name.i <- vec[i]
  hist(hour$count[hour$weathersit == i],
     main = name.i,
     xlab = "Number of Rents",
     ylab = "Frequency",
     breaks = 10,
     col = "yellow3",
     border = "black")
  
# the line indicating median value
abline(v = median(hour$count[hour$weathersit == i]),
       col = "black", 
       lwd = 3, 
       lty = 2) 

# the line indicating mean value
abline(v = mean(hour$count[hour$weathersit == i]),
       col = "blue", 
       lwd = 3, 
       lty = 2) 
}

6. Is there a significant difference between total bike rentals on holidays and working days?
### TASK 3

t <- t.test(hour$count[hour$holiday == 0],
       hour$count[hour$holiday == 1])

# apa format
apa(t)

# TASK 8

beanplot(count ~ holiday,
         data = hour,
         main = "Bike Rents by Type of a Day",
         xlab = "Type of Day",
         ylab = "Number of rents",
         col = bean.cols,
         lwd = 1,
         what = c(1,1,1,0),
         log = ""
         )
