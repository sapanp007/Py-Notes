
"""logging and datetime module """

# from datetime import datetime, timedelta
# import logging
# log_etn = datetime.now().strftime('%d_%b_%Y_%H_%M_%S')
# logging.basicConfig(filename = f"log_file_{log_etn}.log", level = logging.INFO, format = '%(asctime)s - %(message)s')
# # format names - process, asctime, message
# print(datetime.now())
# print(datetime.now().strftime('%d-%b-%Y %H %M %S'))
# x = datetime.now().strftime('%d-%b-%Y %H %M %S')
# print(type(datetime.now().strftime('%d-%b-%Y %H %M %S')))
# print(datetime.now() + timedelta(days = 3, hours = 65, minutes = 7, seconds = 78)) # years and months doesn't work
# d = datetime(1993, 12, 1, 1, 13, 13)
# print(d)
# z = datetime.strptime(x, '%d-%b-%Y %H %M %S')
# from datetime import datetime
# date_string = "Feb 25 2020 9:20PM" #AM/PM
# print(datetime.strptime(date_string,'%b %d %Y %I:%M%p'))
# print(type(z),z)
# logging.info("all done")


""" argparse module"""
# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument("--s",help='Store a simple value')
# parser.add_argument('-c', action='store_const',
#                     dest='constant_value',
#                     const='value-to-store',
#                     help='Store a constant value')
# results = parser.parse_args()
# print(f's value = {results.s}')

# import argparse
# def main():
# 	print(args.s)
# if __name__ == "__main__":
# 	parser = argparse.ArgumentParser()
# 	parser.add_argument("a",help = "it assigns a value")
# 	parser.add_argument("--s",help = "it assigns a value", type = int , default = 89, required = True)
# 	args = parser.parse_args()
# 	main()

"""
keys-  
    type
    required
    default
    help
- or -- makes args optional arguments
without - and -- it makes that param mandatory
I don't see a combine usage of  default and required = True usage together
"""

# import subprocess
# # result = subprocess.run("ls", shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
# result = subprocess.run("awk -F' ' '{print $1}'  123.txt", stdout = subprocess.PIPE, shell = True )
# for i in result.stdout.decode().split('\n'):
# 	print(i)

# import subprocess
# res=subprocess.run("cd /Users/ ; cd sappradh/Documents && ls -lrt | grep Python",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
# print(res.stdout.decode())

# $ false ; echo "OK"
# OK
# $ true ; echo "OK"
# OK
# $ false && echo "OK"
# $ true && echo "OK"
# OK
# $ false || echo "OK"
# OK
# $ true || echo "OK"
# $


# import random
# print(random.random()) #prints value between 0-1 (1- exclusive)
# print(random.randint(1,6)) #both inclusive
# print(random.uniform(1,2))
# l1=['red','green','blue' ]
# print(random.choice(l1)) 
# print(random.choices(l1,k=10,weights=[5,6,3]))


## *args **kwargs
# def func(*args,**kwargs):
#      arguments=locals()
#      print(arguments)
#      for i in arguments:
#           print(i)
#      for i in args:
#           print(i)
#      for i,j in kwargs.items():
#           print(i,j)
# #func('sa','1','3',sapan=8,sagar=9)
# #func(1,2,3,4,5,sapan=4,sagar=5)
# tup=['Sapan','Sagar','Pradhan']
# dic={'Sapan':5,'Sagar':10,'Pradhan':22}
# func(*tup,**dic)

# import time
# from functools import wraps
# def decorattor_func(original_func):
#      @wraps(original_func)
#      def wrapper_func(*args,**kwargs):
#           print("Inside 1st wrapper function")
#           try:
#                result=original_func(*args,**kwargs)
#                return result
#           except ZeroDivisionError:
#                print("divide by zero error")
#      return wrapper_func

# def my_time(original_func):
#      @wraps(original_func)
#      def wrapper_func(*args,**kwargs):
#           print("Inside my_time wrapper function")
#           start=time.perf_counter()
#           result= original_func(*args,**kwargs)
#           end=time.perf_counter()
#           print(f'total time taken = {round(end-start,2)}')
#           return result
#      return wrapper_func

#@my_time
#@decorattor_func
# def original_func(x,y):
#      print("Original func executed")
#      return x+y
# #original_func=decorattor_func(original_func)
# #print(original_func(1,2))
# original_func=my_time(decorattor_func(original_func))
# print(original_func(2,4))


# student={'name':'Sapan', 'age':[26,24], 'address':'Blr'}
# print(student)
# print(student.keys())
# print(student.values())
# print(student.items())
# print(student.get('wow','Not Found')) #returns none/default
# student.update({'name':'Sagar','sex':'M'})
# print ( sorted((student.items() )) ) # returns a list of tuple though
# sort_dict=sorted(student.items(),key= lambda x: str(x[1]) , reverse=True) 
# import collections
# stu1= collections.OrderedDict(sort_dict)
# print(stu1.items())
# dd=collections.defaultdict(int)
# for i,j in sort_dict:
#      dd[i]=j
# print(dd.items())
# print(dd['newkey1'])
# print(dd.items())

# import collections
# c=collections.Counter('sapansagar')
# print(c)
# print(c.most_common(1)[0][0])
# print(c.elements) # returns an iter
# print(list(c.elements()))
# a=collections.Counter(a=2,b=5)
# b=collections.Counter(a=1,b=2)
# a.subtract(b) #a changes b doesn't
# print(a)
# print(b)
# print(collections.deque('Sapan',3))

# set1={'W','BD','C'}
# print(sorted(set1))
# l1=[1,2,3,4,'sapam']
# l2=[]
# for i in l1:
#      l2.append(str(i) )
# print(sorted(l2))


# l1=[1,2,9,3,4,5]
# l1.remove(2) #REMOVES ITEM IF FOUND ELSE VALUERROR
# print(l1)
# del l1[0:1]
# print(l1)
# l1.pop()
# print(l1)

# l1=[1,2,3,2,3,4,4,5]
# l2=list(sorted(set(l1)))
# print(l2)

# t1=(2,1,3,4,2)
# print(sorted(t1))

# s1={8,7,5,5}
# print(s1)
# s1.add(2)
# s1.remove(5)
# print(s1)

# cx_Oracle.DatabaseError
# ModuleNotFoundError
# ZeroDivisionError
# StopIteration
# TypeError
# ValueError
# KeyError

# mem_profile.memory_usage_resource()

# LEGB Rule

# a.intersection(b)
# a.difference(b)
# a.union(b)

# msg="Sapan Sagar"
# # print(msg.lower())
# # print(msg.count("S"))
# print(msg.find("Sagar")) #returns the index of the word(not letter)
# print(msg.replace("Sagar","Pradhan"))
# print(dir(msg)) #returns a list of the functions associated 
#print(help(str))

#-5 to 256 int id() func works

# import sys
# print(sys.path) #checks the import files names in this list of path
# import os
# print(os.__file__)
# print(sys.version)

# pip help
# pip list
# pip list --outdated
# pip freeze > newfile.txt
# pip install -r newfile.txt

# import os
# print(os.path.expanduser('~'))
# filename=os.path.join(os.getcwd(),'xyz.txt')
# with open(filename,'r') as f:
#      # print(f.read()) #whole thing s string
#      # f.seek(0)
#      # print(f.readline()) #only one line
#      # f.seek(0)
#      # print(f.readlines()) #returns a list containing each line as element
#      g=(i for i in f.readlines())
#      print(g)
#      for i in g:
#           print(i,end="")



# class A():
#      def func1(self):
#           print("In A")
# class B():
#      def func1(self):
#           print("In B")
# class C():
#      def func1(self):
#           print("In C")
# class D(A,C,B):
#      # def func1(self):
#      #      print("In D")
#      pass

# obj1=D()
# obj1.func1()


# import re
# text_to_search=''' psnsapsn
# sagar 222 444
# dssdaadf '''
# pattern = re.compile(r'(?<!psn)sa')
# result= pattern.finditer(text_to_search)
# for i in result:
#      print(i)
#      print(i.start(),i.end(),i.group(0))

# (?=foo)	Lookahead	Asserts that what immediately follows the current position in the string is foo
# (?<=foo)	Lookbehind	Asserts that what immediately precedes the current position in the string is foo
# (?!foo)	Negative Lookahead	Asserts that what immediately follows the current position in the string is not foo
# (?<!foo)	Negative Lookbehind	Asserts that what immediately precedes the current position in the string is not foo


# import json
# import collections 
# d1='''{
#   "data": 
#   [{
#     "type": "articles",
#     "id": "1",
#     "attributes": {
#       "title": "JSON:API paints my bikeshed!",
#       "body": "The shortest article. Ever.",
#       "created": "2015-05-22T14:56:29.000Z",
#       "updated": "2015-05-22T14:56:28.000Z"
#     },
#     "relationships": {
#       "author": {
#         "data": {"id": "42", "type": "people"}
#       }
#     }
#   }],
#   "included": [
#     {
#       "type": "people",
#       "id": "42",
#       "attributes": {
#         "name": "John",
#         "age": 80,
#         "gender": "male"
#       }
#     }
#   ]
# }'''

# d2='''{
#   "data": 
#   [{
#     "type": "articles",
#     "id": "1",
#     "attributes": {
#       "title": "JSON:API paints my bikeshed!",
#       "body": "The shortest article. Ever.",
#       "created": "2015-05-22T14:56:29.000Z",
#       "updated": "2015-05-22T14:56:28.000Z"
#     },
#     "relationships": {
#       "author": {
#         "data": {"type": "people","id": "42"}
#       }
#     }
#   }],
#   "included": [
#     {
#       "type": "people",
#       "id": "42",
#       "attributes": {
#         "gender": "male"
#         "name": "John",
#         "age": 80,
#       }
#     }
#   ]
# }'''

#x = json.loads(d1, object_hook=lambda d : collections.namedtuple('X', d.keys()) (*d.values())  ) 
# l=[]
# for i in range(len(x)):
#      l.append(x[i])
# print(l)



# new_list=[]
# def dic(d):
#      for i in d.keys():
#           if isinstance(d[i],dict):
#                dic(d[i])
#           elif isinstance(d[i],(list,tuple)) and d[i]!= ([],()) and isinstance(d[i][0],dict) :
#                dic(d[i][0])
          
#           if isinstance(d[i],(int,str)):
#                new_list.append((i,d[i]))
#           else:
#                new_list.append((i,sorted(d[i])))
# dic(d)
# print(new_list)


#Idempotent

# import requests
# url='https://xkcd.com/353/'
# r=requests.get(url)
# # print(r.status_code)
# # print(r.content) #retuens data in bytes to write into a file
# # print(r.text) # returns the source code

# print(r.ok)


# global a
# _a= 5
# def outer():
#      a=9
#      def inner():
#           nonlocal a
#           a=3
#           print(a)
#      inner()
#      print(a)
# outer()
# print(_a)

#nonlocal -- neither global or local / enclosing


# def cf():
#      while True:
#           val=yield
#           print(val)
# def pf(c):
#      while True:
#           val=range(1,11)
#           for i in val:
#                c.send(i)
#                yield
# if __name__ =='__main__':
#      c=cf()
#      next(c)
#      p=pf(c)
#      for wow in range(10):
#           next(p)

#FACTORIAL GEN
# def fact(value):
#      i=1
#      while i<=value:
#           fact=1
#           j=1
#           for j in range(j,i+1):
#                fact=fact*j
#           yield fact
#           i+=1
# for i in fact(5):
#      print(i)


#Memoization: 
# d={}
# def fib(n):
#      if n in d:
#           return d[n]
#      if n<=1:
#           value= 1
#      else:
#           value= (fib(n-1)+fib(n-2))
#      d[n]=value
#      return value
# for i in range(1000):
#      print(fib(i))


# from functools import lru_cache
# @lru_cache(maxsize=1000)
# def fib(n):
#      if n<=1:
#           return 1
#      else:
#           return (fib(n-1)+fib(n-2))
# for i in range(1000):
#      print(i,": ", fib(i))


# from collections import namedtuple
# Color=namedtuple('Color',['red','green','blue'])
# white=Color(55,23,24)
# blue=Color(55,23,24)
# print(white[2])

# import PyPDF2
# with open('/Users/sappradh/Downloads/Madhu_Resume.pdf','r') as f:
#      pdf=PyPDF2.PdfFileReader(f)
#      information = pdf.getDocumentInfo()
#      number_of_pages = pdf.getNumPages()

#      print(information)

# import cx_Oracle
# cogs_connection = cx_Oracle.connect('cogs' + '/' + 'password' + '@' + '''(DESCRIPTION =
#      (ADDRESS = (PROTOCOL = TCPS)(HOST = hostname)(PORT = 8080))
#      (CONNECT_DATA =
#      (SERVER = DEDICATED)
#      (SERVICE_NAME = service_name)
#      )
#      )''')
# cogs_connection.autocommit = True
# cursor_name = cogs_connection.cursor()

# class A():
#      def __init__(self,filename):
#           self.filename=filename

#      def create_generator(self):
#           with open(f'{self.filename}','r') as f:
#                return ( items.replace('\n','').split(",") for items in f.readlines() )

#      def load_to_table(self,table_name):
#           gen_obj=self.create_generator()
#           for rows in gen_obj:
#                cursor_name.execute(f"insert into {table_name} values({rows[0]},{rows[1]},{rows[2]},{rows[3]},{rows[4]},'01-AUG-2019',{rows[5]},{rows[6]})")

# file1=A('/Users/sappradh/Downloads/netarch_data.csv')
# file1.load_to_table('fct_ecor_bw_cost_tmp')

# cursor_name.close()
# cogs_connection.close()







# l1=[{'time': 3,
#   'discussion': [{'Good afternoon.': 0},
#    {'Thanks for calling dogs.': 0},
#    {"That insurance, you mean, how may I help you today? Hi, My name's Charlie.": 0},
#    {"I'm calling from the sales team.": 0},
#    {"I've got a customer on the phone and they're looking for a quote for their dog, but we're having a bit of difficulty finding a braid.": 0},
#    {'They dropped.': 0},
#    {"The dog is a silky terrier cross, but we've only got Australian silky terrier on our system and they are saying that it's a different dogs.": 0},
#    {"They're wondering if they can put down your cheek area because apparently that's the same thing.": 0}]},
#  {'time': 33,
#   'discussion': [{"I just want to confirm with you whether if they put down your shit area, but it's silky terrier on the certificate off the dog.": 0},
#    {"Can they bring up problems later? Okay, on Or let me just ask, What is the breed of the So the Brady's a silky terrier cross, but the silky terrier is more dominant, but we don't have silky terrier on a system.": 0},
#    {"We've only got Australian silky terrier silky career across Chihuahua.": 0}]},
#  {'time': 63,
#   'discussion': [{'Yep.': 0},
#    {'Okay.': 0},
#    {'And, um, what is on this list? Mm.': 0},
#    {'Sorry that you can only check.': 0},
#    {"So there's only Australian still keep Ariel, but they're saying it's not an Australian silky terrier.": 0}]},
#  {'time': 93,
#   'discussion': [{'Just a stereo.': 0},
#    {'Okay.': 0},
#    {'I would just ask my support here if we could, uh, or how we could actually have it replaced.': 0},
#    {'All right? Yeah.': 0},
#    {'Okay.': 0},
#    {'One moment, please, Charlie.': 0},
#    {'Thank you.': 0}]},
#  {'time': 123, 'discussion': []},
#  {'time': 153, 'discussion': []},
#  {'time': 183, 'discussion': []},
#  {'time': 213, 'discussion': []},
#  {'time': 243, 'discussion': []},
#  {'time': 273, 'discussion': []},
#  {'time': 303, 'discussion': []},
#  {'time': 333, 'discussion': []},
#  {'time': 363, 'discussion': []},
#  {'time': 393,
#   'discussion': [{'Thanks for waiting on Charlie.': 0},
#    {'Yes.': 0},
#    {'Yes.': 0},
#    {'It could be weeping on the line.': 0},
#    {'Yes.': 0},
#    {'OK, I actually checked.': 0},
#    {'They were my support.': 0},
#    {'I took all of the Australian circuit area could not be replaced with the Tokyo area.': 0},
#    {'Those are actually two different a breed.': 0},
#    {'But yeah, the if this is actually the case, Charlie, if there is any documents that the customer cannot provide so that we could check the domain breed off the bed.': 0}]},
#  {'time': 423,
#   'discussion': [{'Yes, sir.': 0},
#    {'He said that on the documents.': 0},
#    {"It is still keep carrier Cross to our Okay, Uh, that is the domain breed off the bet, and that's really read.": 0},
#    {'That is that is listed on the document.': 0},
#    {"Yeah, that's what he said.": 0},
#    {'I What should I put down on the quote? Yeah, because, um, if, uh, this is a case that yeah, even us I apologised status, Charlie, even as we could not check this.': 0}]},
#  {'time': 453,
#   'discussion': [{'But if that is the information that is written on the document.': 0},
#    {'Um, let me just go back to my support.': 0},
#    {'One woman, please try and be as quick as possible.': 0},
#    {'I understand.': 0}]},
#  {'time': 483,
#   'discussion': [{'I hate that noise.': 0},
#    {'Standard line.': 0},
#    {'Thank you.': 0}]},
#  {'time': 513,
#   'discussion': [{"You're being transferred to a picture or claims consultant, please be sure to have all required information ready.": 0}]},
#  {'time': 543, 'discussion': []},
#  {'time': 573, 'discussion': []},
#  {'time': 603,
#   'discussion': [{'There appears to be no one available to take your call.': 0},
#    {"Please advise the customer that you are requesting a call back and that you'll hear from the appropriate person as soon as possible.": 0}]},
#  {'time': 633, 'discussion': []},
#  {'time': 663,
#   'discussion': [{'All right, Charlie? Yes, Yes.': 0},
#    {"Actually, I'm trying to coordinate the plane because I'm trying to get in touch with them so that we could check.": 0},
#    {'What is the information that we could put down? Yes.': 0},
#    {'Unfortunately, our name is not answering the call.': 0}]},
#  {'time': 693,
#   'discussion': [{"I've been.": 0},
#    {'So could we just put it to Al across minutes? Talk to our Ah, yeah.': 0},
#    {'That define, Actually.': 0},
#    {"Even though if you're going to put in unknown or two all across that fine.": 0},
#    {'However, if the, um if the er customer will actually submit a claim and there might be some issue with our claims team, that is why we need to identify them.': 0},
#    {"So for now, if that's the case.": 0}]},
#  {'time': 723,
#   'discussion': [{'Yeah, you could just, uh, put in to our lacrosse and we could just leave a note on the policy.': 0},
#    {'That is the case.': 0},
#    {'Okay, no problem.': 0},
#    {"We'll let the customer know that.": 0},
#    {"I just want to get back to them as soon as possible because they're not very happy.": 0},
#    {"They've been on hold for a long time, but thank you.": 0},
#    {'Thank you.': 0},
#    {'All right, Thank you.': 0}]}]



# def func1():
#      for i in l1:
#           for j in i['discussion']:
#                for k in j.keys():
#                     print(k,end=" ")



# class Person:
#     name = ""
#     age = 0

#     def __init__(self, personName, personAge):
#         self.name = personName
#         self.age = personAge

#     def __repr__(self):
#         # return {'name':self.name, 'age':self.age}
#         return '__repr__ returned'

#     def __str__(self):
#         # return 'Person(name='+self.name+', age='+str(self.age)+ ')'
#         return '__str__ returned'        

# p = Person('Pankaj', 34)
# print(p)
# by default dunder str is looked first and then __repr__ and just the object without print function goes for dunder repr method
# print('{} {}'.format(3,5))


# MsiExec.exe is the executable program of the Windows Installer used to interpret installation packages 
# and install products on target systems. 

# net use  -- to access a shared folder, returns 0 if path is valid 

# import module -- simply imports everything including private variables/methods/others ;
# 					have to type modulename.function() to access function

# from module import *  -- Imports everything except private stuff
# 						no need to use the module name, function() can be called directly

# import sys
# print(sys.argv)
# gives a list with first value as filename and then the parametrs after that
# ex:  ['C:\\Users\\spradhan\\Documents\\Python-Scripts\\test_python.py']

# from lxml import etree
# tree = etree.parse("C:\\Users\\spradhan\\Documents\\Python-Scripts\\ivy-5.1.0.8.0.xml")
# for items in tree.getroot().getchildren():
# 	for item in items.getchildren():
# 		# print(item.tag,item.attrib,item.text)
# 		if item.attrib.get("name")=="mne.Extension": print(item.attrib.get("rev") )
# 		elif item.attrib.get("name")=="mne.Installer": print(item.attrib.get("rev") )

# CMD /C    Run Command and then terminate
# CMD /K    Run Command and then return to the CMD prompt.

# LBYL - Look Before You Leave - check to see if the object has certain attribute and if that's callable and then call it (mostly by if/else)
# Example - When printing form a dict check if the key is present of not and then print ranther than using the try catch directly
# The abvove is also simillar to another concept "Easier to Ask Forgiveness than Permission" (EAFP) 
# where you directly call the function and try to see if it works if not then throw an exception 
# rather than checking the access of checking if that should be callable which is the non-pythonic way of doing it.
#Duck Typing- To see if an object can perform a certain task without worrying about the object type 

# class Person:
# 	def fly(self):
# 		print("I can fly")
# 	def jump(self):
# 		print("I can jump")
# class Animal:
# 	def fly(self):
# 		print("fly")
# 	def jump(slef):
# 		print("jump")

# def fly_and_jump(cls_object):
	#non duck-typed
	# if isinstance(cls_object,Person):
	# 	cls_object.fly()
	# 	cls_object.jump()
	# else:
	# 	print("not an object")

	#LBYL
	# if hasattr(cls_object,'fly'):
	# 	if callable(cls_object.fly):
	# 		cls_object.fly()
	# if hasattr(cls_object,'jump'):
	# 	if callable(cls_object.jump):
	# 		cls_object.jump()

	#duck typed #EAFP #pythonic
	# try:
	# 	cls_object.fly()
	# 	cls_object.jump()
	# 	cls_object.bark()
	# except Exception as e:
	# 	print(e)

# p=Person()
# a=Animal()
# fly_and_jump(p)
# fly_and_jump(a)


# class TheHobbit:
# 	def __len__(self):
# 		return 34

# the_hobbit = TheHobbit()
# print(len(the_hobbit))
# my_str = "Hello World"
# print(len(my_str))

# print(type(TheHobbit()))
# <class '__main__.TheHobbit'>
# print(type(TheHobbit))
#<class 'type'>-- Type is the meta class, all of it's instances are classes
# You can also call type() with three arguments—type(<name>, <bases>, <dct>):

# <name> specifies the class name. This becomes the __name__ attribute of the class.
# <bases> specifies a tuple of the base classes from which the class inherits. This becomes the __bases__ attribute of the class.
# <dct> specifies a namespace dictionary containing definitions for the class body. This becomes the __dict__ attribute of the class.
#Dynamic class creation can be done using type cmetaclass

# class Foo:
# 	pass
# def new(cls):
# 	x=object.__new__(cls)
# 	x.attr=100
# 	return x
# Foo.__new__=new
# f=Foo()
# print(f.attr)
# print(f)

#creating a metaclass
# class Meta(type):
	# def __new__(cls,name,bases,dct):
	# 	x= super().__new__(cls,name,bases,dct)
	# 	x.attr=100
	# 	return x

	# def __init__(cls,name,bases,dct):
	# 	cls.attr=100

# class Foo(metaclass=Meta):
# 	pass
# f=Foo()
# print(f.attr)
# class Goo(metaclass=Meta):
# 	pass
# g=Goo()
# print(g.attr)
#MetaClass=ClassFactory



# informal interfaces 
# class InformalParserInterface:
#     def load_data_source(self, path: str, file_name: str) -> str:
#         """Load in the file for extracting text."""
#         pass
#     def extract_text(self, full_file_name: str) -> dict:
#         """Extract text from the currently loaded file."""
#         pass
# class PdfParser(InformalParserInterface):
#     """Extract text from a PDF"""
#     def load_data_source(self, path: str, file_name: str) -> str:
#         """Overrides InformalParserInterface.load_data_source()"""
#         pass

#     def extract_text(self, full_file_path: str) -> dict:
#         """Overrides InformalParserInterface.extract_text()"""
#         pass
# class EmlParser(InformalParserInterface):
#     """Extract text from an email"""
#     def load_data_source(self, path: str, file_name: str) -> str:
#         """Overrides InformalParserInterface.load_data_source()"""
#         pass

#     def extract_text_from_email(self, full_file_path: str) -> dict:
#         """A method defined only in EmlParser.
#         Does not override InformalParserInterface.extract_text()
#         """
#         pass
# print(issubclass(PdfParser,InformalParserInterface))
# print(issubclass(EmlParser,InformalParserInterface))
# print(PdfParser.__mro__)
# print(EmlParser.__mro__)

# concrete class is a subclass of the interface that provides an implementation of the interface’s methods

# Meta class interface creation
# class ParserMeta(type):
# 	def __instancecheck__(cls,instance):
# 		print(instance)
# 		return cls.__subclasscheck__(type(instance))
# 	def __subclasscheck__(cls,subclass):
# 		print(subclass)
# 		return (hasattr(subclass,'load_data_source') and 
#                 callable(subclass.load_data_source) and 
#                 hasattr(subclass, 'extract_text') and 
#                 callable(subclass.extract_text))


# f=ParserMeta('Foo',(),{})
# # print(type(f))
# # print(type(f()))
# print(f.__instancecheck__(f()))  #checking if f() which is Foo class is an instance of ParserMeta Class

# class UpdatedInformalParserInterface(metaclass=ParserMeta):
#     """This interface is used for concrete classes to inherit from.
#     There is no need to define the ParserMeta methods as any class
#     as they are implicitly made available via .__subclasscheck__().
#     """
#     pass

# class PdfParserNew:
#     """Extract text from a PDF."""
#     def load_data_source(self, path: str, file_name: str) -> str:
#         """Overrides UpdatedInformalParserInterface.load_data_source()"""
#         pass

#     def extract_text(self, full_file_path: str) -> dict:
#         """Overrides UpdatedInformalParserInterface.extract_text()"""
#         pass

# class EmlParserNew:
#     """Extract text from an email."""
#     def load_data_source(self, path: str, file_name: str) -> str:
#         """Overrides UpdatedInformalParserInterface.load_data_source()"""
#         pass

#     def extract_text_from_email(self, full_file_path: str) -> dict:
#         """A method defined only in EmlParser.
#         Does not override UpdatedInformalParserInterface.extract_text()
#         """
#         pass

# print(issubclass(PdfParserNew, UpdatedInformalParserInterface))
# print(issubclass(EmlParserNew, UpdatedInformalParserInterface))


# Formal Interface
# Using abc.ABCMeta
# To enforce the subclass instantiation of abstract methods, you’ll utilize Python’s builtin ABCMeta from the abc module.
#  Going back to your UpdatedInformalParserInterface interface, you created your own metaclass, ParserMeta, 
#  with the overridden dunder methods .__instancecheck__() and .__subclasscheck__().

# Rather than create your own metaclass, you’ll use abc.ABCMeta as the metaclass. 
# Then, you’ll overwrite .__subclasshook__() in place of .__instancecheck__() and .__subclasscheck__(), 
# as it creates a more reliable implementation of these dunder methods.
# import abc
# class FormalParserInterface(metaclass=abc.ABCMeta):
#     @classmethod
#     def __subclasshook__(cls, subclass):
#         return (hasattr(subclass, 'load_data_source') and 
#                 callable(subclass.load_data_source) and 
#                 hasattr(subclass, 'extract_text') and 
#                 callable(subclass.extract_text) or 
#                 NotImplemented)

#     @abc.abstractmethod
#     def load_data_source(self, path: str, file_name: str):
#         """Load in the data set"""
#         raise NotImplementedError

#     @abc.abstractmethod
#     def extract_text(self, full_file_path: str):
#         """Extract text from the data set"""
#         raise NotImplementedError

# class PdfParserNew(FormalParserInterface):
#     """Extract text from a PDF."""
#     def load_data_source(self, path: str, file_name: str) -> str:
#         """Overrides FormalParserInterface.load_data_source()"""
#         pass

#     def extract_text(self, full_file_path: str) -> dict:
#         """Overrides FormalParserInterface.extract_text()"""
#         pass

# class EmlParserNew(FormalParserInterface):
#     """Extract text from an email."""
#     def load_data_source(self, path: str, file_name: str) -> str:
#         """Overrides FormalParserInterface.load_data_source()"""
#         pass

#     def extract_text_from_email(self, full_file_path: str) -> dict:
#         """A method defined only in EmlParser.
#         Does not override FormalParserInterface.extract_text()
#         """
#         pass
# pdf_parser = PdfParserNew()
# eml_parser = EmlParserNew() 
# will raise error during instance creation as the subclass is not overriding all the methods, 
# extra methods in the subclass is fine though



# import requests
# proxies = {"http":"http://webgateway.itm.mcafee.com:9090",
#            "https":"http://webgateway.itm.mcafee.com:9090", }
# user_name = 'svcacct-mis'
# password = 'XyLm86sb]L$Xdk-U'
# url = 'https://artifactory-lvs.corpzone.internalzone.com/artifactory/list/bri-approved-local/mcafee/dataprot/mne.Package/5.0.0.56.0/MNE-5.0.0.pkg-56.zip'
# target_path='google.zip'
# response = requests.get(url, stream=True,proxies=proxies,auth=(user_name,password))
# with open(target_path, "wb") as f:
# 	for chunk in response.iter_content(chunk_size=8192):
# 		if chunk: # filter out keep-alive new chunks 
# 			f.write(chunk)

# import os
# import logging
# print(os.getcwd())
# logfileName='C:\\Users\\spradhan\\Documents\\Python-Scripts\\log_test.log'
# logging.basicConfig(level=logging.INFO,filename='C:\\Users\\spradhan\\Documents\\Python-Scripts\\log_test.log', filemode='w', format='%(filename)s - %(levelname)s - %(message)s')
# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')

# import traceback
# def func(a,b,c):
# 	print(a,b,c)
# 	print(traceback.extract_stack())
# def func1():
# 	func(1,2,3)
# print(23)
# func1()

# import os
# from configobj import ConfigObj
# CONFIG_FILE='pod.cfg'
# pod_config = ConfigObj(CONFIG_FILE)
# pod_config['header']={}
# pod_config['header']['name']='sapan'
# pod_config['header']['name1']='sapan'
# pod_config['header']['name2']='sapan'
# pod_config['header']['name3']='sapan'
# pod_config.write()
# print(pod_config)


# class A():
# 	def __init__(self,name):
# 		self.name=name
# 	def __str__(self):
# 		return f"dadafaf {self.name}"

# a=A('dada')
# print(a)



#######################  Take snapshot for OCR ###########
# import win32con
# import win32gui
# import win32process
# from desktopmagic.screengrab_win32 import getRectAsImage
# def _find_window_handle(pid):
#     def callback(hwnd, hwnds):
#         if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
#             _, found_pid = win32process.GetWindowThreadProcessId(hwnd)
#             if found_pid == pid:
#                 hwnds.append(hwnd)

#         return True

#     found_hwnd = None
#     hwnds = []
#     win32gui.EnumWindows(callback, hwnds)

#     if hwnds:
#         found_hwnd = hwnds[0]
#     return found_hwnd
# hwnd=_find_window_handle(233476)
# print(hwnd)
# rect256=getRectAsImage(win32gui.GetWindowRect(hwnd))
# rect256.save('xyz.png',format='png')
########################################################################################

# from difflib import get_close_matches
# print(get_close_matches('appel', ['ape', 'apple', 'peach', 'puppy'],n=1,cutoff=0.5) )

# import pytesseract
# from PIL import Image
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
# print(pytesseract.image_to_string(Image.open('53PW10RS5X64-20200416-121317.png')))
########################################################################################

# def set_controller_screen_resolution(width='1280', height='720'):
#     """The default controller resolution might be small (e.g. 1264x496) and
#     to avoid change in test behaviour due to screen resolution issues we can set user defined size.
#     :param width: Width of the controller display
#     :param height: Height of the controller display
#     """
#     try:
#         import win32api
#         import win32con
#         import pywintypes
#         disp_change_successful = 0
#         disp_change_restart = 1
#         disp_change_failed = -1
#         disp_change_badmode = -2

#         controller_width = win32api.GetSystemMetrics(0)
#         controller_height = win32api.GetSystemMetrics(1)
#         print("Controller resolution before changes: {}x{}".format(controller_width, controller_height))

#         if int(controller_width) != int(width) or int(controller_height) != int(height):
#             devmode = pywintypes.DEVMODEType()
#             devmode.PelsWidth = int(width)
#             devmode.PelsHeight = int(height)
#             devmode.Fields = win32con.DM_PELSWIDTH | win32con.DM_PELSHEIGHT
#             result = win32api.ChangeDisplaySettings(devmode, 0)
#             if result == disp_change_successful:
#                 print("The settings change was successful.")
#             elif result == disp_change_restart:
#                 print("Controller requires restart after applied resolution changes.")
#             elif result == disp_change_failed:
#                 print("Error: ChangeDisplaySettings - graphics mode is not supported.")
#             elif result == disp_change_badmode:
#                 print("Error: The display driver failed the specified graphics mode.")
#             else:
#                 print("Unknown return code received: {}".format(result))
#         else:
#             print("Skipping controller resolution change.")

#         new_controller_width = win32api.GetSystemMetrics(0)
#         new_controller_height = win32api.GetSystemMetrics(1)
#         print("Resolution has been set to {}x{}".format(new_controller_width, new_controller_height))
#     except Exception as e:
#         print(e)

# set_controller_screen_resolution()
#################################################################################################

## Lambda always accepts key as param and sorted always returns a list, by default keys
# >>> d={(1,2,3):(4,5,6),(5,8,9):(3,68,8)}
# >>> d
# {(1, 2, 3): (4, 5, 6), (5, 8, 9): (3, 68, 8)}
# >>> sorted(d)
# [(1, 2, 3), (5, 8, 9)]
# >>> sorted(d,key=lambda x : x[1])
# [(1, 2, 3), (5, 8, 9)]
# >>> d={(9,2,3):(4,5,6),(5,8,9):(3,68,8)}
# >>> sorted(d,key=lambda x : x[1])
# [(9, 2, 3), (5, 8, 9)]
# >>> sorted(d,key=lambda x : x[0])
# [(5, 8, 9), (9, 2, 3)]
# >>> sorted(d,key=lambda x : d[x][2])
# [(9, 2, 3), (5, 8, 9)]

###################################################################################################

# import os
# import zipfile
# try:
# 	dest="C:\\Users\\spradhan\\Documents\\Python-Scripts\\google.zip"
# 	# dest="C:\\Users\\spradhan\\Documents\\Python-Scripts\\dict.py"
# 	# dest="C:\\Users\\spradhan\\Documents\\Python-Scripts\\ivy-5.1.0.8.0.xml"
# 	if os.path.splitext(dest)[1]==".zip":
# 		zipfile.ZipFile(dest)
# except zipfile.BadZipFile:
# 	print("Downloading artifact again using chunk method")
# except:
# 	print("Exception in download_artifact")
# else:
# 	print ("Download completed")
# 	result = True

###################################################################################################
# from distutils.spawn import find_executable
# import subprocess
# def launch_vmrc():
#     # disable_vmrc_hints()
#     result = False
#     executable = find_executable("vmrc", "C:\\Program Files (x86)\\VMware\\VMware Remote Console")

#     vmrc_token = "vmrc://clone:cst-VCT-52e50a99-5780-838d-0d5b-6dc3c8ca65cf--tp-B5-72-8A-A8-99-42-9F-38-5E-6E-82-EF-45-E1-13-14-02-6D-9A-8D@cda-vc01.beaeng.mfeeng.org:443/?moid=vm-2142761"

#     if executable and vmrc_token:
#         run_command = executable + ' ' + vmrc_token
#         process = subprocess.Popen(run_command, stdout=subprocess.PIPE,
#                                         stdin=subprocess.PIPE, universal_newlines=True)
#         result = True
#     return result

# print(launch_vmrc())


############################################################################

# @step(u'opening vmrc for more than 20 times')
# def step_impl(context):
#     for i in range(12):
#         for pa in context.scenario.preboot_actions_list:
#             pb_steps = PrebootSteps()
#             pb_steps.vmrc_test()
#             pa.set_preboot_steps(pb_steps)
#             pa.execute_preboot_steps()

# def vmrc_test(self,timeout=180):
#     ocr_params = OCR_Params(timeout=timeout,
#                             text_to_find='Drive Encryption',
#                             crop={'left': 20, 'width': 60, 'top': 25, 'height': 40},
#                             greyscale=True,
#                             sharpen=True)
#     self.interaction_steps["default"].append(ocr_params)
#     entry_list = ['<5>']
#     self.interaction_steps["default"].append(entry_list)

# Feature: VMRC Test
# @VMRC @PREBOOT
#   Scenario: Opening more than 20 VMRC tokens
#     Given an 'active' and 'decrypted' managed MDE client
#     When the client is restarted
#     Then opening vmrc for more than 20 times


##################################################################################

# import mysql.connector
# from mysql.connector import Error
# try:
#     connection = mysql.connector.connect(host='mysql.brieng.nai.org',
#                                          database='CDAPodStack',
#                                          user='cda_podstack_usr',
#                                          password='Hu6kah3ta7ailookein3phe0iZughech')
#     if connection.is_connected():
#         db_Info = connection.get_server_info()
#         print("Connected to MySQL Server version ", db_Info)
#         cursor = connection.cursor()
#         cursor.execute("select database();")
#         record = cursor.fetchone()
#         print("You're connected to database: ", record)
# except Error as e:
#     print("Error while connecting to MySQL", e)
# finally:
#     if (connection.is_connected()):
#         cursor.close()
#         connection.close()
#         print("MySQL connection is closed")


##########################################################################

############## 	Windows app interaction

# from pywinauto import application
# app = application.Application()
# app.connect(title_re = ".*Notepad.*")
# app_dialog = app.top_window()
# app_dialog.minimize()
# app_dialog.restore()
# app_dialog.maximize()
# app_dialog.close()


# import warnings
# import random
# import time
# from pywinauto import application
# from pywinauto.findwindows import WindowAmbiguousError, WindowNotFoundError
# #APPS_POOL = ['Chrome', 'GVIM', 'Notepad', 'Calculator', 'SourceTree', 'Outlook']
# APPS_POOL = ['670W19096407']
# # Select random app from the pull of apps
# def show_rand_app():
#     # Init App object
#     app = application.Application()
#     random_app = random.choice(APPS_POOL)
#     try:
#         print('Select "%s"' % random_app)
#         app.connect(title_re=".*%s.*" % random_app)
#         # Access app's window object
#         app_dialog = app.top_window()
#         app_dialog.restore()
#         time.sleep(1)
#         app_dialog.set_focus()
#         time.sleep(1)
#         app_dialog.minimize()
#         time.sleep(1)
#     except(WindowNotFoundError):
#         print('"%s" not found' % random_app)
#         pass
#     except(WindowAmbiguousError):
#         print('There are too many "%s" windows found' % random_app)
#         pass
# for i in range(2):
#     with warnings.catch_warnings():
#         warnings.simplefilter("ignore")
#         show_rand_app()
#     time.sleep(1)



# TEXT = '["kiarix moreno","116224357500406255237","z120gbkosz2oc3ckv23bc10hhwrudlcjy04",1409770337,"com.youtube.www/watch?v\u003dp1JPKLa-Ofc:https","es"]'
# import json, ast, re
# r = re.search(r'\["(?P<name>[^"]*)","(?P<number1>[^"]*)","(?P<data>[^"]*)",(?P<number2>\d*),"(?P<website>[^"]*)","(?P<language>[^"]*)"\]', TEXT).groupdict()
# print(r)

# s = '\nvlan 101\nname One \n\n interface vlan101\n description Routing VLAN\n ip address 100.100.101.0 255.255.255.0'
# import re
# pattern = re.compile(r'\nvlan (?P<vlan>\d+)\nname (?P<name>[a-zA-Z]+)[\s\S]* address (?P<ip_address>[\.\d ]+)')
# print(pattern.search(s).groupdict())

# print(r)
# text = """73.92.19.149 - - [13/Mar/2021:20:44:37 +0000] "GET /images/icons/common/Icon_Protect.svg HTTP/1.1" 200 6090 "https://prosimodemo.admin.prosimo.io/dashboard/main" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36"
# 73.92.19.149 - - [13/Mar/2021:20:44:37 +0000] "GET /images/icons/common/Icon_MainDashboard_User.svg HTTP/1.1" 200 737 "https://prosimodemo.admin.prosimo.io/dashboard/main" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36"
# 73.92.19.149 - - [13/Mar/2021:20:44:37 +0000] "GET /images/icons/common/Icon_countries.svg HTTP/1.1" 200 727 "https://prosimodemo.admin.prosimo.io/dashboard/main" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36"""

# import re
# r = re.split(r'\s+', text)
# # print(r)

# with open("f1.txt","r") as f:
    # for line in f:
    #     print(line)

    # while len(f.readline())>0:
    #     print(f.readline())
    #     f.seek(f.tell()+1)

# text = """73.92.19.149 - - [13/Mar/2021:20:44:37 +0000] "GET /images/icons/common/Icon_Protect.svg HTTP/1.1" 200 6090 "https://prosimodemo.admin.prosimo.io/dashboard/main" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36"""
# pattern = re.compile(r'(?P<user>[\d.]*)[\s\S]*(?P<type>(GET|POST)) (?P<path>[\s\S]*) [\s\S]*" (?P<status_code>\d*) \d* "(?P<url>[\s\S]*)"[\s\S]* (?P<last_col>\w*\/\d*\.\d*)')
# print(pattern.search(text).groupdict())

# class A:
# 	def __init__(self,name,age):
# 		self.name = name 
# 		self.age = age 
# 	def f1(self):
# 		return 5
# 	def __str__(self):
# 		return "new_name"
# 	def __eq__(self, other):
# 		if isinstance(other,A):
# 			return self.age == other.age
# 		else:
# 			return False
# a=A('sapan',89)
# b=A('madhu',89)
# print(a == b)

# get all the objects
# import gc 
# print(gc.get_objects())

# s = (1,2,[1,2])
# print(id(s[0]), id(s[1]), id(s[2]))
# for i in range(100000):
# 	s[2].append(i)
# print(id(s[0]), id(s[1]), id(s[2]))

# l = [1,2]
# print(id(l))
# l.append(1)
# print(id(l))
# l+=[5]
# print(id(l))
# l=l+[9]
# print(id(l))

#mutable default arguments
# def f1(i,s=[]):
# 	s.append(i)
# 	return s
# print(f1(3))
# print(f1(8))


# l1=[1,2]
# l2=[3,4]
# l3=[1,2]
# l4=[3,4]
# x = zip(l1,l2,l3,l4)
# for i in x:
# 	print(i)

""" __new__ method"""
# class B:
# 	x = 90
# 	def __init__(self,*args, **kwargs):
# 		print(self)
#
# class A:
# 	def __new__(cls, *args, **kwargs):
# 		print(cls, args, kwargs)
# 		# ins = object.__new__(B)
# 		ins = super().__new__(cls)
# 		print(ins)
# 		return ins
#
# 	def __init__(self,*args, **kwargs):
# 		print("inside A init")
#
# a = A(45,45, sapan =  90)

