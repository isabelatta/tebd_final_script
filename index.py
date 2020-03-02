from mysql_connector import MysqlConnector
from random import *
from artigo import Artigo
from autor import Autor
from autor_artigo import AutorArtigo
from revisao import Revisao


def insertRegister(connect_mysql):
  artigo = Artigo()
  artigo.insert(connect_mysql)

  ids_autores = []
  numero_autores = randint(1, 7)

  for x in range(numero_autores):
    autor = Autor()
    autor.insert(connect_mysql)
    ids_autores.append(autor.get_id())

  for id_autor in ids_autores:
    autor_artigo = AutorArtigo(id_autor, artigo.get_id())
    autor_artigo.insert(connect_mysql)

  revisao = Revisao(choice(ids_autores), artigo.get_id())
  revisao.insert(connect_mysql)

def main():
  connect_mysql = MysqlConnector('localhost', 'root', '12345678', 'tebd')
  connect_mysql.check_connection()
  continuarInsercao = 1
  while (continuarInsercao):
    for x in range(20000):
      insertRegister(connect_mysql)
    continuarInsercao = input('Deseja continuar? (1 - Continuar) || (0 - Parar) ')



if __name__ == "__main__":
  main()