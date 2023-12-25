from bs4 import BeautifulSoup 
import requests
import ipdb
from Course import Course
import json

class Scraper:
    def __init__(self):
        self.courses = []

    def get_page(self):
        doc =  BeautifulSoup(requests.get("http://learn-co-curriculum.github.io/site-for-scraping/courses").text, 'html.parser')

        for course in doc.select('.post'):
            print(type(course))

            title = course.select("h2")[0].text if course.select("h2") else ''
            date = course.select(".date")[0].text if course.select(".date") else ''
            description = course.select("p")[0].text  if course.select("p") else ''

            new_course = Course(title, date, description)
            self.courses.append(new_course)
        ipdb.set_trace()

scraper = Scraper()  # Creates an instance of the Scraper class
scraper.get_page()  # Call the get_page method on the instance


    
