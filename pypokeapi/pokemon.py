import req 

class Pokemon:

    def __init__(self, pokemon):
        self.pokemon = str(pokemon).lower()


    # Retrives information on an ability.
    def fetch_ability(self, _ability):
        return req.send_request('https://pokeapi.co/api/v2/ability/%s' % _ability)
    
    
    # Retrieves relevant locations for a pokemon.
    def fetch_location(self):
        return req.send_request('https://pokeapi.co/api/v2/pokemon/%s/encounters' % self.pokemon)
    
    
    # Retrieves pokemon of a colour.
    def fetch_colour(self, _colour):
        return req.send_request('https://pokeapi.co/api/v2/pokemon-color/%s' % _colour)
    
    
    # Retrieves forms of a pokemon.
    def fetch_forms(self):
        return req.send_request('https://pokeapi.co/api/v2/pokemon-form/%s' % self.pokemon)
    
    
    # Retrieves habitats that pokemon can be located in.
    def fetch_habitats(self, _habitat):
        return req.send_request('https://pokeapi.co/api/v2/pokemon-habitat/%s' % _habitat)
    
   
   # Retrieves species of a pokemon.
    def fetch_species(self):
        return req.send_request('https://pokeapi.co/api/v2/pokemon-species/%s' % self.pokemon)
    
    
    # Retrieves statistics of a given move.
    def fetch_stats(self, _move):
        return req.send_request('https://pokeapi.co/api/v2/stat/%s' % _move)
    
    
    # Retrieves type strength and weaknesses.
    def fetch_types(self, _type):
        return req.send_request('https://pokeapi.co/api/v2/stat/%s' % _type)
    

    # Retrieves pokemon of a given gender.
    def fetch_genders(self, _gender):
        return req.send_request('https://pokeapi.co/api/v2/gender/%s' % _gender)