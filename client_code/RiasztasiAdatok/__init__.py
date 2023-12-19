from ._anvil_designer import RiasztasiAdatokTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class RiasztasiAdatok(RiasztasiAdatokTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    riasztast_ado_list = []
    for row in app_tables.riasztastado.search():
        riasztast_ado_list.append((row["ShortName"], row))
    
    self.riasztast_igenylo.items = riasztast_ado_list

    # Any code you write here will run before the form opens.
