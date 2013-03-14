# Warning: untested

londonMap <- function(city, data)
{
	colors <- c("darkred", "darkblue", "darkgreen", "black", "darkorange", "purple")	
	par(omi=c(0,0,0,0), mai=c(0,0,0,0))
	
	PlotOnStaticMap(city, data$lat[1], data$lon[1], col=colors[data$group[1]], cex=1, pch=19)
	for (i in 2:length(data$lat))
	{
		PlotOnStaticMap(city, data$lat[1], data$lon[1], col=colors[data$group[1]], cex=1, add=T)
	}
}


# Data format: csv
# Columns:
#	lat, lon, group_id

library(RgoogleMaps)
library(ReadImages)

London <- GetMap(center=c(51.514910,-0.126858), zoom =12, destfile = "London.jpg", maptype = "terrain")
data <- read.table(file.choose(), sep=",")
londonMap(London, data)
