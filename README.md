# pypokeapi 

Pypokeapi is a python wrapper that allows you to interact with the PokeAPI. The API is specifically focused
on the pokemon video games.

![pypokeapi logo](https://i.postimg.cc/T3vLzCrK/pypokeapilogo.png)

# Features

- Allows you to obtain information about a specific pokemon.
- Allows you to obtain information about a specific species.
- Allows you to obtain information about a specific ability.
- Allows you to obtain information about a specific type of pokemon.
- Allows you to get a list of pokemon.


# Installation


## PyPI
I *extremely* advise that this package is downloaded from pip using the following command below.

``` pip install pypokeapi ```

## Cloning

If you would like to simply *clone* this repository then simply use the following command below.

``` git clone https://github.com/m-attz/py-pokeapi.git ```



# Methods
Here are the methods you may use. All of these methods will print out a **JSON** object of the
information that you are requesting.

```
pokeapi.getPokemon("YOUR POKEMON")
pokeapi.getSpecies("YOUR POKEMON")
pokeapi.getType("NUMBER HERE")
pokeapi.getAbility("ABILITY HERE")
pokeapi.getListOfPokemon("COUNT HERE")
```



# Usage

```
from pypokeapi import pokeapi

pokeapi.getPokemon("pikachu")
```

# Links

-[PyPI pypokeapi](https://pypi.org/project/pypokeapi/)

-[PokeAPI](https://pokeapi.co/) 



# License

This project is licensed under [GNU General Public License v3.0 or later](https://spdx.org/licenses/GPL-3.0-or-later.html)

