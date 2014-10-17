parse_url.py

A demonstration program.

The instructions were:

"Using a language of your choice, write a small GUI program that takes a URL, 
breaks it down into its individual components as defined in RFC 3986 and 
displays those components to the user."

There was no mention of which OS(s) it should run on, which I assume was deliberate.

For reasons of simplicity, quickness, and portability, I decided to use Python with 
the Tkinter module.

The resulting script should work on any machine with python installed. It uses 
only python modules which are included as part of the standard python distribution.

It has been tested on Debian and Ubuntu Linux, and OSX

Usage
-----

./parse_url.py [-c] [-h] [url]

If run with no arguments, it will display a window allowing the user to enter a
URL to be parsed. If a url is given on the command line, it will immediately 
parse the URL and display the results in the window.

If the -c option is given with a URL, it will behave as a command line program,
and will display the results to the console.

The -h option will display a short help message.


