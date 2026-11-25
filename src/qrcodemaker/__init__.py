import qrcode as qr
from flask import Flask, request, render_template, send_from_directory, url_for, redirect, flash
class NotALinkError(Exception):
    def __init__(self):
        super().__init__('The link provided does not meet our requirements')

class qrcode:
    def __init__(self, link : str):
        if self.__isLink(link):
            self.__link = link
        else:
            raise NotALinkError()
        
        self.__makeQR()
        
        
    def __isLink(self, link : str)-> bool:
        if not ("http" in link or "https" in link):
            return False
        
        if not "." in link:
            return False
        
        return True
    
    def __makeQR(self):
        self.__qr = qr.make(self.__link)
    
    @property
    def link(self):
        return self.__link
    
    @property
    def qr(self):
        return self.__qr
    
class app:
    def __init__(self):
        self.__app = Flask(__name__)
        self.__app.secret_key = 'THIS ONLY ENABLES FLASHES'
        
        self.__defRoutes()
        
        self.__app.run(port=5500, debug=True)
    
    def __defRoutes(self):
        @self.__app.route('/')
        def root():
            return render_template('index.html')
        
        @self.__app.route("/createQR", methods=["POST"])
        def createQR():
            try:
                link = request.form.get('link')
                code = qrcode(link)
                code.qr.save('src/qrcodemaker/static/qrcode.png')
                
                return send_from_directory('static', 'qrcode.png')
            
            except NotALinkError as e:
                print('FLASHING')
                flash(str(e), 'error')
                return redirect('/')
            
        
    
def main() -> None:
    main = app()
    
if __name__ == "__main__":
    main()