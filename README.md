# 🐍 Django CRUD API

Minimalistyczny projekt backendowy oparty na Django, Django REST Framework oraz PostgreSQL. Gotowy do uruchomienia w kontenerze Docker – zawiera testy jednostkowe oraz REST API do zarządzania zadaniami (Tasks).

## 📦 Technologie

- Python 3.11  
- Django 4.2  
- Django REST Framework  
- PostgreSQL  
- Docker + docker-compose  
- pytest (testy jednostkowe)

---

## 🚀 Uruchomienie projektu

### 1. Klonowanie repozytorium

```bash
git clone https://github.com/ciborowskigrzegorz-bit/django-crud-api.git
cd django-crud-api/backend
```

### 2. Uruchomienie przez Docker

```bash
docker-compose up --build
```

Aplikacja powinna działać pod adresem:

```
http://localhost:8000/api/tasks/
```

---

## 📚 Endpointy API

| Metoda | Endpoint           | Opis                        |
|--------|--------------------|-----------------------------|
| GET    | `/api/tasks/`      | Lista wszystkich zadań     |
| POST   | `/api/tasks/`      | Dodanie nowego zadania     |
| GET    | `/api/tasks/{id}/` | Pobranie konkretnego zadania |
| PUT    | `/api/tasks/{id}/` | Aktualizacja zadania       |
| DELETE | `/api/tasks/{id}/` | Usunięcie zadania          |

---

## ✅ Testowanie

Aby uruchomić testy jednostkowe:

```bash
docker-compose run web python manage.py test
```

---

## 📁 Struktura projektu

```
backend/
├── manage.py
├── core/          ← Ustawienia projektu Django
├── tasks/         ← Aplikacja z CRUD
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── tests.py
├── requirements.txt
├── Dockerfile
└── docker-compose.yml
```

---

## ✍️ Autor

Grzegorz Ciborowski  
🔗 [LinkedIn](https://www.linkedin.com/in/grzesiek-ciborowski-46854b185/)  
📦 [GitHub](https://github.com/ciborowskigrzegorz-bit)

---

## 📄 Licencja

Projekt udostępniony na licencji MIT.
