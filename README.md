# Sprint_7 API-автотесты для сервиса "Яндекс.Самокат"
### URL: https://qa-scooter.praktikum-services.ru/

## Инструкция по запуску автотестов:
Склонировать репозиторий:

```bash
git clone https://github.com/Alenyshka2023/Sprint_7.git
``` 

Перейти в директорию проекта:
```bash
cd Sprint_7
``` 

Создать виртуальное окружение:
```bash
python -m venv venv
``` 
Активировать виртуальное окружение (команда для Windows):
```bash
.\venv\Scripts\activate
``` 
Установить зависимости:
```bash
pip install -r requirements.txt
```
Запустить тесты:
```bash
pytest -v --alluredir=allure_results 
```
Сгенерировать отчет Allure:
```bash
allure serve allure_results 
```