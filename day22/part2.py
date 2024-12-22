from collections import defaultdict

def get_new_secret(secret):
  secret = (secret ^ (secret * 64)) % 16777216
  secret = (secret ^ (secret // 32)) % 16777216
  return (secret ^ (secret * 2048)) % 16777216

secrets = list(map(int, open(0).read().splitlines()))

sequences_total_value = defaultdict(int)

for secret in secrets:
  prices = [int(str(secret)[-1:])]
  for _ in range(2000):
    secret = get_new_secret(secret)
    prices.append(int(str(secret)[-1:]))

  already_found = defaultdict(bool)
  for i in range(1, len(prices) - 3):
    d1 = prices[i] - prices[i - 1]
    d2 = prices[i + 1] - prices[i]
    d3 = prices[i + 2] - prices[i + 1]
    d4 = prices[i + 3] - prices[i + 2]
    if not already_found[(d1, d2, d3, d4)]:
      already_found[(d1, d2, d3, d4)] = True
      sequences_total_value[(d1, d2, d3, d4)] += prices[i + 3]
print(max(sequences_total_value.values()))
