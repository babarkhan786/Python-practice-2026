samosa = ('Aalo, piaz, sabz mirch, anar dana, dhania, maida, namak')
print(samosa)
# if use single qutation, brackets will not appear 
samosa_1 = ("Aalo", "piaz", "sabz mirch", "anar dana", "dhania", "maida", "namak")
print(samosa_1)
# pros:
#1. it reduce the human efforts for coding
#2. easy to write for long datasets
#3. easy to recall

# starategy
#1. do not use reserve words used by python 
# False      await      else       import     pass
#None       break      except     in         raise
#True       class      finally    is         return
#and        continue   for        lambda     try
#as         def        from       nonlocal   while
#assert     del        global     not        with
#async      elif       if         or         yield

#2. dont ever write variable names with spaces, use underscore _
#3. do not capitalize
#4. always use short words
#5. do not use special characters,
#6. use numbers in start @ # etc
#7. variable should be meaningfull
#8. global trends eg. df for data frame, plot plt
#9. don't ever repeat same variable names
#10. do not use operators in variables
#11. add new variables eg, samosa, samosa_1, samosa_2
#12. don't use variables inside quttions


x = 2+3+9*12*(2/3)
name_2 = ("my name is babar")
fruit_baskit = ("Apple", "Banana", "Pineapple", "Pear", "Peach", "Mangoes")
print(fruit_baskit)
print(samosa)
print(x)

print(type(samosa))
print(type(x))
print(type(fruit_baskit))

x_1 = "15" # string
print(x_1)
print(type(x_1))

# float
x_1 = 15.7 # float
print(x_1)
print(type(x_1))

#change from str to int
x_1 = int(x_1) # conveted to intiger
print(type(x_1))