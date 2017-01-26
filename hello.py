#!/usr/bin/env python

# ^ this thing is called the "shebang"

import os
import json
import cgi
import Cookie

form = cgi.FieldStorage()
username = form.getvalue('user')
password = form.getvalue('password')

C = Cookie.SimpleCookie()
C.load(os.environ["HTTP_COOKIE"])


print "Content-Type: text/html"


if username == "bob" and password == "hunter2":
	print "Set-Cookie: loggedin=true"

print	# end of the header
print "<HTML><BODY>"
print "<H1>Hello World!</H1>"
print "Your magic tracking number is:"
print form.getvalue("magic_tracking_number")

print "<P>Your Browser is"
if "Firefox" in os.environ["HTTP_USER_AGENT"]:
	print "Firebox"
elif "Chrome" in os.environ["HTTP_USER_AGENT"]:
	print "Chrome"
else:
	print os.environ["HTTP_USER_AGENT"]

print "<FORM method='POST'><INPUT name='user'><INPUT name='password' type='password'>"
print "<INPUT type='submit'></FORM>" 


print "<P>Username: " + str(username)
print "<P>Password: " + str(password)

if username == "bob" and password == "hunter2":
	print "<P>Login successful!"

if "loggedin" in C:
	print "<P>Logged in:" + str(C["loggedin"].value)
else:
	print "<P>No cookie"

#print "Hello world~*~"

#print json.dumps(dict(os.environ), indent=2, sort_keys=True)
