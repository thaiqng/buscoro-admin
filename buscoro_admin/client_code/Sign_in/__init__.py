from ._anvil_designer import Sign_inTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.facebook.auth
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Sign_in(Sign_inTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    
  def button_sign_in_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.item['email'] and self.item['password']:
      try:
        anvil.users.login_with_email(self.item['email'], self.item['password'])
        open_form('Home')
      except:
        anvil.Notification("Please enter the right email and password.", timeout=3).show()
    else:
      anvil.Notification("Please enter email and password.", timeout=3).show()
      
    

