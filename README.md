<H2>Розгорнути проект</H2>
<H3>Скачуєм репозиторій з GitHub:</H3>

`git clone https://github.com/pshkravets/TTPH.git` <br>

Далі нам потрібно розгорнути проект. Я докеризував проект 
тому у вас є два варіанти: <br>

<H3>Через Dockerfile:</H3>
Знаходимо шлях до репозиторію: <br>
`cd path_to_your_reposetoriy` <br><br>

Будуємо втілення (image): <br><br>
`docker build -t ttask-PH .`

Запускаємо контейнер: <br>
`docker run -d -p 5000:5000 ttask-PH`


<H3>На пряму:</H3>
Знаходимо шлях до репозиторію: <br>
`cd <path to your reposetoriy>` <br>
Запускаємо проект <br
`python views.py`


<H2>API:</H2>
Маємо три ендпоінта: <br>
_http://127.0.0.1:5000/tokenize_ <br>
_http://127.0.0.1:5000/pos_tag_ <br>
_http://127.0.0.1:5000/ner_

На них можемо відправляти лише **POST** запити та в тілі запиту 
вказуємо текст який нас цікавить. 

<H3>Приклад запиту з програмою Postman:</H3>

Зпходимо в програму вибираєм метод **POST** а в URL вказуємо 
`http://127.0.0.1:5000/tokenize`
Далі переходимо в розділ _Body_ вибираємо тип даних _raw_ та _JSON_.
Прописуємо тіло запиту:<br>
` { ` <br>
`    "text": "Hello World!"` <br>
`}` <br>

Результат повинен бути такий:<br>
`{`<br>
`    "tokens": [` <br> 
`        "Hello",` <br>
`        "World",` <br>
`        "!"` <br>
`    ]` <br>
`}`