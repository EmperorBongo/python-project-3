from pprint import pprint
import csv


# Melon class represents a type of melon with various attributes
class Melon:
    # Constructor method to initialize a Melon object
    def __init__(self, melon_id, common_name, price, image_url, color, seedless):
        self.melon_id = melon_id
        self.common_name = common_name
        self.price = price
        self.image_url = image_url
        self.color = color
        self.seedless = seedless
    
    def __repr__(self):
        """convenience method to show information about melon in console"""
        return f"<Melon: {self.melon_id}, {self.common_name}>"
    
    def price_str(self):
        """return price formatted as string $x.xx"""
        return f"{self.price:.2f}"

# Dictionary to store Melon objects with their IDs as keys
melon_dict = {}

# Open the CSV file containing melon data
with open("melons.csv") as csvfile:
   rows = csv.DictReader(csvfile)

   for row in rows:
      melon_id = row['melon_id']
      # Create a Melon object for each row in the CSV file
      melon = Melon(
         melon_id,
         row['common_name'],
         float(row['price']),
         row['image_url'],
         row['color'],
         # Convert the string 'seedless' to a boolean value
         eval(row['seedless']))
      # Store the Melon object in the dictionary using its ID as the key
      melon_dict[melon_id] = melon


# Function to retrieve a Melon object by its unique identifier
def get_by_id(melon_id):
    """Returns melon object by unique identifier"""
    return melon_dict[melon_id]

# Function to retrieve a list of all Melon objects
def get_all():
   """Return list of melons."""
   return list(melon_dict.values())
