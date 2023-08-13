# Using flask we are making this lab computer as server.
from flask import Flask
from flask import request # It will request to return something from the URL

app = Flask(__name__) # Creating object of the flask and '__name__' parameter is passed.



"""Inside a server multiple functions are running. So instead calling function name directly, we can expose this function name to
an URL and then we call it. This will make function name plateform independent. Because URL is language independent."""

"""To have access this hello_world() first we have to search out to the server. Then port number and then we have to give the 
above route after that only we will be able to access the function."""

@app.route("/") # Decorating 'hello_world()' using aap.route(). It is also called as binding function to a path
def hello_world():# Using URL anyone should be able to access this function
    return "Hello, World!"

@app.route("/hello1")#It will create a different route/URL for hello_world1()."/hello1" will be distingusing feature in the URL
def hello_world1():
# So the file URL:'https://black-secretary-ajyqi.pwskills.app:5000/hello1'
    return 'Hello World 1'

@app.route("/hello2")#It will create a different route/URL for hello_world1()."/hello2" will be distingusing feature in the URL
# So the file URL:'https://black-secretary-ajyqi.pwskills.app:5000/hello2'
def hello_world2():
    return 'Hello World 2'

#################################################################################################################################
"""Write afunction which will take data similar to google search and return some output"""
#################################################################################################################################
@app.route('/input_data')
def request_input():
    data = request.args.get('x') # The way to pass data to URL
    return "This is my input from URL{}".format(data)
# The final URL will be:'https://black-secretary-ajyqi.pwskills.app:5000/input_data?x=<the input we wish to enter>'

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
