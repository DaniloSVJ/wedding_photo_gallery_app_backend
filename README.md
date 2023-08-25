Para iniciar o projeto você primeiro vai criar o banco de dados.

Instale o banco de dados postgres no seu computador
veja o site: https://www.postgresql.org/
Istale segundo seu sistema operacional
nome do banco sugerido: wedding_gallery

Coloquei os dados na variavel do ambiente no arquivo .env.

  DATABASE_NAME = wedding_gallery
  DATABASE_USER = postgres    
  DATABASE_PASSWORD= 123456
  DATABASE_HOST=localhost
  DATABASE_PORT=5432

Agora instale o virtualenv na pasta do seu projeto com o comando abaixo:

 pip install virtualenv

Ative o virtual env:
linux:
  source nome_do_ambiente/bin/activate

windows:
  nome_do_ambiente\Scripts\activate

Agora execute o comando para instalar todas as libs:

  pip install -r requirements.txt

Feito isso rode o projeto:
  python manage.py runserver  

Para ver a documentação abra no seus navegador o seguinte endereço:
  http://127.0.0.1:8000/swagger/

No admin vc precisa criar primeiro um usuario:
  python manage.py createsuperuser

  - digite um email e senha.

Para abrir o admin:
  http://127.0.0.1:8000/admin/

No link Uploaded excels.
  Vc pode fazer um upload de arquivo excel para cadastrar varios usuarios ao mesmo tempo.
  
   








