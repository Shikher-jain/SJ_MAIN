class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, n):
        if n < 2:
            return 0

        # Initialize a boolean list of size n+1 with True values
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers

        p = 2
        while p * p <= n:
            if is_prime[p]:
                # Mark all multiples of p as non-prime
                for multiple in range(p * p, n + 1, p):
                    is_prime[multiple] = False
            p += 1

        # Count the number of primes
        prime_count = sum(is_prime)
        return prime_count


n=19
print(Solution().solve(n))