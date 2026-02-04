# Contact Manager

## How to Run
```
python main.py
```

## Requirements
```
pip install customtkinter pillow
```

## Project Structure
```
Contact Manager/
├── main.py              # Entry point - starts the app
├── models.py            # Contact class - stores contact data
├── manager.py           # ContactManager - handles save/load/delete
├── screens/
│   ├── __init__.py      # Exports the screen classes
│   ├── contact_card.py  # ContactCard - one contact in the list
│   ├── main_screen.py   # MainScreen - contact list 
│   └── form_screen.py   # FormScreen - add/edit contact form
├── data/
│   └── contacts.json    # Saved contacts (JSON file)
└── photos/              # Contact photos folder
```
