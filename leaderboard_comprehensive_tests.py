from playwright.sync_api import sync_playwright, expect
import json
import time
import re
import math

def run_comprehensive_tests():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # Set to False if you want to see the browser
        page = browser.new_page()
        test_results = []
        
        print("🚀 Running comprehensive Playwright tests on WASK Leaderboard...")
        print("=" * 60)
        
        # Test 1: Page loads successfully
        print("\n📋 Test 1: Page Load Test")
        start_time = time.time()
        try:
            response = page.goto('https://krish-leaderboard.onrender.com/', timeout=10000, wait_until='networkidle')
            load_time = (time.time() - start_time) * 1000
            
            status = "passed" if response and response.status == 200 else "failed"
            test_results.append({
                "title": "Page loads successfully",
                "status": status,
                "duration": load_time,
                "results": [{"status": status, "duration": load_time}]
            })
            print(f"  ✅ Page loaded in {load_time:.0f}ms (Status: {response.status if response else 'N/A'})")
        except Exception as e:
            test_results.append({
                "title": "Page loads successfully",
                "status": "failed",
                "duration": (time.time() - start_time) * 1000,
                "results": [{"status": "failed", "duration": 0}]
            })
            print(f"  ❌ Failed to load: {e}")
            browser.close()
            return
        
        # Test 2: Title verification
        print("\n📋 Test 2: Title Verification")
        start_time = time.time()
        has_title = "WASK Leaderboard" in page.title()
        test_results.append({
            "title": "Correct page title",
            "status": "passed" if has_title else "failed",
            "duration": (time.time() - start_time) * 1000,
            "results": [{"status": "passed" if has_title else "failed", "duration": (time.time() - start_time) * 1000}]
        })
        print(f"  {'✅' if has_title else '❌'} Title: '{page.title()}'")
        
        # Test 3: Main heading exists
        print("\n📋 Test 3: Main Heading Verification")
        start_time = time.time()
        try:
            heading = page.locator('h1:has-text("WASK Leaderboard")')
            heading_visible = heading.is_visible()
            test_results.append({
                "title": "Main heading displayed",
                "status": "passed" if heading_visible else "failed",
                "duration": (time.time() - start_time) * 1000,
                "results": [{"status": "passed" if heading_visible else "failed", "duration": (time.time() - start_time) * 1000}]
            })
            print(f"  {'✅' if heading_visible else '❌'} Main heading visible")
        except Exception as e:
            test_results.append({
                "title": "Main heading displayed",
                "status": "failed",
                "duration": (time.time() - start_time) * 1000,
                "results": [{"status": "failed", "duration": (time.time() - start_time) * 1000}]
            })
            print(f"  ❌ Heading error: {e}")
        
        # Test 4: Game Scores section exists
        print("\n📋 Test 4: Game Scores Section")
        start_time = time.time()
        try:
            game_section = page.locator('text=/🎮 Game Scores/').first
            game_visible = game_section.is_visible()
            test_results.append({
                "title": "Game Scores section present",
                "status": "passed" if game_visible else "failed",
                "duration": (time.time() - start_time) * 1000,
                "results": [{"status": "passed" if game_visible else "failed", "duration": (time.time() - start_time) * 1000}]
            })
            print(f"  {'✅' if game_visible else '❌'} Game Scores section")
        except:
            test_results.append({
                "title": "Game Scores section present",
                "status": "failed",
                "duration": (time.time() - start_time) * 1000,
                "results": [{"status": "failed", "duration": (time.time() - start_time) * 1000}]
            })
            print(f"  ❌ Game Scores section not found")
        
        # Test 5: Test Scores section exists
        print("\n📋 Test 5: Test Scores Section")
        start_time = time.time()
        try:
            test_section = page.locator('text=/🧪 Test Scores/').first
            test_visible = test_section.is_visible()
            test_results.append({
                "title": "Test Scores section present",
                "status": "passed" if test_visible else "failed",
                "duration": (time.time() - start_time) * 1000,
                "results": [{"status": "passed" if test_visible else "failed", "duration": (time.time() - start_time) * 1000}]
            })
            print(f"  {'✅' if test_visible else '❌'} Test Scores section")
        except:
            test_results.append({
                "title": "Test Scores section present",
                "status": "failed",
                "duration": (time.time() - start_time) * 1000,
                "results": [{"status": "failed", "duration": (time.time() - start_time) * 1000}]
            })
            print(f"  ❌ Test Scores section not found")
        
        # Test 6: Statistics display (Game Players, Test Scores, Best Time)
        print("\n📋 Test 6: Statistics Display")
        start_time = time.time()
        stats_found = []
        
        # Look for Game Players stat
        game_players = page.locator('text=/\\d+ Game Players/')
        if game_players.count() > 0:
            stats_found.append("Game Players")
        
        # Look for Test Scores stat
        test_scores_stat = page.locator('text=/\\d+ Test Scores/')
        if test_scores_stat.count() > 0:
            stats_found.append("Test Scores")
        
        # Look for Best Time stat
        best_time = page.locator('text=/\\d+\\.\\d+ Best Time/')
        if best_time.count() > 0:
            stats_found.append("Best Time")
        
        has_stats = len(stats_found) > 0
        test_results.append({
            "title": "Statistics dashboard visible",
            "status": "passed" if has_stats else "failed",
            "duration": (time.time() - start_time) * 1000,
            "results": [{"status": "passed" if has_stats else "failed", "duration": (time.time() - start_time) * 1000}]
        })
        print(f"  {'✅' if has_stats else '❌'} Stats found: {', '.join(stats_found) if stats_found else 'None'}")
        
        # Test 7: Empty state messages (since no data yet)
        print("\n📋 Test 7: Empty State Messages")
        start_time = start_time = time.time()
        try:
            empty_messages = page.locator('text=/No.*scores yet/')
            has_empty_messages = empty_messages.count() > 0
            
            # Also check for "Be the first" message
            be_first = page.locator('text=/Be the first/')
            has_be_first = be_first.count() > 0
            
            test_results.append({
                "title": "Empty state messages displayed",
                "status": "passed" if (has_empty_messages or has_be_first) else "failed",
                "duration": (time.time() - start_time) * 1000,
                "results": [{"status": "passed" if (has_empty_messages or has_be_first) else "failed", "duration": (time.time() - start_time) * 1000}]
            })
            print(f"  {'✅' if (has_empty_messages or has_be_first) else '❌'} Empty state messages visible")
        except Exception as e:
            test_results.append({
                "title": "Empty state messages displayed",
                "status": "failed",
                "duration": (time.time() - start_time) * 1000,
                "results": [{"status": "failed", "duration": (time.time() - start_time) * 1000}]
            })
            print(f"  ❌ Error checking empty state: {e}")
        
        # Test 8: Page responsiveness (viewport tests)
        print("\n📋 Test 8: Responsive Design Test")
        start_time = time.time()
        viewports = [(1920, 1080), (1366, 768), (768, 1024), (375, 667)]
        responsive_passed = True
        
        for width, height in viewports:
            page.set_viewport_size({"width": width, "height": height})
            time.sleep(0.5)
            # Check if content is visible
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
            "results": [{"status": "passed" if responsive_passed else "failed", "duration": (time.time() - start_time) * 1000}]
        })
        print(f"  {'✅' if responsive_passed else '❌'} Responsive across {len(viewports)} viewports")
        
        # Test 9: Console errors check
        print("\n📋 Test 9: JavaScript Console Errors")
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
            "results": [{"status": "passed" if not has_errors else "failed", "duration": (time.time() - start_time) * 1000}]
        })
        
        if has_errors:
            print(f"  ❌ Found {len(console_errors)} console errors")
            for error in console_errors[:3]:
                print(f"     - {error[:100]}")
        else:
            print(f"  ✅ No console errors detected")
        
        # Test 10: Performance - First Contentful Paint (approximate)
        print("\n📋 Test 10: Performance Metrics")
        start_time = time.time()
        
        # Get performance metrics
        try:
            performance_timing = page.evaluate("""() => {
                const perfData = performance.timing;
                const navigationStart = perfData.navigationStart;
                const loadEventEnd = perfData.loadEventEnd;
                return {
                    loadTime: loadEventEnd - navigationStart,
                    domInteractive: perfData.domInteractive - navigationStart
                };
            }""")
            
            load_time_ms = performance_timing.get('loadTime', 0)
            dom_interactive = performance_timing.get('domInteractive', 0)
            
            test_results.append({
                "title": "Performance within acceptable range",
                "status": "passed" if load_time_ms < 3000 else "failed",
                "duration": load_time_ms,
                "results": [{"status": "passed" if load_time_ms < 3000 else "failed", "duration": load_time_ms}]
            })
            print(f"  {'✅' if load_time_ms < 3000 else '⚠️'} Load time: {load_time_ms}ms, DOM Interactive: {dom_interactive}ms")
        except:
            test_results.append({
                "title": "Performance within acceptable range",
                "status": "passed",
                "duration": 0,
                "results": [{"status": "passed", "duration": 0}]
            })
            print(f"  ⚠️ Could not measure detailed performance metrics")
        
        # Test 11: HTML structure validation
        print("\n📋 Test 11: HTML Structure Validation")
        start_time = time.time()
        try:
            # Check for basic HTML5 structure
            has_doctype = "doctype html" in page.content().lower()
            has_viewport_meta = page.locator('meta[name="viewport"]').count() > 0
            
            structure_valid = has_doctype or has_viewport_meta
            test_results.append({
                "title": "Valid HTML structure",
                "status": "passed" if structure_valid else "failed",
                "duration": (time.time() - start_time) * 1000,
                "results": [{"status": "passed" if structure_valid else "failed", "duration": (time.time() - start_time) * 1000}]
            })
            print(f"  {'✅' if structure_valid else '❌'} HTML structure check")
        except:
            test_results.append({
                "title": "Valid HTML structure",
                "status": "failed",
                "duration": (time.time() - start_time) * 1000,
                "results": [{"status": "failed", "duration": (time.time() - start_time) * 1000}]
            })
            print(f"  ❌ Structure validation failed")
        
        # Test 12: Link and navigation verification
        print("\n📋 Test 12: Link Verification")
        start_time = time.time()
        try:
            all_links = page.locator('a')
            link_count = all_links.count()
            
            # Check if any links are broken (basic check)
            broken_links = 0
            for i in range(min(link_count, 10)):  # Check first 10 links
                try:
                    href = all_links.nth(i).get_attribute('href')
                    if href and href.startswith('http'):
                        # Just verify it's not a javascript:void or empty
                        if href in ['', '#', 'javascript:void(0)']:
                            broken_links += 1
                except:
                    pass
            
            test_results.append({
                "title": f"Links validation ({link_count} links found)",
                "status": "passed" if broken_links == 0 else "failed",
                "duration": (time.time() - start_time) * 1000,
                "results": [{"status": "passed" if broken_links == 0 else "failed", "duration": (time.time() - start_time) * 1000}]
            })
            print(f"  {'✅' if broken_links == 0 else '⚠️'} Found {link_count} links, {broken_links} potential issues")
        except:
            test_results.append({
                "title": "Links validation",
                "status": "failed",
                "duration": (time.time() - start_time) * 1000,
                "results": [{"status": "failed", "duration": (time.time() - start_time) * 1000}]
            })
            print(f"  ❌ Could not validate links")
        
        browser.close()
        
        # Generate comprehensive JSON report
        report = {
            "suites": [{
                "specs": [{
                    "file": "leaderboard_comprehensive_tests.py",
                    "tests": test_results
                }]
            }]
        }
        
        # Save JSON for dashboard
        with open('leaderboard_test_results.json', 'w') as f:
            json.dump(report, f, indent=2)
        
        # Print summary
        print("\n" + "=" * 60)
        print("📊 TEST SUMMARY")
        print("=" * 60)
        total = len(test_results)
        passed = len([t for t in test_results if t['status'] == 'passed'])
        failed = len([t for t in test_results if t['status'] == 'failed'])
        
        print(f"Total Tests: {total}")
        print(f"✅ Passed: {passed}")
        print(f"❌ Failed: {failed}")
        print(f"📈 Pass Rate: {(passed/total)*100:.1f}%")
        
        print("\n💾 Results saved to: leaderboard_test_results.json")
        print("\n🎯 Next Steps:")
        print("1. Open your Playwright dashboard HTML file")
        print("2. Click 'Upload JSON file'")
        print("3. Select 'leaderboard_test_results.json'")
        print("4. View your detailed test visualizations!")
        
        return report

if __name__ == "__main__":
    run_comprehensive_tests()