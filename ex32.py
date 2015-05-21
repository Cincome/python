the_count= [1,2,3,4,5]
fruits= ['apples','oranges','pears','apricots']
change= [1, 'pennies',2,'dimes',3,'quarters']

# first kind of for loop
for number in the_count:
	print "This is count %d" %number

#same
for fruit in fruits:
	print "A fruit of type %s" %fruit

#mixed list
# have to use %r
for i in change:
	print "I got %r" %i

#build list
elements =[]

#use range function to create 0-5 counts
for i in range(0,6):
	print "Adding %d to the list." %i 
	#append is understood by lists
	elements.append(i)

#print them out
for i in elements:
	print "Element was: %d" %i