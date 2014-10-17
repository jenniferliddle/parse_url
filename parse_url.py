#!/usr/bin/env python

#
# parse_url.py
#
# Parse a URL into its component parts according to RFC 3986
#
# Author: Jennifer Liddle <jennifer@jsquared.co.uk>
#
# Date: 17th October 2014
#
# Licence: Apache 2.0 License <http://www.apache.org/licenses/LICENSE-2.0>
#
import sys
from Tkinter import *
from urlparse import urlparse
from urlparse import urlunparse
import getopt

# small class to hold results of parsing
class result:
    pass

#
# Display usage message and exit
#
def displayUsage():
    print sys.argv[0], ": Parse a URL into its constituent parts"
    print 
    print sys.argv[0], "[-c][-h] [url]"
    print "Where:  -c  means work as a command line program"
    print "        -h  display this help message and exit"
    print "       url  is the url to parse"
    sys.exit(2)

#
# Display results as text
#
def printURL(url):
    userinfo = url.username if url.username else ''
    userinfo += ':' if url.password != '' else ''
    userinfo += url.password if url.password else ''
  
    print 'Scheme Name      :  ', url.scheme
    print 'Hierarchical Part:  ', url.netloc + url.path
    print '    Authority    :      ', url.netloc
    print '        Userinfo :         ', userinfo
    print '        Host     :         ', url.hostname
    print '        Port     :         ', url.port
    print '    Path         :      ', url.path
    print 'Query            :      ', url.query
    print 'Fragment         :      ', url.fragment

# callback to enable <Return> to work the same way as pressing the "Parse" button
def callback_return(event):
    callback()

#
# Fill in the values on the GUI
#
def callback():
    url = urlparse(result.url.get())

    userinfo = url.username if url.username else ''
    if (url.password):
        userinfo += ':' + url.password

    result.scheme.set(url.scheme)
    result.hierarchy.set(url.netloc + url.path)
    result.authority.set(url.netloc)
    result.userinfo.set(userinfo)
    result.host.set(url.hostname)
    result.path.set(url.path)
    result.query.set(url.query)
    result.fragment.set(url.fragment)

    # this will raise an exception if the port is not numeric
    try:
        result.port.set(url.port)
    except:
        result.port.set('')

#
# Display results as GUI
#
def displayURL(url):
    top = Tk()
    top.title("Parse URL according to RFC 3986")
    top.geometry("850x400+100+100")

    result.url = StringVar()
    result.scheme = StringVar()
    result.hierarchy = StringVar()
    result.authority = StringVar()
    result.userinfo = StringVar()
    result.host = StringVar()
    result.port = StringVar()
    result.path = StringVar()
    result.query = StringVar()
    result.fragment = StringVar()

    r = 1

    Label(top, text="Enter URL to parse").grid(row=r,column=1);
    ent = Entry(top,textvariable=result.url,width=80)
    ent.grid(row=r,column=2)
    ent.focus()
    Button(command=callback,text='Parse').grid(row=r,column=3)
    r = r+1

    Label(top,text="Scheme").grid(sticky='w',padx=10,pady=5,row=r,column=1)
    Entry(top,state='readonly',textvariable=result.scheme,width=50).grid(sticky='w',row=r,column=2,columnspan=2)
    r = r+1

    Label(top,text='Hierarchy').grid(sticky='w',padx=10,pady=5,row=r,column=1)
    Entry(top,state='readonly',textvariable=result.hierarchy,width=50).grid(sticky='w',row=r,column=2,columnspan=2)
    r = r+1

    Label(top,text='Authority').grid(stick='w',padx=20,pady=5,row=r,column=1)
    Entry(top,state='readonly',textvariable=result.authority,width=50).grid(sticky='w',padx=20,row=r,column=2,columnspan=2)
    r = r+1

    Label(top,text='Userinfo').grid(stick='w',padx=40,pady=5,row=r,column=1)
    Entry(top,state='readonly',textvariable=result.userinfo,width=50).grid(sticky='w',padx=40,row=r,column=2,columnspan=2)
    r = r+1

    Label(top,text='Host').grid(stick='w',padx=40,pady=5,row=r,column=1)
    Entry(top,state='readonly',textvariable=result.host,width=50).grid(sticky='w',padx=40,row=r,column=2,columnspan=2)
    r = r+1

    Label(top,text='Port').grid(stick='w',padx=40,pady=5,row=r,column=1)
    Entry(top,state='readonly',textvariable=result.port,width=50).grid(sticky='w',padx=40,row=r,column=2,columnspan=2)
    r = r+1

    Label(top,text='Path').grid(sticky='w',padx=20,pady=5,row=r,column=1)
    Entry(top,state='readonly',textvariable=result.path,width=50).grid(sticky='w',padx=20,row=r,column=2,columnspan=2)
    r = r+1

    Label(top,text='Query').grid(stick='w',padx=10,pady=5,row=r,column=1)
    Entry(top,state='readonly',textvariable=result.query,width=50).grid(stick='w',row=r,column=2,columnspan=2)
    r = r+1

    Label(top,text='Fragment').grid(sticky='w',padx=10,pady=5,row=r,column=1)
    Entry(top,state='readonly',textvariable=result.fragment,width=50).grid(sticky='w',row=r,column=2,columnspan=2)
    r = r+1

    top.bind("<Return>", callback_return)

    # if a URL was given on the command line, then display it
    if (url):
        result.url.set(urlunparse(url))
        callback()

    top.mainloop()

#
# Parse the command line options
#
command = False
try:
    opts, args = getopt.getopt(sys.argv[1:],"h?c",['help'])
except getopt.GetoptError:
    print 'Unrecognised paramater'
    displayUsage()

for opt, arg in opts:
    if opt in ('-h', '-?', '--help'):
        displayUsage()
    elif opt in ("-c", "--command"):
        command = True

url = ''
if (len(args) > 0):
    url = args[0]

parsed_url = urlparse(url)

if (command):
    printURL(parsed_url)
else:
    displayURL(parsed_url)


