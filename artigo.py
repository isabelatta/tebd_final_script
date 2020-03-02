
from faker import Faker

class Artigo(object):
  def __init__(self):
    fake = Faker()
    self.resumo = fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)
    self.created_at = fake.date_time(tzinfo=None, end_datetime=None)
    self.updated_at = self.created_at
    self.id = None

  def insert(self, cnx):
    insert_id = cnx.insert(
      'artigo',
      resumo=self.resumo,
      created_at=self.created_at,
      updated_at=self.updated_at
    )
    self.id = insert_id

  def get_id(self):
    return self.id