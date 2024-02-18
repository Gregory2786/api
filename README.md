# Nome
Gregory Almeida Silva

# Objetivo
Esse projeto tem como por objetivo construir uma api para recuperar dados de uma base de dados.

# Tecnologias 
Python
Flask

# Como utilizar
Para podermos acessar as funcionalidades do projeto,
primeiramente precisamos baixar os arquivos do repositorio e os abra no VS code e execute o projeto.
logo em seguida sera disponibilizado um link para testarmos a api, o link sera esse http://localhost:5000, recomendo utilizar o Postman para fazer os testes
de requisiçoes .

# Banco de Dados

pessoas = [

    {
       'id': 1,
       'nome': 'Maria', 
    },
    
    {
       'id': 2,
       'nome': 'Joaquin', 
    },
    
    {
       'id': 3,
       'nome': 'Afonso', 
    },

]


# [GET]/pessoas
Descrição: retorna todas as pessoas


    {
       'id': 1,
       'nome': 'Maria', 
    },
    
    {
       'id': 2,
       'nome': 'Joaquin', 
    },
    
    {
       'id': 3,
       'nome': 'Afonso', 
    }

  # [GET]/pessoas{id}
  Descrição: retorna uma pessoa com base no id

  EX: http://localhost:5000/pessoas/2
  
  retorno:  
    {
         'id': 2,
         'nome': 'Joaquin', 
    }

  # [PUT]/pessoas{id}
  Descrição: edita os dados de uma pessoa com base no Id

  EX: http://localhost:5000/pessoas/1
  Novos dados:
  
   {
       'id': 1,
       'nome': 'Antonio'
   }

  retorno: 
   
    {
       'id': 1,
       'nome': 'Antonio', 
    },
    
    {
       'id': 2,
       'nome': 'Joaquin', 
    },
    
    {
       'id': 3,
       'nome': 'Afonso', 
    }

# [POST]/pessoa{id}
Descrição: adiciona novas pessoas a base de dados

Ex: 

{
   'id': 4,
   'nome': 'Carlos',
}

retorno:
  
  {
       'id': 1,
       'nome': 'Maria', 
    },
    
    {
       'id': 2,
       'nome': 'Joaquin', 
    },
    
    {
       'id': 3,
       'nome': 'Afonso', 
    },
    {
        'id': 4,
        'nome': 'Carlos',
   }

  #[DELETE]/pessoas{id}
  Descrição: exclui os dados de uma pessoa de acordo com o seu numero de id

  EX: http://localhost:5000/pessoas/1

  retorno: 
  
  {
       'id': 2,
       'nome': 'Joaquin', 
    },
    
    {
       'id': 3,
       'nome': 'Afonso', 
    }



  # Referencias
  https://www.youtube.com/watch?v=FBLAV1SbJFk
