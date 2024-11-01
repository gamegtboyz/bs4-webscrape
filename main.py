from bs4 import BeautifulSoup

# open and read the content of specific files
# the first argument is the source files whicih we wants to open it. In case of to open the file from different directory, the path is required.
# the second argument is what method (read, write, or do both) which we want to apply when open the file.
# assign the alias onto the file, like we do with variable name.
with open('home.html', 'r') as html_file:
    content = html_file.read()
    ###print(content)      # the content should be printed out onto the terminal

    # create an instance of beautifulsoup, then specify the method
    soup = BeautifulSoup(content, 'lxml')
    ###print(soup.prettify())  # the shuld be printed out onto terminal

    # grab some specific informations. in this case, we want to grab all <h5> tags
    
    ###tags = soup.find('h5')  # this line only finds out first h5 element, then stops execution since we have 3 'h5' tags in the page.
    ###courses_html_tags = soup.find_all('h5')      # this will return all h5 tags in page 
    # iterate to display what we've got
    ###for course in courses_html_tags:
    ###    print(course.text)

    # build up some program to gather the course and price, respectively
    # gather all 'div' contents which contain class='card'. since python reserve 'class' keyword, we need to add underscore after 'class'
    course_cards = soup.find_all('div', class_='card')
    for course in course_cards: 

        # scope what we want in gathering. in this case is text in course name, and text in button which contains strings of price.
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]    # split the whole strings with whitespace, then gather the last element, where's the price located.

        # print out an output
        print(f'{course_name} costs {course_price}')