from collections import Counter

if __name__ == "__main__":
  inputString = list(input("Enter a string: "))
  wc = Counter(inputString)

  max_count = max(wc.values())

  max_chars = [char for char, count in wc.items() if count == max_count]

  print(max_chars, max_count)
