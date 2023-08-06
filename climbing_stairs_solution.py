def climbing_stairs(n):
    if n == 1:
        return 1

    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1

    # Calculate the number of ways to reach each step from step 2 to n.
    for i in range(2, n + 1):
        # Number of ways to reach the i-th step is the sum of ways to reach
        # the (i - 1)-th step and the (i - 2)-th step.
        dp[i] = dp[i - 1] + dp[i - 2]
        # Explanation: To reach the i-th step, we have two options:
        #   1. Take one step from the (i - 1)-th step, which gives us dp[i - 1] ways.
        #   2. Take two steps from the (i - 2)-th step, which gives us dp[i - 2] ways.
        # Since these are distinct ways to reach the i-th step, we sum them up.

    # The result is the number of ways to reach the top (the nth step).
    return dp[n]

# Test the function with an example.
n_steps = 2
print(climbing_stairs(n_steps))  # Output: 8