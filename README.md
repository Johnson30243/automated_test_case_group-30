# Automated Test Case Generation System — Version 4.0

A desktop academic prototype built with Python and Tkinter. It brings four testing modules together in one application with a refreshed navy-and-teal interface.

## Modules

1. **Arithmetic testing** — accepts a restricted arithmetic expression using `x` and `y`; supports `+`, `-`, `*`, `/`, `%`, `**`, parentheses and unary signs. Generates seven representative test inputs and reports expected/actual results.
2. **User login validation** — manual login check plus seven generated scenarios, including valid credentials, wrong password, unknown username and empty fields.
3. **Student grading** — manual score check plus 14 generated scenarios covering grade bands, boundaries, decimals, invalid range, text and empty input.
4. **Age validation** — manual age check plus 10 generated scenarios covering eligibility boundary, underage, invalid ranges, decimal, text and empty input.

Each module displays test IDs, scenarios, expected results, actual results and PASS/FAIL status. Each module can export its results to a separate CSV report.

## Requirements

- Windows 10/11
- Python 3.9 or later
- Tkinter (included with most standard Windows Python installations)
- No third-party packages required

## Run in VS Code

1. Extract the ZIP archive to a folder, for example `AUTOMATED_TEST_V4`.
2. Open VS Code.
3. Choose **File → Open Folder** and select the extracted `AUTOMATED_TEST_V4` folder.
4. Open **Terminal → New Terminal**.
5. Run:

```powershell
py main.py
```

You can also double-click `run.bat` on Windows.

## Demonstration login account

- Username: `student`
- Password: `DemoPass123!`

These are fictional demonstration credentials. The login module checks a local function only; it does not connect to a database, web server or real account. Do not use personal or real account credentials.

## Student grading scale used in this prototype

- A: 70–100
- B: 60–69
- C: 50–59
- D: 45–49
- E: 40–44
- F: 0–39
- Scores below 0 or above 100 are invalid.

Confirm that these bands match the current official departmental grading policy before presenting the system as representing the department's rules.

## Age validation rule

The demonstration rule accepts whole-number ages from 0 through 120. Ages 18 and above are labelled `ELIGIBLE`; ages 0–17 are labelled `NOT ELIGIBLE`. Negative ages, ages above 120, decimal values, text and blank input are handled as invalid/validation errors. This is a configurable example rule, not a legal determination of eligibility for any real service.

## Files

- `main.py` — main Tkinter application and CSV export functions
- `safe_expression.py` — restricted arithmetic expression parser/evaluator
- `test_generator.py`, `test_runner.py` — arithmetic test generation and execution
- `login_auth.py`, `login_test_generator.py`, `login_test_runner.py` — demonstration login module
- `student_grading.py` — grading logic and generated grading test cases
- `age_validation.py` — age validation logic and generated age test cases
- `smoke_test.py` — command-line checks for all four test modules
- `run.bat` — Windows launch helper

## Academic scope and limitations

This is a teaching/research prototype for simple functions. The login credentials are hard-coded demonstration values and are not suitable for real authentication. The arithmetic expected-result oracle uses a separate validated calculation path, but it is not a formal independent oracle. The test cases are predefined representative scenarios, not a guarantee of exhaustive testing or automatic testing of arbitrary source-code files. Record the actual test results and explain these limitations in the project report.
