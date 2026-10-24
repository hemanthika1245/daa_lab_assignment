# Campus Lost and Found Matcher (RGUKT Ongole DAA Project 5)

## Run
1. Install Python 3.10 or later.
2. Open this folder in VS Code.
3. Open Terminal > New Terminal in VS Code. Make sure the terminal is in the `daa_project_assignment` folder (the folder containing `common.py`).
4. Run:
   - Windows: `py 05_lost_found/app.py` (or `python 05_lost_found/app.py`)
   - macOS/Linux: `python3 05_lost_found/app.py`
5. Open the URL printed by the terminal, normally http://127.0.0.1:8000.
6. Keep the terminal open while using the app. Press Ctrl+C in that terminal to stop it.

No extra pip packages are required. Reports are saved in `05_lost_found/data.json`.

## Try the PDF worked example
- Add Lost / Bottle / Blue steel bottle / Library / 2026-10-08.
- Add Found with the same category, description, location, and date.
- Enter report ID 1 under Suggest matches. Report 2 should score 9 (category 3, shared words 3, location 2, nearby date 1).
- Search `bottle`, then test manual status changes.

Use fictional items only and no personal contact details. A suggested match is not proof of ownership. This is a local classroom prototype, not a shared campus service.

## Required assignment work
The PDF asks you to add at least one extension, document at least six tests (input, expected result, actual result), write a short report, submit complete source and instructions, and record a 3-minute demo. Explain which code is reference code, your changes, and any AI assistance. Understand the code before submitting.
