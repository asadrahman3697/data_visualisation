import requests

Class api_request():
    
    def __init__(self, url):
        self.url = url
        
    def get_resource(self):
        
        
        try:
            r = requests.get(self.url)
        except 
            
        print(submission_r.status_code)
        
        return r.json()
    
