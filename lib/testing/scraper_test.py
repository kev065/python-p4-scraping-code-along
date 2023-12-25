from bs4 import BeautifulSoup, element
from Scraper import Scraper

class Test_Scraper:
    '''Scraper in Scraper.py'''

    def test_get_page(self):
        "uses Beautiful Soup to get the HTML from a web page"
        scraper = Scraper()
        doc = scraper.get_page()
        assert(isinstance(doc, BeautifulSoup))

    def test_get_courses(self):
        "Test get_courses"
        scraper = Scraper()
        doc = scraper.get_page()
        course_offerings = scraper.get_courses()
        assert(len(course_offerings) != 0)

    def test_make_courses(self):
        "Test self.courses"
        scraper = Scraper()
        doc = scraper.get_page()
        courses = scraper.make_courses(doc)
        assert(isinstance(courses, list))
        assert(len(courses) != 0)
