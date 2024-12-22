def get_new_secret(secret):
  secret = (secret ^ (secret * 64)) % 16777216
  secret = (secret ^(secret // 32)) % 16777216
  return (secret ^ (secret * 2048)) % 16777216

secrets = list(map(int, open(0).read().splitlines()))
res = 0
for secret in secrets:
  for _ in range(2000):
    secret = get_new_secret(secret)
  res += secret
print(res)