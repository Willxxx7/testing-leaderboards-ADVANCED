# 🎭 Playwright Test Dashboard

An automated testing dashboard for the WASK Leaderboard application that generates beautiful, interactive visualizations of test results.

## ✨ Features

- ✅ 12 automated tests for the leaderboard
- 📊 Interactive dashboard with charts and visualizations
- 📥 Export results as CSV
- 🚀 One-command workflow
- 📱 Responsive design for all devices

## 🚀 Quick Start

### Step 1: Clone the repository

```bash
git clone https://github.com/your-username/playwright-dashboard.git
cd playwright-dashboard
```

### Step 2: Install requirements

```bash
pip install -r requirements.txt
playwright install
```

### Step 3: Run the dashboard

```bash
python run_full_workflow.py
```

That’s it. Your browser should open automatically with the test dashboard.

## 📋 File Overview

| File                                   | Purpose                                         |
| -------------------------------------- | ----------------------------------------------- |
| `leaderboard_comprehensive_tests.py` | Contains 12 automated tests for the leaderboard |
| `test_dashboard.py`                  | Creates the interactive HTML dashboard          |
| `run_full_workflow.py`               | Runs tests and opens the dashboard              |
| `requirements.txt`                   | Lists the Python packages needed                |

## 🎮 How to Use

### Option 1: Everything automated

```bash
python run_full_workflow.py
```

This will:

- Run all 12 tests automatically
- Save results to `leaderboard_test_results.json`
- Launch the dashboard in your browser

### Option 2: Run tests only

```bash
python leaderboard_comprehensive_tests.py
```

### Option 3: View dashboard only

```bash
python test_dashboard.py
```

### Option 4: Use a custom port

```bash
python test_dashboard.py --port 8888
```

## 📊 Understanding Test Results

### Test Status

| Icon | Meaning | What to do              |
| ---- | ------- | ----------------------- |
| ✅   | Passed  | Nothing — it works     |
| ❌   | Failed  | Check the error message |
| ⚠️ | Skipped | Not a problem           |

### Performance Badges

| Badge     | Time                 | Meaning           |
| --------- | -------------------- | ----------------- |
| ⚡ Fast   | `< 0.5 seconds`    | Excellent         |
| ✓ Normal | `0.5–1.5 seconds` | Good              |
| 🐢 Slow   | `> 1.5 seconds`    | Needs improvement |

## 🔧 What Gets Tested

The tests check:

- Page loads correctly
- Title is correct
- Game Scores section exists
- Test Scores section exists
- Statistics display properly
- Empty state messages work
- Responsive design on phone, tablet, and desktop
- No JavaScript errors
- Page loads fast
- HTML structure is valid
- No broken links
- Performance metrics

## 🐛 Troubleshooting

### Module not found

```bash
pip install -r requirements.txt
```

### Browser not found

```bash
playwright install
```

### Dashboard won't open

```bash
python test_dashboard.py --port 8888
```

### Tests are too slow

Set `headless=True` for normal runs, or `headless=False` if you want to watch the browser during debugging.

### Website is down

The leaderboard site may be temporarily offline. Try again later.

## 💡 Pro Tips for Students

- Run tests headlessly for speed.
- Save screenshots of failures.
- Export results for reports.
- Write your own tests using the template file.

## 📤 Exporting Results

### To CSV

Use the dashboard’s **Export to CSV** button.

### To JSON

Results are automatically saved to `leaderboard_test_results.json`.

## 📚 Additional Resources

- [Playwright Documentation](https://playwright.dev/python/)
- [Pytest Documentation](https://docs.pytest.org/)
- [Chart.js Documentation](https://www.chartjs.org/)

## 🎓 Assignment Checklist

- Python 3.8+ installed
- Git installed
- Repository cloned successfully
- `pip install -r requirements.txt` worked
- `playwright install` completed
- `python run_full_workflow.py` ran without errors
- Dashboard opened in browser
- Test results and charts are visible
- CSV export works
- You understand what each test does

## 📄 License

This project is for educational purposes.

Happy testing! 🚀
