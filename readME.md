
# 🎭 Playwright Test Dashboard

An automated testing dashboard for any leaderboard application (IoT Game Leaderboards, custom leaderboards). Generates interactive visualizations of test results with detailed JSON reports.

💡 Why this is important: This is End-to-End (E2E) Testing — a professional DevOps CI/CD technique!

## ✨ Features

- ✅ 12 automated tests for any leaderboard website
- 📊 Interactive dashboard with charts
- 📥 JSON/CSV export for reports
- 🚀 Student-proof: Prompted for URL/title at runtime
- 🌐 Render.com cold start proof (60s timeout)
- 📱 Responsive design testing included
- 🎯 Works with ANY leaderboard deployment

## 🚀 Quick Start

### Prerequisites

```bash
pip install playwright
playwright install
```

### Step 1: Run tests (prompts for your details)

In Terminal enter:

```
python leaderboard_comprehensive_tests.py
```

Program will prompt:
In Terminal enter:

```
Enter your leaderboard URL: https://your-app.onrender.com/
Enter your page title: Your IoT Game Leaderboard if asked for!
```

**OR with CLI args (no prompts):**

In Terminal enter:

```
python leaderboard_comprehensive_tests.py "https://your-app.onrender.com/" "Your Game Title"
```

### Step 2: View results

- ✅ Tests run automatically (30–90s for Render)
- 📄 leaderboard_test_results.json created
- 🎯 Open your Playwright dashboard → Upload JSON

## 📋 File Overview

| File                               | Purpose                             |
| ---------------------------------- | ----------------------------------- |
| leaderboard_comprehensive_tests.py | Main file — All 12 tests + prompts |
| test_dashboard.py                  | Interactive HTML dashboard + charts |
| run_full_workflow.py               | Tests + auto-launch dashboard       |

## 🎮 Student Workflow

```bash
# 1. Deploy your IoT game leaderboard
# 2. Test it (2 options):

# OPTION A: Interactive prompts (easiest):
python leaderboard_comprehensive_tests.py
# Enter URL when prompted
# Enter title when prompted

# OPTION B: One command (no prompts):
python leaderboard_comprehensive_tests.py "https://student123.onrender.com/" "IoT Drone Race Leaderboard"

# 3. View JSON report + 80%+ pass rate!
```

## 🧪 What Gets Tested (Universal)

| #  | Test           | Checks                            |
| -- | -------------- | --------------------------------- |
| 1  | Page Load      | Handles Render cold starts        |
| 2  | Page Title     | Matches your custom title         |
| 3  | Main Heading   | `<h1>Your Title</h1>` visible   |
| 4  | 🎮 Game Scores | Section exists                    |
| 5  | 🧪 Test Scores | Section exists                    |
| 6  | Statistics     | "X Game Players", "Y Test Scores" |
| 7  | Empty States   | "No scores yet" messaging         |
| 8  | Responsive     | Phone/tablet/desktop              |
| 9  | Console Errors | No JavaScript errors              |
| 10 | Performance    | Load time <3s                     |
| 11 | HTML Structure | Valid doctype + viewport          |
| 12 | Links          | Navigation works                  |

## ⚙️ Platforms Supported

| Platform | URL Format                      | Cold Start |
| -------- | ------------------------------- | ---------- |
| Render   | https://name.onrender.com/      | 30–60s ✅ |
| Firebase | https://project.web.app/        | Instant    |
| Railway  | https://project.up.railway.app/ | <30s       |
| Local    | http://localhost:5000/          | Instant    |

## 📊 Student Instructions (Copy-Paste)

🚀 YOUR IoT LEADERBOARD TEST CHECKLIST

- Deployed to Render/Firebase/Railway
- Run python leaderboard_comprehensive_tests.py
- Enter your URL + title when prompted
- JSON report generated (leaderboard_test_results.json)
- Pass rate >75% ✅
- Screenshot results for submission

## 🔧 Render.com Cold Start Fix

Normal behavior: First load = 30–60s (free tier)
Script handles: 60s timeout + networkidle wait
Pro tip: Visit URL in browser first to "wake up" Render

## 🎓 Gloucestershire College Marking

| Pass Rate | Grade | Notes                         |
| --------- | ----- | ----------------------------- |
| 100%      | ⭐    | Production ready              |
| 80–99%   | ✅    | Excellent                     |
| 60–79%   | ✓    | Good — fix critical issues   |
| <60%      | ⚠️  | Fix page load + core sections |

## 🐛 Troubleshooting

| Error               | Fix                                               |
| ------------------- | ------------------------------------------------- |
| ModuleNotFoundError | pip install playwright                            |
| Browser not found   | playwright install                                |
| Timeout 60s         | Render still spinning up — wait 2 mins           |
| Title failed        | Check title matches your `<h1>` exactly         |
| 503 error           | Render cold start — script handles automatically |

## 💡 Pro Tips

- Run with headless=False first to debug visually
- Test localhost first before Render deploy
- Save JSON reports weekly to track improvements
- 80%+ pass = Distinction-level work

## 🎯 Assignment Submission

1. Deploy your IoT game leaderboard
2. Run python leaderboard_comprehensive_tests.py
3. Screenshot test results (JSON + pass rate)
4. Submit JSON file + screenshots + reflection

**Happy automated testing! 🚀**

*Perfect for Level 3 IoT/DevOps modules at Gloucestershire College*

---

✅ Updated! Now emphasizes the interactive prompts (no config editing needed). Students you just run the script and type your URL/title. 🎯
