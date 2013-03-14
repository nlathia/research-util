# Warning: untested

library(maps)
library(geosphere)

# Data Structure: csv
# Columns:
#	originLat, originLon, destinationLat, destinationLon, frequency
data <- read.table(file.choose(), sep=",")

# Map of the whole world
map("world", col="#002200", fill=TRUE, bg="black", lwd=0.05, boundary=FALSE)

# Limit to Europe only
# xlim <- c(-20, 50)
# ylim <- c(30, 71)
# map("world", col="#002200", fill=TRUE, bg="black", lwd=0.05, xlim=xlim, ylim=ylim)

for (i in 1:length(data$originLat))
{
	inter <- gcIntermediate(c(data$originLon[i], data$originLat[i]), c(data$destinationLon[i], data$destinationLat[i]), n=50, addStartEnd=TRUE)
	lines(inter, col="azure4", lwd=(data$frequency[i]/max(data$frequency))*3)
}