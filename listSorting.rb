require 'pry'

class Sorter

  def initialize(input, output)
    @input = input
    @output = output
    @file_read
    @array
  end

  def read
    f = File.open(@input, "r")
    @file_read = f.read
    f.close
  end

  def convert_to_arr
    # converting string to array removing non-numbers and non-letters
    @array = @file_read.split(" ").map {|s| s.gsub /\W/, ""}
  end

  def sort
    # storing indicies of number strings to map them back later
    num_indicies = @array.map {|i| @array.index(i) if (i =~ /\d/) == 0}.compact
    # if there are no numbers
    if num_indicies.empty?
      @array.sort!
      #if there are only numbers
    elsif num_indicies.length == @array.length
      @array = @array.map {|n| n.to_i}.sort
    else
      # separating numbers and words for proper sort
      separation = @array.partition {|c| (c =~ /\d/) == 0}
      # sorting first array. Converting to integer in order to sort numbers bigger than 10
      separation[0] = separation[0].map {|n| n.to_i}.sort
      # sorting array of words and letters
      separation[1].sort!
      # inserting numbers in their original spots
      index = 0
      separation[0].each do |num|
        #inserting and sorted integers inside of array of sorted strings, simultaniously converting them into strings
        @array = separation[1].insert(num_indicies[index], num.to_s)
        # switching index for another iteration
        index += 1
      end
    end
  end

  def write
    f = File.new(@output, "w")
    f.write @array.join(" ")
  end

  def exe
    self.read
    self.convert_to_arr
    self.sort
    self.write
  end
end

Sorter.new(ARGV[0], ARGV[1]).exe