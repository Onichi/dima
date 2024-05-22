from app import db, create_app
from app.models import *
from datetime import date
app = create_app()

# Вот это ниже работает
def populate_db():
    db.drop_all()
    db.create_all()

    employees = [
        Employee(full_name="Иван Иванов", age=30, gender="Мужской", address="ул. Ленина, д. 1", phone="555-1234",
                 passport_data="AB123456", position_code="P01"),
        Employee(full_name="Анна Смирнова", age=28, gender="Женский", address="ул. Пушкина, д. 2", phone="555-5678",
                 passport_data="CD789012", position_code="P02"),
        Employee(full_name="Мария Соколова", age=35, gender="Женский", address="ул. Чехова, д. 3", phone="555-9101",
                 passport_data="EF345678", position_code="P03"),
        Employee(full_name="Алексей Кузнецов", age=40, gender="Мужской", address="ул. Горького, д. 4", phone="555-1122",
                 passport_data="GH901234", position_code="P01"),
        Employee(full_name="Дмитрий Попов", age=45, gender="Мужской", address="ул. Лермонтова, д. 5", phone="555-3344",
                 passport_data="IJ567890", position_code="P02"),
        Employee(full_name="Елена Новикова", age=32, gender="Женский", address="ул. Тверская, д. 6", phone="555-5566",
                 passport_data="KL234567", position_code="P03"),
        Employee(full_name="Николай Морозов", age=29, gender="Мужской", address="ул. Невская, д. 7", phone="555-7788",
                 passport_data="MN890123", position_code="P01"),
        Employee(full_name="Ольга Петрова", age=37, gender="Женский", address="ул. Ладожская, д. 8", phone="555-9900",
                 passport_data="OP456789", position_code="P02"),
        Employee(full_name="Виктор Киселев", age=31, gender="Мужской", address="ул. Волкова, д. 9", phone="555-1123",
                 passport_data="QR123456", position_code="P03"),
        Employee(full_name="Татьяна Баранова", age=34, gender="Женский", address="ул. Жукова, д. 10", phone="555-4455",
                 passport_data="ST789012", position_code="P01")
    ]
    db.session.bulk_save_objects(employees)

    positions = [
        Position(code="P01", name="Менеджер", salary=50000, duties="Управление командой и проектами",
                 requirements="5 лет опыта, лидерские качества"),
        Position(code="P02", name="Разработчик", salary=60000, duties="Разработка и поддержка программного обеспечения",
                 requirements="3 года опыта, навыки программирования"),
        Position(code="P03", name="Дизайнер", salary=55000, duties="Дизайн пользовательских интерфейсов и графики",
                 requirements="4 года опыта, навыки дизайна"),
        Position(code="P04", name="Тестировщик", salary=45000,
                 duties="Тестирование программного обеспечения на наличие ошибок",
                 requirements="2 года опыта, внимательность к деталям"),
        Position(code="P05", name="Аналитик", salary=52000, duties="Анализ данных и предоставление инсайтов",
                 requirements="3 года опыта, аналитические навыки")
    ]
    db.session.bulk_save_objects(positions)
    advertisement_types = [
        AdvertisementType(code="A01", name="Билборд", description="Большая наружная реклама"),
        AdvertisementType(code="A02", name="Онлайн", description="Цифровая реклама на веб-сайтах"),
        AdvertisementType(code="A03", name="ТВ", description="Телевизионные рекламные ролики"),
        AdvertisementType(code="A04", name="Радио", description="Рекламные ролики на радио"),
        AdvertisementType(code="A05", name="Печать", description="Реклама в журналах и газетах")
    ]
    db.session.bulk_save_objects(advertisement_types)
    additional_services = [
        AdditionalService(code="S01", name="Дизайн", description="Услуги графического дизайна", cost=200),
        AdditionalService(code="S02", name="Копирайтинг", description="Услуги по созданию контента", cost=150),
        AdditionalService(code="S03", name="SEO", description="Услуги по оптимизации поисковых систем", cost=250),
        AdditionalService(code="S04", name="Фотография", description="Услуги профессиональной фотографии", cost=300),
        AdditionalService(code="S05", name="Видеопроизводство", description="Услуги по производству видео", cost=500)
    ]
    db.session.bulk_save_objects(additional_services)
    locations = [
        Location(code="L01", name="Центр города", location="ул. Ленина", type_code="A01",
                 description="Зона с высоким трафиком", cost=1000),
        Location(code="L02", name="Пригород", location="ул. Березовая", type_code="A02", description="Жилая зона",
                 cost=800),
        Location(code="L03", name="Торговый центр", location="ул. Шопинг", type_code="A03", description="Торговая зона",
                 cost=1200),
        Location(code="L04", name="Шоссе", location="Магистраль 5", type_code="A01",
                 description="Зона с высокой видимостью", cost=1500),
        Location(code="L05", name="Аэропорт", location="Терминал 1", type_code="A04",
                 description="Зона для путешественников", cost=1300),
        Location(code="L06", name="Парк", location="Центральный парк", type_code="A05", description="Зона отдыха",
                 cost=700),
        Location(code="L07", name="Университет", location="Кампус", type_code="A02", description="Зона для студентов",
                 cost=900),
        Location(code="L08", name="Офис", location="Деловой район", type_code="A01", description="Корпоративная зона",
                 cost=1100),
        Location(code="L09", name="Пляж", location="Побережье", type_code="A05", description="Туристическая зона",
                 cost=1400),
        Location(code="L10", name="Станция", location="Железнодорожная станция", type_code="A03",
                 description="Зона для пассажиров", cost=950)
    ]
    db.session.bulk_save_objects(locations)

    customers = [
        Customer(code="C01", full_name="Алексей Федоров", address="ул. Ленина, д. 12", phone="555-1234"),
        Customer(code="C02", full_name="Ирина Николаева", address="ул. Пушкина, д. 15", phone="555-5678"),
        Customer(code="C03", full_name="Петр Васильев", address="ул. Чехова, д. 18", phone="555-9101"),
        Customer(code="C04", full_name="Марина Павлова", address="ул. Горького, д. 21", phone="555-1122"),
        Customer(code="C05", full_name="Сергей Лебедев", address="ул. Лермонтова, д. 24", phone="555-3344"),
        Customer(code="C06", full_name="Екатерина Козлова", address="ул. Тверская, д. 27", phone="555-5566"),
        Customer(code="C07", full_name="Михаил Петров", address="ул. Невская, д. 30", phone="555-7788"),
        Customer(code="C08", full_name="Юлия Симонова", address="ул. Ладожская, д. 33", phone="555-9900"),
        Customer(code="C09", full_name="Виктор Сидоров", address="ул. Волкова, д. 36", phone="555-1123"),
        Customer(code="C10", full_name="Ольга Егорова", address="ул. Жукова, д. 39", phone="555-4455")
    ]
    db.session.bulk_save_objects(customers)
    orders = [
        Order(order_date=date(2024, 1, 1), start_date=date(2024, 1, 2), end_date=date(2024, 1, 10),
              customer_code='C001', location_code='L001', service1_code='S001', service2_code='S002',
              service3_code='S003', cost=50000, payment_mark=True, employee_code='E001'),
        Order(order_date=date(2024, 1, 3), start_date=date(2024, 1, 4), end_date=date(2024, 1, 11),
              customer_code='C002', location_code='L002', service1_code='S002', service2_code='S003',
              service3_code='S004', cost=60000, payment_mark=True, employee_code='E002'),
        Order(order_date=date(2024, 1, 5), start_date=date(2024, 1, 6), end_date=date(2024, 1, 12),
              customer_code='C003', location_code='L003', service1_code='S003', service2_code='S004',
              service3_code='S005', cost=55000, payment_mark=False, employee_code='E003'),
        Order(order_date=date(2024, 1, 7), start_date=date(2024, 1, 8), end_date=date(2024, 1, 14),
              customer_code='C004', location_code='L004', service1_code='S004', service2_code='S005',
              service3_code='S001', cost=70000, payment_mark=True, employee_code='E004'),
        Order(order_date=date(2024, 1, 9), start_date=date(2024, 1, 10), end_date=date(2024, 1, 16),
              customer_code='C005', location_code='L005', service1_code='S005', service2_code='S001',
              service3_code='S002', cost=65000, payment_mark=True, employee_code='E005'),
        Order(order_date=date(2024, 1, 11), start_date=date(2024, 1, 12), end_date=date(2024, 1, 18),
              customer_code='C006', location_code='L006', service1_code='S001', service2_code='S002',
              service3_code='S003', cost=50000, payment_mark=True, employee_code='E006'),
        Order(order_date=date(2024, 1, 13), start_date=date(2024, 1, 14), end_date=date(2024, 1, 20),
              customer_code='C007', location_code='L007', service1_code='S002', service2_code='S003',
              service3_code='S004', cost=60000, payment_mark=True, employee_code='E007'),
        Order(order_date=date(2024, 1, 15), start_date=date(2024, 1, 16), end_date=date(2024, 1, 22),
              customer_code='C008', location_code='L008', service1_code='S003', service2_code='S004',
              service3_code='S005', cost=55000, payment_mark=False, employee_code='E008'),
        Order(order_date=date(2024, 1, 17), start_date=date(2024, 1, 18), end_date=date(2024, 1, 24),
              customer_code='C009', location_code='L009', service1_code='S004', service2_code='S005',
              service3_code='S001', cost=70000, payment_mark=True, employee_code='E009'),
        Order(order_date=date(2024, 1, 19), start_date=date(2024, 1, 20), end_date=date(2024, 1, 26),
              customer_code='C010', location_code='L010', service1_code='S005', service2_code='S001',
              service3_code='S002', cost=65000, payment_mark=True, employee_code='E010')
    ]
    db.session.bulk_save_objects(orders)

    db.session.commit()
    print("bla")
if __name__ == '__main__':
    with app.app_context():
        # user = db.session.query(Employee).first()
        # print(user.id, user.position_code)
        populate_db()
#
