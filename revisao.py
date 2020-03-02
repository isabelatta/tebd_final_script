
from faker import Faker
from random import *

class Revisao(object):
  def __init__(self, autor, artigo):
    fake = Faker()
    self.autor = autor
    self.artigo = artigo
    self.nota = randint(0, 10)
    self.comentario = fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)
    self.created_at = fake.date_time(tzinfo=None, end_datetime=None)
    self.updated_at = self.created_at
    self.id = None

  def insert(self, cnx):
    insert_id = cnx.insert(
      'revisao',
      autor_id=self.autor,
      artigo_id=self.artigo,
      nota=self.nota,
      comentario=self.comentario,
      created_at=self.created_at,
      updated_at=self.updated_at
    )
    self.id = insert_id

  def get_id(self):
    return self.id