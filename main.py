text = input().replace(" ", "").lower()
print("YES" if text == text[::-1] else "NO")