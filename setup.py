from distutils.core import setup

setup(
    name = "django-crawler",
    version = "0.1",
    packages = [
        "crawler",
        "crawler.management",
        "crawler.management.commands",
        "crawler.plugins",
    ],
    author = "Amal P Mathew",
    author_email = "amalpmathew90@gmail.com",
    description = "A web crawler using Python Django",
    url = "https://github.com/amalpmk/Django_Crawler/tree/master",
)
