from ._anvil_designer import RiasztasiAdatokTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import Adatlap

class RiasztasiAdatok(RiasztasiAdatokTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    riasztast_ado_list = []
    for row in app_tables.riasztastado.search():
        riasztast_ado_list.append((row["ShortName"], row))
    
    self.riasztast_igenylo.items = riasztast_ado_list

    # Any code you write here will run before the form opens.

  def riasztasi_adatok_mentes_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    Adatlap.riasztas_tipusa = self.riasztas_tipusa_dropdown.selected_value()
    Adatlap.riasztas_datuma = self.riasztas_datuma.date()
    Adatlap.riasztas_idopont = self.riasztas_idopont.text()
    Adatlap.riasztasi_cim = self.riasztasi_cim.text()
    Adatlap.riasztas_koordinata = self.riasztas_koordinataja.text()
    Adatlap.riasztas_helyenek_leirasa = self.riasztas_hely_leiras.text()
    Adatlap.riasztas_leirasa = self.riasztas_leirasa.text()
    Adatlap.riasztast_igenylo = self.riasztast_igenylo.selected_value()
    Adatlap.bejelento_adatai = self.bejelento_adatai.text()
    Adatlap.helyszini_iranyito_neve = self.helyszini_iranyito_nev.text()
    Adatlap.helyszini_iranyito_beosztasa = self.helyszini_iranyito_beosztas.text()
    Adatlap.helyszini_iranyito_telefonszama = self.helyszini_iranyito_telefonszam.text()
    Adatlap.helyszini_iranyito_emailcime = self.helyszini_iranyito_email.text()
    Adatlap.pmkmsz_iranyito = self.pmkmsz_iranyito.selected_value()
