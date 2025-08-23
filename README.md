# Django CRUD API

Prosty projekt REST API oparty na Django, implementujący operacje Create, Read, Update i Delete (CRUD) do zarządzania elementami.

## 🚀 Funkcjonalności

* Autoryzacja użytkowników z wykorzystaniem JWT.
* Operacje CRUD dla zarządzania elementami.
* Testy automatyczne przy użyciu `pytest` i `pytest-django`.
* Baza danych SQLite do developmentu i testów.

## 🛠️ Technologie

* Django 5.2.5
* Django REST Framework
* SQLite
* pytest
* pytest-django

## 📦 Instalacja

1. Sklonuj repozytorium:

```bash
git clone https://github.com/ciborowskigrzegorz-bit/django-crud-api.git
cd django-crud-api
```

2. Utwórz i aktywuj wirtualne środowisko:

```bash
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. Zainstaluj zależności:

```bash
pip install -r requirements.txt
```

4. Wykonaj migracje:

```bash
python manage.py migrate
```

5. Utwórz superużytkownika:

```bash
python manage.py createsuperuser
```

6. Uruchom serwer deweloperski:

```bash
python manage.py runserver
```

API będzie dostępne pod adresem `http://127.0.0.1:8000/`.

## 🧪 Uruchamianie testów

Aby uruchomić testy automatyczne:

```bash
pytest
```

Testy znajdują się w katalogu `api/tests/`.

## 📄 Endpointy API

* `POST /api/items/` – utwórz nowy element.
* `GET /api/items/` – pobierz listę elementów.
* `GET /api/items/{id}/` – pobierz element po ID.
* `PUT /api/items/{id}/` – zaktualizuj element po ID.
* `DELETE /api/items/{id}/` – usuń element po ID.

Wszystkie endpointy wymagają autoryzacji.

## ✍️ Autor

Grzegorz Ciborowski  
🔗 [LinkedIn](https://www.linkedin.com/in/grzesiek-ciborowski-46854b185/)  
📦 [GitHub](https://github.com/ciborowskigrzegorz-bit)

---

## 📄 Licencja

Projekt udostępniony na licencji MIT.
