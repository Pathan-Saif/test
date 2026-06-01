text = input()
vowels = set("aeiouAEIOU")
print(sum(1 for ch in text if ch in vowels))