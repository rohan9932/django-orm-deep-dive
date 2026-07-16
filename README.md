# Django ORM Deep Dive

A hands-on repo for exploring the Django ORM in depth — querysets, relations,
annotations, and API-backed examples to build a solid intuition for how
Django talks to the database.

## Structure

```
django-orm-deep-dive/
├── api/       # DRF views/serializers used to exercise ORM queries over HTTP
├── orm/       # Core Django app — models and ORM experiments
├── manage.py
├── requirements.txt
└── db.sqlite3
```

## Setup

```bash
git clone https://github.com/rohan9932/django-orm-deep-dive.git
cd django-orm-deep-dive
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## What this covers

- Queryset basics: filtering, chaining, `Q` objects
- Relations: `ForeignKey`, `OneToOne`, `ManyToMany` and related lookups
- Annotations and aggregation (`annotate`, `aggregate`, `F` expressions)
- `select_related` / `prefetch_related` and query optimization
- Exposing ORM queries through a small DRF API for hands-on testing

## Notes

This is a learning/practice repo — not a production project.
