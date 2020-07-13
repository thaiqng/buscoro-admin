from ._anvil_designer import Create_brandTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.facebook.auth
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Create_brand(Create_brandTemplate):
  def __init__(self, brand=None, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def link_back_click(self, **event_args):
    """This method is called when the link is clicked"""
    anvil.open_form('Home')

