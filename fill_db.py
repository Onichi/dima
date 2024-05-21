from app import db, create_app
from app.models import *
from datetime import date
app = create_app()

# Вот это ниже работает
def populate_db():
    db.drop_all()
    db.create_all()
    position1 = Position(code="1")

    db.session.add_all([position1])
    db.session.commit()

    # Add data to the 'Employees' table
    employee1 = Employee(position_code=1)

    db.session.add_all([employee1])
    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        user = db.session.query(Employee).first()
        print(user.id, user.position_code)
        # populate_db()
#

# Выбираем произвольного пользователя



# # Выводим информацию о пользователе
# print("Employee Information:")
# print(f"Full Name: {user.full_name}")
# print(f"Age: {user.age}")
# print(f"Gender: {user.gender}")
# print(f"Address: {user.address}")
# print(f"Phone: {user.phone}")
# print(f"Passport Data: {user.passport_data}")
# print(f"Position: {user.position.position_name}")
# print(f"Salary: {user.position.salary}")
# print(f"Responsibilities: {user.position.responsibilities}")
# print(f"Requirements: {user.position.requirements}")


#
# def populate_db():
#     # Очистка базы данных
#     db.drop_all()
#     db.create_all()
#
#     # Заполнение таблицы "Должности"
#     positions = [
#         Position(code='P001', name='Директор', salary=150000, duties='Управление компанией',
#                  requirements='Высшее образование'),
#         Position(code='P002', name='Менеджер', salary=60000, duties='Работа с клиентами',
#                  requirements='Опыт работы от 2 лет'),
#         Position(code='P003', name='Бухгалтер', salary=70000, duties='Ведение бухгалтерии',
#                  requirements='Опыт работы от 3 лет'),
#         Position(code='P004', name='Маркетолог', salary=80000, duties='Разработка маркетинговых стратегий',
#                  requirements='Высшее образование'),
#         Position(code='P005', name='Секретарь', salary=40000, duties='Административная поддержка',
#                  requirements='Без требований')
#     ]
#     db.session.bulk_save_objects(positions)
#
#     # Заполнение таблицы "Сотрудники"
#     employees = [
#         Employee(code='E001', full_name='Иванов Иван Иванович', age=45, gender='Мужской', address='ул. Ленина, д. 1',
#                  phone='89991234567', passport_data='89993567890', position_code='P001'),
#         Employee(code='E002', full_name='Петров Петр Петрович', age=34, gender='Мужской', address='ул. Пушкина, д. 2',
#                  phone='89997654321', passport_data='89993678901', position_code='P002'),
#         Employee(code='E003', full_name='Сидорова Анна Ивановна', age=29, gender='Женский',
#                  address='ул. Гагарина, д. 3', phone='89993456789', passport_data='3456 789012', position_code='P003'),
#         Employee(code='E004', full_name='Михайлова Елена Петровна', age=41, gender='Женский',
#                  address='ул. Тверская, д. 4', phone='89994567890', passport_data='4567 890123', position_code='P004'),
#         Employee(code='E005', full_name='Федоров Дмитрий Сергеевич', age=37, gender='Мужской',
#                  address='ул. Красная, д. 5', phone='89995678901', passport_data='5678 901234', position_code='P005'),
#         Employee(code='E006', full_name='Кузнецов Сергей Иванович', age=33, gender='Мужской',
#                  address='ул. Победы, д. 6', phone='89996789012', passport_data='6789 012345', position_code='P002'),
#         Employee(code='E007', full_name='Новикова Марина Олеговна', age=28, gender='Женский',
#                  address='ул. Московская, д. 7', phone='89997890123', passport_data='7890 123456',
#                  position_code='P003'),
#         Employee(code='E008', full_name='Борисов Николай Андреевич', age=39, gender='Мужской',
#                  address='ул. Садовая, д. 8', phone='89998901234', passport_data='8901 234567', position_code='P004'),
#         Employee(code='E009', full_name='Ершова Наталья Викторовна', age=35, gender='Женский',
#                  address='ул. Зеленая, д. 9', phone='89999012345', passport_data='9012 345678', position_code='P005'),
#         Employee(code='E010', full_name='Орлова Оксана Николаевна', age=30, gender='Женский',
#                  address='ул. Солнечная, д. 10', phone='89990123456', passport_data='0123 456789', position_code='P002')
#     ]
#     db.session.bulk_save_objects(employees)
#
#     # Заполнение таблицы "Виды рекламы"
#     ad_types = [
#         AdvertisementType(code='A001', name='Баннерная реклама', description='Размещение баннеров на сайтах.'),
#         AdvertisementType(code='A002', name='Контекстная реклама', description='Реклама в поисковых системах.'),
#         AdvertisementType(code='A003', name='Таргетированная реклама', description='Реклама в социальных сетях.'),
#         AdvertisementType(code='A004', name='Видео реклама', description='Реклама на видео платформах.'),
#         AdvertisementType(code='A005', name='Нативная реклама', description='Реклама, встроенная в контент.')
#     ]
#     db.session.bulk_save_objects(ad_types)
#
#     # Заполнение таблицы "Дополнительные услуги"
#     services = [
#         AdditionalService(code='S001', name='SEO оптимизация',
#                           description='Повышение позиций сайта в поисковых системах.', cost=15000),
#         AdditionalService(code='S002', name='Анализ рынка', description='Исследование рынка и целевой аудитории.',
#                           cost=20000),
#         AdditionalService(code='S003', name='Создание контента',
#                           description='Разработка и создание уникального контента.', cost=12000),
#         AdditionalService(code='S004', name='SMM продвижение', description='Продвижение в социальных сетях.',
#                           cost=18000),
#         AdditionalService(code='S005', name='Email маркетинг',
#                           description='Рассылка рекламных материалов по электронной почте.', cost=10000)
#     ]
#     db.session.bulk_save_objects(services)
#
#     # Заполнение таблицы "Места расположения"
#     locations = [
#         Location(code='L001', name='Центральный офис', location='г. Москва, ул. Ленина, д. 1', type_code='A001',
#                  description='Центральный офис компании.', cost=100000),
#         Location(code='L002', name='Филиал 1', location='г. Санкт-Петербург, ул. Пушкина, д. 2', type_code='A002',
#                  description='Филиал в Санкт-Петербурге.', cost=80000),
#         Location(code='L003', name='Филиал 2', location='г. Казань, ул. Гагарина, д. 3', type_code='A003',
#                  description='Филиал в Казани.', cost=60000),
#         Location(code='L004', name='Филиал 3', location='г. Новосибирск, ул. Тверская, д. 4', type_code='A004',
#                  description='Филиал в Новосибирске.', cost=70000),
#         Location(code='L005', name='Филиал 4', location='г. Екатеринбург, ул. Красная, д. 5', type_code='A005',
#                  description='Филиал в Екатеринбурге.', cost=65000),
#         Location(code='L006', name='Филиал 5', location='г. Нижний Новгород, ул. Победы, д. 6', type_code='A001',
#                  description='Филиал в Нижнем Новгороде.', cost=50000),
#         Location(code='L007', name='Филиал 6', location='г. Челябинск, ул. Московская, д. 7', type_code='A002',
#                  description='Филиал в Челябинске.', cost=55000),
#         Location(code='L008', name='Филиал 7', location='г. Самара, ул. Садовая, д. 8', type_code='A003',
#                  description='Филиал в Самаре.', cost=60000),
#         Location(code='L009', name='Филиал 8', location='г. Омск, ул. Зеленая, д. 9', type_code='A004',
#                  description='Филиал в Омске.', cost=45000),
#         Location(code='L010', name='Филиал 9', location='г. Ростов-на-Дону, ул. Солнечная, д. 10', type_code='A005',
#                  description='Филиал в Ростове-на-Дону.', cost=40000)
#     ]
#     db.session.bulk_save_objects(locations)
#
#     # Заполнение таблицы "Заказчики"
#     customers = [
#         Customer(code='C001', full_name='Алексеев Алексей Алексеевич', address='г. Москва, ул. Ленина, д. 1',
#                  phone='89991234567'),
#         Customer(code='C002', full_name='Борисова Борислава Борисовна', address='г. Санкт-Петербург, ул. Пушкина, д. 2',
#                  phone='89997654321'),
#         Customer(code='C003', full_name='Васильев Василий Васильевич', address='г. Казань, ул. Гагарина, д. 3',
#                  phone='89993456789'),
#         Customer(code='C004', full_name='Григорьев Григорий Григорьевич', address='г. Новосибирск, ул. Тверская, д. 4',
#                  phone='89994567890'),
#         Customer(code='C005', full_name='Дмитриева Дарья Дмитриевна', address='г. Екатеринбург, ул. Красная, д. 5',
#                  phone='89995678901'),
#         Customer(code='C006', full_name='Ефремов Евгений Евгеньевич', address='г. Нижний Новгород, ул. Победы, д. 6',
#                  phone='89996789012'),
#         Customer(code='C007', full_name='Жукова Жанна Жановна', address='г. Челябинск, ул. Московская, д. 7',
#                  phone='89997890123'),
#         Customer(code='C008', full_name='Захаров Захар Захарович', address='г. Самара, ул. Садовая, д. 8',
#                  phone='89998901234'),
#         Customer(code='C009', full_name='Иванова Ирина Ивановна', address='г. Омск, ул. Зеленая, д. 9',
#                  phone='89999012345'),
#         Customer(code='C010', full_name='Ковалев Константин Константинович',
#                  address='г. Ростов-на-Дону, ул. Солнечная, д. 10', phone='89990123456')
#     ]
#     db.session.bulk_save_objects(customers)
#
#     # Заполнение таблицы "Заказы"
#     orders = [
#         Order(order_date=date(2024, 1, 1), start_date=date(2024, 1, 2), end_date=date(2024, 1, 10),
#               customer_code='C001', location_code='L001', service1_code='S001', service2_code='S002',
#               service3_code='S003', cost=50000, payment_mark=True, employee_code='E001'),
#         Order(order_date=date(2024, 1, 3), start_date=date(2024, 1, 4), end_date=date(2024, 1, 11),
#               customer_code='C002', location_code='L002', service1_code='S002', service2_code='S003',
#               service3_code='S004', cost=60000, payment_mark=True, employee_code='E002'),
#         Order(order_date=date(2024, 1, 5), start_date=date(2024, 1, 6), end_date=date(2024, 1, 12),
#               customer_code='C003', location_code='L003', service1_code='S003', service2_code='S004',
#               service3_code='S005', cost=55000, payment_mark=False, employee_code='E003'),
#         Order(order_date=date(2024, 1, 7), start_date=date(2024, 1, 8), end_date=date(2024, 1, 14),
#               customer_code='C004', location_code='L004', service1_code='S004', service2_code='S005',
#               service3_code='S001', cost=70000, payment_mark=True, employee_code='E004'),
#         Order(order_date=date(2024, 1, 9), start_date=date(2024, 1, 10), end_date=date(2024, 1, 16),
#               customer_code='C005', location_code='L005', service1_code='S005', service2_code='S001',
#               service3_code='S002', cost=65000, payment_mark=True, employee_code='E005'),
#         Order(order_date=date(2024, 1, 11), start_date=date(2024, 1, 12), end_date=date(2024, 1, 18),
#               customer_code='C006', location_code='L006', service1_code='S001', service2_code='S002',
#               service3_code='S003', cost=50000, payment_mark=True, employee_code='E006'),
#         Order(order_date=date(2024, 1, 13), start_date=date(2024, 1, 14), end_date=date(2024, 1, 20),
#               customer_code='C007', location_code='L007', service1_code='S002', service2_code='S003',
#               service3_code='S004', cost=60000, payment_mark=True, employee_code='E007'),
#         Order(order_date=date(2024, 1, 15), start_date=date(2024, 1, 16), end_date=date(2024, 1, 22),
#               customer_code='C008', location_code='L008', service1_code='S003', service2_code='S004',
#               service3_code='S005', cost=55000, payment_mark=False, employee_code='E008'),
#         Order(order_date=date(2024, 1, 17), start_date=date(2024, 1, 18), end_date=date(2024, 1, 24),
#               customer_code='C009', location_code='L009', service1_code='S004', service2_code='S005',
#               service3_code='S001', cost=70000, payment_mark=True, employee_code='E009'),
#         Order(order_date=date(2024, 1, 19), start_date=date(2024, 1, 20), end_date=date(2024, 1, 26),
#               customer_code='C010', location_code='L010', service1_code='S005', service2_code='S001',
#               service3_code='S002', cost=65000, payment_mark=True, employee_code='E010')
#     ]
#     db.session.bulk_save_objects(orders)
#
#     # Подтверждение изменений
#     db.session.commit()
#
# if __name__ == '__main__':
#     with app.app_context():
#         populate_db()
#
