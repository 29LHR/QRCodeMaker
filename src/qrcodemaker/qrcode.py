import qrcode as qr
import pillow as PIL

class NotALinkError(Exception):
    def __init__(self):
        super().__init__('The link provided does not meet our requirements')

class qrcode:
    def __init__(self, link : str):
        if self.__isLink(link):
            self.__link = link
        else:
            return NotALinkError()
    
    
    def __isLink(self, link : str)-> bool:
        if not ("http" in link or "https" in link):
            return False
        
        if not "." in link:
            return False
        
        return True