pugpe
=====

Site do PugPE


Softwate utilizados
-------------------

- Python
- Django
- Docker

Instalação (usando sqlite)
--------------------------

- sudo docker-compose run --rm app python manage.py syncdb 
- sudo docker-compose run --rm app python manage.py migrate


Rodando
-------

- sudo docker-compose run --service-ports --rm app python manage.py runserver 0.0.0.0:8000
- Acesse o site em http://localhost:8000


Testes
------

- sudo docker-compose run --service-ports --rm app python manage.py test


Contribuidores
--------------
- Renato Oliveira
- Fernando Rocha
- Gileno Filho
- Filipe Ximenes

License
-------

Copyright 2012 Pug-PE and contributors.

Licensed under The MIT License (MIT).
