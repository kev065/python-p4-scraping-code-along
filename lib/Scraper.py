from bs4 import BeautifulSoup 
import requests
from Course import Course
import json

class Scraper:
    def __init__(self):
        self.courses = []

    def get_page(self):
        doc =  BeautifulSoup(requests.get("http://learn-co-curriculum.github.io/site-for-scraping/courses").text, 'html.parser')

        for course in doc.select('.post'):
            title = course.select("h2")[0].text if course.select("h2") else ''
            date = course.select(".date")[0].text if course.select(".date") else ''
            description = course.select("p")[0].text  if course.select("p") else ''

            new_course = Course(title, date, description)
            self.courses.append(new_course)
        return doc  # Return the BeautifulSoup object

    def get_courses(self):
        return self.courses

    def make_courses(self, doc):
        for course in doc.select('.post'):
            title = course.select("h2")[0].text if course.select("h2") else ''
            date = course.select(".date")[0].text if course.select(".date") else ''
            description = course.select("p")[0].text  if course.select("p") else ''

            new_course = Course(title, date, description)
            self.courses.append(new_course)
        return self.courses
    
    def print_courses(self):
        for course in self.courses:
            print(course)

scraper = Scraper()  # Create an instance of the Scraper class
scraper.get_page()  # Call the get_page method on the instance
scraper.print_courses()  # Call the print_courses method on the instance
