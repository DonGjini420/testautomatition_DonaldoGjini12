# 🚀 Hur man kör Uppgiften

## 1️⃣ Pytest Tests (13 API + 2 UI)

```bash
python -m pytest -v
```

Eller bara API-tester (snabbare):
```bash
python -m pytest tests/test_api.py -v
```

**Förväntat resultat:** ✅ 15/15 tests passed

---

## 2️⃣ k6 Load Test (Prestanda)

**Alternativ A - Batch Script (rekommenderat):**
```bash
.\k6_run.bat k6/load_test.js
```

**Alternativ B - Direkt kommando:**
```bash
& "C:\Users\User\k6\k6-v0.50.0-windows-amd64\k6.exe" run k6/load_test.js
```

**Förväntat resultat:**
- ✅ ~400+ HTTP requests genomförda
- ✅ Genomsnittlig svarstid < 400ms
- ✅ Prestanda checksningar passar

---

## 3️⃣ Git Repository

Visa commits:
```bash
git log --oneline -5
```

Visa branches:
```bash
git branch -a
```

GitHub: https://github.com/DonGjini420/testautomatition_DonaldoGjini12

---

## 📊 Projektöversikt

| Komponent | Kommando | Status |
|-----------|----------|--------|
| API Tests | `pytest tests/test_api.py -v` | ✅ 13/13 |
| UI Tests | `pytest tests/test_ui.py -v` | ✅ 2/2 |
| Load Test | `.\k6_run.bat k6/load_test.js` | ✅ Körbar |
| Git | `git log --oneline` | ✅ 6 commits |
| GitHub | Link | ✅ Pushad |

---

## 📁 Viktiga Filer

- `src/clients/loan_api_client.py` - API klient
- `src/pages/home_page.py` - HomePage Page Object
- `src/pages/application_form_page.py` - ApplicationFormPage Page Object
- `src/helpers/__init__.py` - Testdata & API-nycklar
- `tests/test_api.py` - API tests
- `tests/test_ui.py` - UI tests
- `k6/load_test.js` - Load test script
- `k6_run.bat` - k6 runner script
- `pytest.ini` - Pytest config
- `GODKÄNT_RAPPORT.md` - Godkännande rapport

---

## ✅ Klar för Inlämning!

Allt fungerar! Du kan nu lämna in uppgiften. 🎉

Se `GODKÄNT_RAPPORT.md` för detaljerad rapport.
