# Step 1: Take user input
user_input <- readline(prompt = "Enter numbers (separated by spaces): ")

# Step 2: Convert user input to a numeric vector
user_input <- as.numeric(strsplit(user_input, " ")[[1]])

# Step 3: Calculate minimum and maximum values
min_value <- min(user_input)
max_value <- max(user_input)

# Step 4: Perform min-max normalization
normalized_input <- (user_input - min_value) / (max_value - min_value)

# Step 5: Print normalized input
print(normalized_input)
