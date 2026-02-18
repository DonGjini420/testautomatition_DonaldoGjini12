# Söderbröder — Testautomation (Loan Lab)

Detta repository innehåller ett komplett testautomationsprojekt för Söderbröder Loan Lab.
Det inkluderar API-tester (Pytest), UI Page Objects (Playwright) och ett k6 load-test för prestanda.

## Snabböversikt
- Ramverk: Pytest + Playwright + k6
- Språk: Python 3.11+ (testat med 3.14)
- Repo: https://github.com/DonGjini420/testautomatition_DonaldoGjini12

## Projektstruktur

```
testautomatition_DonaldoGjini/
├── src/
│   ├── clients/loan_api_client.py           # API-klient (create/get/update/delete)
│   ├── pages/home_page.py                   # HomePage Page Object
│   ├── pages/application_form_page.py       # ApplicationFormPage Page Object
│   └── helpers/__init__.py                  # Testdata, API-nycklar, Faker
├── tests/
│   ├── conftest.py                          # Playwright fixtures
│   ├── test_api.py                          # 13 API-tester
│   └── test_ui.py                           # 2 POM-tester
├── k6/
│   └── load_test.js                         # k6 load-test
├── data/testdata.csv                        # CSV testdata (exempelrader)
├── INSTRUKTIONER.md                         # Körinstruktioner
├── TEST_RESULTS_SUMMARY.md                  # Sammanfattning av körningar
├── GODKÄNT_RAPPORT.md                       # Slutgiltig inlämningsrapport
├── k6_run.bat                               # Hjälpskript för k6
├── pytest.ini
├── requirements.txt
└── README.md
```

## Förutsättningar
- Python 3.11+ installerat
- Playwright (installera med `pip install -r requirements.txt` och kör `playwright install`)
- k6 (finns inkluderat i projektet under `C:\Users\User\k6\...` i denna miljö). Alternativt installera via Chocolatey eller ladda ner från https://k6.io

## Installera beroenden

```powershell
python -m pip install -r requirements.txt
python -m playwright install
```

## Kör tester

- Kör alla Pytest-tester:
	```powershell
	python -m pytest -v
	```

- Kör enbart API-tester (snabbare):
	```powershell
	python -m pytest tests/test_api.py -v
	```

## Kör k6 load-test

Det finns ett hjälpskript för att köra k6 enkelt (använder lokalt nedladdad k6):

```powershell
.\k6_run.bat k6/load_test.js
```

eller direkt (om du har k6 i PATH):

```powershell
& "C:\Users\User\k6\k6-v0.50.0-windows-amd64\k6.exe" run k6/load_test.js
```

## Viktiga anmärkningar
- API-nycklar och testpersonnummer finns i `src/helpers/__init__.py`.
- Testpersonnummer är officiella svenska testnummer och används för GDPR-kompatibilitet.
- k6-checks och thresholds är konfigurerade för att vara realistiska för testmiljön.

## Vad att lämna in
- Projektmappen (hela repo)
- PowerPoint-presentation: `Git_Uppgift_Soderbröder_Loan_Lab.pptx`
- Slutgiltig rapport: `GODKÄNT_RAPPORT.md`

## Kontakta
Vid frågor om körning eller inlämning — skriv en kommentar i repot eller kontakta mig.

Lycka till — du är redo att lämna in! 🎉

