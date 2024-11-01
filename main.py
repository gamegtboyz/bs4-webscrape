from bs4 import BeautifulSoup

# open and read the content of specific files
# the first argument is the source files whicih we wants to open it. In case of to open the file from different directory, the path is required.
# the second argument is what method (read, write, or do both) which we want to apply when open the file.
# assign the alias onto the file, like we do with variable name.
with open('home.html', 'r') as html_file:
    content = html_file.read()
    print(content)