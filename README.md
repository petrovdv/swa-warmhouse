# Спринт 1

Решение проектной работы.

# Задание 1. Анализ и планирование

### 1. Описание функциональности монолитного приложения

**Управление отоплением:**

- Пользователи могут управлять отоплением в доме, выставляя нужную температуру в системе.
- Пользователь не может самостоятельно подключить систему отопления в доме к системе. Подключение осуществляется специалистом по обслуживанию клиентов. 

**Мониторинг температуры:**

- Пользователи могут проверять температуру в доме.

### 2. Анализ архитектуры монолитного приложения

Архитектура приложения представляет из себя монолит на Go с СУБД Postgres. Всё синхронно. Никаких асинхронных вызовов, микросервисов и реактивного взаимодействия в системе нет. Всё управление идёт от сервера к датчику. Данные о температуре также получаются через запрос от сервера к датчику

### 3. Определение доменов и границы контекстов

Опишите здесь домены, которые вы выделили.

[![Alt text for the image](https://www.plantuml.com/plantuml/svg/SoWkIImgAStDuNBAJrBGjLDmpCbCJbMmKiX8pSd9vt98pKi1IW80 "Optional text")](https://www.plantuml.com/plantuml/svg/SoWkIImgAStDuNBAJrBGjLDmpCbCJbMmKiX8pSd9vt98pKi1IW80)

[![Sprites/Icons - open link](https://www.plantuml.com/plantuml/svg/hP9BZzem4CVl-HHUr0ChBPj3sqkbIek0Tf5uK1v5FQ59F05NZfrw9l3rEmvXD-f3wg4dE_EV-VyyCtaYXi1rQPCxut9RQrGdvee-f6c0o-FHyAdEQiAGUyVe-37tPLfPSB5cGAojoTBHky4gXdRpMLe2CGO97KPI0SPXUAoYVtAdiP1FDPvydOwMYyq_WBYkG8Uthq0Zwg2GZ05LmJ3IZQVn73LweNnQBhR3_MIpd4_-AwY9mGN9bpXu_pgrMrSfk6DjeMtwT_axdE5lMaa_x84mdF7NyautQNmxjJET3RyjTzl3VhfzFimcdoUBSVy-ILQIu5q_9ZwetgWczYM6djnNw2kBYa_0oY5gLGMlwvn9n3VNJZ_s6a3lFdbPO9ygaEBDQXWzsWRZTNj2LKgACeun592trYpnlCLUDH26kiZikw2RKnS5bH7ZuMeQ_UEmulaCJbia1TOgsPqa4YdhZoRlsiNihjSuw-jCgiV0a05XT9gRF7Zo1QlDbrbZxQscsnWUb0yQWnASFFliJOvo5ZwKmCQxBgopAs4cQxJjlA-psX5Ij6z-FKc8UgD8Vt-M3-jhxysJrmYQqdr4HVa9dPPz_mG0 "Sprites/Icons")](https://www.plantuml.com/plantuml/uml/hP9BZzem4CVl-HHUr0ChBPj3sqkbIek0Tf5uK1v5FQ59F05NZfrw9l3rEmvXD-f3wg4dE_EV-VyyCtaYXi1rQPCxut9RQrGdvee-f6c0o-FHyAdEQiAGUyVe-37tPLfPSB5cGAojoTBHky4gXdRpMLe2CGO97KPI0SPXUAoYVtAdiP1FDPvydOwMYyq_WBYkG8Uthq0Zwg2GZ05LmJ3IZQVn73LweNnQBhR3_MIpd4_-AwY9mGN9bpXu_pgrMrSfk6DjeMtwT_axdE5lMaa_x84mdF7NyautQNmxjJET3RyjTzl3VhfzFimcdoUBSVy-ILQIu5q_9ZwetgWczYM6djnNw2kBYa_0oY5gLGMlwvn9n3VNJZ_s6a3lFdbPO9ygaEBDQXWzsWRZTNj2LKgACeun592trYpnlCLUDH26kiZikw2RKnS5bH7ZuMeQ_UEmulaCJbia1TOgsPqa4YdhZoRlsiNihjSuw-jCgiV0a05XT9gRF7Zo1QlDbrbZxQscsnWUb0yQWnASFFliJOvo5ZwKmCQxBgopAs4cQxJjlA-psX5Ij6z-FKc8UgD8Vt-M3-jhxysJrmYQqdr4HVa9dPPz_mG0)

### **4. Проблемы монолитного решения**

- Самостоятельно подключить свой датчик к системе пользователь не может. Каждая установка сопровождается выездом специалиста по подключению системы отопления в доме к текущей версии системы.
- Нынешнее приложение компании позволяет только управлять отоплением в доме и проверять температуру.
- …

Если вы считаете, что текущее решение не вызывает проблем, аргументируйте свою позицию.

### 5. Визуализация контекста системы — диаграмма С4

Добавьте сюда диаграмму контекста в модели C4.

Чтобы добавить ссылку в файл Readme.md, нужно использовать синтаксис Markdown. Это делают так:

```markdown
[Текст ссылки](URL)
```

Замените `Текст ссылки` текстом, который хотите использовать для ссылки. Вместо `URL` вставьте адрес, на который должна вести ссылка. Например:

```markdown
[Посетите Яндекс](https://ya.ru/)
```

# Задание 2. Проектирование микросервисной архитектуры

В этом задании вам нужно предоставить только диаграммы в модели C4. Мы не просим вас отдельно описывать получившиеся микросервисы и то, как вы определили взаимодействия между компонентами To-Be системы. Если вы правильно подготовите диаграммы C4, они и так это покажут.

**Диаграмма контейнеров (Containers)**

Добавьте диаграмму.

**Диаграмма компонентов (Components)**

Добавьте диаграмму для каждого из выделенных микросервисов.

**Диаграмма кода (Code)**

Добавьте одну диаграмму или несколько.

# Задание 3. Разработка ER-диаграммы

Добавьте сюда ER-диаграмму. Она должна отражать ключевые сущности системы, их атрибуты и тип связей между ними.

# Задание 4. Создание и документирование API

### 1. Тип API

Укажите, какой тип API вы будете использовать для взаимодействия микросервисов. Объясните своё решение.

### 2. Документация API

Здесь приложите ссылки на документацию API для микросервисов, которые вы спроектировали в первой части проектной работы. Для документирования используйте Swagger/OpenAPI или AsyncAPI.

# Задание 5. Работа с docker и docker-compose

Перейдите в apps.

Там находится приложение-монолит для работы с датчиками температуры. В README.md описано как запустить решение.

Вам нужно:

1) сделать простое приложение temperature-api на любом удобном для вас языке программирования, которое при запросе /temperature?location= будет отдавать рандомное значение температуры.

Locations - название комнаты, sensorId - идентификатор названия комнаты

```
	// If no location is provided, use a default based on sensor ID
	if location == "" {
		switch sensorID {
		case "1":
			location = "Living Room"
		case "2":
			location = "Bedroom"
		case "3":
			location = "Kitchen"
		default:
			location = "Unknown"
		}
	}

	// If no sensor ID is provided, generate one based on location
	if sensorID == "" {
		switch location {
		case "Living Room":
			sensorID = "1"
		case "Bedroom":
			sensorID = "2"
		case "Kitchen":
			sensorID = "3"
		default:
			sensorID = "0"
		}
	}
```

2) Приложение следует упаковать в Docker и добавить в docker-compose. Порт по умолчанию должен быть 8081

3) Кроме того для smart_home приложения требуется база данных - добавьте в docker-compose файл настройки для запуска postgres с указанием скрипта инициализации ./smart_home/init.sql

Для проверки можно использовать Postman коллекцию smarthome-api.postman_collection.json и вызвать:

- Create Sensor
- Get All Sensors

Должно при каждом вызове отображаться разное значение температуры

Ревьюер будет проверять точно так же.


# **Задание 6. Разработка MVP**

Необходимо создать новые микросервисы и обеспечить их интеграции с существующим монолитом для плавного перехода к микросервисной архитектуре. 

### **Что нужно сделать**

1. Создайте новые микросервисы для управления телеметрией и устройствами (с простейшей логикой), которые будут интегрированы с существующим монолитным приложением. Каждый микросервис на своем ООП языке.
2. Обеспечьте взаимодействие между микросервисами и монолитом (при желании с помощью брокера сообщений), чтобы постепенно перенести функциональность из монолита в микросервисы. 

В результате у вас должны быть созданы Dockerfiles и docker-compose для запуска микросервисов. 
