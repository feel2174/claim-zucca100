# -*- coding: utf-8 -*-
import csv
from collections import defaultdict

SRC = r'C:\Users\devzu\Documents\research.csv'
OUT_DIR = r'C:\Users\devzu\AppData\Local\Temp\claude\C--Users-devzu-Documents\d3092015-96e6-4b53-9b60-a0775041dae0\scratchpad'

rows = []
with open(SRC, encoding='utf-8') as f:
    lines = f.readlines()

# header is at index 9 (line 10), data starts at index 10
header = lines[9].strip().split(',')
data_lines = lines[10:]

reader = csv.reader(data_lines)
parsed = []
for r in reader:
    if len(r) < 9:
        continue
    title, source, views, users, views_per_user, avg_eng, events, key_event, revenue = r[:9]
    try:
        views = float(views)
        users = float(users)
        events = float(events)
        revenue = float(revenue)
    except ValueError:
        continue
    parsed.append({
        'title': title,
        'source': source,
        'views': views,
        'users': users,
        'events': events,
        'revenue': revenue,
    })

print(f"Total parsed rows: {len(parsed)}")

total_views = sum(p['views'] for p in parsed)
total_revenue = sum(p['revenue'] for p in parsed)
print(f"TOTAL views: {total_views:,.0f}  TOTAL revenue: {total_revenue:,.2f}  overall RPM: {total_revenue/total_views*1000:.2f}")

# ---- Aggregate by page title ----
by_title = defaultdict(lambda: {'views':0.0,'users':0.0,'events':0.0,'revenue':0.0,'sources':defaultdict(float)})
for p in parsed:
    d = by_title[p['title']]
    d['views'] += p['views']
    d['users'] += p['users']
    d['events'] += p['events']
    d['revenue'] += p['revenue']
    d['sources'][p['source']] += p['views']

title_stats = []
for title, d in by_title.items():
    rpm = (d['revenue']/d['views']*1000) if d['views']>0 else 0
    top_source = max(d['sources'].items(), key=lambda kv: kv[1])[0] if d['sources'] else ''
    title_stats.append((title, d['views'], d['users'], d['revenue'], rpm, top_source, len(d['sources'])))

# ---- Aggregate by source/medium ----
by_source = defaultdict(lambda: {'views':0.0,'revenue':0.0})
for p in parsed:
    d = by_source[p['source']]
    d['views'] += p['views']
    d['revenue'] += p['revenue']

source_stats = []
for source, d in by_source.items():
    rpm = (d['revenue']/d['views']*1000) if d['views']>0 else 0
    source_stats.append((source, d['views'], d['revenue'], rpm))

with open(OUT_DIR + r'\by_title_all.tsv', 'w', encoding='utf-8') as out:
    out.write("title\tviews\tusers\trevenue\trpm\ttop_source\tn_sources\n")
    for row in sorted(title_stats, key=lambda x: -x[3]):
        out.write("\t".join(str(x) for x in row) + "\n")

with open(OUT_DIR + r'\by_source_all.tsv', 'w', encoding='utf-8') as out:
    out.write("source\tviews\trevenue\trpm\n")
    for row in sorted(source_stats, key=lambda x: -x[1]):
        out.write("\t".join(str(x) for x in row) + "\n")

# Top by RPM among pages with meaningful traffic (views >= 100)
sig = [t for t in title_stats if t[1] >= 100]
with open(OUT_DIR + r'\top_rpm_min100views.tsv', 'w', encoding='utf-8') as out:
    out.write("title\tviews\tusers\trevenue\trpm\ttop_source\tn_sources\n")
    for row in sorted(sig, key=lambda x: -x[4])[:80]:
        out.write("\t".join(str(x) for x in row) + "\n")

# Top by total revenue
with open(OUT_DIR + r'\top_revenue.tsv', 'w', encoding='utf-8') as out:
    out.write("title\tviews\tusers\trevenue\trpm\ttop_source\tn_sources\n")
    for row in sorted(title_stats, key=lambda x: -x[3])[:80]:
        out.write("\t".join(str(x) for x in row) + "\n")

# Naver-driven pages specifically (title mostly from naver search)
naver_keys = ['naver']
naver_rows = []
for title, d in by_title.items():
    nv = sum(v for s,v in d['sources'].items() if 'naver' in s.lower())
    if d['views']>0 and nv/d['views'] >= 0.5 and d['views']>=50:
        rpm = (d['revenue']/d['views']*1000) if d['views']>0 else 0
        naver_rows.append((title, d['views'], nv/d['views'], d['revenue'], rpm))

with open(OUT_DIR + r'\naver_dominant_pages.tsv', 'w', encoding='utf-8') as out:
    out.write("title\tviews\tnaver_share\trevenue\trpm\n")
    for row in sorted(naver_rows, key=lambda x: -x[3]):
        out.write("\t".join(str(x) for x in row) + "\n")

print("DONE. Wrote by_title_all.tsv, by_source_all.tsv, top_rpm_min100views.tsv, top_revenue.tsv, naver_dominant_pages.tsv")
print(f"Unique titles: {len(by_title)}  Unique sources: {len(by_source)}  Naver-dominant significant pages: {len(naver_rows)}")
