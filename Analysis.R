col_names <- names(data)
data[,col_names] <- lapply(data[,col_names] , factor)
a <- table(data$Platform)
# Pie Chart with Percentages
library(plotrix)
#slices <- c(493, 4, 173, 583, 24, 14, 10, 510)
#lbls <- c("Android", "ifttt", "iPad", "iPhone", "Mobile Web", "The Social Jukebox", "TweetDeck", "Twitter Web Client")
slices <- c(52, 173, 493, 510, 583)
lbls <- c("Others", "iPad", "Android","Twitter Web Client", "iPhone")
pct <- round(slices/sum(slices)*100)
lbls <- paste(lbls, pct) # add percents to labels 
lbls <- paste(lbls,"%",sep="") # ad % to labels 
pie(slices,labels = lbls, col=rainbow(length(lbls)),main="Pie Chart of User Platform", )

pie3D(slices,labels=lbls,explode=0.1,
      main="Pie Chart of Platforms ")
