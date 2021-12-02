message = ""
while message != "Done" and message != "done":
  message = input()
  letters = list(message)
  if message == "Done" or message == "done":
    pass
  else:
    letters.reverse()
    for letter in letters:
      print(letter, end="")
    print()