
---

# 🎭 Playwright Test Dashboard

An automated testing dashboard for **any** leaderboard application (IoT Game Leaderboards, custom leaderboards). Generates interactive visualizations of test results with detailed JSON reports.

> 💡 **Why this is important:** This is **End-to-End (E2E) Testing** — a professional DevOps CI/CD technique!

## ✨ Features

* ✅ **12 automated tests** for any leaderboard website
* 📊 **Interactive dashboard** with charts
* 📥 **JSON/CSV export** for reports
* 🚀  **Student-proof** : Change **2 lines** for any URL/title
* 🌐 **Render.com cold start proof** (60s timeout)
* 📱 **Responsive design** testing included
* 🎯 **Works with ANY leaderboard** deployment

## 🚀 Quick Start

## Prerequisites

<pre class="not-prose w-full rounded font-mono text-sm font-extralight"><div class="codeWrapper bg-subtle text-light selection:text-super selection:bg-super/10 my-md relative flex flex-col rounded-lg font-mono text-sm font-medium"><div class="translate-y-xs -translate-x-xs bottom-xl mb-xl flex h-0 items-start justify-end sm:sticky sm:top-xs"><div class="overflow-hidden border-subtlest ring-subtlest divide-subtlest bg-base rounded-full"><div class="border-subtlest ring-subtlest divide-subtlest bg-subtle"><button data-testid="copy-code-button" aria-label="Copy code" type="button" class="focus-visible:bg-quiet hover:bg-quiet text-quiet hover:text-foreground font-sans focus:outline-none outline-none outline-transparent transition duration-300 ease-out select-none items-center relative group/button font-semimedium justify-center text-center items-center rounded-full cursor-pointer active:scale-[0.97] active:duration-150 active:ease-outExpo origin-center whitespace-nowrap inline-flex text-sm h-8 aspect-square" data-state="closed"><div class="flex items-center min-w-0 gap-two justify-center"><div class="flex shrink-0 items-center justify-center size-4"><svg role="img" class="inline-flex fill-current shrink-0" width="16" height="16" stroke-width="1.75"><use xlink:href="#pplx-icon-copy"></use></svg></div></div></button></div></div></div><div class="-mt-xl"><div><div data-testid="code-language-indicator" class="text-quiet bg-quiet py-xs px-sm inline-block rounded-br rounded-tl-lg text-xs font-thin">bash</div></div><div><span><code><span><span>pip </span><span class="token token">install</span><span> playwright
</span></span><span><span>playwright </span><span class="token token">install</span></span></code></span></div></div></div></pre>

## Step 1: Update YOUR 2 lines in `leaderboard_comprehensive_tests.py`

<pre class="not-prose w-full rounded font-mono text-sm font-extralight"><div class="codeWrapper bg-subtle text-light selection:text-super selection:bg-super/10 my-md relative flex flex-col rounded-lg font-mono text-sm font-medium"><div class="translate-y-xs -translate-x-xs bottom-xl mb-xl flex h-0 items-start justify-end sm:sticky sm:top-xs"><div class="overflow-hidden border-subtlest ring-subtlest divide-subtlest bg-base rounded-full"><div class="border-subtlest ring-subtlest divide-subtlest bg-subtle"><button data-testid="copy-code-button" aria-label="Copy code" type="button" class="focus-visible:bg-quiet hover:bg-quiet text-quiet hover:text-foreground font-sans focus:outline-none outline-none outline-transparent transition duration-300 ease-out select-none items-center relative group/button font-semimedium justify-center text-center items-center rounded-full cursor-pointer active:scale-[0.97] active:duration-150 active:ease-outExpo origin-center whitespace-nowrap inline-flex text-sm h-8 aspect-square" data-state="closed"><div class="flex items-center min-w-0 gap-two justify-center"><div class="flex shrink-0 items-center justify-center size-4"><svg role="img" class="inline-flex fill-current shrink-0" width="16" height="16" stroke-width="1.75"><use xlink:href="#pplx-icon-copy"></use></svg></div></div></button></div></div></div><div class="-mt-xl"><div><div data-testid="code-language-indicator" class="text-quiet bg-quiet py-xs px-sm inline-block rounded-br rounded-tl-lg text-xs font-thin">python</div></div><div><span><code><span><span class="token token"># STUDENT CONFIG - CHANGE THESE 2 LINES ONLY 👇</span><span>
</span></span><span><span>APP_URL </span><span class="token token operator">=</span><span></span><span class="token token">"https://your-leaderboard.onrender.com/"</span><span>
</span></span><span><span>TITLE_TEXT </span><span class="token token operator">=</span><span></span><span class="token token">"Your IoT Game Leaderboard"</span><span></span><span class="token token"># Matches your <h1></span></span></code></span></div></div></div></pre>

## Step 2: Run tests

<pre class="not-prose w-full rounded font-mono text-sm font-extralight"><div class="codeWrapper bg-subtle text-light selection:text-super selection:bg-super/10 my-md relative flex flex-col rounded-lg font-mono text-sm font-medium"><div class="translate-y-xs -translate-x-xs bottom-xl mb-xl flex h-0 items-start justify-end sm:sticky sm:top-xs"><div class="overflow-hidden border-subtlest ring-subtlest divide-subtlest bg-base rounded-full"><div class="border-subtlest ring-subtlest divide-subtlest bg-subtle"><button data-testid="copy-code-button" aria-label="Copy code" type="button" class="focus-visible:bg-quiet hover:bg-quiet text-quiet hover:text-foreground font-sans focus:outline-none outline-none outline-transparent transition duration-300 ease-out select-none items-center relative group/button font-semimedium justify-center text-center items-center rounded-full cursor-pointer active:scale-[0.97] active:duration-150 active:ease-outExpo origin-center whitespace-nowrap inline-flex text-sm h-8 aspect-square" data-state="closed"><div class="flex items-center min-w-0 gap-two justify-center"><div class="flex shrink-0 items-center justify-center size-4"><svg role="img" class="inline-flex fill-current shrink-0" width="16" height="16" stroke-width="1.75"><use xlink:href="#pplx-icon-copy"></use></svg></div></div></button></div></div></div><div class="-mt-xl"><div><div data-testid="code-language-indicator" class="text-quiet bg-quiet py-xs px-sm inline-block rounded-br rounded-tl-lg text-xs font-thin">bash</div></div><div><span><code><span><span>python leaderboard_comprehensive_tests.py</span></span></code></span></div></div></div></pre>

**OR with CLI args (easiest):**

<pre class="not-prose w-full rounded font-mono text-sm font-extralight"><div class="codeWrapper bg-subtle text-light selection:text-super selection:bg-super/10 my-md relative flex flex-col rounded-lg font-mono text-sm font-medium"><div class="translate-y-xs -translate-x-xs bottom-xl mb-xl flex h-0 items-start justify-end sm:sticky sm:top-xs"><div class="overflow-hidden border-subtlest ring-subtlest divide-subtlest bg-base rounded-full"><div class="border-subtlest ring-subtlest divide-subtlest bg-subtle"><button data-testid="copy-code-button" aria-label="Copy code" type="button" class="focus-visible:bg-quiet hover:bg-quiet text-quiet hover:text-foreground font-sans focus:outline-none outline-none outline-transparent transition duration-300 ease-out select-none items-center relative group/button font-semimedium justify-center text-center items-center rounded-full cursor-pointer active:scale-[0.97] active:duration-150 active:ease-outExpo origin-center whitespace-nowrap inline-flex text-sm h-8 aspect-square" data-state="closed"><div class="flex items-center min-w-0 gap-two justify-center"><div class="flex shrink-0 items-center justify-center size-4"><svg role="img" class="inline-flex fill-current shrink-0" width="16" height="16" stroke-width="1.75"><use xlink:href="#pplx-icon-copy"></use></svg></div></div></button></div></div></div><div class="-mt-xl"><div><div data-testid="code-language-indicator" class="text-quiet bg-quiet py-xs px-sm inline-block rounded-br rounded-tl-lg text-xs font-thin">bash</div></div><div><span><code><span><span>python leaderboard_comprehensive_tests.py </span><span class="token token">"https://your-app.onrender.com/"</span><span></span><span class="token token">"Your Game Title"</span></span></code></span></div></div></div></pre>

## Step 3: View results

* ✅ Tests run automatically (30–90s for Render)
* 📄 `leaderboard_test_results.json` created
* 🎯 Open your Playwright dashboard → Upload JSON

## 📋 File Overview

| File                                   | Purpose                                             |
| -------------------------------------- | --------------------------------------------------- |
| `leaderboard_comprehensive_tests.py` | **Main file**— All 12 tests + student config |
| `test_dashboard.py`                  | Interactive HTML dashboard + charts                 |
| `run_full_workflow.py`               | Tests + auto-launch dashboard                       |

## 🎮 Student Workflow

<pre class="not-prose w-full rounded font-mono text-sm font-extralight"><div class="codeWrapper bg-subtle text-light selection:text-super selection:bg-super/10 my-md relative flex flex-col rounded-lg font-mono text-sm font-medium"><div class="translate-y-xs -translate-x-xs bottom-xl mb-xl flex h-0 items-start justify-end sm:sticky sm:top-xs"><div class="overflow-hidden border-subtlest ring-subtlest divide-subtlest bg-base rounded-full"><div class="border-subtlest ring-subtlest divide-subtlest bg-subtle"><button data-testid="copy-code-button" aria-label="Copy code" type="button" class="focus-visible:bg-quiet hover:bg-quiet text-quiet hover:text-foreground font-sans focus:outline-none outline-none outline-transparent transition duration-300 ease-out select-none items-center relative group/button font-semimedium justify-center text-center items-center rounded-full cursor-pointer active:scale-[0.97] active:duration-150 active:ease-outExpo origin-center whitespace-nowrap inline-flex text-sm h-8 aspect-square" data-state="closed"><div class="flex items-center min-w-0 gap-two justify-center"><div class="flex shrink-0 items-center justify-center size-4"><svg role="img" class="inline-flex fill-current shrink-0" width="16" height="16" stroke-width="1.75"><use xlink:href="#pplx-icon-copy"></use></svg></div></div></button></div></div></div><div class="-mt-xl"><div><div data-testid="code-language-indicator" class="text-quiet bg-quiet py-xs px-sm inline-block rounded-br rounded-tl-lg text-xs font-thin">bash</div></div><div><span><code><span><span class="token token"># 1. Deploy your IoT game leaderboard</span><span>
</span></span><span><span></span><span class="token token"># 2. Test it (2 options):</span><span>
</span></span><span>
</span><span><span></span><span class="token token"># OPTION A: Edit 2 lines in tests.py then:</span><span>
</span></span><span>python leaderboard_comprehensive_tests.py
</span><span>
</span><span><span></span><span class="token token"># OPTION B: One command with your details:</span><span>
</span></span><span><span>python leaderboard_comprehensive_tests.py </span><span class="token token">"https://student123.onrender.com/"</span><span></span><span class="token token">"IoT Drone Race Leaderboard"</span><span>
</span></span><span>
</span><span><span></span><span class="token token"># 3. View JSON report + 80%+ pass rate!</span></span></code></span></div></div></div></pre>

## 🧪 What Gets Tested (Universal)

| #  | Test           | Checks                                |
| -- | -------------- | ------------------------------------- |
| 1  | Page Load      | Handles Render cold starts            |
| 2  | Page Title     | Matches your custom title             |
| 3  | Main Heading   | `<h1>Your Title</h1>`visible        |
| 4  | 🎮 Game Scores | Section exists                        |
| 5  | 🧪 Test Scores | Section exists                        |
| 6  | Statistics     | “X Game Players”, “Y Test Scores” |
| 7  | Empty States   | “No scores yet” messaging           |
| 8  | Responsive     | Phone/tablet/desktop                  |
| 9  | Console Errors | No JavaScript errors                  |
| 10 | Performance    | Load time <3s                         |
| 11 | HTML Structure | Valid doctype + viewport              |
| 12 | Links          | Navigation works                      |

## ⚙️ Platforms Supported

| Platform | URL Format                          | Cold Start |
| -------- | ----------------------------------- | ---------- |
| Render   | `https://name.onrender.com/`      | 30–60s ✅ |
| Firebase | `https://project.web.app/`        | Instant    |
| Railway  | `https://project.up.railway.app/` | <30s       |
| Local    | `http://localhost:5000/`          | Instant    |

## 📊 Student Instructions (Copy-Paste)

🚀 **YOUR IoT LEADERBOARD TEST CHECKLIST**

* Deployed to Render/Firebase/Railway
* Edit 2 lines in tests.py OR use CLI args
* Run `python leaderboard_comprehensive_tests.py`
* JSON report generated (`leaderboard_test_results.json`)
* Pass rate >75% ✅
* Screenshot results for submission

## 🔧 Render.com Cold Start Fix

**Normal behavior:** First load = 30–60s (free tier)
**Script handles:** 60s timeout + networkidle wait
**Pro tip:** Visit URL in browser first to “wake up” Render

## 🎓 Gloucestershire College Marking

| Pass Rate | Grade | Notes                         |
| --------- | ----- | ----------------------------- |
| 100%      | ⭐    | Production ready              |
| 80–99%   | ✅    | Excellent                     |
| 60–79%   | ✓    | Good — fix critical issues   |
| <60%      | ⚠️  | Fix page load + core sections |

## 🐛 Troubleshooting

| Error                   | Fix                                               |
| ----------------------- | ------------------------------------------------- |
| `ModuleNotFoundError` | `pip install playwright`                        |
| `Browser not found`   | `playwright install`                            |
| `Timeout 60s`         | Render still spinning up — wait 2 mins           |
| `Title failed`        | Check `TITLE_TEXT`matches your `<h1>`         |
| `503 error`           | Render cold start — script handles automatically |

## 💡 Pro Tips

* Run with `headless=False` first to debug visually
* Test localhost first before Render deploy
* Save JSON reports weekly to track improvements
* 80%+ pass = **Distinction-level work**

## 🎯 Assignment Submission

1. **Deploy** your IoT game leaderboard
2. **Run** `python leaderboard_comprehensive_tests.py`
3. **Screenshot** test results (JSON + pass rate)
4. **Submit** JSON file + screenshots + reflection

**Happy automated testing!** 🚀

*Perfect for Level 3 IoT/DevOps modules at Gloucestershire College*

---

Would you like me to add badges (e.g., Python version, Playwright, CI/CD tested) or keep it classroom-focused as-is?
