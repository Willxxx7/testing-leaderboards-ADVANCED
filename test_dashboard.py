#!/usr/bin/env python3
"""
Playwright Test Results Dashboard - Python Version
Creates an interactive web dashboard from JSON test results
"""

import json
import os
import webbrowser
import tempfile
from pathlib import Path
from datetime import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler
import threading
import webbrowser

def create_dashboard_html(test_results_file='leaderboard_test_results.json'):
    """
    Create an HTML dashboard from test results JSON file
    """
    
    # Read the test results
    try:
        with open(test_results_file, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        # Create sample data if file doesn't exist
        data = create_sample_data()
    except json.JSONDecodeError:
        print(f"❌ Error: {test_results_file} is not valid JSON")
        return None
    
    # Extract test results
    tests = []
    if 'suites' in data:
        for suite in data['suites']:
            if 'specs' in suite:
                for spec in suite['specs']:
                    if 'tests' in spec:
                        for test in spec['tests']:
                            # Handle different possible field names
                            test_name = test.get('title') or test.get('name', 'Unnamed Test')
                            status = test.get('status', 'unknown')
                            duration_ms = test.get('duration', 0)
                            # Convert to seconds if it's in milliseconds (likely > 100)
                            if duration_ms > 100:
                                duration_sec = duration_ms / 1000
                            else:
                                duration_sec = duration_ms
                            
                            tests.append({
                                'name': test_name,
                                'status': status,
                                'duration': duration_sec,
                                'file': spec.get('file', 'unknown')
                            })
    
    # Calculate statistics
    total_tests = len(tests)
    passed_tests = len([t for t in tests if t['status'] == 'passed'])
    failed_tests = len([t for t in tests if t['status'] == 'failed'])
    pass_rate = (passed_tests / total_tests * 100) if total_tests > 0 else 0
    total_duration = sum(t['duration'] for t in tests)
    avg_duration = total_duration / total_tests if total_tests > 0 else 0
    
    # Find slowest and fastest tests
    if tests:
        slowest_test = max(tests, key=lambda x: x['duration'])
        fastest_test = min(tests, key=lambda x: x['duration'])
    else:
        slowest_test = fastest_test = {'name': 'N/A', 'duration': 0}
    
    # Generate table rows
    table_rows = []
    for test in tests:
        status_class = "status-passed" if test['status'] == 'passed' else "status-failed"
        status_text = "✅ Passed" if test['status'] == 'passed' else "❌ Failed"
        
        # Determine performance badge
        if test['duration'] < 0.5:
            performance = "⚡ Fast"
        elif test['duration'] < 1.5:
            performance = "✓ Normal"
        else:
            performance = "🐢 Slow"
        
        table_rows.append(f"""
        <tr>
            <td style="padding: 12px; border-bottom: 1px solid #e0e0e0;">{test['name'][:60]}</td>
            <td style="padding: 12px; border-bottom: 1px solid #e0e0e0;"><span class="status-badge {status_class}">{status_text}</span></td>
            <td style="padding: 12px; border-bottom: 1px solid #e0e0e0;">{test['duration']:.2f}s</td>
            <td style="padding: 12px; border-bottom: 1px solid #e0e0e0;">{test['file']}</td>
            <td style="padding: 12px; border-bottom: 1px solid #e0e0e0;">{performance}</td>
        </tr>
        """)
    
    table_html = '\n'.join(table_rows) if table_rows else '<tr><td colspan="5" style="text-align:center; padding: 20px;">No test results found</td></tr>'
    
    # Generate HTML content without using f-strings for JavaScript
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Playwright Test Dashboard - Python Edition</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }}
        
        .container {{
            max-width: 1400px;
            margin: 0 auto;
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            overflow: hidden;
        }}
        
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            text-align: center;
        }}
        
        .header h1 {{
            font-size: 2.5em;
            margin-bottom: 10px;
        }}
        
        .header p {{
            opacity: 0.9;
            font-size: 1.1em;
        }}
        
        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            padding: 30px;
            background: #f8f9fa;
        }}
        
        .stat-card {{
            background: white;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            text-align: center;
            transition: transform 0.3s ease;
        }}
        
        .stat-card:hover {{
            transform: translateY(-5px);
        }}
        
        .stat-card.passed {{
            border-bottom: 4px solid #28a745;
        }}
        
        .stat-card.failed {{
            border-bottom: 4px solid #dc3545;
        }}
        
        .stat-card.rate {{
            border-bottom: 4px solid #17a2b8;
        }}
        
        .stat-number {{
            font-size: 48px;
            font-weight: bold;
            margin: 10px 0;
        }}
        
        .stat-label {{
            color: #666;
            font-size: 14px;
            text-transform: uppercase;
            letter-spacing: 1px;
        }}
        
        .stat-card.passed .stat-number {{ color: #28a745; }}
        .stat-card.failed .stat-number {{ color: #dc3545; }}
        .stat-card.rate .stat-number {{ color: #17a2b8; }}
        
        .charts-container {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(500px, 1fr));
            gap: 30px;
            padding: 30px;
        }}
        
        .chart-box {{
            background: white;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            position: relative;
        }}
        
        .chart-box h3 {{
            margin-bottom: 20px;
            color: #333;
            text-align: center;
        }}
        
        canvas {{
            max-height: 300px;
            width: 100%;
        }}
        
        .table-container {{
            padding: 30px;
            overflow-x: auto;
        }}
        
        table {{
            width: 100%;
            border-collapse: collapse;
            background: white;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        
        th {{
            background: #667eea;
            color: white;
            padding: 15px;
            text-align: left;
            font-weight: 600;
        }}
        
        td {{
            padding: 12px 15px;
            border-bottom: 1px solid #e0e0e0;
        }}
        
        tr:hover {{
            background: #f5f5f5;
        }}
        
        .status-badge {{
            display: inline-block;
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: bold;
        }}
        
        .status-passed {{
            background: #d4edda;
            color: #155724;
        }}
        
        .status-failed {{
            background: #f8d7da;
            color: #721c24;
        }}
        
        .footer {{
            background: #f8f9fa;
            padding: 20px;
            text-align: center;
            color: #666;
            border-top: 1px solid #e0e0e0;
        }}
        
        .btn {{
            background: #667eea;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 8px;
            cursor: pointer;
            margin: 5px;
            font-size: 14px;
            transition: background 0.3s ease;
        }}
        
        .btn:hover {{
            background: #5a67d8;
        }}
        
        .button-group {{
            text-align: center;
            padding: 20px;
        }}
        
        @media (max-width: 768px) {{
            .charts-container {{
                grid-template-columns: 1fr;
            }}
            .stats-grid {{
                grid-template-columns: 1fr;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🎭 Playwright Test Dashboard</h1>
            <p>Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
            <p>📁 Results from: {test_results_file}</p>
        </div>
        
        <div class="stats-grid">
            <div class="stat-card">
                <div class="stat-label">📊 Total Tests</div>
                <div class="stat-number">{total_tests}</div>
                <div class="stat-label">All tests executed</div>
            </div>
            <div class="stat-card passed">
                <div class="stat-label">✅ Passed</div>
                <div class="stat-number">{passed_tests}</div>
                <div class="stat-label">{pass_rate:.1f}% of total</div>
            </div>
            <div class="stat-card failed">
                <div class="stat-label">❌ Failed</div>
                <div class="stat-number">{failed_tests}</div>
                <div class="stat-label">{100-pass_rate:.1f}% of total</div>
            </div>
            <div class="stat-card rate">
                <div class="stat-label">⏱️ Avg Duration</div>
                <div class="stat-number">{avg_duration:.2f}s</div>
                <div class="stat-label">per test</div>
            </div>
        </div>
        
        <div class="charts-container">
            <div class="chart-box">
                <h3>📊 Pass/Fail Distribution</h3>
                <canvas id="pieChart"></canvas>
            </div>
            <div class="chart-box">
                <h3>⏱️ Test Duration Comparison</h3>
                <canvas id="barChart"></canvas>
            </div>
            <div class="chart-box">
                <h3>📈 Pass Rate Gauge</h3>
                <canvas id="gaugeChart"></canvas>
                <div id="gaugeCenterText" style="position: absolute; top: 55%; left: 50%; transform: translate(-50%, -50%); font-size: 28px; font-weight: bold; color: #28a745; pointer-events: none;">{pass_rate:.0f}%</div>
            </div>
            <div class="chart-box">
                <h3>🏆 Performance Highlights</h3>
                <div style="padding: 20px;">
                    <p><strong>🚀 Fastest Test:</strong> {fastest_test['name'][:50]} ({fastest_test['duration']:.2f}s)</p>
                    <p><strong>🐢 Slowest Test:</strong> {slowest_test['name'][:50]} ({slowest_test['duration']:.2f}s)</p>
                    <p><strong>📊 Pass Rate:</strong> {pass_rate:.1f}%</p>
                    <p><strong>⏱️ Total Duration:</strong> {total_duration:.2f}s</p>
                </div>
            </div>
        </div>
        
        <div class="table-container">
            <h3 style="margin-bottom: 20px;">📋 Detailed Test Results</h3>
            <table>
                <thead>
                    <tr>
                        <th>Test Name</th>
                        <th>Status</th>
                        <th>Duration (seconds)</th>
                        <th>File</th>
                        <th>Performance</th>
                    </tr>
                </thead>
                <tbody>
                    {table_html}
                </tbody>
            </table>
        </div>
        
        <div class="button-group">
            <button class="btn" onclick="location.reload()">🔄 Refresh Data</button>
            <button class="btn" onclick="exportToCSV()">📥 Export to CSV</button>
        </div>
        
        <div class="footer">
            <p>💡 <strong>Tip:</strong> Run <code>python test_dashboard.py --update</code> to refresh results</p>
            <p>🔧 Dashboard generated by Python Test Dashboard v1.0</p>
        </div>
    </div>
    
    <script>
        // Test data
        const tests = {json.dumps(tests)};
        const passedCount = {passed_tests};
        const failedCount = {failed_tests};
        
        // Pie Chart
        const pieCtx = document.getElementById('pieChart').getContext('2d');
        new Chart(pieCtx, {{
            type: 'pie',
            data: {{
                labels: ['✅ Passed', '❌ Failed'],
                datasets: [{{
                    data: [passedCount, failedCount],
                    backgroundColor: ['#28a745', '#dc3545'],
                    borderWidth: 0
                }}]
            }},
            options: {{
                responsive: true,
                maintainAspectRatio: true,
                plugins: {{
                    legend: {{ position: 'bottom' }}
                }}
            }}
        }});
        
        // Bar Chart - Top 10 longest tests
        const sortedTests = [...tests].sort((a, b) => b.duration - a.duration).slice(0, 10);
        const barCtx = document.getElementById('barChart').getContext('2d');
        new Chart(barCtx, {{
            type: 'bar',
            data: {{
                labels: sortedTests.map(t => t.name.length > 30 ? t.name.substring(0, 27) + '...' : t.name),
                datasets: [{{
                    label: 'Duration (seconds)',
                    data: sortedTests.map(t => t.duration),
                    backgroundColor: sortedTests.map(t => t.status === 'passed' ? '#28a745' : '#dc3545'),
                    borderRadius: 8
                }}]
            }},
            options: {{
                responsive: true,
                maintainAspectRatio: true,
                scales: {{
                    y: {{
                        beginAtZero: true,
                        title: {{ display: true, text: 'Seconds' }}
                    }}
                }},
                plugins: {{
                    tooltip: {{
                        callbacks: {{
                            label: (ctx) => ctx.raw.toFixed(2) + ' seconds'
                        }}
                    }}
                }}
            }}
        }});
        
        // Gauge Chart
        const passRate = {pass_rate};
        const gaugeCtx = document.getElementById('gaugeChart').getContext('2d');
        new Chart(gaugeCtx, {{
            type: 'doughnut',
            data: {{
                labels: ['Pass Rate', 'Remaining'],
                datasets: [{{
                    data: [passRate, 100 - passRate],
                    backgroundColor: ['#28a745', '#e0e0e0'],
                    borderWidth: 0,
                    cutout: '70%'
                }}]
            }},
            options: {{
                responsive: true,
                maintainAspectRatio: true,
                plugins: {{
                    tooltip: {{
                        callbacks: {{
                            label: (ctx) => ctx.label + ': ' + ctx.raw.toFixed(1) + '%'
                        }}
                    }},
                    legend: {{ position: 'bottom' }}
                }}
            }}
        }});
        
        // Export to CSV function
        function exportToCSV() {{
            let csv = 'Test Name,Status,Duration (seconds),File\\n';
            tests.forEach(test => {{
                csv += `"${{test.name}}",${{test.status}},${{test.duration}},${{test.file}}\\n`;
            }});
            
            const blob = new Blob([csv], {{ type: 'text/csv' }});
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'test_results.csv';
            a.click();
            URL.revokeObjectURL(url);
            alert('✅ CSV file downloaded!');
        }}
    </script>
</body>
</html>"""
    
    return html_content

def create_sample_data():
    """Create sample test data for demonstration"""
    return {
        "suites": [{
            "specs": [{
                "file": "sample_tests.py",
                "tests": [
                    {"title": "Homepage loads successfully", "status": "passed", "duration": 1234},
                    {"title": "User login functionality", "status": "passed", "duration": 2345},
                    {"title": "Dashboard data loads", "status": "failed", "duration": 3456},
                    {"title": "API response time", "status": "passed", "duration": 567},
                    {"title": "Database connection", "status": "passed", "duration": 890},
                ]
            }]
        }]
    }

def run_dashboard(test_results_file='leaderboard_test_results.json', port=8000):
    """Run the dashboard server"""
    
    print("🎭 Starting Playwright Test Dashboard...")
    print("=" * 50)
    
    # Check if results file exists
    if not os.path.exists(test_results_file):
        print(f"⚠️ Warning: {test_results_file} not found")
        print("📝 Creating sample data for demonstration...")
    
    # Create HTML content
    html_content = create_dashboard_html(test_results_file)
    
    if html_content is None:
        print("❌ Failed to create dashboard")
        return
    
    # Create temporary HTML file
    temp_file = os.path.join(tempfile.gettempdir(), 'playwright_dashboard.html')
    with open(temp_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"✅ Dashboard created at: {temp_file}")
    print(f"🌐 Opening dashboard in your browser...")
    
    # Open in browser
    webbrowser.open(f'file://{temp_file}')
    
    print(f"📊 Dashboard opened successfully!")
    print("💡 Press Ctrl+C in terminal to stop the server (if running)")
    
    # Keep the script running (optional)
    try:
        while True:
            import time
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n👋 Dashboard closed")

def update_test_results():
    """Run the comprehensive test suite to update results"""
    print("🔄 Running test suite to update results...")
    print("=" * 50)
    
    # Import and run the test suite
    try:
        import leaderboard_comprehensive_tests
        leaderboard_comprehensive_tests.run_comprehensive_tests()
        print("✅ Test results updated successfully!")
        return True
    except ImportError:
        print("❌ Could not find leaderboard_comprehensive_tests.py")
        print("💡 Please run the test script manually first:")
        print("   python leaderboard_comprehensive_tests.py")
        return False
    except Exception as e:
        print(f"❌ Error running tests: {e}")
        return False

if __name__ == "__main__":
    import sys
    
    # Parse command line arguments
    if len(sys.argv) > 1:
        if sys.argv[1] == '--update':
            update_test_results()
        elif sys.argv[1] == '--help':
            print("""
Playwright Test Dashboard - Usage:
    
    python test_dashboard.py              # Start dashboard with existing results
    python test_dashboard.py --update     # Run tests and update results first
    python test_dashboard.py --help       # Show this help message
    
Options:
    --update    : Run the comprehensive test suite before starting dashboard
            """)
        else:
            run_dashboard()
    else:
        run_dashboard()