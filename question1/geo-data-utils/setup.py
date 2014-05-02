from distutils.core import setup

setup(
    name = "geotools",
    version = "0.1-alpha",
    author = "Jason Goodell",
    author_email = "jasongoodell@mac.com",
    description = ("A small package that holds some utils for getting some geo data."),
    packages=['geotools'],
    scripts=['get-state-data'],
    )
