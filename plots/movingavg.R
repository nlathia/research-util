# Plot some data and a moving average on top of it
# Assumes:
#	1. Data Format: csv data with X, Y headers
#	2. Data is over 24 hours
#	3. Moving Average is 10 sample, 2-sided

data <- read.table(file.choose(), sep=",", header=T)

plot(data$X, data$Y, col=grey(.5), type="l", axes=F, xlim=c(0,24))
axis(1, labels=0:24, at=0:24)
axis(2)
box()
grid()

f <- rep(1/10, 10)
y_lag <- filter(a$prob, f, sides=2)

lines(a$hour, y_lag, col="red", lwd=2)

