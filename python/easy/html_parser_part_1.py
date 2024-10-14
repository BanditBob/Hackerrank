"""
html_parser_part_1.py
"""

from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)

    def handle_startendtag(self, data):
        print("Encountered some data  :", data)


def main():
    parser = MyHTMLParser()


if __name__ == "__main__":
    main()
