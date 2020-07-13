import anvil.secrets
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.email
import anvil.facebook.auth
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime, timezone

def encrypt_password(plaintext):
  return anvil.secrets.encrypt_with_key('password_key', plaintext)

def decrypt_password(ciphertext):
  return anvil.secrets.decrypt_with_key('password_key', ciphertext)

# Check if the password has at least 12 characters and contains at least 01 non-alphanumeric character.
def check_secure_password(password):
  if len(password) >= 12 and password.isalnum() is False:
    return True
  else:
    return False

# Create new table row. Only super-admin can do this.
@anvil.server.callable
def create_admin(super_admin, new_admin):
  if super_admin['email'] is "admin@bazari.mx" and super_admin['password'] is anvil.secrets.get_secret('super_admin_password'):
    
    # Check secure password.
    if check_secure_password(new_admin['password']):
      password_hash=encrypt_password(new_admin['password'])
      return app_tables.admins.add_row(
        email=new_admin['email'],
        password_hash=password_hash,
        signed_up=datetime.now(timezone.utc)
      )
    else:
      anvil.Notification("Password must contain at least 12 characters AND 01 non-alphanumeric character.",timeout=3).show()
  else:
    anvil.Notification("You are not authorized to create a new admin.",timeout=3).show()

# Check sign in with exception.
@anvil.server.callable
def sign_in_admin(admin_to_sign_in):
  # Check that the admin given is really a row in the ‘admins’ table.
  if app_tables.admins.has_row(admin_to_sign_in):
    admin=app_tables.admins.get(admin_to_sign_in['email'])
    
    # Check password.
    if admin_to_sign_in['password'] is decrypt_password(admin['password_hash']):
      admin_copy=admin
      admin_copy['last_login']=datetime.now(timezone.utc)
      update_admin(admin, admin_copy)
      return
    else:
      raise Exception("Incorrect password")
  else:
    raise Exception ("Admin does not exist.") 
    
# Update user: name, updated, last_login.
@anvil.server.callable
def update_admin(admin, admin_copy):
  # Check that the admin given is really a row in the ‘admins’ table.
  if app_tables.admins.has_row(admin):
    admin_copy['updated']=datetime.now(timezone.utc)
    admin.update(**admin_copy)
  else:
    raise Exception ("Admin does not exist.")
    
# Reset password directly in the app.
@anvil.server.callable
def reset_password_admin(admin, new_password):
  # Check secure password.
  if check_secure_password(new_admin['password']):  
    password_hash=encrypt_password(new_password)
    admin_copy=admin
    admin_copy['password_hash']=password_hash
    update_admin(admin, admin_copy)
  else:
    anvil.Notification("Password must contain at least 12 characters AND 01 non-alphanumeric character.",timeout=3).show()
  
# Change name directly in the app.
@anvil.server.callable
def change_name_admin(admin, new_name):
  admin_copy=admin
  admin_copy['name']=new_name
  update_admin(admin, admin_copy)
  