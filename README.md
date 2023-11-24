# HBnB — Phase 1: Console & Static Front End

**AirBnB Clone · Phase 1 of 4**

This project is the foundation of the ALX **HBnB** (Holberton Bed and Breakfast) capstone. Covers building the backend domain model in Python, persist data as JSON, exercise everything through a custom command interpreter, and prototype the listing UI with pure HTML and CSS—no web framework yet.

| Phase | Project | Focus |
|-------|------------|-------|
| **1 — current phase** | `AirBnB_clone` | Python OOP, console, JSON storage, static HTML/CSS |
| 2 | [AirBnB_clone_v2](https://github.com/mgn-dev/AirBnB_clone_v2) | Flask routes and Jinja2 templates |
| 3 | [AirBnB_clone_v3](https://github.com/mgn-dev/AirBnB_clone_v3) | REST API and CRUD endpoints |
| 4 | [AirBnB_clone_v4](https://github.com/mgn-dev/AirBnB_clone_v4) | MySQL, SQLAlchemy, Swagger, dynamic JS, auth |

---

## Skills covered


- Design a reusable **base model** with UUID identity, timestamps, and dictionary serialization
- Apply **object-oriented inheritance** to model real-world entities (users, places, cities, amenities, reviews)
- Build a **command interpreter** (`cmd` module) with primary and advanced syntax
- Persist application state with **JSON serialization** via a dedicated storage engine
- Write **unit tests** and enforce **PEP 8** style across model modules
- Build a **static web front end** that mirrors the AirBnB listing layout using semantic HTML and layered CSS

---

## Project Structure

```
AirBnB_clone/
├── console.py              # HBnB command interpreter entry point
├── models/
│   ├── base_model.py       # Parent class: id, created_at, updated_at, to_dict()
│   ├── user.py             # User (email, password, first/last name)
│   ├── state.py            # State (name)
│   ├── city.py             # City (name, state_id)
│   ├── place.py            # Place (location, pricing, amenities)
│   ├── amenity.py          # Amenity (name)
│   ├── review.py           # Review (text, place_id, user_id)
│   ├── __init__.py         # Exposes storage singleton and all model classes
│   └── engine/
│       └── file_storage.py # JSON read/write, in-memory __objects registry
├── tests/
│   └── test_models/        # Unit tests for every model and FileStorage
└── web_static/
    ├── 0-index.html … 8-index.html   # Progressive HTML milestones
    └── styles/                       # Matching CSS layers (common, header, footer, filters, places)
```

---

## Domain Model

All entity classes inherit from `BaseModel`, which assigns a UUID, tracks `created_at` / `updated_at`, registers the instance with storage, and exposes `to_dict()` for serialization.

| Class | Key Attributes | Relationships |
|-------|----------------|---------------|
| `User` | email, password, first_name, last_name | Owns places and reviews |
| `State` | name | Has many cities |
| `City` | name, state_id | Has many places |
| `Place` | name, description, rooms, bathrooms, guests, price, lat/lng, amenity_ids | Belongs to city and user |
| `Amenity` | name | Referenced by places |
| `Review` | text, place_id, user_id | Links users to places |

`FileStorage` keeps objects in `__objects` keyed as `ClassName.id`, writes them to `file.json`, and reloads on startup.

---

## The Console (Command Interpreter)

Run the interpreter interactively:

```bash
./console.py
```

The console displays the `(hbnb)` prompt.

### Primary Commands

| Command | Syntax | Description |
|---------|--------|-------------|
| `create` | `create <ClassName>` | Instantiate a model, save to JSON, print the id |
| `show` | `show <ClassName> <id>` | Print the string representation of an instance |
| `destroy` | `destroy <ClassName> <id>` | Delete an instance and persist the change |
| `all` | `all [ClassName]` | List all instances, optionally filtered by class |
| `update` | `update <ClassName> <id> <attr> <value>` | Set an attribute and save |
| `quit` / `EOF` | — | Exit the interpreter |

### Advanced Syntax

Models also support dot-notation calls:

```
User.all()
User.count()
User.show("<id>")
User.destroy("<id>")
User.update("<id>", "name", "value")
User.update("<id>", {"name": "value"})
```

### Example Session

```
(hbnb) create User
a1b2c3d4-e5f6-7890-abcd-ef1234567890
(hbnb) update User a1b2c3d4-e5f6-7890-abcd-ef1234567890 email "guest@hbnb.io"
(hbnb) update User a1b2c3d4-e5f6-7890-abcd-ef1234567890 password "secret"
(hbnb) create Place
b2c3d4e5-f6a7-8901-bcde-f12345678901
(hbnb) all Place
(hbnb) quit
```

Non-interactive usage:

```bash
echo "all User" | ./console.py
```

---

## Static Front End (`web_static/`)

The `web_static` directory implements the AirBnB-style listing page in incremental tasks:

| Task | Files | Skill |
|------|-------|-------|
| 0 | `0-index.html` | Minimal valid HTML5 skeleton |
| 1 | `1-index.html` | Head, body, title |
| 2 | `2-index.html`, `styles/2-common.css` | Global box model and typography |
| 3 | `3-index.html`, header/footer CSS | Layout regions |
| 4 | `4-index.html`, filters CSS | Search filter bar |
| 5–8 | `5-index.html` … `8-index.html` | Place cards, responsive listing grid |

Open any `N-index.html` in a browser to preview that milestone. Styles are split into composable stylesheets (`3-common.css`, `6-filters.css`, `8-places.css`, etc.) so each layer builds on the previous one.

---

## Testing

Run the model test suite:

```bash
python3 -m unittest discover tests
```

Tests cover PEP 8 compliance, docstrings, instantiation, and `FileStorage` round-trips.

---

## Environment

- **Python** 3.x
- **OS** Linux (Ubuntu) recommended
- No external Python packages required for the console and models

---

## What Comes Next

In **[Phase 2](https://github.com/mgn-dev/AirBnB_clone_v2)** Phase 2 adds static-only delivery with **Flask**: route handlers, query parameters, and **Jinja2 templates** that render data from the same model layer introduced in Phase 1.

---

## License

Public domain.
