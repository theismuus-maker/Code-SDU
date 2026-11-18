#indexing

name = "theis muusmann"

#looks at a string in a variable and know what caractor it is
#[start:stop:step_lenght] 
first_name = name[0:5:1]
# the stop index is nok in the intervale so that is why we need to type a number one bigger than we want

print(first_name.capitalize())

#you can also just take on charahter by just have a number in [x]

last_name = name[6:14:1]
print(last_name.capitalize())


fun_name = name[::2]
print(fun_name)

#leaving the stop and start index to nothing python will automatic start from the first character and end at last character in a stirng
#leaving the step index to nothing pyhton will automatic set steps to 1


reversed_name = name[::-1]
print(reversed_name)

website = "http://google.com"
website = "http://tv2.com"


# a variables character haves to values a negativ and a positiv. If we look at a string from behind it starts at -1
slice_for_website = slice(7,-4)

print(website[slice_for_website])

# the index here is smart for the http:// and .com because it will alwas remove that part 