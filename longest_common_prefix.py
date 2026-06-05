words=["Hlo","Hly","Hlu"]

def longest_prefix(words):
  if not words:
     return ""
  first_word = words[0]

  for i in range(len(first_word)): 
      char = first_word[i]

      for word in words:
         if i >=len(word) or word[i] != char:
            return first_word[:i]
  return first_word
print(longest_prefix(words))

#TC O(M+N)
