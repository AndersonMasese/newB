#.*.F means function

#from sys import argv
#if len(argv) > 1:
#    if len(argv[1]):
#        if ".nub" in argv[1]:
#           filepath = argv[1]
#
#with open(filepath,'r+') as f:
#proposed by codeinfig.wordpress.com

import re

operators = ['+','-']
conditionals = ['if','when'] #then replaces the : as in if x=3 :

with open('txt.nub','r+') as f:
	filecontent = f.read()+' <EOF> '

values={} #global so as to be accessible from funcs

def parseF(textlist):
	data=textlist
	incr_var = 0
	while incr_var < len(data) :
		forwardIndex = incr_var + 1
		backwardIndex = incr_var - 1
		if forwardIndex >= len(data): #preventing out of bounds in array
			forwardIndex = incr_var

		cur_token = data[incr_var]
		next_token = data[forwardIndex]
		previous_token = data[backwardIndex]
		index=data.index(cur_token)

		if 'ASS' in cur_token:
			cur_token+=''+cur_token.replace('ASS ','')


		if cur_token == 'output':
			#print(cur_token)
			#print(next_token)
			if next_token in values :
				print(values[next_token]) #printing the var by fetching the value
			else :
				print(next_token.replace('STRING','').replace('NUM','').strip())


		incr_var+=1


def tokenF(load):
	data = load #takes in a list
	t_var=''
	incr_var=0
	#num = ['0','1','2','3','4','5','6','7','8','9'] not needed checked in isdigit()

	while incr_var < len(data):
		cur_char = data[incr_var]
		index=data.index(cur_char) #get index of current char

		pattern=r"'(.)*'" #regex for string
		match= re.search(pattern,cur_char)

		if cur_char == '=':        #cur_char is not only one char but can also be 20 for example
			data[index] = 'ASS '+data[index]

			var_name = data[index-1]
			var_value = data[index+1]
			values[var_name]=var_value #adding to dict
			data[index-1] = 'VAR '+ data[index-1]

		elif cur_char in conditionals :
			data[index] = 'COND ' + data[index]


		elif cur_char.isdigit()==True:    # or unicode.isNumeric()
			data[index] = 'NUM '+data[index]

		elif cur_char in operators:
			data[index] = 'OPER '+data[index]
			B4=data[index-1]
			After=data[index+1]
			if B4.isdigit()==False :
				data[index-1] = 'VAR '+data[index-1]

		elif match is not None:
			data[index] = 'STRING '+data[index]

		incr_var+=1

	return data
	#print(values)

def splitF(feed):
	raw = feed
	rawChar = ['(',')','+','-','*','/','&','%','=',' ','\n',';','/*','*/']
	formattedChar = [' ( ',' ) ',' + ',' - ',' * ',' / ',' & ',' % ',' = ','  ',' NEWLINE ',' ; ',' /* ',' */ '] #replace with space
	incr_var = 0
	while incr_var < len(rawChar):
		raw =''+raw.replace(rawChar[incr_var],formattedChar[incr_var])
		incr_var +=1
	#print(raw)
	return raw.split()

print(splitF(filecontent))                                    #debug
print(tokenF(splitF(filecontent)))
print(values)
print(' ')
print(parseF(tokenF(splitF(filecontent))))                    #real


#now we'll do the operation part. in parsing we'll not do the assignment since we've already done it, we'll concentrate on operations ia 






# s= "'frewfgreg'"
# pattern = r"'(.)*'"

# match= re.search(pattern,s) 
# if match is not None:
# 	print(match.group)
