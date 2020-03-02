
from faker import Faker

class AutorArtigo(object):
  def __init__(self, autor, artigo):
    fake = Faker()
    self.autor = autor
    self.artigo = artigo
    self.created_at = fake.date_time(tzinfo=None, end_datetime=None)
    self.updated_at = self.created_at
    self.id = None

  def insert(self, cnx):
    insert_id = cnx.insert(
      'autor_artigo',
      autor_id=self.autor,
      artigo_id=self.artigo,
      created_at=self.created_at,
      updated_at=self.updated_at
    )
    self.id = insert_id

  def get_id(self):
    return self.id