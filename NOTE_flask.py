
#################################################################################################################################################
# 1. Using Flask we want to create an API and using that API we want to expose 'hello_world()' function to outer-world so that anyone with the  #
# URL will be able to access  'hello_world()' function from any where.                                                                          #
#                                                                                                                                               #
# 2. Using API we expose some some part of code or function in Server to the Client. Then Client can access that function and execute it to get #
# desired data. The good thing about API is that the framework, programming language etc. that Client is using needn't be same as of functions  #
# in Server.                                                                                                                                    #
#################################################################################################################################################

# Using flask we are making this lab computer as server.
from flask import Flask
from flask import request # It will request to return something from the URL

app = Flask(__name__) # Creating object of the flask and '__name__' parameter is passed.

"""
Inside a server multiple functions are running. So instead of calling function name directly, we can call it using URL. Because, if call function using function its name
then this function calling task become plateform, framework, programming language dependent. But calling the function using URL makes it plateform, framework, programming
language independent.
"""

"""
To have access this hello_world() first we have to search out to the server. Then port number and then we have to give the 
above route after that only we will be able to access the function.
"""

@app.route("/") # Decorating 'hello_world()' using aap.route(). It is also called as binding function to a path.
def hello_world():# Using URL anyone should be able to access this function
    # So the file URL:'https://black-secretary-ajyqi.pwskills.app:5000
    # Here: 'https://black-secretary-ajyqi.pwskills.app' is URL to the server
    # Here: '5000' is the port number of the server where this 'hello_world()' function is running.
    return "Hello, World!"

@app.route("/hello1")#It will create a different route/URL for hello_world1()."/hello1" will be distingusing feature in the URL
def hello_world1():
    # So the file URL:'https://black-secretary-ajyqi.pwskills.app:5000/hello1'
    # Here:'https://black-secretary-ajyqi.pwskills.app' is URL to the server.
    # Here : '5000' is the port number in the server where this 'hello_world()' function is running.
    # Here : '/hello1' is the route to the 'hello_world()' function.
    return 'Hello World 1'

@app.route("/hello2")#It will create a different route/URL for hello_world1()."/hello2" will be distingusing feature in the URL
def hello_world2():
    # So the file URL:'https://black-secretary-ajyqi.pwskills.app:5000/hello2'
    # Here : 'https://black-secretary-ajyqi.pwskills.app:' URL to the server.
    # Here : '5000' is the port number in the server where this 'hello_world()' function is running.
    # Here : '/hello2' is the route to the 'hello_world()' function.
    return 'Hello World 2'

#################################################################################################################################
# """Write a function which will take data similar to google search and return some output."""                                   #
#################################################################################################################################
@app.route('/input_data')
def request_input():
    data = request.args.get('x') # A way to give input data using URL
    return "This is my input from URL:{}".format(data)
    # The final URL will be:'https://black-secretary-ajyqi.pwskills.app:5000/input_data?x=<the input we wish to enter>'
    
    """
    After running the above function suppose our input is: Khanjan. So the resultant URL will be:
    'https://black-secretary-ajyqi.pwskills.app:5000/input_data?x=Khanjan'
    # Here : 'https://black-secretary-ajyqi.pwskills.app:' URL to the server.
    # Here : '5000' is the port number in the server where this 'hello_world()' function is running.
    # Here : '/input_data' is the route to the 'request_input()' function.
    # Here : '?x=Khanjan' is the way to pass the input. Here only 'Khanjan' is the input.

    Since in the server the 'request_input()' function is running so it will take 'Khanjan' as input and will return the following:
    'This is my input from URL:Khanjan'
    """

if __name__=="__main__":
    app.run(host="0.0.0.0")# This will make entire lab computer as server.

#################################################################################################################################
"""From the above we have copy the path 'https://black-secretary-ajyqi.pwskills.app' then put and colon (:) and enter 5000      #
then press enter. 5000 is the default port number for the flask. So the total URL will be:                                      #
'https://black-secretary-ajyqi.pwskills.app:5000'."""                                                                           #
                                                                                                                                #
"""This entire 'https://black-secretary-ajyqi.pwskills.app:5000' browsing unit is the client. So we are able to execute pythonic#
function hello_world() from the URL or browser itself."""                                                                       #
                                                                                                                                #
"""Using this URL/API 'https://black-secretary-ajyqi.pwskills.app:5000' I am able to expose the hello_world() to the outside    #
world."""                                                                                                                       #
                                                                                                                                #
"""Using HTTP protocol I have created a route and using that we have execute the hello_world() without calling it in pythonic   #
way. This makes things plateform independent because now it we want execute code from some other language, then also we don't   #
need to call functions of that language. Simply URL will do the job. This makes things plateform independent."""                #
#################################################################################################################################
