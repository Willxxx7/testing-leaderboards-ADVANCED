from playwright.sync_api import sync_playwright
import json
import time
import re
import os
from datetime import datetime

def run_comprehensive_tests():
    """
    Run comprehensive Playwright tests on any leaderboard website
    Students will be prompted to enter their leaderboard URL
    """
    
    print("\n" + "="*60)
    print("🎮 IoT Game Leaderboard Testing Tool")
    print("="*60)
    print("\nThis tool will test your leaderboard website and generate a report.")
    print("It checks for:")
    print("  ✅ Page loading")
    print("  ✅ Titles and headings")
    print("  ✅ Game/score sections")
    print("  ✅ Statistics display")
    print("  ✅ Responsive design")
    print("  ✅ Console errors")
    print("  ✅ Performance metrics")
    print("  ✅ And more...")
    
    # Ask for the URL
    print("\n" + "-"*60)
    url = input("📱 Enter your leaderboard URL: ").strip()
    
    # Validate URL
    if not url:
        print("❌ No URL entered. Please run the program again.")
        return None
    
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
        print(f"🔗 Adding https:// → {url}")
    
    print(f"\n✅ Testing leaderboard at: {url}")
    print("🚀 Starting tests... (this may take a moment)")
    print("="*60)
    
    # Ask if they want to see the browser
    show_browser = input("\n👁️ Show browser during testing? (y/n): ").strip().lower()
    headless = show_browser != 'y'
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless)
        page = browser.new_page()
        test_results = []
        
        # Get site name for display
        site_name = extract_site_name(url)
        
        print(f"\n🎯 Testing: {site_name}")
        print("-"*40)
        
        # Test 1: Page loads successfully
        print("\n📋 Test 1: Page Load Test")
        start_time = time.time()
        try:
            response = page.goto(url, timeout=15000, wait_until='networkidle')
            load_time = (time.time() - start_time) * 1000
            
            status = "passed" if response and response.status == 200 else "failed"
            test_results.append({
                "title": "Page loads successfully",
                "status": status,
                "duration": load_time,
                "details": f"Status code: {response.status if response else 'N/A'}"
            })
            print(f"  ✅ Page loaded in {load_time:.0f}ms")
            print(f"  📊 Status: {response.status if response else 'N/A'}")
        except Exception as e:
            test_results.append({
                "title": "Page loads successfully",
                "status": "failed",
                "duration": (time.time() - start_time) * 1000,
                "details": str(e)
            })
            print(f"  ❌ Failed to load: {e}")
            print("\n💡 Tip: Check if your website is online and the URL is correct")
            browser.close()
            return None
        
        # Test 2: Title verification
        print("\n📋 Test 2: Page Title Check")
        start_time = time.time()
        page_title = page.title()
        has_title = len(page_title.strip()) > 0
        test_results.append({
            "title": "Page has a title",
            "status": "passed" if has_title else "failed",
            "duration": (time.time() - start_time) * 1000,
            "details": f"Title: '{page_title[:50]}'" if page_title else "No title found"
        })
        if has_title:
            print(f"  ✅ Title found: '{page_title[:50]}'")
        else:
            print(f"  ❌ No title found - add a <title> tag")
        
        # Test 3: Main heading exists
        print("\n📋 Test 3: Main Heading Check")
        start_time = time.time()
        try:
            heading = page.locator('h1').first
            heading_visible = heading.is_visible()
            heading_text = heading.text_content() if heading_visible else "Not found"
            test_results.append({
                "title": "Main heading (H1) exists",
                "status": "passed" if heading_visible else "failed",
                "duration": (time.time() - start_time) * 1000,
                "details": f"Heading: '{heading_text[:50]}'"
            })
            if heading_visible:
                print(f"  ✅ Main heading: '{heading_text[:50]}'")
            else:
                print(f"  ❌ No H1 heading found - add a main heading")
        except Exception as e:
            test_results.append({
                "title": "Main heading (H1) exists",
                "status": "failed",
                "duration": (time.time() - start_time) * 1000,
                "details": "No H1 element found"
            })
            print(f"  ❌ No H1 heading found")
        
        # Test 4: Look for game/score related content
        print("\n📋 Test 4: Game/Score Content Detection")
        start_time = time.time()
        
        # Common keywords in leaderboards
        keywords = ['game', 'score', 'leaderboard', 'ranking', 'player', 'points', 'level']
        found_keywords = []
        
        page_content = page.content().lower()
        for keyword in keywords:
            if keyword in page_content:
                found_keywords.append(keyword)
        
        # Check for tables (common in leaderboards)
        has_tables = page.locator('table').count() > 0
        if has_tables:
            found_keywords.append("tables")
        
        # Check for lists
        has_lists = page.locator('ul, ol').count() > 0
        if has_lists:
            found_keywords.append("lists")
        
        has_content = len(found_keywords) > 0
        test_results.append({
            "title": "Game/Score content detected",
            "status": "passed" if has_content else "warning",
            "duration": (time.time() - start_time) * 1000,
            "details": f"Found: {', '.join(found_keywords[:5])}" if found_keywords else "No game/score keywords found"
        })
        
        if has_content:
            print(f"  ✅ Found content: {', '.join(found_keywords[:5])}")
        else:
            print(f"  ⚠️ No game/score content detected - make sure your leaderboard displays scores")
        
        # Test 5: Numbers/Statistics detection
        print("\n📋 Test 5: Statistics Display Check")
        start_time = time.time()
        
        # Look for numbers (scores, points, etc.)
        try:
            # Find elements with numbers (potential scores)
            numbered_elements = page.locator(':has-text(/\\d+/)')
            number_count = numbered_elements.count()
            
            # Look for specific stat patterns
            stat_patterns = []
            if 'score' in page_content:
                stat_patterns.append("scores")
            if 'point' in page_content:
                stat_patterns.append("points")
            if 'rank' in page_content:
                stat_patterns.append("rankings")
            if 'time' in page_content:
                stat_patterns.append("times")
            
            has_stats = number_count > 0 or len(stat_patterns) > 0
            test_results.append({
                "title": "Statistics/numbers displayed",
                "status": "passed" if has_stats else "warning",
                "duration": (time.time() - start_time) * 1000,
                "details": f"Found {number_count} elements with numbers" if number_count > 0 else "No numbers found"
            })
            
            if has_stats:
                print(f"  ✅ Found statistics: {', '.join(stat_patterns) if stat_patterns else f'{number_count} numbers'}")
            else:
                print(f"  ⚠️ No statistics or numbers found - are you displaying scores?")
        except:
            test_results.append({
                "title": "Statistics/numbers displayed",
                "status": "warning",
                "duration": (time.time() - start_time) * 1000,
                "details": "Could not detect statistics"
            })
            print(f"  ⚠️ Could not detect statistics")
        
        # Test 6: Responsive design
        print("\n📋 Test 6: Responsive Design Test")
        start_time = time.time()
        viewports = [(1920, 1080), (1366, 768), (768, 1024), (375, 667)]
        responsive_passed = True
        
        for width, height in viewports:
            page.set_viewport_size({"width": width, "height": height})
            time.sleep(0.2)
            content_visible = page.locator('body').is_visible()
            if not content_visible:
                responsive_passed = False
                break
        
        # Reset to default viewport
        page.set_viewport_size({"width": 1280, "height": 720})
        
        test_results.append({
            "title": "Responsive design works",
            "status": "passed" if responsive_passed else "failed",
            "duration": (time.time() - start_time) * 1000,
            "details": f"Tested on {len(viewports)} screen sizes"
        })
        
        if responsive_passed:
            print(f"  ✅ Works on all {len(viewports)} screen sizes tested")
        else:
            print(f"  ❌ Issues on some screen sizes - check mobile responsiveness")
        
        # Test 7: Console errors
        print("\n📋 Test 7: JavaScript Console Errors")
        start_time = time.time()
        console_errors = []
        
        def handle_console(msg):
            if msg.type == 'error':
                console_errors.append(msg.text)
        
        page.on('console', handle_console)
        page.reload()
        time.sleep(1)
        
        has_errors = len(console_errors) > 0
        test_results.append({
            "title": "No JavaScript console errors",
            "status": "passed" if not has_errors else "failed",
            "duration": (time.time() - start_time) * 1000,
            "details": f"Found {len(console_errors)} errors" if has_errors else "Clean console"
        })
        
        if has_errors:
            print(f"  ❌ Found {len(console_errors)} console errors")
            for error in console_errors[:2]:
                print(f"     ⚠️ {error[:80]}")
        else:
            print(f"  ✅ No console errors detected")
        
        # Test 8: Performance check
        print("\n📋 Test 8: Performance Check")
        start_time = time.time()
        
        try:
            # Simple performance check
            performance_data = page.evaluate("""() => {
                const perfData = performance.timing;
                const loadTime = perfData.loadEventEnd - perfData.navigationStart;
                return { loadTime: loadTime };
            }""")
            
            load_time_ms = performance_data.get('loadTime', 0)
            
            if load_time_ms < 2000:
                perf_status = "passed"
                perf_msg = f"Fast load time: {load_time_ms}ms"
            elif load_time_ms < 4000:
                perf_status = "warning"
                perf_msg = f"Okay load time: {load_time_ms}ms"
            else:
                perf_status = "failed"
                perf_msg = f"Slow load time: {load_time_ms}ms - consider optimizing"
            
            test_results.append({
                "title": "Good performance",
                "status": perf_status,
                "duration": load_time_ms,
                "details": perf_msg
            })
            print(f"  { '✅' if perf_status == 'passed' else '⚠️' if perf_status == 'warning' else '❌'} {perf_msg}")
        except:
            test_results.append({
                "title": "Good performance",
                "status": "warning",
                "duration": 0,
                "details": "Could not measure performance"
            })
            print(f"  ⚠️ Could not measure detailed performance")
        
        # Test 9: Link check
        print("\n📋 Test 9: Link Check")
        start_time = time.time()
        try:
            all_links = page.locator('a')
            link_count = all_links.count()
            
            test_results.append({
                "title": "Links are present",
                "status": "passed" if link_count > 0 else "warning",
                "duration": (time.time() - start_time) * 1000,
                "details": f"Found {link_count} links"
            })
            
            if link_count > 0:
                print(f"  ✅ Found {link_count} links on your page")
            else:
                print(f"  ⚠️ No links found - consider adding navigation")
        except:
            test_results.append({
                "title": "Links are present",
                "status": "warning",
                "duration": (time.time() - start_time) * 1000,
                "details": "Could not check links"
            })
            print(f"  ⚠️ Could not check links")
        
        # Test 10: Data structure for leaderboard
        print("\n📋 Test 10: Leaderboard Structure Check")
        start_time = time.time()
        
        structure_found = []
        if page.locator('table').count() > 0:
            structure_found.append(f"{page.locator('table').count()} table(s)")
        if page.locator('ul').count() > 0:
            structure_found.append(f"{page.locator('ul').count()} list(s)")
        if page.locator('div[class*="card"]').count() > 0:
            structure_found.append("cards")
        if page.locator('div[class*="score"]').count() > 0:
            structure_found.append("score elements")
        
        test_results.append({
            "title": "Leaderboard data structure",
            "status": "passed" if len(structure_found) > 0 else "warning",
            "duration": (time.time() - start_time) * 1000,
            "details": f"Found: {', '.join(structure_found)}" if structure_found else "No clear structure detected"
        })
        
        if structure_found:
            print(f"  ✅ Found: {', '.join(structure_found)}")
        else:
            print(f"  ⚠️ No clear leaderboard structure - use tables or lists for scores")
        
        browser.close()
        
        # Generate report
        print("\n" + "="*60)
        print("📊 GENERATING REPORT")
        print("="*60)
        
        # Calculate summary
        total_tests = len(test_results)
        passed_tests = len([t for t in test_results if t['status'] == 'passed'])
        failed_tests = len([t for t in test_results if t['status'] == 'failed'])
        warnings = len([t for t in test_results if t['status'] == 'warning'])
        pass_rate = (passed_tests / total_tests * 100) if total_tests > 0 else 0
        
        # Create report
        report = {
            "url": url,
            "site_name": site_name,
            "timestamp": datetime.now().isoformat(),
            "summary": {
                "total_tests": total_tests,
                "passed": passed_tests,
                "failed": failed_tests,
                "warnings": warnings,
                "pass_rate": f"{pass_rate:.1f}%"
            },
            "tests": test_results
        }
        
        # Save JSON report
        json_filename = f"{sanitize_filename(site_name)}_test_results.json"
        with open(json_filename, 'w') as f:
            json.dump(report, f, indent=2)
        
        # Create HTML report for easy viewing
        html_filename = create_html_report(report, site_name)
        
        # Print final summary
        print(f"\n{'='*60}")
        print("📊 TEST SUMMARY")
        print(f"{'='*60}")
        print(f"Website: {site_name}")
        print(f"URL: {url}")
        print(f"\nResults:")
        print(f"  ✅ Passed: {passed_tests}/{total_tests}")
        print(f"  ❌ Failed: {failed_tests}/{total_tests}")
        if warnings > 0:
            print(f"  ⚠️ Warnings: {warnings}")
        print(f"  📈 Pass Rate: {pass_rate:.1f}%")
        
        # Provide feedback
        print(f"\n{'='*60}")
        print("💡 FEEDBACK & SUGGESTIONS")
        print(f"{'='*60}")
        
        if pass_rate == 100:
            print("🎉 Excellent! Your leaderboard passed all tests!")
            print("   Great job implementing all the requirements!")
        elif pass_rate >= 80:
            print("👍 Good work! Your leaderboard is almost there.")
            print("   Check the failed tests above for minor improvements.")
        elif pass_rate >= 60:
            print("📝 Getting there! Your leaderboard has the basics.")
            print("   Focus on fixing the failed tests to improve.")
        else:
            print("🔄 Your leaderboard needs some work.")
            print("   Review the failed tests and check:")
            print("   - Is your website publicly accessible?")
            print("   - Does it display game scores?")
            print("   - Does it have proper headings and structure?")
        
        print(f"\n📁 Reports saved:")
        print(f"   📄 JSON: {json_filename}")
        print(f"   🌐 HTML: {html_filename}")
        
        print(f"\n🎯 Next Steps:")
        print(f"   1. Open {html_filename} in your browser")
        print(f"   2. Review detailed test results")
        print(f"   3. Fix any failed tests")
        print(f"   4. Run this tool again to see improvements!")
        
        # Open HTML report automatically
        try:
            import webbrowser
            webbrowser.open(f'file://{os.path.abspath(html_filename)}')
            print(f"\n🌐 Opening HTML report in your browser...")
        except:
            pass
        
        return report

def extract_site_name(url):
    """Extract a readable site name from URL"""
    # Remove protocol
    name = re.sub(r'^https?://', '', url)
    # Remove www
    name = re.sub(r'^www\.', '', name)
    # Get main domain part
    name = name.split('/')[0]
    # Remove TLD (.com, .onrender.com, etc.)
    name = re.sub(r'\..*$', '', name)
    # Clean up
    name = name.replace('-', ' ').title()
    return name

def sanitize_filename(name):
    """Create a safe filename from site name"""
    # Remove special characters
    safe_name = re.sub(r'[^\w\-_\. ]', '_', name)
    # Replace spaces with underscores
    safe_name = safe_name.replace(' ', '_')
    return safe_name

def create_html_report(report, site_name):
    """Create an easy-to-read HTML report"""
    
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Leaderboard Test Results - {site_name}</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 20px;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 20px;
            overflow: hidden;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
        }}
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            text-align: center;
        }}
        .summary {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            padding: 30px;
            background: #f8f9fa;
        }}
        .summary-card {{
            background: white;
            padding: 20px;
            border-radius: 15px;
            text-align: center;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        .summary-number {{
            font-size: 48px;
            font-weight: bold;
            margin: 10px 0;
        }}
        .passed .summary-number {{ color: #28a745; }}
        .failed .summary-number {{ color: #dc3545; }}
        .warnings .summary-number {{ color: #ffc107; }}
        .rate .summary-number {{ color: #17a2b8; }}
        .tests {{
            padding: 30px;
        }}
        .test-item {{
            background: white;
            border: 1px solid #e0e0e0;
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 15px;
            transition: transform 0.2s;
        }}
        .test-item:hover {{
            transform: translateX(5px);
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        .test-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 10px;
        }}
        .test-title {{
            font-size: 18px;
            font-weight: 600;
        }}
        .status {{
            padding: 5px 15px;
            border-radius: 20px;
            font-weight: bold;
            font-size: 14px;
        }}
        .status-passed {{
            background: #d4edda;
            color: #155724;
        }}
        .status-failed {{
            background: #f8d7da;
            color: #721c24;
        }}
        .status-warning {{
            background: #fff3cd;
            color: #856404;
        }}
        .test-details {{
            color: #666;
            font-size: 14px;
            margin-top: 10px;
            padding-top: 10px;
            border-top: 1px solid #f0f0f0;
        }}
        .footer {{
            background: #f8f9fa;
            padding: 20px;
            text-align: center;
            color: #666;
        }}
        @media (max-width: 768px) {{
            .summary {{
                grid-template-columns: 1fr;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🎮 IoT Game Leaderboard Test Report</h1>
            <p>Tested: {site_name}</p>
            <p>URL: {report['url']}</p>
            <p>Date: {report['timestamp']}</p>
        </div>
        
        <div class="summary">
            <div class="summary-card passed">
                <div class="summary-label">✅ Passed Tests</div>
                <div class="summary-number">{report['summary']['passed']}</div>
                <div class="summary-label">out of {report['summary']['total_tests']}</div>
            </div>
            <div class="summary-card failed">
                <div class="summary-label">❌ Failed Tests</div>
                <div class="summary-number">{report['summary']['failed']}</div>
            </div>
            <div class="summary-card warnings">
                <div class="summary-label">⚠️ Warnings</div>
                <div class="summary-number">{report['summary']['warnings']}</div>
            </div>
            <div class="summary-card rate">
                <div class="summary-label">📈 Pass Rate</div>
                <div class="summary-number">{report['summary']['pass_rate']}</div>
            </div>
        </div>
        
        <div class="tests">
            <h2>📋 Detailed Test Results</h2>
            {generate_test_items_html(report['tests'])}
        </div>
        
        <div class="footer">
            <p>💡 Run the test tool again after making improvements to see your progress!</p>
            <p>🔧 Generated by IoT Game Leaderboard Testing Tool</p>
        </div>
    </div>
</body>
</html>"""
    
    filename = f"{sanitize_filename(site_name)}_test_report.html"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    return filename

def generate_test_items_html(tests):
    """Generate HTML for test items"""
    items_html = []
    for test in tests:
        status_class = f"status-{test['status']}"
        status_text = test['status'].upper()
        
        items_html.append(f"""
        <div class="test-item">
            <div class="test-header">
                <div class="test-title">📌 {test['title']}</div>
                <div class="status {status_class}">{status_text}</div>
            </div>
            <div class="test-details">
                <strong>Duration:</strong> {test['duration']:.0f}ms<br>
                <strong>Details:</strong> {test.get('details', 'No additional details')}
            </div>
        </div>
        """)
    
    return '\n'.join(items_html)

if __name__ == "__main__":
    print("""
    ╔══════════════════════════════════════════════════════════╗
    ║     IoT Game Leaderboard Testing Tool                    ║
    ║     Test your leaderboard website automatically!         ║
    ╚══════════════════════════════════════════════════════════╝
    """)
    
    # Run the tests
    run_comprehensive_tests()
    
    print("\n✨ Thanks for using the IoT Game Leaderboard Testing Tool!")
    print("   Press Enter to exit...")
    input()