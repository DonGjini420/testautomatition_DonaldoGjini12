# Söderbröder Loan Lab - Test Automation Framework

Automatiserat testramverk för Söderbröder Loan Lab API och webapplikation.

## Installation

```bash
pip install -r requirements.txt
playwright install chromium
```

## Köra Tester

```bash
# Alla tester
pytest -v

# Endast API-tester
pytest tests/test_api.py -v

# Endast UI-tester
pytest tests/test_ui.py -v

# Prestandatest
k6 run k6/load_test.js
```

## Struktur

- `src/pages/` - Page Object Model för UI-tester
- `src/clients/` - API-klient
- `src/helpers/` - Testdata och fixtures
- `tests/` - Automatiska tester
- `k6/` - Prestandatester
- `data/` - Testdata CSV
