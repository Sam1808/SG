# Market for Spider Group
 
>*Преа́мбула: в связи со спецификой условий выполнения задачи, код далее написан исходя из  следующих принципов:*
>   - *Больше, не значит лучше.*
>   - *Сначала функционал, потом оптимизация.*
>   - *Делаешь, как понимаешь.*<br>
>
>*Подробности специфики не уточняю, однако автор полностью согласен со всей критикой в части, например, оптимизации кода.*

<br>

## Общее описание.

### Код написан по заданию [Spider Group](https://spider.ru/).

<br>

**Поставленные задачи:**
- Построить структуру БД используя Django ORM.
- Настроить редактирование этих данных в Django admin.
- Написать API для получения данных из этих моделей используя DjangoRestFramework и django_filters.

**Реализованные сущности:**
- Пользователь (*переопределенная модель Django*)
- Категория
- Компания
- Продукт

**Структура БД согласно задания:**<br><br>
![Схема БД](screenshots/01_schema.png)

**Разработаны следующие ресурсы API:**

1. Регистрация пользователя;
2. Авторизация пользователя по DRF токену;
3. Список категорий;
4. Список активных компаний;
5. Список активных продуктов, включая: 
    - фильтрация по компании,
    - фильтрация по категории,
    - поиск по неполному наименованию;
6. Детальная карточка продукта;
7. Создание/Изменение/Удаление (*обязательная авторизация*).

<br>

## 1. Установка. 
<br>

Для корректной работы вам нужен **Python 3.7 или выше**.

1.1 Скачайте код:<br>
`git clone https://github.com/Sam1808/SG.git`

1.2 Создайте виртуальное окружение, [активируте](https://devpractice.ru/python-lesson-17-virtual-envs/#p33) его и перейдите в папку `spider_project`:<br>
`python3 -m venv _название_окружения_`

1.3 Обновите установщик пакетов `pip` (*не помешает*) и установите зависимости:<br>
`pip install --upgrade pip`<br>
`pip install -r requirements.txt`

1.4 Примените существующие миграции:<br>
`python manage.py migrate`

1.5 Создайте суперпользователя (администратора):<br>
`python manage.py createsuperuser`

1.6 Запустите локальный сервер:<br>
`python manage.py runserver`<br>
который будет доступен по адресу<br>
`http://127.0.0.1:8000/`

1.7. Наслаждайтесь (*обязательное условие*).
<br><br>

## 2. Использование

<br>

### 2.1 Подготовка 

Для того чтобы проверить корректность работы API по пунктам 3-7 (см. *Разработаны следующие ресурсы API*) предлагается вручную добавить объекты сущностей Категория, Компания, Продукты. Заодно убедиться в правильной работе Django admin (см. *Поставленные задачи*).

Для этого... Переходим в раздел администратора<br>
`http://127.0.0.1:8000/admin/ `<br>
Вводим логин/пароль (*см. пункт 1.5*), получаем следующий интерфейс:<br><br>
![Django admin site](screenshots/02_admin.png)<br><br>
Введите тестовые данные для каждой из сущностей, например так: <br><br>
![Categories](screenshots/03_categories.png)<br>
![Companies](screenshots/03_companies.png)<br>
![Products](screenshots/03_products.png)<br>
<br><br>

### 2.2 Регистрация пользователя

API регистрации пользователя реализовано через Django Rest Framework (DRF), по ссылке: <br>
`http://127.0.0.1:8000/registr/ `<br>
Получаем следующий API интерфейс: <br><br>
![Registration](screenshots/04_registr.png)<br>

Реализованы обязательные поля Логина, Пароля и E-mail`а. <br><br>
Давайте , например для [Spider Group](https://spider.ru/) создадим настоящего **Spiderman**: <br><br>
![Create spiderman](screenshots/04_create_spiderman.png)<br><br>

В случае успешного создания пользователя API возвращает `"response": true`.

<br>
 
### 2.3 Авторизация пользователя по DRF токену
Для реализации токенов выбрана технология [JSON Web Token](https://ru.wikipedia.org/wiki/JSON_Web_Token).

Авторизация в примерах отражена в пункте **2.8 Создание/Изменение/Удаление**.

Здесь же мы остановимся на создании Токена для пользователя, его проверке и обновлении.

Итак, зарегистрированный пользователь может получить JWT Токен на странице: <br>
`http://127.0.0.1:8000/auth/jwt/create`<br>
Для получения Токена необходимо указать Логин и Пароль.<br>
Получаем токены для **Spiderman`a**:

![Create Token for spiderman](screenshots/05_token_create.png)<br><br>

После, API отдает пользователю Токен авторизации (*access token*) и Токен обновления (*refresh token*).<br>

![Create spiderman](screenshots/05_token_result.png)<br><br>

Доступность Токена проверяется по ссылке: 
`http://127.0.0.1:8000/auth/jwt/verify` <br>

Обновление Токена: 
`http://127.0.0.1:8000/auth/jwt/refresh`


Использование Токенов реализовано на библиотеке [SimpleJWT](https://github.com/SimpleJWT/django-rest-framework-simplejwt), большинство настроек сохранены по умолчанию.

<br>

### 2.4 Список категорий
API списка Категорий доступно по ссылке:<br>
`http://127.0.0.1:8000/categories/` <br>
Согласно условий - исключительно режим `read only`.

<br>

### 2.5 Список активных компаний
API списка Компаний доступно по ссылке:<br>
`http://127.0.0.1:8000/companies/` <br>
Опять же, исключительно режим `read only`.<br> Обратите внимание, что в списке только *активные* Компании. Т. об. если на шаге 2.1 при внесении компаний вы не указали *Доступность компании* (по умолчанию значение False), то по запросу к API вы получите пустой список.

<br>

### 2.6 Список активных продуктов

API списка Продуктов доступно по ссылке:<br>
`http://127.0.0.1:8000/activeproducts/` <br>
Традиционно режим `read only` и только продукты с отмеченным флагом *Доступность продукта*.

Реализована фильтрация, согласно задания:
- фильтрация по Компании<br>
`http://127.0.0.1:8000/activeproducts/?company=id`, где `id` - это `id` компании, продукты которой надо отобразить;
- фильтрация по Категории<br>
`http://127.0.0.1:8000/activeproducts/?category=id`, где `id` - это `id` конкретной категории продуктов;
- фильтрация по неполному наименованию Продукта;<br> 
`http://127.0.0.1:8000/activeproducts/?title=наименование продукта`

Примеры:
1. Давайте заведем через Django Admin несколько сущеностей Продукт с примерно одинаковым названием, например `test1`, `test2`, `test3`. Некоторые из них должны быть *активными*. Проверим поиск с условиеми *неполного* наименования: <br>
`http://127.0.0.1:8000/activeproducts/?title=test`<br>
Получим спискок всех *активных* продуктов, где в имени продукта есть `test`.
2. А ещё фильтры можно использовать совместно. Например, запрос всех продуктов, где в имени есть `test` , категории с id равной 1 и компании с id номер 2, будет выглядить так: <br>
`http://127.0.0.1:8000/activeproducts/?title=test&category=1&company=2`

<br>
<br>

### 2.7 Детальная карточка продукта

API Детальной карточки продукта доступно по ссылке:<br>
`http://127.0.0.1:8000/product/id`<br> 
Где `id` - это идентификационный номер Продукта, чью детальную карточку вы хотите просмотреть/получить в режиме `read only`.

<br>

### 2.8 Создание/Изменение/Удаление

Реализовано API Создание/Изменение/Удаление... для сущности "Продукт". Для операций [CRUD](https://ru.wikipedia.org/wiki/CRUD) неоходима авторизация по JWT (*наконец-таки!*). 
При этом "Создание" отделено от "Изменения/Удаления" на разные ресурсы API (*хотите узнать почему - спросите у меня об этом при личной встрече*). 
Далее все процессы будут описаны примерами, для реализации которых используем [Postman](https://www.postman.com/).
<br><br>

#### 2.8.1 Создание объекта cущности Продукт при обязательной JWT авторизации.

Для начала выберем пользователя, от чьего имени будем авторизовываться, проверим доступность его Токена и при необходимости обновим его (*все то, что вы делали в пункте 2.2*)

API создания объекта реализовано по ссылке:<br>
`http://127.0.0.1:8000/createproduct/` <br>

Для успешной авторизации укажем в интерфейсе [Postman](https://www.postman.com/) легитимный Access Токен выбранного пользователя:<br><br>
![Add Token](screenshots/06_create_product_with_token.png)<br><br>
В теле (*Body*) запроса укажем обязательные поля для создания продукта и отправим запрос `POST`.
Здесь мы сделаем для нашего Spiderman`a паутину "против врагов".<br><br>
![Add Body](screenshots/06_create_product_goods.png)<br><br>
Если все получилось, то вы увидите ответ сервера в виде только что созданного Продукта.<br><br>
![Product result](screenshots/06_create_product_result.png)<br><br>

<br><br>

#### 2.8.2 Изменение и Удаление Продукта при обязательной JWT авторизации.


Правила почти те же - легитимный Access Токен. Убедитесь, что он у вас есть и для изменения/удаления карточки Продукта обратитесь по ссылке:<br>
`http://127.0.0.1:8000/modifyproduct/id`<br> 
Где `id` - это идентификационный номер Продукта, который вы хотите изменить/удалить.<br> 

API позволяет использовать методы `PUT`, `PATCH`, `DELETE` (*и никуда не деться от `GET`*), и если с последним все ясно, то между `PUT` и `PATCH` есть разница, будьте внимательны. 

Подставив свежий Токен, давайте изменим только что созданный Продукт.<br><br>
![Product patch](screenshots/07_patch_product.png)<br><br>
Поменяли описание и применяем метод `PATCH`. В ответ прийдет измененный продукт:<br><br>
![Product patch result](screenshots/07_patch_product_result.png)<br><br>

С удалением тоже никаких проблем. Просто применяем метод `DELETE`. Если пришел пустой ответ, то указанный продукт удален.<br><br>
![Product delete](screenshots/07_delete_product_result.png)<br><br>

> Если вы дочитали до конца, и вам понравилось - поставьте *звездочку* репозиторию.<br>
> Или не ставьте... :)
