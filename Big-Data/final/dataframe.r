# Create two vectors
vector1 <- c(1, 2, 3, 4, 5, 1)  # Add a duplicate value
vector2 <- c("A", "B", "C", "D", "E", "A")  # Add a duplicate value

# Create a data frame using the vectors
df <- data.frame(vector1, vector2)

# Display duplicate elements
duplicates <- df[duplicated(df), ]
print("Duplicate elements:")
print(duplicates)

# Display unique rows
unique_rows <- unique(df)
print("Unique rows:")
print(unique_rows)