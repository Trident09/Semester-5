# Create a vector of numbers
numbers <- c(10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

# Calculate and print the mean
mean_value <- mean(numbers)
print(paste("Mean: ", mean_value))

# Calculate and print the median
median_value <- median(numbers)
print(paste("Median: ", median_value))

# Calculate and print the mode
mode_value <- as.numeric(names(which.max(table(numbers))))
print(paste("Mode: ", mode_value))

# Calculate and print the range
range_value <- range(numbers)
print(paste("Range: ", range_value))

# Create a histogram
hist(numbers, main = "Histogram of Numbers", xlab = "Numbers", col = "blue", border = "white")