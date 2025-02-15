# create user 
import person
class User:
  # create user 
  def __init__(self, user_name, password, email, salt):
    self.user_name = user_name
    self.password = password
    self.eemil = email
    self.salt = salt
    
  def __repr__(self):
    # create method
    print(f'user name {self.user_name}')
  # hash password
  def hashPassword(self):
    pass



if __name__ == '__main':
  juma = User('qasimi','jrhw123',32)
  
  
    

