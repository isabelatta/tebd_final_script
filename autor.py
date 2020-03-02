
from faker import Faker
from random import *

class Autor(object):
  def __init__(self):
    fake = Faker()
    self.nome = fake.name()
    self.endereco = fake.address()
    self.email = fake.email()
    self.telefone = fake.phone_number()
    self.local_emprego = fake.address()
    self.numero_inscricao = fake.ean8()
    self.data_vencimento = fake.date_time(tzinfo=None, end_datetime=None)
    self.cartao_credito = fake.credit_card_provider(card_type=None)
    self.voluntario = randint(0, 1)
    self.created_at = fake.date_time(tzinfo=None, end_datetime=None)
    self.updated_at = self.created_at
    self.id = None

  def insert(self, cnx):
    insert_id = cnx.insert(
      'autor',
      nome=self.nome,
      endereco=self.endereco,
      email=self.email,
      tel=self.telefone,
      local_emprego=self.local_emprego,
      numero_inscricao=self.numero_inscricao,
      data_vencimento=self.data_vencimento,
      cartao_credito=self.cartao_credito,
      voluntario=self.voluntario,
      created_at=self.created_at,
      updated_at=self.updated_at
    )
    self.id = insert_id
  


  def get_id(self):
    return self.id