# Curs Programare Distribuita — Python

Solutii la temele de laborator si proiectele realizate in cadrul cursului de
**Programare Distribuita**, folosind **Python 3.12**.

---

## Structura

### Laboratoare

| Lab | Tema | Exemple |
|-----|------|---------|
| **L1** | Bazele limbajului, input/output, conditii | conversie C<->F, calcul dobanda, par/impar, verificare numar prim |
| **L2** | Bucle si logica | sistem de notare, multipli, ghicirea numarului, numere impare |
| **L3** | Functii | distanta dintre puncte, factorial, verificare palindrom |
| **L4** | Liste si tupluri | maxim/minim, eliminare duplicate, cautare in tuplu |
| **L5** | Dictionare si procesare | index inversat, suma perechi unice, frecventa cuvintelor |
| **L6** | Procesare de siruri | palindrom, inversare cuvinte, run-length encoding |
| **L7** | Lucrul cu fisiere | numarare cuvinte, filtrare linii, inversare linii |
| **L8** | Module si pachete | pachet `geometry` (cerc, dreptunghi), operatii matematice |
| **L9** | Programare orientata pe obiecte | cont bancar, manager de angajati, forme geometrice |

### Proiect — Contact Manager

Aplicatie desktop de gestiune a contactelor, cu interfata grafica
(**customtkinter**), structurata pe ecrane si cu persistenta in JSON.

- Adaugare / editare / stergere contacte
- Fotografie de profil pentru fiecare contact
- Salvare automata in `data/contacts.json`
- Arhitectura pe module: `models.py`, `manager.py`, `screens/`

---

## Rulare

Fiecare exercitiu este un script independent:

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
- Biblioteca standard (fisiere, colectii, OOP, module)
- **customtkinter** + **Pillow** (proiectul Contact Manager)
