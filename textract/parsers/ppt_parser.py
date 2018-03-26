from .utils import ShellParser
import re

def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext
        
        
class Parser(ShellParser):
    """Extract text from ppt files using ppthtml.
    """
     
    def extract(self, filename, **kwargs):
        stdout, stderr = self.run(['ppthtml', filename])
        return cleanhtml(stdout)