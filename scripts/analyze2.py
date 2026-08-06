# -*- coding: utf-8 -*-
import csv, re
from collections import defaultdict

SRC = r'C:\Users\devzu\Documents\research.csv'
OUT_DIR = r'C:\Users\devzu\AppData\Local\Temp\claude\C--Users-devzu-Documents\d3092015-96e6-4b53-9b60-a0775041dae0\scratchpad'

with open(SRC, encoding='utf-8') as f:
    lines = f.readlines()
data_lines = lines[10:]
reader = csv.reader(data_lines)
parsed = []
for r in reader:
    if len(r) < 9: continue
    title, source, views, users, vpu, avg_eng, events, key_event, revenue = r[:9]
    try:
        views=float(views); users=float(users); revenue=float(revenue)
    except ValueError:
        continue
    parsed.append({'title':title,'source':source,'views':views,'users':users,'revenue':revenue})

by_title = defaultdict(lambda: {'views':0.0,'revenue':0.0})
for p in parsed:
    d = by_title[p['title']]
    d['views'] += p['views']
    d['revenue'] += p['revenue']

# --- brand grouping ---
def brand_of(title):
    if title.endswith('- 더픽'): return '더픽'
    if '생활정보 나침반' in title: return '생활정보 나침반'
    if '주카 비즈' in title: return '주카 비즈'
    return '기타/미분류'

brand_stats = defaultdict(lambda: {'views':0.0,'revenue':0.0,'pages':0})
for title,d in by_title.items():
    b = brand_of(title)
    brand_stats[b]['views'] += d['views']
    brand_stats[b]['revenue'] += d['revenue']
    brand_stats[b]['pages'] += 1

with open(OUT_DIR + r'\brand_stats.tsv','w',encoding='utf-8') as out:
    out.write("brand\tpages\tviews\trevenue\trpm\n")
    for b,d in sorted(brand_stats.items(), key=lambda kv:-kv[1]['revenue']):
        rpm = d['revenue']/d['views']*1000 if d['views'] else 0
        out.write(f"{b}\t{d['pages']}\t{d['views']:.0f}\t{d['revenue']:.2f}\t{rpm:.2f}\n")

# --- pareto: revenue concentration ---
title_list = sorted(by_title.items(), key=lambda kv: -kv[1]['revenue'])
total_rev = sum(d['revenue'] for _,d in title_list)
total_pages = len(title_list)
cum = 0.0
milestones = [0.5,0.7,0.8,0.9,0.95]
mi = 0
with open(OUT_DIR + r'\pareto.txt','w',encoding='utf-8') as out:
    out.write(f"Total unique pages(keywords): {total_pages}, total revenue: {total_rev:.2f}\n")
    for i,(t,d) in enumerate(title_list,1):
        cum += d['revenue']
        if mi < len(milestones) and cum/total_rev >= milestones[mi]:
            out.write(f"Top {i} pages ({i/total_pages*100:.1f}% of pages) = {milestones[mi]*100:.0f}% of revenue\n")
            mi += 1

# --- pattern keyword tagging ---
patterns = {
    '바로가기(퀵링크)': r'바로가기',
    '고객센터/AS': r'고객센터|AS센터|as\s*센터|상담원|상담사',
    '앱/설치 다운로드': r'앱\s*다운로드|설치|다운로드',
    '신청/조회(정부지원)': r'신청|지원금|보조금|바우처|연금|모의계산',
    '보험금청구': r'보험금|보험\s*청구',
    '홈페이지': r'홈페이지',
    '고유가/생활지원금': r'고유가|생활지원금|민생지원금',
    '테스트/성격유형': r'테스트|MBTI|SBTI',
    '편성표/방송': r'편성표|온에어|OTT|시청',
    '연예/투표/팬덤': r'투표|인스타|팬카페|콘서트|티켓',
    '정당가입탈당': r'당원가입|탈당|입당',
}
tag_stats = defaultdict(lambda: {'views':0.0,'revenue':0.0,'pages':0})
untagged_rev = 0.0
untagged_pages = 0
for title,d in by_title.items():
    matched = False
    for tag,pat in patterns.items():
        if re.search(pat, title, re.IGNORECASE):
            tag_stats[tag]['views'] += d['views']
            tag_stats[tag]['revenue'] += d['revenue']
            tag_stats[tag]['pages'] += 1
            matched = True
    if not matched:
        untagged_rev += d['revenue']
        untagged_pages += 1

with open(OUT_DIR + r'\pattern_tags.tsv','w',encoding='utf-8') as out:
    out.write("pattern\tpages\tviews\trevenue\trpm\tavg_revenue_per_page\n")
    for tag,d in sorted(tag_stats.items(), key=lambda kv:-kv[1]['revenue']):
        rpm = d['revenue']/d['views']*1000 if d['views'] else 0
        avgp = d['revenue']/d['pages'] if d['pages'] else 0
        out.write(f"{tag}\t{d['pages']}\t{d['views']:.0f}\t{d['revenue']:.2f}\t{rpm:.2f}\t{avgp:.3f}\n")
    out.write(f"(미분류)\t{untagged_pages}\t-\t{untagged_rev:.2f}\t-\t{untagged_rev/untagged_pages if untagged_pages else 0:.3f}\n")

# --- low-view but nonzero revenue pages: proof of "certain top ranking + clear CTA" niche pages ---
niche = [(t,d) for t,d in by_title.items() if 0 < d['views'] <= 300 and d['revenue']>0]
niche.sort(key=lambda x: -(x[1]['revenue']/x[1]['views']))
with open(OUT_DIR + r'\niche_low_traffic_high_rpm.tsv','w',encoding='utf-8') as out:
    out.write("title\tviews\trevenue\trpm\n")
    for t,d in niche[:60]:
        rpm = d['revenue']/d['views']*1000
        out.write(f"{t}\t{d['views']:.0f}\t{d['revenue']:.4f}\t{rpm:.2f}\n")

print("done")
