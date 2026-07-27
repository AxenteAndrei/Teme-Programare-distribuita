# Curs Programare Distribuită — Python

Soluții la temele de laborator și proiectele realizate în cadrul cursului de
**Programare Distribuită**, folosind **Python 3.12**.

Repo-ul conține exercițiile pe laboratoare (L1–L9), care acoperă progresiv
bazele limbajului Python, plus un proiect mai amplu cu interfață grafică.

---

## Structură

### Laboratoare

| Lab | Temă | Exemple |
|-----|------|---------|
| **L1** | Bazele limbajului, input/output, condiții | conversie °C↔°F, calcul dobândă, par/impar, verificare număr prim |
| **L2** | Bucle și logică | sistem de notare, multipli, ghicirea numărului, numere impare |
| **L3** | Funcții | distanța dintre puncte, factorial, verificare palindrom |
| **L4** | Liste și tupluri | maxim/minim, eliminare duplicate, căutare în tuplu |
| **L5** | Dicționare și procesare | index inversat, sumă perechi unice, frecvența cuvintelor |
| **L6** | Procesare de șiruri | palindrom, inversare cuvinte, run-length encoding |
| **L7** | Lucrul cu fișiere | numărare cuvinte, filtrare linii, inversare linii |
| **L8** | Module și pachete | pachet `geometry` (cerc, dreptunghi), operații matematice |
| **L9** | Programare orientată pe obiecte | cont bancar, manager de angajați, forme geometrice |

### Proiect — Contact Manager

Aplicație desktop de gestiune a contactelor, cu interfață grafică
(**customtkinter**), structurată pe ecrane și cu persistență în JSON.

- Adăugare / editare / ștergere contacte
- Fotografie de profil pentru fiecare contact
- Salvare automată în `data/contacts.json`
- Arhitectură pe module: `models.py`, `manager.py`, `screens/`

Detalii și instrucțiuni de rulare în
[`Proiect Contact Manager/README.md`](Proiect%20Contact%20Manager/README.md).

---

## Rulare

Fiecare exercițiu este un script independent:

```bash
python L1/verificareNumarPrim.py
```

Pentru proiectul Contact Manager:

```bash
cd "Proiect Contact Manager"
pip install customtkinter pillow
python main.py
```

---

## Tehnologii

- **Python 3.12**
- Bibliotecă standard (fișiere, colecții, OOP, module)
- **customtkinter** + **Pillow** (proiectul Contact Manager)
