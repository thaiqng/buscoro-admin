from ._anvil_designer import All_brandsTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.facebook.auth
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class All_brands(All_brandsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    
  def get_brand_by_code_name(self):
    if self.item['code_name']:
      if anvil.server.call('get_brand_by_code_name', self.item['code_name']):
        return anvil.server.call('get_brand_by_code_name', self.item['code_name'])

  def link_get_brand_click(self, **event_args):
    """This method is called when the link is clicked"""
    brand=self.get_brand_by_code_name()
    if brand:
      anvil.open_form('Create_brand', brand)
    else:
      anvil.Notification("Please enter the right code name.", timeout=3).show()
      

  def button_add_brand_show(self, **event_args):
    """This method is called when the Button is shown on the screen"""
    anvil.open_form('Create_brand')


