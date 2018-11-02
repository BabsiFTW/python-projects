sample = ['GTA','GGG','CAC']

"""The project should have methods for each of the following:

Given a file, read in the DNA for each suspect and save it as a string
Take a DNA string and split it into a list of codons
Iterate through a suspect's codon list to see how many of their codons match the sample codons
Pick the right suspect to continue the investigation on"""

#start by adding a method called read_dna. It should take one parameter, called dna_file. 

def read_dna(dna_file):
  #create a variable called dna_data and set it equal to an empty string
  dna_data = str("")
  #use with to open dna_file in read-only mode, as f
  with open(dna_file, "r") as f:
    #add a for loop inside the with block
    for line in f:
      #add line to the empty dna_data using +=
      dna_data += line
  #return dna_data on the next line
  return dna_data

#Add a new method called dna_codons. It should take one parameter called dna
def dna_codons(dna):
  #create an empty list called codons
  codons = []
  #add a for loop. The loop should have a range from 0 to the length of dna. It should also iterate in increments of 3
  for i in range(0, len(dna), 3):
  # add a line that checks if the iterator, when incremented by 3, exceeds the length of dna
    if (i + 3) < len(dna):
      #add to the list using the .append() method
      codons.append(dna[i:i + 3])
  #return codons
  return codons

#add a method called match_dna. It should take one parameter called dna.
def match_dna(dna):
  #add a variable called matches and set it equal to zero
  matches = 0
 	#add a for loop that iterates through the dna list. Call the iterator codon.
  for codon in dna:
    #add an if statement that checks if the codon is also in the sample list.
    if codon in sample:
      #increment matches by 1 using the += operator
      matches += 1
   #return the matches variable.
  return matches
      
#  add a method called is_criminal that takes a parameter called dna_sample.
def is_criminal(dna_sample):
  #create a variable called dna_data. Set it equal to the result of calling the read_dna() method on the dna_sample parameter
  dna_data = read_dna(dna_sample)
	#create a variable called codons. Set it equal to the result of calling the dna_codons() method with dna_data as the argument.
  codons = dna_codons(dna_data)
  #add an if statement that checks if the number of matches is greater than or equal to three
  num_matches = match_dna(codons)
  if num_matches >= 3:
    #print out the number of matches using string formatting
    print "Found %i matches. The investigation should continue." % num_matches
    #Add an else block that prints the number of matches using string formatting
  else:
    print "Found %i matches. The suspect can be freed." % num_matches

#call the is_criminal() method separately on the three .txt files
is_criminal("suspect1.txt")
is_criminal("suspect2.txt")    
is_criminal("suspect3.txt")
