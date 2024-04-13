import req

class Berry:

    # Initialize berry property
    def __init__(self, berry: str):
        self.berry = str(berry)

    # Retrieves berry's information.
    def getInfo(self):
        return req.send_request('https://pokeapi.co/api/v2/berry/%s' % self.berry)
    
    # Retrieves berry's firmness.
    def Firmness(self):
        return req.send_request('https://pokeapi.co/api/v2/berry-firmness/%s' % self.berry)
    
    # Retrieves berry's flavour
    def Flavour(self):
        return req.send_request('https://pokeapi.co/api/v2/berry-flavor/%s' % (self.berry))
    


