try = s[0]
best = ''

for n in range(1, len(s)):
    if len(try) > len(best):
        best = try
    if s[n] >= s[n-1]:
        try = try + s[n]
    else:
        try = s[n]
print('Longest substring in alphabetical order is: ' + best)