***Тестовое задание в компанию e.Com***

**Написано на Python3.11**

*Тесты:*
- Тесты находятся в __test_main.py__
- Запускаются командой _pytest_ предварительно активировав виртуальное окружение.

*FastAPI:*

- Запускается через файл _main.py_ при помощи команды _python main.py_.

*Manager:*

- В файле _manager.py_ есть класс _Manager_ который и реализует весь функционал проверки и валидации данных из тела запроса с шаблонами.

*DB:*

- Шаблоны в БД хранятся в виде сериализованной json строки.

Данное приложение ищет подходящую форму шаблонов для тела запроса по адресу _/get_form_, и возвращает имя шаблона все поля которого присутствуют в теле запроса, иначе ответ что подходящего запроса не найдено.
