"""Version 4.0 desktop GUI: arithmetic, login, grading and age test modules."""
import csv
import tkinter as tk
from tkinter import ttk, messagebox, filedialog

from safe_expression import parse_expression, ExpressionError
from test_runner import run_tests
from login_auth import authenticate
from login_test_runner import run_login_tests
from student_grading import grade_score, run_grading_tests
from age_validation import validate_age, run_age_tests

# Modern, calm navy-and-teal theme using only Python's built-in Tkinter.
BG = "#F3F6FB"
CARD = "#FFFFFF"
NAVY = "#14243A"
NAVY_2 = "#203A5B"
TEAL = "#087E8B"
TEXT = "#1F2D3D"
MUTED = "#68778D"
GREEN = "#16845B"
RED = "#C43D4B"
BORDER = "#DCE4EF"

class TestGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Automated Test Case Generation System Group 30 | Version 4.0")
        self.root.geometry("1320x850")
        self.root.minsize(1000, 680)
        self.root.configure(bg=BG)
        self.results = {"arithmetic": [], "login": [], "grading": [], "age": []}
        self._configure_style()
        self._build_header()
        self._build_tabs()
        self._build_footer()

    def _configure_style(self):
        style = ttk.Style()
        try: style.theme_use("clam")
        except tk.TclError: pass
        style.configure("TFrame", background=BG)
        style.configure("Card.TFrame", background=CARD)
        style.configure("TLabel", background=BG, foreground=TEXT, font=("Segoe UI", 10))
        style.configure("Card.TLabel", background=CARD, foreground=TEXT, font=("Segoe UI", 10))
        style.configure("Muted.TLabel", background=CARD, foreground=MUTED, font=("Segoe UI", 9))
        style.configure("Title.TLabel", background=NAVY, foreground="white", font=("Segoe UI", 19, "bold"))
        style.configure("Subtitle.TLabel", background=NAVY, foreground="#D6E3F2", font=("Segoe UI", 10))
        style.configure("Section.TLabel", background=CARD, foreground=NAVY, font=("Segoe UI", 13, "bold"))
        style.configure("TButton", font=("Segoe UI", 9, "bold"), padding=(13, 8), background=TEAL, foreground="white", borderwidth=0)
        style.map("TButton", background=[("active", "#066A75"), ("disabled", "#AAB8C8")], foreground=[("disabled", "#F5F7FA")])
        style.configure("Secondary.TButton", background=NAVY_2, foreground="white")
        style.map("Secondary.TButton", background=[("active", NAVY)])
        style.configure("TEntry", padding=7, fieldbackground="white", foreground=TEXT)
        style.configure("TNotebook", background=BG, borderwidth=0, tabmargins=(3, 5, 3, 0))
        style.configure("TNotebook.Tab", background="#E5ECF5", foreground=NAVY, padding=(18, 11), font=("Segoe UI", 10, "bold"))
        style.map("TNotebook.Tab", background=[("selected", CARD)], foreground=[("selected", TEAL)])
        style.configure("Treeview", background="white", fieldbackground="white", foreground=TEXT, rowheight=30, font=("Segoe UI", 9), bordercolor=BORDER)
        style.configure("Treeview.Heading", background="#EAF0F7", foreground=NAVY, font=("Segoe UI", 9, "bold"), padding=8)
        style.map("Treeview", background=[("selected", "#D8EEF0")], foreground=[("selected", NAVY)])
        style.configure("TLabelframe", background=CARD, bordercolor=BORDER)
        style.configure("TLabelframe.Label", background=CARD, foreground=NAVY, font=("Segoe UI", 10, "bold"))

    def _build_header(self):
        header = tk.Frame(self.root, bg=NAVY, padx=26, pady=19)
        header.pack(fill="x")
        tk.Label(header, text="AUTOMATED TEST CASE GENERATION SYSTEM ", bg=NAVY, fg="white", font=("Segoe UI", 19, "bold")).pack(anchor="w")
        tk.Label(header, text="Generate  •  Execute  •  Evaluate  |  Four practical testing modules", bg=NAVY, fg="#D6E3F2", font=("Segoe UI", 10)).pack(anchor="w", pady=(5, 0))
        tk.Label(header, text="GROUP 30", bg=TEAL, fg="white", font=("Segoe UI", 9, "bold"), padx=12, pady=5).place(relx=1.0, rely=0.15, anchor="ne")

    def _build_tabs(self):
        outer = ttk.Frame(self.root, padding=(18, 12, 18, 8))
        outer.pack(fill="both", expand=True)
        self.tabs = ttk.Notebook(outer)
        self.tabs.pack(fill="both", expand=True)
        self.arithmetic_tab = ttk.Frame(self.tabs, padding=14)
        self.login_tab = ttk.Frame(self.tabs, padding=14)
        self.grading_tab = ttk.Frame(self.tabs, padding=14)
        self.age_tab = ttk.Frame(self.tabs, padding=14)
        self.tabs.add(self.arithmetic_tab, text="  Arithmetic Testing  ")
        self.tabs.add(self.login_tab, text="  User Login Testing  ")
        self.tabs.add(self.grading_tab, text="  Student Grading  ")
        self.tabs.add(self.age_tab, text="  Age Validation  ")
        self._build_arithmetic_tab()
        self._build_login_tab()
        self._build_grading_tab()
        self._build_age_tab()

    def _card(self, parent, padding=14):
        card = ttk.Frame(parent, style="Card.TFrame", padding=padding)
        card.pack(fill="x", pady=(0, 11))
        return card

    def _intro(self, parent, title, description):
        card = self._card(parent, 15)
        ttk.Label(card, text=title, style="Section.TLabel").pack(anchor="w")
        ttk.Label(card, text=description, style="Muted.TLabel", wraplength=1100).pack(anchor="w", pady=(4, 0))
        return card

    def _table(self, parent, columns, headings, widths):
        holder = ttk.Frame(parent, style="Card.TFrame")
        holder.pack(fill="both", expand=True)
        table = ttk.Treeview(holder, columns=columns, show="headings", height=11)
        ybar = ttk.Scrollbar(holder, orient="vertical", command=table.yview)
        xbar = ttk.Scrollbar(holder, orient="horizontal", command=table.xview)
        table.configure(yscrollcommand=ybar.set, xscrollcommand=xbar.set)
        for col in columns:
            table.heading(col, text=headings[col])
            table.column(col, width=widths[col], minwidth=75, anchor="center", stretch=True)
        table.grid(row=0, column=0, sticky="nsew")
        ybar.grid(row=0, column=1, sticky="ns")
        xbar.grid(row=1, column=0, sticky="ew")
        holder.rowconfigure(0, weight=1)
        holder.columnconfigure(0, weight=1)
        table.tag_configure("PASS", foreground=GREEN)
        table.tag_configure("FAIL", foreground=RED)
        return table

    def _actions(self, parent, run_command, export_command, run_text="Generate and Run Tests", export_text="Export CSV Report"):
        bar = ttk.Frame(parent, style="Card.TFrame")
        bar.pack(fill="x", pady=(0, 9))
        ttk.Button(bar, text=run_text, command=run_command).pack(side="left", padx=(0, 8))
        ttk.Button(bar, text=export_text, style="Secondary.TButton", command=export_command).pack(side="left")

    def _summary(self, parent, initial):
        label = tk.Label(parent, text=initial, bg="#EAF3F6", fg=NAVY, anchor="w", padx=13, pady=10, font=("Segoe UI", 9, "bold"))
        label.pack(fill="x", pady=(9, 0))
        return label

    def _build_arithmetic_tab(self):
        tab = self.arithmetic_tab
        self._intro(tab, "Arithmetic expression testing", "Enter a simple function using x and y. The system generates representative inputs, executes the expression and compares expected and actual results.")
        form = self._card(tab)
        ttk.Label(form, text="Function name", style="Card.TLabel").grid(row=0, column=0, sticky="w", padx=(0, 8), pady=5)
        self.function_name = tk.StringVar(value="MyFunction")
        ttk.Entry(form, textvariable=self.function_name, width=22).grid(row=0, column=1, sticky="w", padx=(0, 18), pady=5)
        ttk.Label(form, text="Expression", style="Card.TLabel").grid(row=0, column=2, sticky="w", padx=(0, 8), pady=5)
        self.expression = tk.StringVar(value="x + y")
        ttk.Entry(form, textvariable=self.expression).grid(row=0, column=3, sticky="ew", pady=5)
        form.columnconfigure(3, weight=1)
        ttk.Label(form, text="Operators: +  −  *  /  %  **     Example: (x * y) + 5", style="Muted.TLabel").grid(row=1, column=0, columnspan=4, sticky="w", pady=(5, 0))
        self._actions(tab, self.execute_arithmetic, lambda: self.export("arithmetic", ["id", "input", "expected", "actual", "status"], "arithmetic_test_report.csv"))
        self.arithmetic_table = self._table(tab, ("id", "input", "expected", "actual", "status"), {"id":"Test Case ID", "input":"Input Values", "expected":"Expected Result", "actual":"Actual Result", "status":"Status"}, {"id":210,"input":180,"expected":210,"actual":260,"status":100})
        self.arithmetic_summary = self._summary(tab, "Ready. Enter an expression and generate test cases.")

    def _build_login_tab(self):
        tab = self.login_tab
        self._intro(tab, "User login validation", "Test successful login, incorrect credentials, unknown users and missing input fields. This is a local demonstration account, not a production authentication service.")
        form = self._card(tab)
        ttk.Label(form, text="Username", style="Card.TLabel").grid(row=0, column=0, sticky="w", padx=5, pady=6)
        self.login_username = tk.StringVar()
        ttk.Entry(form, textvariable=self.login_username, width=28).grid(row=0, column=1, sticky="w", padx=5, pady=6)
        ttk.Label(form, text="Password", style="Card.TLabel").grid(row=1, column=0, sticky="w", padx=5, pady=6)
        self.login_password = tk.StringVar()
        self.password_entry = ttk.Entry(form, textvariable=self.login_password, width=28, show="*")
        self.password_entry.grid(row=1, column=1, sticky="w", padx=5, pady=6)
        self.show_password = tk.BooleanVar(value=False)
        ttk.Checkbutton(form, text="Show password", variable=self.show_password, command=lambda: self.password_entry.configure(show="" if self.show_password.get() else "*")).grid(row=1, column=2, sticky="w", padx=8)
        ttk.Button(form, text="Check Login", command=self.check_manual_login).grid(row=0, column=2, sticky="w", padx=8)
        self.login_message = ttk.Label(form, text="Enter the demonstration credentials.", style="Muted.TLabel")
        self.login_message.grid(row=2, column=0, columnspan=4, sticky="w", padx=5, pady=(7, 0))
        ttk.Label(form, text="Demo account: student  |  DemoPass123!", style="Muted.TLabel").grid(row=3, column=0, columnspan=4, sticky="w", padx=5, pady=(7, 0))
        self._actions(tab, self.execute_login, lambda: self.export("login", ["id", "scenario", "username", "expected", "actual", "status"], "login_test_report.csv"), "Generate and Run Login Tests", "Export Login CSV")
        self.login_table = self._table(tab, ("id", "scenario", "username", "expected", "actual", "status"), {"id":"Test ID", "scenario":"Test Scenario", "username":"Username", "expected":"Expected Result", "actual":"Actual Result", "status":"Status"}, {"id":85,"scenario":250,"username":135,"expected":165,"actual":165,"status":85})
        self.login_summary = self._summary(tab, "Generate login test cases to see the results.")

    def _build_grading_tab(self):
        tab = self.grading_tab
        self._intro(tab, "Student grading test module", "Validate student marks and check that the correct grade is assigned. The configured scale is A: 70–100, B: 60–69, C: 50–59, D: 45–49, E: 40–44 and F: 0–39.")
        form = self._card(tab)
        ttk.Label(form, text="Try one score (0–100)", style="Card.TLabel").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.grade_input = tk.StringVar()
        ttk.Entry(form, textvariable=self.grade_input, width=18).grid(row=0, column=1, sticky="w", padx=5, pady=5)
        ttk.Button(form, text="Check Grade", command=self.check_manual_grade).grid(row=0, column=2, sticky="w", padx=8, pady=5)
        self.grade_message = ttk.Label(form, text="Enter a score to check its grade.", style="Muted.TLabel")
        self.grade_message.grid(row=1, column=0, columnspan=4, sticky="w", padx=5, pady=5)
        self._actions(tab, self.execute_grading, lambda: self.export("grading", ["id", "scenario", "input", "expected", "actual", "status"], "student_grading_test_report.csv"), "Generate and Run Grading Tests", "Export Grading CSV")
        self.grading_table = self._table(tab, ("id", "scenario", "input", "expected", "actual", "status"), {"id":"Test ID", "scenario":"Test Scenario", "input":"Score", "expected":"Expected Grade", "actual":"Actual Grade", "status":"Status"}, {"id":85,"scenario":230,"input":110,"expected":145,"actual":145,"status":85})
        self.grading_summary = self._summary(tab, "Generate grading test cases to see the results.")

    def _build_age_tab(self):
        tab = self.age_tab
        self._intro(tab, "Age validation test module", "Check age inputs against a configurable demonstration rule: whole-number ages from 0 to 120 are accepted, and people aged 18 or above are marked eligible.")
        form = self._card(tab)
        ttk.Label(form, text="Try an age in whole years", style="Card.TLabel").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.age_input = tk.StringVar()
        ttk.Entry(form, textvariable=self.age_input, width=18).grid(row=0, column=1, sticky="w", padx=5, pady=5)
        ttk.Button(form, text="Validate Age", command=self.check_manual_age).grid(row=0, column=2, sticky="w", padx=8, pady=5)
        self.age_message = ttk.Label(form, text="Enter an age to check eligibility.", style="Muted.TLabel")
        self.age_message.grid(row=1, column=0, columnspan=4, sticky="w", padx=5, pady=5)
        self._actions(tab, self.execute_age, lambda: self.export("age", ["id", "scenario", "input", "expected", "actual", "status"], "age_validation_test_report.csv"), "Generate and Run Age Tests", "Export Age CSV")
        self.age_table = self._table(tab, ("id", "scenario", "input", "expected", "actual", "status"), {"id":"Test ID", "scenario":"Test Scenario", "input":"Age", "expected":"Expected Result", "actual":"Actual Result", "status":"Status"}, {"id":85,"scenario":230,"input":110,"expected":145,"actual":145,"status":85})
        self.age_summary = self._summary(tab, "Generate age test cases to see the results.")

    def _build_footer(self):
        footer = tk.Frame(self.root, bg="#E7EDF5", padx=18, pady=8)
        footer.pack(fill="x")
        tk.Label(footer, text="Academic prototype  •  Python + Tkinter  •  Reports can be exported as CSV", bg="#E7EDF5", fg=MUTED, font=("Segoe UI", 9)).pack(side="left")
        tk.Label(footer, text="V4.0", bg="#E7EDF5", fg=TEAL, font=("Segoe UI", 9, "bold")).pack(side="right")

    def _populate(self, table, rows, fields):
        table.delete(*table.get_children())
        for row in rows:
            table.insert("", "end", values=tuple(row[field] for field in fields), tags=(row["status"],))

    def _set_summary(self, label, rows, module):
        passed = sum(row["status"] == "PASS" for row in rows)
        failed = len(rows) - passed
        label.configure(text=f"{module}  |  Total: {len(rows)}     Passed: {passed}     Failed: {failed}")

    def execute_arithmetic(self):
        expression = self.expression.get().strip()
        if not expression:
            messagebox.showerror("Missing expression", "Enter an arithmetic expression.")
            return
        try:
            parse_expression(expression)
            self.results["arithmetic"] = run_tests(expression)
        except ExpressionError as exc:
            messagebox.showerror("Invalid expression", str(exc)); return
        except Exception as exc:
            messagebox.showerror("Execution error", str(exc)); return
        self._populate(self.arithmetic_table, self.results["arithmetic"], ["id", "input", "expected", "actual", "status"])
        self._set_summary(self.arithmetic_summary, self.results["arithmetic"], self.function_name.get().strip() or "Arithmetic function")

    def check_manual_login(self):
        username, password = self.login_username.get(), self.login_password.get()
        if not username.strip() or not password:
            text, color = "VALIDATION ERROR: username and password are required.", RED
        elif authenticate(username, password):
            text, color = "LOGIN SUCCESS: demonstration account accepted.", GREEN
        else:
            text, color = "LOGIN REJECTED: username or password is incorrect.", RED
        self.login_message.configure(text=text, foreground=color)

    def execute_login(self):
        self.results["login"] = run_login_tests()
        self._populate(self.login_table, self.results["login"], ["id", "scenario", "username", "expected", "actual", "status"])
        self._set_summary(self.login_summary, self.results["login"], "Login testing")

    def check_manual_grade(self):
        raw = self.grade_input.get().strip()
        try:
            value = float(raw) if raw else ""
            result = grade_score(value)
        except ValueError:
            result = "VALIDATION ERROR"
        color = GREEN if result in {"A", "B", "C", "D", "E", "F"} else RED
        self.grade_message.configure(text=f"Result: {result}", foreground=color)

    def execute_grading(self):
        self.results["grading"] = run_grading_tests()
        self._populate(self.grading_table, self.results["grading"], ["id", "scenario", "input", "expected", "actual", "status"])
        self._set_summary(self.grading_summary, self.results["grading"], "Student grading")

    def check_manual_age(self):
        raw = self.age_input.get().strip()
        try:
            value = int(raw) if raw else ""
            result = validate_age(value)
        except ValueError:
            result = "VALIDATION ERROR"
        color = GREEN if result == "ELIGIBLE" else (TEAL if result == "NOT ELIGIBLE" else RED)
        self.age_message.configure(text=f"Result: {result}", foreground=color)

    def execute_age(self):
        self.results["age"] = run_age_tests()
        self._populate(self.age_table, self.results["age"], ["id", "scenario", "input", "expected", "actual", "status"])
        self._set_summary(self.age_summary, self.results["age"], "Age validation")

    def export(self, key, fields, default_name):
        rows = self.results[key]
        if not rows:
            messagebox.showinfo("No report", "Run this module's tests before exporting a report.")
            return
        path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")], initialfile=default_name)
        if not path: return
        try:
            with open(path, "w", newline="", encoding="utf-8-sig") as file:
                writer = csv.DictWriter(file, fieldnames=fields)
                writer.writeheader(); writer.writerows(rows)
            messagebox.showinfo("Export complete", f"Report saved successfully:\n{path}")
        except OSError as exc:
            messagebox.showerror("Export failed", str(exc))

if __name__ == "__main__":
    root = tk.Tk()
    app = TestGeneratorApp(root)
    root.mainloop()
