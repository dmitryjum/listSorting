import pdb
import re
import sys

class Sorter:
  def __init__(self, input, output):
    self.input = input
    self.output = output
    self.file_read = ""
    self.array = []

  def read(self):
    try:
      f = open(self.input, "r")
    except IOError:
      print "Can't read the file, try different .txt file or try again"
    else:
      # reading the file and removing new line symbol
      self.file_read = f.read().rstrip('\n')
      f.close()

  def convert_to_arr(self):
    self.array = self.file_read.split(" ")

  def remove_extra(self):
    # removing all non-number and non-letter/word symbols
    self.array = [re.sub(r'\W', "", i) for i in self.array]

    # helper method for map function to find all number strings
  def number_string(self, n):
    if re.match(r'\d', n) != None:
      return self.array.index(n)
    # helper method for map function to convert string to integer
  def to_i(self, i):
    return int(i)
    # helper method for map function to convert integer to string
  def to_s(self, i):
    return str(i)

  def sort(self):
    # grabbing all number string indicies for further mapping
    num_indicies = map(self.number_string, self.array)
    # stripping list of indicies from None values  
    num_indicies = filter(lambda x: x != None, num_indicies)
    # if our text file contains only words
    if len(num_indicies) == 0:
      self.array.sort()
    # if our text file contains only numbers    
    elif len(num_indicies) == len(self.array):
    # converting string numbers to integers for correct sorting
    # (numbers > 10 don't sort well being strings)
      self.array = map(self.to_i, self.array)
      self.array.sort()
    # bringing them back to strings to be able to join to big string and write back to file      
      self.array = map(self.to_s, self.array)
    else:
    # preparing 2 lists to separate numbers from words for separate sorting and further maping      
      digits, non_digits = [], []
      for d in self.array:
        # if number
        if re.match(r'\d', d) != None:
          digits.append(d)
        else:
          non_digits.append(d)
      digits = map(self.to_i, digits)
      digits.sort()
      digits = map(self.to_s, digits)
      non_digits.sort()
      index = 0
      for d in digits:
        # inserting numbers in non_numbers list according to indicies from original list
        # but in ascending order this time
        non_digits.insert(num_indicies[index], d)
        index += 1
        # assining local list to instance list to carry it further
      self.array = non_digits

  def write(self):
    f = open(self.output, "w")
    try:
      new_text = " ".join(self.array)
    except TypeError:
      print "join function requires string, you might be trying to joing integers, I'll convert them for you"
      self.array = map(self.to_i, self.array)
      new_text= " ".join(self.array)
      f.write(new_text)
      f.close()
    else:
    f.write(new_text)
    f.close()
    print "Your original file has been sorted, please check your new file"

  def exe(self):
    self.read()
    self.convert_to_arr()
    self.remove_extra()
    self.sort()
    self.write()

sorter = Sorter(sys.argv[1], sys.argv[2])
sorter.exe()