# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from font_b64 import regular, semibold, bold, extrabold

TEMPLATE = r"""<!DOCTYPE html>
<meta charset="utf-8">
<title>실비보험 청구방법 · 보험사별 보험금 청구 바로가기 38곳 | 청구친구</title>
<meta name="description" content="삼성생명·현대해상 등 38개 보험사의 보험금 청구 페이지 바로가기 모음. 실손(실비)보험 청구방법, 필요서류, 처리기간, 소멸시효까지 한 번에 확인하세요.">
<style>
  @font-face {
    font-family: 'Pretendard';
    font-weight: 400;
    font-style: normal;
    font-display: swap;
    src: url(data:font/woff2;base64,__REGULAR__) format('woff2');
  }
  @font-face {
    font-family: 'Pretendard';
    font-weight: 600;
    font-style: normal;
    font-display: swap;
    src: url(data:font/woff2;base64,__SEMIBOLD__) format('woff2');
  }
  @font-face {
    font-family: 'Pretendard';
    font-weight: 700;
    font-style: normal;
    font-display: swap;
    src: url(data:font/woff2;base64,__BOLD__) format('woff2');
  }
  @font-face {
    font-family: 'Pretendard';
    font-weight: 800;
    font-style: normal;
    font-display: swap;
    src: url(data:font/woff2;base64,__EXTRABOLD__) format('woff2');
  }

  :root {
    color-scheme: light;
    --page: #ffffff;
    --band: #eef4ff;
    --band-ink: #1c2a4d;
    --surface: #ffffff;
    --surface-2: #f6f7f9;
    --ink: #191b1f;
    --ink-2: #5b606b;
    --muted: #9297a1;
    --line: #ececee;
    --border: rgba(25,27,31,0.08);
    --accent: #3562f7;
    --accent-ink: #ffffff;
    --accent-soft: #eaf0ff;
    --accent-2: #e8823c;
    --shadow: 0 1px 2px rgba(25,27,31,0.04), 0 8px 20px rgba(25,27,31,0.05);
  }
  /* Committed to a single light theme by design — see chat context. */
  :root[data-theme="dark"] { color-scheme: light; }

  * { box-sizing: border-box; }
  body {
    margin: 0;
    background: var(--page);
    color: var(--ink);
    font-family: 'Pretendard', -apple-system, BlinkMacSystemFont, 'Apple SD Gothic Neo',
      'Malgun Gothic', system-ui, sans-serif;
    line-height: 1.6;
    -webkit-font-smoothing: antialiased;
  }
  a { color: inherit; }
  .num { font-variant-numeric: tabular-nums; }

  /* ---- header ---- */
  header.site {
    display: flex;
    align-items: center;
    justify-content: space-between;
    max-width: 1080px;
    margin: 0 auto;
    padding: 24px 24px 22px;
  }
  .brand { display: flex; align-items: center; gap: 8px; font-weight: 800; font-size: 18px; letter-spacing: -0.01em; }
  .brand .mark {
    width: 30px; height: 30px; border-radius: 9px; background: var(--accent);
    color: var(--accent-ink); display: flex; align-items: center; justify-content: center;
    flex-shrink: 0;
  }
  nav.site-nav { display: flex; gap: 30px; font-size: 14px; font-weight: 600; color: var(--ink-2); }
  nav.site-nav a { text-decoration: none; }
  nav.site-nav a:hover { color: var(--ink); }

  /* ---- hero: soft pale band, not a saturated block ---- */
  .hero { background: var(--band); }
  .hero-inner { max-width: 1080px; margin: 0 auto; padding: 32px 24px 24px; }
  .hero-top { display: flex; align-items: flex-start; justify-content: space-between; gap: 16px; flex-wrap: wrap; margin-bottom: 14px; }
  .kicker {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: rgba(255,255,255,0.7);
    color: var(--accent);
    font-size: 12px;
    font-weight: 700;
    padding: 5px 11px;
    border-radius: 999px;
    flex-shrink: 0;
    white-space: nowrap;
  }
  h1.hero-title {
    font-size: 27px;
    font-weight: 800;
    letter-spacing: -0.02em;
    line-height: 1.3;
    margin: 0 0 6px;
    text-wrap: balance;
    max-width: 22ch;
    color: var(--band-ink);
  }
  h1.hero-title .accent { color: var(--accent); }
  .hero-sub {
    font-size: 14px;
    color: var(--ink-2);
    max-width: 50ch;
    margin: 0;
  }
  .hero-controls { display: flex; align-items: center; gap: 10px; flex-wrap: wrap; margin-top: 16px; }
  .search-bar {
    display: flex;
    gap: 6px;
    background: var(--surface);
    border-radius: 12px;
    padding: 4px;
    flex: 1 1 320px;
    max-width: 420px;
    box-shadow: var(--shadow);
  }
  .search-bar input {
    flex: 1;
    border: none;
    background: transparent;
    padding: 10px 12px;
    font-size: 14px;
    color: var(--ink);
    outline: none;
    font-family: inherit;
  }
  .search-bar input::placeholder { color: var(--muted); }
  .search-bar button {
    background: var(--accent);
    color: var(--accent-ink);
    border: none;
    border-radius: 9px;
    padding: 0 18px;
    font-weight: 700;
    font-size: 13.5px;
    cursor: pointer;
    font-family: inherit;
  }
  .chips { display: flex; gap: 6px; flex-wrap: wrap; }
  .chip {
    background: rgba(255,255,255,0.6);
    border: none;
    color: var(--band-ink);
    font-size: 12px;
    font-weight: 600;
    padding: 6px 12px;
    border-radius: 999px;
    cursor: pointer;
    font-family: inherit;
  }
  .chip:hover { background: var(--surface); }

  /* ---- main ---- */
  main { max-width: 1080px; margin: 0 auto; padding: 36px 24px 80px; }
  section { margin-bottom: 40px; }
  .section-head { display: flex; align-items: center; justify-content: space-between; margin-bottom: 16px; gap: 12px; flex-wrap: wrap; }
  .eyebrow { font-size: 11.5px; font-weight: 800; letter-spacing: 0.09em; text-transform: uppercase; color: var(--accent); margin-bottom: 8px; }
  h2 { font-size: 18px; font-weight: 800; margin: 0; letter-spacing: -0.01em; }
  .section-sub { font-size: 14px; color: var(--ink-2); margin: 6px 0 0; max-width: 60ch; }
  .section-count { font-size: 13px; color: var(--muted); font-weight: 600; white-space: nowrap; }

  /* ---- category segmented control ---- */
  .segmented { display: inline-flex; background: var(--surface-2); border-radius: 10px; padding: 3px; gap: 2px; flex-wrap: wrap; }
  .seg-btn {
    border: none; background: transparent; color: var(--ink-2);
    font-family: inherit; font-size: 12.5px; font-weight: 700;
    padding: 7px 13px; border-radius: 7px; cursor: pointer;
  }
  .seg-btn .c { font-weight: 600; color: var(--muted); margin-left: 4px; }
  .seg-btn.is-active { background: var(--surface); color: var(--ink); box-shadow: var(--shadow); }
  .seg-btn.is-active .c { color: var(--accent); }

  /* ---- FAQ: accordion, one row at a time ---- */
  .faq-list { border: 1px solid var(--line); border-radius: 14px; overflow: hidden; }
  .faq-row { border-top: 1px solid var(--line); }
  .faq-row:first-child { border-top: none; }
  .faq-row summary {
    display: flex; align-items: center; justify-content: space-between; gap: 12px;
    padding: 14px 20px; cursor: pointer; list-style: none;
    font-size: 14px; font-weight: 700; color: var(--ink);
  }
  .faq-row summary::-webkit-details-marker { display: none; }
  .faq-row summary::after { content: '⌄'; color: var(--muted); font-size: 13px; flex-shrink: 0; }
  .faq-row[open] summary::after { color: var(--accent); content: '⌃'; }
  .faq-a { font-size: 13.5px; color: var(--ink-2); margin: 0; padding: 0 20px 16px; line-height: 1.7; }
  .faq-a b { color: var(--ink); font-weight: 700; }

  /* ---- company grid: compact list rows ---- */
  .co-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px; }
  .co-card {
    background: var(--surface);
    border: 1px solid var(--line);
    border-radius: 10px;
    padding: 10px 12px;
    display: flex;
    align-items: center;
    gap: 10px;
    text-decoration: none;
    transition: box-shadow .15s ease, border-color .15s ease;
  }
  .co-card:hover { box-shadow: var(--shadow); border-color: transparent; }
  .co-badge {
    width: 28px; height: 28px; border-radius: 8px; background: var(--surface-2); color: var(--ink);
    display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 11.5px; flex-shrink: 0;
  }
  .co-name-col { min-width: 0; flex: 1; display: flex; flex-direction: column; }
  .co-name { font-weight: 800; font-size: 13.5px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
  .co-tag { font-size: 10.5px; font-weight: 600; color: var(--muted); }
  .co-arrow { font-size: 14px; color: var(--accent); flex-shrink: 0; }
  .co-card[hidden] { display: none; }

  .empty-state { text-align: center; padding: 40px 20px; color: var(--muted); font-size: 14px; display: none; }
  .empty-state.show { display: block; }

  .notice {
    background: var(--surface-2);
    border-radius: 14px;
    padding: 18px 22px;
    font-size: 13px;
    color: var(--ink-2);
  }
  .notice b { color: var(--ink); }
  .notice ul { margin: 0; padding-left: 18px; }
  .notice li { margin-bottom: 8px; }
  .notice li:last-child { margin-bottom: 0; }

  /* ---- claim guide section ---- */
  .guide-steps { display: grid; grid-template-columns: repeat(5, 1fr); gap: 10px; }
  .guide-step { background: var(--surface); border: 1px solid var(--line); border-radius: 12px; padding: 16px 14px; }
  .guide-step-num {
    width: 24px; height: 24px; border-radius: 999px; background: var(--accent-soft); color: var(--accent);
    display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 12px; margin-bottom: 10px;
  }
  .guide-step h3 { font-size: 13.5px; font-weight: 800; margin: 0 0 6px; color: var(--ink); }
  .guide-step p { font-size: 12.5px; color: var(--ink-2); margin: 0; line-height: 1.6; }

  .guide-meta { display: flex; gap: 10px; margin-top: 14px; flex-wrap: wrap; }
  .guide-stat { flex: 1; min-width: 140px; background: var(--surface-2); border-radius: 12px; padding: 14px 16px; }
  .guide-stat b { display: block; font-size: 18px; color: var(--accent); margin-bottom: 2px; }
  .guide-stat span { font-size: 12px; color: var(--ink-2); }

  .guide-docs { margin-top: 14px; border: 1px solid var(--line); border-radius: 14px; overflow: hidden; }
  .guide-docs table { width: 100%; border-collapse: collapse; font-size: 12.5px; }
  .guide-docs th, .guide-docs td { text-align: left; padding: 10px 14px; border-top: 1px solid var(--line); }
  .guide-docs thead th { background: var(--surface-2); color: var(--ink-2); font-weight: 700; border-top: none; }
  .guide-docs tbody th { color: var(--ink); font-weight: 700; white-space: nowrap; }
  .guide-docs td { color: var(--ink-2); }

  .guide-note { font-size: 12.5px; color: var(--muted); text-align: center; margin: 14px 0 0; }
  .guide-cta { margin-top: 14px; text-align: center; }
  .guide-cta a {
    display: inline-flex; align-items: center; gap: 6px; background: var(--accent); color: var(--accent-ink);
    font-weight: 700; font-size: 13.5px; padding: 11px 20px; border-radius: 999px; text-decoration: none;
  }

  footer { border-top: 1px solid var(--line); }
  .footer-inner { max-width: 1080px; margin: 0 auto; padding: 36px 24px; }
  .footer-brand { display: flex; align-items: center; gap: 9px; font-weight: 800; font-size: 15px; margin-bottom: 8px; }
  .footer-brand .mark {
    width: 24px; height: 24px; border-radius: 7px; background: var(--accent); color: var(--accent-ink);
    display: flex; align-items: center; justify-content: center; flex-shrink: 0;
  }
  footer p { font-size: 12.5px; color: var(--muted); margin: 4px 0 0; max-width: 62ch; }

  @media (max-width: 900px) {
    .co-grid { grid-template-columns: repeat(2, 1fr); }
    nav.site-nav { display: none; }
    .hero-top { flex-direction: column; }
    .guide-steps { grid-template-columns: repeat(2, 1fr); }
  }
  @media (max-width: 560px) {
    .co-grid { grid-template-columns: 1fr; }
    h1.hero-title { font-size: 22px; }
    .guide-steps { grid-template-columns: 1fr; }
  }
</style>

<header class="site">
  <div class="brand">
    <span class="mark">
      <svg width="15" height="15" viewBox="0 0 24 24" fill="none"><path d="M12 2L4 5v6c0 5.2 3.4 9.6 8 11 4.6-1.4 8-5.8 8-11V5l-8-3z" fill="currentColor" opacity="0.95"/><path d="M8.5 12.2l2.4 2.4 4.6-4.8" stroke="var(--surface)" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
    </span>
    청구친구
  </div>
  <nav class="site-nav">
    <a href="#guide">청구방법</a>
    <a href="#life">생명보험</a>
    <a href="#nonlife">손해보험</a>
    <a href="#silson24">실손24</a>
    <a href="#notice">안내</a>
    <a href="#disclaimer">면책조항</a>
  </nav>
</header>

<div class="hero">
  <div class="hero-inner">
    <div class="hero-top">
      <h1 class="hero-title">보험사 이름만 알면,<br><span class="accent">청구친구</span>에서 바로.</h1>
      <span class="kicker">✦ 공식 페이지로만 연결</span>
    </div>
    <p class="hero-sub">38개 보험사의 청구 창구를 한곳에 모았어요. 검색하고 눌러서 공식 페이지로 이동하세요.</p>
    <div class="hero-controls">
      <form class="search-bar" onsubmit="return false;">
        <input id="searchInput" type="text" placeholder="보험사명을 입력하세요 (예: 삼성화재, 교보생명)" oninput="filterCompanies()">
        <button type="button" onclick="document.getElementById('searchInput').focus()">검색</button>
      </form>
      <div class="chips">
        <span class="chip" onclick="setSearch('삼성')">삼성</span>
        <span class="chip" onclick="setSearch('현대')">현대해상</span>
        <span class="chip" onclick="setSearch('교보')">교보생명</span>
        <span class="chip" onclick="setSearch('한화')">한화</span>
        <span class="chip" onclick="setSearch('KB')">KB손해보험</span>
      </div>
    </div>
  </div>
</div>

<main>

  <section>
    <div class="section-head">
      <h2>어떤 보험 청구가 필요하세요?</h2>
      <div class="segmented">
        <button class="seg-btn is-active" onclick="setCategory('all', this)">전체 <span class="c num">38</span></button>
        <button class="seg-btn" onclick="setCategory('life', this)">생명보험 <span class="c num">22</span></button>
        <button class="seg-btn" onclick="setCategory('non-life', this)">손해보험 <span class="c num">16</span></button>
        <button class="seg-btn" onclick="setCategory('direct', this)">바로 청구 가능 <span class="c num">34</span></button>
      </div>
    </div>
  </section>

  <section id="guide">
    <div class="section-head">
      <div>
        <div class="eyebrow">How to claim</div>
        <h2>실비보험 청구방법, 5단계로 끝내기</h2>
      </div>
    </div>

    <div class="guide-steps">
      <div class="guide-step">
        <div class="guide-step-num">1</div>
        <h3>진료·치료 받기</h3>
        <p>병원·약국에서 치료받고 진료비 영수증, 처방전(약 처방 시)을 꼭 챙겨두세요.</p>
      </div>
      <div class="guide-step">
        <div class="guide-step-num">2</div>
        <h3>서류 준비하기</h3>
        <p>치료비가 10만 원 이하면 영수증·처방전만으로 충분한 경우가 많아요. 초과 시 진단서가 추가로 필요해요.</p>
      </div>
      <div class="guide-step">
        <div class="guide-step-num">3</div>
        <h3>접수 채널 선택</h3>
        <p>실손24 연계 병원이면 병원에서 바로 전송돼요. 아니라면 가입한 보험사의 앱·홈페이지·팩스로 접수하세요.</p>
      </div>
      <div class="guide-step">
        <div class="guide-step-num">4</div>
        <h3>심사 진행</h3>
        <p>보험사가 제출 서류를 확인하고 심사해요. 서류가 부족하면 추가 요청이 올 수 있어요.</p>
      </div>
      <div class="guide-step">
        <div class="guide-step-num">5</div>
        <h3>보험금 지급</h3>
        <p>서류가 갖춰지면 3영업일 이내 지급이 원칙이에요. 조사가 필요하면 최대 30영업일까지 걸릴 수 있어요.</p>
      </div>
    </div>

    <div class="guide-meta">
      <div class="guide-stat"><b>3영업일</b><span>서류 완비 시 표준 지급 기한</span></div>
      <div class="guide-stat"><b>최대 30영업일</b><span>조사·심사가 필요한 경우</span></div>
      <div class="guide-stat"><b>3년</b><span>보험금 청구권 소멸시효(사고일 기준)</span></div>
    </div>

    <div class="guide-docs">
      <div style="overflow-x:auto">
        <table>
          <thead><tr><th>청구 유형</th><th>10만 원 이하</th><th>10만 원 초과</th></tr></thead>
          <tbody>
            <tr><th>통원(외래)</th><td>진료비 영수증 + 처방전(약제비 영수증)</td><td>위 서류 + 진단서 또는 진료확인서</td></tr>
            <tr><th>입원</th><td>입퇴원확인서 + 진료비 계산서·영수증</td><td>위 서류 + 진단서(수술 시 수술확인서 추가)</td></tr>
            <tr><th>공통</th><td colspan="2">보험사 소정 청구서 양식, 신분증 사본, 보험금 수령 계좌 사본</td></tr>
          </tbody>
        </table>
      </div>
    </div>

    <p class="guide-note">정확한 서류·기준은 가입한 상품과 보험사 약관마다 달라요. 아래에서 가입한 보험사를 찾아 공식 안내를 확인하세요.</p>
    <div class="guide-cta">
      <a href="#life">가입한 보험사 찾아 바로 접수하기 →</a>
    </div>
  </section>

  <section>
    <div class="section-head"><h2>보험금 청구, 왜 유독 어렵게 느껴질까요?</h2></div>
    <div class="faq-list">

      <details class="faq-row" open>
        <summary>왜 보험금 청구는 항상 복잡하고 어렵게 느껴질까요?</summary>
        <p class="faq-a"><b>청구 창구가 보험사마다 다 다르기 때문</b>이에요. 어떤 곳은 앱, 어떤 곳은 홈페이지 사이버창구, 어떤 곳은 팩스·우편까지 써야 해서 매번 어디서 청구할지부터 찾아야 합니다.</p>
      </details>

      <details class="faq-row">
        <summary>청구 페이지를 찾아도 또 헤매게 되는 이유는요?</summary>
        <p class="faq-a">보험사 홈페이지는 상품 가입·상담·이벤트 메뉴에 밀려 <b>"보험금 청구" 메뉴가 몇 단계 안쪽에 숨어있는 경우</b>가 많아요. 모바일에서는 더 찾기 힘들죠.</p>
      </details>

      <details class="faq-row">
        <summary>청구 기한이 따로 있나요? 늦으면 못 받나요?</summary>
        <p class="faq-a">보험금 청구권의 소멸시효는 <b>원칙적으로 사고일로부터 3년</b>이에요. 이 기간이 지나면 정당한 사유가 있어도 청구가 어려워질 수 있어요.</p>
      </details>

      <details class="faq-row">
        <summary>여러 보험사에 가입돼 있으면 한 번에 청구할 수 없나요?</summary>
        <p class="faq-a"><b>청구는 가입한 보험사마다 각각 진행</b>해야 해요. 통합 조회 서비스가 있어도 최종 접수는 보험사별 창구를 거쳐야 해서, 한곳에 모아둔 바로가기가 더 유용해요.</p>
      </details>

      <details class="faq-row">
        <summary>실비(실손의료비) 청구할 때 필요한 서류가 뭔가요?</summary>
        <p class="faq-a">일반적으로 <b>진단서(또는 진료확인서)·진료비 계산서·영수증·처방전(약제비 영수증)</b>이 필요해요. 통원 치료비가 <b>10만 원 이하</b>면 대부분 보험사가 진단서 없이 영수증·처방전만으로도 접수해줘서, 굳이 발급비를 들여 진단서를 뗄 필요가 없는 경우가 많아요.</p>
      </details>

      <details class="faq-row">
        <summary>보험금은 청구 후 며칠 만에 들어오나요?</summary>
        <p class="faq-a">표준약관 기준으로 서류가 갖춰지면 <b>3영업일 이내</b> 지급이 원칙이에요. 다만 사고 조사나 심사가 필요한 경우엔 최대 30영업일까지 늦어질 수 있어요.</p>
      </details>

      <details class="faq-row">
        <summary>실손24로 청구하면 되지 않나요? 여긴 왜 필요해요?</summary>
        <p class="faq-a"><b>실손24</b>는 병원이 진료 내역을 보험사로 바로 전송해주는 간편청구 서비스지만, 아직 <b>연계된 병원·약국이 전체의 약 1/4 수준</b>이라 다니는 병원이 연계돼 있지 않으면 이용할 수 없어요. 그럴 땐 보험사 홈페이지·앱으로 직접 청구해야 하는데, 청구친구는 그 창구를 빠르게 찾아드려요. 자세한 건 아래 <a href="#silson24">실손24 안내</a>를 확인하세요.</p>
      </details>

      <details class="faq-row">
        <summary>자동차보험 사고는 어디서 접수하나요?</summary>
        <p class="faq-a">자동차보험은 별도 전문 보험사가 따로 있지 않고, <b>가입한 손해보험사의 사고접수 채널</b>(다이렉트 앱·홈페이지·고객센터)로 접수해요. 아래 손해보험사 목록에서 가입한 회사를 찾아 이동하면 돼요.</p>
      </details>

    </div>
  </section>

  <section>
    <div class="section-head">
      <div>
        <div class="eyebrow">Life Insurance</div>
        <h2 id="life">생명보험사</h2>
      </div>
      <div class="section-count">22개</div>
    </div>
    <div class="co-grid" data-group="life">

      <a class="co-card" data-name="삼성생명" data-cat="life" data-level="direct" href="https://direct.samsunglife.com/customerSupport/insuranceClaimInformation/CustomerSupportInsuranceClaimInformationView">
        <span class="co-badge">삼</span>
        <span class="co-name-col"><span class="co-name">삼성생명</span><span class="co-tag">생명보험</span></span>
        <span class="co-arrow">→</span>
      </a>

      <a class="co-card" data-name="한화생명" data-cat="life" data-level="direct" href="https://www.hanwhalife.com/main/myPage/insurance/accident/MY_INAP000_P10000.do">
        <span class="co-badge">한</span>
        <span class="co-name-col"><span class="co-name">한화생명</span><span class="co-tag">생명보험</span></span>
        <span class="co-arrow">→</span>
      </a>

      <a class="co-card" data-name="교보생명" data-cat="life" data-level="direct" href="https://www.kyobo.com/dgt/web/dti/insurance/accInq/intro">
        <span class="co-badge">교</span>
        <span class="co-name-col"><span class="co-name">교보생명</span><span class="co-tag">생명보험</span></span>
        <span class="co-arrow">→</span>
      </a>

      <a class="co-card" data-name="신한라이프" data-cat="life" data-level="direct" href="https://www.shinhanlife.co.kr/hp/cdhf0020t02.do">
        <span class="co-badge">신</span>
        <span class="co-name-col"><span class="co-name">신한라이프</span><span class="co-tag">생명보험</span></span>
        <span class="co-arrow">→</span>
      </a>

      <a class="co-card" data-name="NH농협생명" data-cat="life" data-level="direct" href="https://www.nhlife.co.kr/ho/cc/HOCC0042M00.nhl">
        <span class="co-badge">NH</span>
        <span class="co-name-col"><span class="co-name">NH농협생명</span><span class="co-tag">생명보험</span></span>
        <span class="co-arrow">→</span>
      </a>

      <a class="co-card" data-name="ABL생명" data-cat="life" data-level="direct" href="https://www.abllife.co.kr/st/custDesk/insSrvcGudn/acdtInsmClamGudn/acdtInsmClamGudn1?page=index">
        <span class="co-badge">AB</span>
        <span class="co-name-col"><span class="co-name">ABL생명</span><span class="co-tag">생명보험</span></span>
        <span class="co-arrow">→</span>
      </a>

      <a class="co-card" data-name="흥국생명" data-cat="life" data-level="direct" href="https://www.heungkuklife.co.kr/cyber/accident/Accident_File_Info.do">
        <span class="co-badge">흥</span>
        <span class="co-name-col"><span class="co-name">흥국생명</span><span class="co-tag">생명보험</span></span>
        <span class="co-arrow">→</span>
      </a>

      <a class="co-card" data-name="iM라이프생명" data-cat="life" data-level="direct" href="https://www.imlifeins.co.kr/BB/BB_D010.do">
        <span class="co-badge">iM</span>
        <span class="co-name-col"><span class="co-name">iM라이프생명</span><span class="co-tag">생명보험</span></span>
        <span class="co-arrow">→</span>
      </a>

      <a class="co-card" data-name="미래에셋생명" data-cat="life" data-level="direct" href="https://life.miraeasset.com/Cmmn/lifePage.do?cp=MNT-IS-204">
        <span class="co-badge">미</span>
        <span class="co-name-col"><span class="co-name">미래에셋생명</span><span class="co-tag">생명보험</span></span>
        <span class="co-arrow">→</span>
      </a>

      <a class="co-card" data-name="KDB생명" data-cat="life" data-level="home" href="https://www.kdblife.co.kr">
        <span class="co-badge">KD</span>
        <span class="co-name-col"><span class="co-name">KDB생명</span><span class="co-tag">생명보험 · 홈페이지</span></span>
        <span class="co-arrow">→</span>
      </a>

      <a class="co-card" data-name="DB생명" data-cat="life" data-level="direct" href="https://www.idblife.com/support/guide/acbf_clm">
        <span class="co-badge">DB</span>
        <span class="co-name-col"><span class="co-name">DB생명</span><span class="co-tag">생명보험</span></span>
        <span class="co-arrow">→</span>
      </a>

      <a class="co-card" data-name="동양생명" data-cat="life" data-level="direct" href="https://www.myangel.co.kr/customer/service/propose/WE_CR_PS_04_05_00.jsp">
        <span class="co-badge">동</span>
        <span class="co-name-col"><span class="co-name">동양생명</span><span class="co-tag">생명보험</span></span>
        <span class="co-arrow">→</span>
      </a>

      <a class="co-card" data-name="메트라이프생명" data-cat="life" data-level="direct" href="https://cyber.metlife.co.kr/claim/billNotice">
        <span class="co-badge">메</span>
        <span class="co-name-col"><span class="co-name">메트라이프생명</span><span class="co-tag">생명보험</span></span>
        <span class="co-arrow">→</span>
      </a>

      <a class="co-card" data-name="KB라이프생명" data-cat="life" data-level="direct" href="https://www.kblife.co.kr/customer-center/benefitClaimMethod.do">
        <span class="co-badge">KB</span>
        <span class="co-name-col"><span class="co-name">KB라이프생명</span><span class="co-tag">생명보험</span></span>
        <span class="co-arrow">→</span>
      </a>

      <a class="co-card" data-name="처브라이프생명" data-cat="life" data-level="direct" href="https://www.chubblife.co.kr/front/ctmcenter/insurance/list.do">
        <span class="co-badge">처</span>
        <span class="co-name-col"><span class="co-name">처브라이프생명</span><span class="co-tag">생명보험</span></span>
        <span class="co-arrow">→</span>
      </a>

      <a class="co-card" data-name="하나생명" data-cat="life" data-level="direct" href="https://www.hanalife.co.kr/csc/accidentInsuranceGuide/accidentInsurancePaymentGuide_1.do">
        <span class="co-badge">하</span>
        <span class="co-name-col"><span class="co-name">하나생명</span><span class="co-tag">생명보험</span></span>
        <span class="co-arrow">→</span>
      </a>

      <a class="co-card" data-name="BNP파리바카디프생명" data-cat="life" data-level="direct" href="https://www.cardif.co.kr/customer-center/보험금-청구.do">
        <span class="co-badge">BN</span>
        <span class="co-name-col"><span class="co-name">BNP파리바카디프생명</span><span class="co-tag">생명보험</span></span>
        <span class="co-arrow">→</span>
      </a>

      <a class="co-card" data-name="푸본현대생명" data-cat="life" data-level="home" href="https://www.fubonhyundai.com">
        <span class="co-badge">푸</span>
        <span class="co-name-col"><span class="co-name">푸본현대생명</span><span class="co-tag">생명보험 · 홈페이지</span></span>
        <span class="co-arrow">→</span>
      </a>

      <a class="co-card" data-name="라이나생명" data-cat="life" data-level="direct" href="https://m.lina.co.kr/ko/wss/claim/claim_receipt.htm">
        <span class="co-badge">라</span>
        <span class="co-name-col"><span class="co-name">라이나생명</span><span class="co-tag">생명보험</span></span>
        <span class="co-arrow">→</span>
      </a>

      <a class="co-card" data-name="AIA생명" data-cat="life" data-level="direct" href="https://www.aia.co.kr/ko/customer-support/customer-guide/insurance-guide/insurance-payment-procedure.html">
        <span class="co-badge">AI</span>
        <span class="co-name-col"><span class="co-name">AIA생명</span><span class="co-tag">생명보험</span></span>
        <span class="co-arrow">→</span>
      </a>

      <a class="co-card" data-name="IBK연금보험" data-cat="life" data-level="home" href="https://www.ibki.co.kr">
        <span class="co-badge">IB</span>
        <span class="co-name-col"><span class="co-name">IBK연금보험</span><span class="co-tag">생명보험 · 홈페이지</span></span>
        <span class="co-arrow">→</span>
      </a>

      <a class="co-card" data-name="교보라이프플래닛" data-cat="life" data-level="direct" href="https://www.lifeplanet.co.kr/contact/pet/HPCG31S2.dev">
        <span class="co-badge">플</span>
        <span class="co-name-col"><span class="co-name">교보라이프플래닛</span><span class="co-tag">생명보험</span></span>
        <span class="co-arrow">→</span>
      </a>

    </div>
  </section>

  <section>
    <div class="section-head">
      <div>
        <div class="eyebrow">Non-Life Insurance</div>
        <h2 id="nonlife">손해보험사</h2>
      </div>
      <div class="section-count">16개</div>
    </div>
    <div class="co-grid" data-group="non-life">

      <a class="co-card non-life" data-name="삼성화재" data-cat="non-life" data-level="direct" href="https://www.samsungfire.com/claim/P_P03_01_01_001.html">
        <span class="co-badge">삼</span>
        <span class="co-name-col"><span class="co-name">삼성화재</span><span class="co-tag">손해보험</span></span>
        <span class="co-arrow">→</span>
      </a>

      <a class="co-card non-life" data-name="현대해상" data-cat="non-life" data-level="direct" href="https://direct.hi.co.kr/service.do?m=a264739757">
        <span class="co-badge">현</span>
        <span class="co-name-col"><span class="co-name">현대해상</span><span class="co-tag">손해보험</span></span>
        <span class="co-arrow">→</span>
      </a>

      <a class="co-card non-life" data-name="메리츠화재" data-cat="non-life" data-level="direct" href="https://www.meritzfire.com/compensation.do">
        <span class="co-badge">메</span>
        <span class="co-name-col"><span class="co-name">메리츠화재</span><span class="co-tag">손해보험</span></span>
        <span class="co-arrow">→</span>
      </a>

      <a class="co-card non-life" data-name="DB손해보험" data-cat="non-life" data-level="direct" href="https://www.idbins.com/pc/bizxpress/ask/ia/FWCLAV1118.shtm">
        <span class="co-badge">DB</span>
        <span class="co-name-col"><span class="co-name">DB손해보험</span><span class="co-tag">손해보험</span></span>
        <span class="co-arrow">→</span>
      </a>

      <a class="co-card non-life" data-name="KB손해보험" data-cat="non-life" data-level="direct" href="https://www.kbinsure.co.kr/CG205010004.ec">
        <span class="co-badge">KB</span>
        <span class="co-name-col"><span class="co-name">KB손해보험</span><span class="co-tag">손해보험</span></span>
        <span class="co-arrow">→</span>
      </a>

      <a class="co-card non-life" data-name="한화손해보험" data-cat="non-life" data-level="direct" href="https://www.hwgeneralins.com/fplaza/compensation/charge00.do">
        <span class="co-badge">한</span>
        <span class="co-name-col"><span class="co-name">한화손해보험</span><span class="co-tag">손해보험</span></span>
        <span class="co-arrow">→</span>
      </a>

      <a class="co-card non-life" data-name="흥국화재" data-cat="non-life" data-level="direct" href="https://www.heungkukfire.co.kr/FRW/compensation/accidentInfo.do">
        <span class="co-badge">흥</span>
        <span class="co-name-col"><span class="co-name">흥국화재</span><span class="co-tag">손해보험</span></span>
        <span class="co-arrow">→</span>
      </a>

      <a class="co-card non-life" data-name="롯데손해보험" data-cat="non-life" data-level="home" href="https://www.lotteins.co.kr">
        <span class="co-badge">롯</span>
        <span class="co-name-col"><span class="co-name">롯데손해보험</span><span class="co-tag">손해보험 · 홈페이지</span></span>
        <span class="co-arrow">→</span>
      </a>

      <a class="co-card non-life" data-name="AXA손해보험" data-cat="non-life" data-level="direct" href="https://www.axa.co.kr/cui/cmk/cl/CMKCLL07M01.html">
        <span class="co-badge">AX</span>
        <span class="co-name-col"><span class="co-name">AXA손해보험</span><span class="co-tag">손해보험</span></span>
        <span class="co-arrow">→</span>
      </a>

      <a class="co-card non-life" data-name="AIG손해보험" data-cat="non-life" data-level="direct" href="https://www.aig.co.kr/wt/dpwtm025.html?menuId=MS216">
        <span class="co-badge">AI</span>
        <span class="co-name-col"><span class="co-name">AIG손해보험</span><span class="co-tag">손해보험</span></span>
        <span class="co-arrow">→</span>
      </a>

      <a class="co-card non-life" data-name="캐롯손해보험" data-cat="non-life" data-level="direct" href="https://www.carrotins.com/desktop/reward/claim/apply/">
        <span class="co-badge">캐</span>
        <span class="co-name-col"><span class="co-name">캐롯손해보험</span><span class="co-tag">손해보험</span></span>
        <span class="co-arrow">→</span>
      </a>

      <a class="co-card non-life" data-name="NH농협손해보험" data-cat="non-life" data-level="direct" href="https://www.nhfire.co.kr/customer/guide/insuranceClaimGuide.nhfire">
        <span class="co-badge">NH</span>
        <span class="co-name-col"><span class="co-name">NH농협손해보험</span><span class="co-tag">손해보험</span></span>
        <span class="co-arrow">→</span>
      </a>

      <a class="co-card non-life" data-name="서울보증보험" data-cat="non-life" data-level="direct" href="https://www.sgic.co.kr/chp/iutf/ib/elcl/cs/claimGuidance/CHPINFO101VM0.mvc">
        <span class="co-badge">서</span>
        <span class="co-name-col"><span class="co-name">서울보증보험</span><span class="co-tag">손해보험</span></span>
        <span class="co-arrow">→</span>
      </a>

      <a class="co-card non-life" data-name="하나손해보험" data-cat="non-life" data-level="direct" href="https://www.hanainsure.co.kr/w/claim/healthReward/accidentReceipt">
        <span class="co-badge">하</span>
        <span class="co-name-col"><span class="co-name">하나손해보험</span><span class="co-tag">손해보험</span></span>
        <span class="co-arrow">→</span>
      </a>

      <a class="co-card non-life" data-name="카카오페이손해보험" data-cat="non-life" data-level="direct" href="https://kakaopayinscorp.co.kr/customer-center/claim-info">
        <span class="co-badge">카</span>
        <span class="co-name-col"><span class="co-name">카카오페이손해보험</span><span class="co-tag">손해보험</span></span>
        <span class="co-arrow">→</span>
      </a>

      <a class="co-card non-life" data-name="신한EZ손해보험" data-cat="non-life" data-level="direct" href="https://www.shinhanez.co.kr/static/cus/CUS50000M01.html?docInfoYn=Y">
        <span class="co-badge">신</span>
        <span class="co-name-col"><span class="co-name">신한EZ손해보험</span><span class="co-tag">손해보험</span></span>
        <span class="co-arrow">→</span>
      </a>

    </div>
    <p class="empty-state" id="emptyState">검색 결과가 없습니다. 보험사명을 다시 확인해주세요.</p>
  </section>

  <section id="silson24">
    <div class="section-head">
      <div>
        <div class="eyebrow">Before you claim</div>
        <h2>실손24, 먼저 시도해보세요</h2>
      </div>
    </div>
    <div class="notice">
      <p><b>실손24</b>는 보험업계·병원이 공동으로 운영하는 실손의료보험금 <b>간편청구 서비스</b>예요. 다녔던 병원이 연계돼 있으면 서류를 직접 챙길 필요 없이 병원이 진료 내역을 보험사로 바로 전송해줘서 앱·홈페이지 몇 번 클릭으로 청구가 끝나요.</p>
      <p style="margin-top:8px">다만 아직 <b>연계 병원·약국이 전체의 약 1/4 수준</b>이라, 다니는 곳이 연계돼 있지 않으면 이용할 수 없어요. 그럴 땐 아래에서 가입한 보험사를 찾아 직접 청구 페이지로 이동하세요 — 청구친구가 그 다음 단계예요.</p>
      <p style="margin-top:8px"><a href="https://www.silson24.or.kr" style="color:var(--accent);font-weight:600">실손24 홈페이지 바로가기 →</a></p>
    </div>
  </section>

  <section id="notice">
    <div class="notice">
      <b>딥링크 검증 현황:</b> 38개사 중 34개사는 실제 보험금 청구 안내/신청 서브페이지를 확인해 연결했습니다. KDB생명·푸본현대생명·IBK연금보험·롯데손해보험 4곳은 로그인 경유 또는 공개 딥링크 미확인으로 홈페이지 링크를 유지 중이며, 확인되는 대로 순차적으로 교체합니다. (참고: MG손해보험은 2026년 파산 절차로 계약이 삼성화재·현대해상·DB손보·KB손보·메리츠화재 5개사로 이전되어 제외했고, 코리안리 등 재보험사는 소비자가 직접 청구할 대상이 아니라 제외했습니다.)
    </div>
  </section>

  <section id="disclaimer">
    <div class="section-head">
      <div>
        <div class="eyebrow">Disclaimer</div>
        <h2>면책조항</h2>
      </div>
    </div>
    <div class="notice">
      <ul>
        <li>각 보험사의 공식 홈페이지·보험금 청구 페이지로 연결하는 <b>링크 모음 서비스</b>이며, 보험 상품의 판매·중개·비교·상담을 하지 않습니다.</li>
        <li>페이지에 표시된 보험사명·로고·상표는 각 보험사에 귀속되며, 어떤 보험사와도 <b>제휴·협찬·위탁 관계가 없습니다.</b></li>
        <li>청구 절차, 필요 서류, 처리 기간, 보상 범위는 가입한 상품·약관마다 다르므로 <b>해당 보험사의 공식 안내를 최종 기준</b>으로 확인해야 합니다.</li>
        <li>연결된 외부 사이트(보험사 공식 페이지)의 주소와 내용은 보험사 사정에 따라 사전 고지 없이 변경될 수 있으며, 정확성·최신성을 보증하지 않습니다.</li>
        <li>제공하는 정보는 청구 창구 안내를 위한 참고용이며, 이를 이용해 발생한 손해에 대해 운영자는 법적 책임을 지지 않습니다.</li>
      </ul>
    </div>
  </section>

</main>

<footer>
  <div class="footer-inner">
    <div class="footer-brand">
      <span class="mark">
        <svg width="13" height="13" viewBox="0 0 24 24" fill="none"><path d="M12 2L4 5v6c0 5.2 3.4 9.6 8 11 4.6-1.4 8-5.8 8-11V5l-8-3z" fill="currentColor"/></svg>
      </span>
      청구친구
    </div>
    <p>보험사 공식 페이지로만 연결하는 링크 모음. 새 탭 없이 클릭 즉시 이동합니다.</p>
    <p>© 2026 청구친구 · 청구 절차는 보험사 공식 안내 기준으로 확인하세요.</p>
  </div>
</footer>

<script>
  window.__activeCat = 'all';
  function filterCompanies() {
    var q = document.getElementById('searchInput').value.trim().toLowerCase();
    var cards = document.querySelectorAll('.co-card');
    var visible = 0;
    cards.forEach(function (card) {
      var name = card.getAttribute('data-name').toLowerCase();
      var catOk = window.__activeCat === 'all' ||
        (window.__activeCat === 'direct' ? card.getAttribute('data-level') === 'direct' : card.getAttribute('data-cat') === window.__activeCat);
      var nameOk = name.indexOf(q) !== -1;
      var show = catOk && nameOk;
      card.hidden = !show;
      if (show) visible++;
    });
    document.getElementById('emptyState').className = visible === 0 ? 'empty-state show' : 'empty-state';
  }
  function setSearch(v) {
    document.getElementById('searchInput').value = v;
    filterCompanies();
  }
  function setCategory(cat, btn) {
    window.__activeCat = cat;
    document.querySelectorAll('.seg-btn').forEach(function (b) { b.classList.remove('is-active'); });
    btn.classList.add('is-active');
    filterCompanies();
  }
</script>
"""

html = (TEMPLATE
        .replace('__REGULAR__', regular)
        .replace('__SEMIBOLD__', semibold)
        .replace('__BOLD__', bold)
        .replace('__EXTRABOLD__', extrabold))

out_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'claim-hub-prototype.html')
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(html)
print('wrote', len(html), 'chars to', out_path)
