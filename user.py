# create user 
import person
class User:
  def __init__(self, user_name, password, email, salt):
    self.user_name = user_name
    self.password = password
    self.eemil = email
    self.salt = salt
  def __reps__(self):
    print(f'user name {self.user_name}')



if __name__ == '__main':
  juma = User('qasimi','jrhw123',32)
  
  
    

