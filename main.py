text = "Python dasturlash tilini organish juda qiziqarli"

words = text.split()

print("So'zlar soni:", len(words))

longest = ""

for word in words:
    if len(word) > len(longest):
        longest = word

print("Eng uzun so'z:", longest)

vowels = 0

for char in text:
    if char.lower() in "aeiou":
        vowels += 1

print("Unli harflar:", vowels)

for word in words:
    print(word.upper())
