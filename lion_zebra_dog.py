# The Art of Giving
# Code written in Python 3

# A python script to read a list of "Art of Giving" quotes and print them
quotes = ["Giving is not an obligation, it's a privilege.", 
          "The giving of love is an education in itself.", 
          "The greatest gift is a portion of thyself.", 
          "Giving comes full circle when it is done from the heart.", 
          "Giving from the heart is what makes life worth living.", 
          "Giving starts the minute we open our eyes each day.", 
          "The joy of giving far outweighs the sorrow of parting.", 
          "The true spirit of giving is to give without expecting anything in return.", 
          "Giving is the greatest joy, the greatest good we can do for others.", 
          "Giving is a form of appreciation and gratitude for the gift of life.",
          "Giving is a way to express your love and kindness to others.", 
          "Giving makes our lives more meaningful and fuller.", 
          "Giving makes us more aware of our blessings and the needs of others.",
          "The best way to give is to give from the heart.", 
          "Don't let the size of your gift determine the size of your heart.", 
          "Giving is the best way to increase our sense of well-being and joy.", 
          "Giving is an acknowledgment of our interconnectedness with others.", 
          "The reward of giving is an abundance of happiness that comes back to us.", 
          "Giving is a way to make the world a better place, for ourselves and others.",
          "Giving of yourself is the greatest gift you can give another.", 
          "Giving is an act of faith in the possibility of miracles.",
          "The secret to giving is to remember that it's not about what you give, but why you give."]

def print_quotes(quotes):
  # Iterate through the list and print each quote
  for quote in quotes:
    print(quote)

  # Print an empty line to separate the quotes
  print()

# Call the function to print the quotes
print_quotes(quotes)