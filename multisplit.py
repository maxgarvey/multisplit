#multisplit, why not?
#12-19-2011, author Max Garvey
def msplit( string, *args ):
  '''msplit function takes a string and a number of string arguments, and will split
  the string on each of the arguments.'''
  mylist = []             #really this is just a handler for _msplit, which takes
                          #a list of string arguments, so we just put each of the
  for arg in args:        #args into a list and run the other function on them
    mylist.append( arg )

  return _msplit( string, mylist, include_empty=False )

def msplit_empty( string, *args ):
  '''msplit empty sets the include empty boo to true so that we will get empty
  string: '' results.'''
  mylist = []

  for arg in args:
    mylist.append( arg )

  return _msplit( string, mylist, include_empty=True )

def _msplit( string, args, include_empty=False ):
  '''msplit function takes a string and a variable number of arguments; it splits
  on each of the arguments and returns a list of the substrings. trying to make it
  behave like split but with multiple possibilities.'''
  outlist = []
  
  string_pos_1 = 0      #basically, how it works is we keep two indexes in the
  string_pos_2 = 0      #string, the second one is the furthest position in the
                        #string and the first one is the start of the substring
  if include_empty:                       #if we reach a substring from args
    while string_pos_2 <= len( string ):  #then the substring from string_pos_1
      for arg in args:                    #to string_pos_2 gets appended to the
        if arg in string[string_pos_1:string_pos_2]:    #list
          outlist.append( string[string_pos_1:(string_pos_2-len(arg))] )
          string_pos_1 = string_pos_2     #and string_pos_1 is set to string_pos_2
      string_pos_2 += 1

  if not include_empty:      #essentially, this second block is the same as the
    while string_pos_2 <= len( string ):  #above, except it doesn't append any
      for arg in args:                    #empty strings to the list.
        if arg in string[string_pos_1:string_pos_2]:
          if string_pos_1 != (string_pos_2-len(arg)):
            outlist.append( string[string_pos_1:(string_pos_2-len(arg))] )
          string_pos_1 = string_pos_2
      string_pos_2 += 1

  if string_pos_1 != string_pos_2:  #if there's anything left at the end, this
    if not include_empty:           #block adds it to the list, if it's not the
      if string[string_pos_1:string_pos_2] != '':   #empty string.
        outlist.append( string[string_pos_1:string_pos_2] )
    else:
      outlist.append( string[string_pos_1:string_pos_2] )

  return outlist

def msplit_alt( string, args, include_empty=False ):
  '''msplit_alt function takes a string and a variable number of arguments; it splits
  on each of the arguments and returns a list of the substrings. trying to make it
  behave like split but with multiple possibilities.'''
  #this is a streamlined version of _msplit, it just has a few less lines of 
  outlist = []  #code because the condition checking takes place inside of the
                #while loop, rather than having 2 while loops.
  string_pos_1 = 0
  string_pos_2 = 0

  while string_pos_2 <= len( string ):
    for arg in args:
      if arg in string[string_pos_1:string_pos_2]:
        if not include_empty:
          if string_pos_1 != (string_pos_2-len(arg)):
            outlist.append( string[string_pos_1:(string_pos_2-len(arg))] )
          string_pos_1 = string_pos_2
        else:
          outlist.append( string[string_pos_1:(string_pos_2-len(arg))] )
          string_pos_1 = string_pos_2
    string_pos_2 += 1

  if string_pos_1 != string_pos_2:
    if not include_empty:
      if string[string_pos_1:string_pos_2] != '':
        outlist.append( string[string_pos_1:string_pos_2] )
    else:
      outlist.append( string[string_pos_1:string_pos_2] )

  return outlist
