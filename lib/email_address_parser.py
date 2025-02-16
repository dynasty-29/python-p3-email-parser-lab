# your code goes here!
import re
class EmailAddressParser:
    def __init__(self, text):
        self.text = text

    def parse(self):
        # Find all emails using the regex and remove duplicates using set()
        emails = set(re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", self.text))
        return sorted(emails)  # Sorted to match the test output order