"""
Represents a musical artist or podcast creator.

This is the simplest class in the hierarchy — no dependencies, no validation.
It introduces two core Python OOP conventions:
  1. The single leading-underscore (_name) signals a non-public attribute.
  2. @property exposes a clean public getter without allowing direct mutation.
"""

#create the artist class
class Artist:
    #constructor
    def __init__ (self, name: str, genre: str):
        self._name = name
        self._genre = genre
    #properties
    @property
    def name(self) -> str:
        return self._name
    @property 
    def genre(self) -> str:
        return self._genre
    #string respresentatiion of the class
    def __str__(self) -> str:
        return f"{self._name} ({self._genre}))"
    
        
  