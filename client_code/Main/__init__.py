from ._anvil_designer import MainTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
from ..RiasztasiAdatok import RiasztasiAdatok
from ..Resztvevok import Resztvevok
from ..RiasztasLezarasa import RiasztasLezarasa

class Main(MainTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    anvil.server.call('create_user')
    anvil.users.login_with_form()

    # set each Link's `tag.form_to_open` attribute to an instance of the Form you want to open
    self.riasztasi_adatok.tag.form_to_open = RiasztasiAdatok()
    self.resztvevok.tag.form_to_open = Resztvevok()
    self.riasztas_lezarasa.tag.form_to_open = RiasztasLezarasa()
    

    # Any code you write here will run before the form opens.

  def riasztási_adatok_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    """A generalised click handler that you can bind to any nav link."""
    # Find out which Form this Link wants to open
    form_to_open = event_args['sender'].tag.form_to_open

    self.content_panel.clear()
    self.content_panel.add_component(form_to_open)

  def resztvevok_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    """A generalised click handler that you can bind to any nav link."""
    # Find out which Form this Link wants to open
    form_to_open = event_args['sender'].tag.form_to_open

    self.content_panel.clear()
    self.content_panel.add_component(form_to_open)

  def riasztott_szerek_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    """A generalised click handler that you can bind to any nav link."""
    # Find out which Form this Link wants to open
    form_to_open = event_args['sender'].tag.form_to_open

    self.content_panel.clear()
    self.content_panel.add_component(form_to_open)

  def riasztás_lezarasa_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    """A generalised click handler that you can bind to any nav link."""
    # Find out which Form this Link wants to open
    form_to_open = event_args['sender'].tag.form_to_open

    self.content_panel.clear()
    self.content_panel.add_component(form_to_open)

  def dokumentumok_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    """A generalised click handler that you can bind to any nav link."""
    # Find out which Form this Link wants to open
    form_to_open = event_args['sender'].tag.form_to_open

    self.content_panel.clear()
    self.content_panel.add_component(form_to_open)
