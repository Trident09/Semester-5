fibonacci <- function(n) {
    if (n <= 0) {
        stop("n must be a positive integer")
    }
    if (n == 1) {
        return(0)
    }
    sequence <- c(0, 1)
    for (i in 3:n) {
        next_number <- sequence[i-1] + sequence[i-2]
        sequence <- c(sequence, next_number)
    }  
    return(sequence)
}
n <- 10
fib_sequence <- fibonacci(n)
print(fib_sequence)
