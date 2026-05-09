from scipy.stats import poisson

# Average rainy days
lam = 10

# Probability of 12 or more rainy days
p1 = 1 - poisson.cdf(11, lam)

# Probability between 12 and 18 rainy days
p2 = poisson.cdf(18, lam) - poisson.cdf(11, lam)

print("Rainy Days Project")

print("Expected rainy days =", lam)

print("Probability of 12 or more rainy days")
print(round(p1, 4))

print("Probability of rainy days between 12 and 18")
print(round(p2, 4))

for i in range(12, 19):

    p = poisson.pmf(i, lam)

    print("Rainy Days =", i)

    print("Probability =", round(p, 4))
    