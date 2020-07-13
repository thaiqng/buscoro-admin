from ._anvil_designer import HomeTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.facebook.auth
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

from ..Dashboard import Dashboard
from ..All_brands import All_brands

home_content='dashboard'
category=None

class Home(HomeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    self.display_content(home_content)
    
  def load_content(self, content):
    content.remove_from_parent()
    self.content_panel.clear()
    self.content_panel.add_component(content)
    
  def display_content(self, content):
    if content is 'dashboard':
      self.link_dashboard_click()
    elif content is 'brands':
      self.link_brands_click()
    elif content is 'account':
      self.link_account_click()

  def link_dashboard_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.load_content(Dashboard())
    home_content='dashboard'

  def link_brands_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.load_content(All_brands())
    home_content='brands'

  def link_account_click(self, **event_args):
    """This method is called when the link is clicked"""
    pass







