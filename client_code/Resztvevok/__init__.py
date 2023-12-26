from ._anvil_designer import ResztvevokTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Resztvevok(ResztvevokTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    onkentesek_list = []
    for row in app_tables.onkentesek.search():
        onkentesek_list.append((row["Name"]))
    
    self.resztvevok.items = onkentesek_list

    # Any code you write here will run before the form opens.
