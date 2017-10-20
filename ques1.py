def words(inputletters):
    inputletters = set(inputletters)
    with open('book1.txt') as qfile:
      with open('book2.txt') as qfile:
        with open('book3.txt') as qfile:
          words = map(str.strip, qfile)
          letters = map(set, words)
          matching = filter(inputletters.issubset, letters)
          longest = max(matching, key=len)
          return longest
