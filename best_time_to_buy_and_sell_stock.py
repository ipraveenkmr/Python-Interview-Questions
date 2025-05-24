# ✅ Constraints:
# Only one transaction allowed (buy once, sell once).

# Cannot sell before you buy.

# ✅ Optimal Solution: One-pass using Two Pointers (O(n) time)
# 🔍 Idea:
# Track the minimum price seen so far.

# At each step, compute the potential profit if sold on the current day.

# Keep track of the maximum profit.


def maxProfit(prices):
    min_price = float('inf')  # Set to infinity initially
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price  # Update min_price if current is lower
        else:
            profit = price - min_price  # Potential profit
            max_profit = max(max_profit, profit)  # Update max profit

    return max_profit


prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))  # Output: 5


# print(maxProfit([7, 6, 4, 3, 1]))  # Output: 0 (No profit possible)
# print(maxProfit([1, 2]))          # Output: 1


# 🧠 Time & Space Complexity:
# Time: O(n) – One pass through the list.

# Space: O(1) – Constant space used.