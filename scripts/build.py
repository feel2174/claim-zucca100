# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, r'C:\Users\devzu\AppData\Local\Temp\claude\C--Users-devzu-Documents\d3092015-96e6-4b53-9b60-a0775041dae0\scratchpad')
from font_b64 import regular, semibold, bold, extrabold

TEMPLATE = r"""<title>보험금 청구 바로가기 모음 | 청구봄</title>
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
    --page: #faf8f4;
    --surface: #ffffff;
    --surface-2: #f1ece2;
    --ink: #1f2421;
    --ink-2: #5b645f;
    --muted: #8b948e;
    --line: #e6e0d3;
    --border: rgba(31,36,33,0.10);
    --accent: #0d9488;
    --accent-ink: #ffffff;
    --accent-soft: #d7f2ee;
    --warm: #d97b32;
    --warm-ink: #ffffff;
    --warm-soft: #fbe6d2;
    --good: #178a43;
  }
  @media (prefers-color-scheme: dark) {
    :root:where(:not([data-theme="light"])) {
      color-scheme: dark;
      --page: #201e1a;
      --surface: #2b2925;
      --surface-2: #363330;
      --ink: #f6f2ea;
      --ink-2: #cdc6b9;
      --muted: #99917f;
      --line: #453f37;
      --border: rgba(255,255,255,0.12);
      --accent: #35d6c0;
      --accent-ink: #10201d;
      --accent-soft: #123634;
      --warm: #f2a35f;
      --warm-ink: #291705;
      --warm-soft: #3c2914;
      --good: #4ade80;
    }
  }
  :root[data-theme="dark"] {
    color-scheme: dark;
    --page: #201e1a;
    --surface: #2b2925;
    --surface-2: #363330;
    --ink: #f6f2ea;
    --ink-2: #cdc6b9;
    --muted: #99917f;
    --line: #453f37;
    --border: rgba(255,255,255,0.12);
    --accent: #35d6c0;
    --accent-ink: #10201d;
    --accent-soft: #123634;
    --warm: #f2a35f;
    --warm-ink: #291705;
    --warm-soft: #3c2914;
    --good: #4ade80;
  }

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
    padding: 22px 24px;
  }
  .brand { display: flex; align-items: center; gap: 9px; font-weight: 800; font-size: 18px; letter-spacing: -0.01em; }
  .brand .mark {
    width: 32px; height: 32px; border-radius: 9px; background: var(--accent);
    color: var(--accent-ink); display: flex; align-items: center; justify-content: center;
    flex-shrink: 0;
  }
  nav.site-nav { display: flex; gap: 28px; font-size: 14px; font-weight: 600; color: var(--ink-2); }
  nav.site-nav a { text-decoration: none; }
  nav.site-nav a:hover { color: var(--ink); }

  /* ---- hero ---- */
  .hero { max-width: 1080px; margin: 0 auto; padding: 40px 24px 8px; }
  .kicker {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: var(--accent-soft);
    color: var(--accent);
    font-size: 12.5px;
    font-weight: 700;
    padding: 6px 12px;
    border-radius: 999px;
    margin-bottom: 20px;
  }
  h1.hero-title {
    font-size: 40px;
    font-weight: 800;
    letter-spacing: -0.02em;
    line-height: 1.22;
    margin: 0 0 16px;
    text-wrap: balance;
    max-width: 16ch;
  }
  h1.hero-title .accent { color: var(--accent); }
  .hero-sub {
    font-size: 16px;
    color: var(--ink-2);
    max-width: 46ch;
    margin: 0 0 28px;
  }
  .search-bar {
    display: flex;
    gap: 8px;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 6px;
    max-width: 560px;
    box-shadow: 0 10px 28px rgba(31,36,33,0.08);
  }
  .search-bar input {
    flex: 1;
    border: none;
    background: transparent;
    padding: 13px 14px;
    font-size: 15px;
    color: var(--ink);
    outline: none;
    font-family: inherit;
  }
  .search-bar input::placeholder { color: var(--muted); }
  .search-bar button {
    background: var(--accent);
    color: var(--accent-ink);
    border: none;
    border-radius: 10px;
    padding: 0 22px;
    font-weight: 700;
    font-size: 14.5px;
    cursor: pointer;
    font-family: inherit;
  }
  .chips { display: flex; gap: 8px; margin-top: 16px; flex-wrap: wrap; }
  .chip {
    background: var(--surface);
    border: 1px solid var(--border);
    color: var(--ink-2);
    font-size: 12.5px;
    font-weight: 600;
    padding: 7px 13px;
    border-radius: 999px;
    cursor: pointer;
    font-family: inherit;
  }
  .chip:hover { border-color: var(--accent); color: var(--accent); }

  /* ---- process strip (replaces illustration) ---- */
  .process {
    display: flex;
    align-items: center;
    gap: 10px;
    margin: 36px 0 4px;
    flex-wrap: wrap;
  }
  .process-step {
    display: flex;
    align-items: center;
    gap: 10px;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 12px 16px;
  }
  .process-step .n {
    width: 24px; height: 24px; border-radius: 50%;
    background: var(--surface-2); color: var(--ink-2);
    font-size: 12px; font-weight: 700;
    display: flex; align-items: center; justify-content: center; flex-shrink: 0;
  }
  .process-step.is-final .n { background: var(--accent); color: var(--accent-ink); }
  .process-step b { font-size: 13.5px; font-weight: 700; }
  .process-step span.d { font-size: 12px; color: var(--muted); }
  .process-arrow { color: var(--muted); font-size: 16px; }

  /* ---- main ---- */
  main { max-width: 1080px; margin: 0 auto; padding: 56px 24px 90px; }
  section { margin-bottom: 56px; }
  .section-head { display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 18px; gap: 12px; flex-wrap: wrap; }
  .eyebrow { font-size: 11.5px; font-weight: 800; letter-spacing: 0.09em; text-transform: uppercase; color: var(--accent); margin-bottom: 6px; }
  h2 { font-size: 22px; font-weight: 800; margin: 0; letter-spacing: -0.01em; }
  .section-sub { font-size: 14px; color: var(--ink-2); margin: 6px 0 0; max-width: 60ch; }
  .section-count { font-size: 13px; color: var(--muted); font-weight: 600; white-space: nowrap; }

  /* ---- category segmented control ---- */
  .segmented {
    display: inline-flex;
    background: var(--surface-2);
    border-radius: 12px;
    padding: 4px;
    gap: 2px;
    flex-wrap: wrap;
  }
  .seg-btn {
    border: none;
    background: transparent;
    color: var(--ink-2);
    font-family: inherit;
    font-size: 13.5px;
    font-weight: 700;
    padding: 10px 18px;
    border-radius: 9px;
    cursor: pointer;
  }
  .seg-btn .c { font-weight: 600; color: var(--muted); margin-left: 4px; }
  .seg-btn.is-active { background: var(--surface); color: var(--ink); box-shadow: 0 2px 8px rgba(31,36,33,0.10); }
  .seg-btn.is-active .c { color: var(--accent); }

  /* ---- FAQ: editorial reason cards ---- */
  .faq-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; }
  .faq-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 22px 24px;
    position: relative;
    overflow: hidden;
  }
  .faq-card::before {
    content: "";
    position: absolute; top: 0; left: 0; right: 0; height: 3px;
    background: var(--accent);
  }
  .faq-card:nth-child(even)::before { background: var(--warm); }
  .faq-tag {
    display: inline-block;
    font-size: 11px; font-weight: 800; letter-spacing: 0.03em;
    color: var(--accent); background: var(--accent-soft);
    border-radius: 6px; padding: 3px 8px; margin-bottom: 12px;
  }
  .faq-card:nth-child(even) .faq-tag { color: var(--warm); background: var(--warm-soft); }
  .faq-q { font-size: 16.5px; font-weight: 800; margin: 0 0 10px; letter-spacing: -0.01em; line-height: 1.4; }
  .faq-a { font-size: 13.5px; color: var(--ink-2); margin: 0; line-height: 1.65; }
  .faq-a b { color: var(--ink); font-weight: 700; }

  /* ---- company grid ---- */
  .co-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px; }
  .co-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 13px;
    padding: 18px 20px;
    display: flex;
    flex-direction: column;
    gap: 12px;
    position: relative;
    overflow: hidden;
    transition: box-shadow .12s ease, transform .12s ease;
  }
  .co-card::before {
    content: "";
    position: absolute; top: 0; left: 0; right: 0; height: 3px;
    background: var(--warm);
  }
  .co-card.non-life::before { background: var(--accent); }
  .co-card:hover { box-shadow: 0 12px 28px rgba(31,36,33,0.10); transform: translateY(-2px); }
  .co-top { display: flex; align-items: center; gap: 12px; }
  .co-badge {
    width: 40px; height: 40px; border-radius: 10px; background: var(--surface-2); color: var(--ink);
    display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 14px; flex-shrink: 0;
  }
  .co-name { font-weight: 800; font-size: 15.5px; }
  .co-tag {
    font-size: 11px; font-weight: 700; color: var(--warm); background: var(--warm-soft);
    display: inline-block; padding: 2px 8px; border-radius: 6px; margin-top: 3px;
  }
  .co-card.non-life .co-tag { color: var(--accent); background: var(--accent-soft); }
  .co-trust { display: flex; align-items: center; gap: 5px; font-size: 12px; color: var(--good); font-weight: 700; }
  .co-cta {
    display: flex; align-items: center; justify-content: space-between;
    background: var(--surface-2);
    border: 1px solid transparent;
    border-radius: 9px;
    padding: 11px 14px;
    font-weight: 700;
    font-size: 13.5px;
    color: var(--ink);
    text-decoration: none;
    margin-top: auto;
  }
  .co-cta:hover { background: var(--accent); color: var(--accent-ink); }
  .co-cta .arrow { font-size: 15px; }
  .link-level { font-size: 10.5px; color: var(--muted); margin-top: -6px; }
  .co-card[hidden] { display: none; }

  .empty-state {
    text-align: center;
    padding: 40px 20px;
    color: var(--muted);
    font-size: 14px;
    display: none;
  }
  .empty-state.show { display: block; }

  .notice {
    background: var(--surface-2);
    border: 1px dashed var(--border);
    border-radius: 12px;
    padding: 16px 20px;
    font-size: 13px;
    color: var(--ink-2);
  }
  .notice b { color: var(--ink); }

  footer { border-top: 1px solid var(--line); }
  .footer-inner { max-width: 1080px; margin: 0 auto; padding: 36px 24px; }
  .footer-brand { display: flex; align-items: center; gap: 9px; font-weight: 800; font-size: 15px; margin-bottom: 8px; }
  .footer-brand .mark {
    width: 24px; height: 24px; border-radius: 7px; background: var(--accent); color: var(--accent-ink);
    display: flex; align-items: center; justify-content: center; flex-shrink: 0;
  }
  footer p { font-size: 12.5px; color: var(--muted); margin: 4px 0 0; max-width: 62ch; }

  @media (max-width: 900px) {
    .co-grid { grid-template-columns: 1fr 1fr; }
    .faq-grid { grid-template-columns: 1fr; }
    nav.site-nav { display: none; }
    h1.hero-title { font-size: 30px; }
  }
  @media (max-width: 560px) {
    .co-grid { grid-template-columns: 1fr; }
  }
</style>

<header class="site">
  <div class="brand">
    <span class="mark">
      <svg width="17" height="17" viewBox="0 0 24 24" fill="none"><path d="M12 2L4 5v6c0 5.2 3.4 9.6 8 11 4.6-1.4 8-5.8 8-11V5l-8-3z" fill="currentColor" opacity="0.9"/><path d="M8.5 12.2l2.4 2.4 4.6-4.8" stroke="var(--surface)" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
    </span>
    청구봄
  </div>
  <nav class="site-nav">
    <a href="#life">생명보험</a>
    <a href="#nonlife">손해보험</a>
    <a href="#notice">안내</a>
  </nav>
</header>

<div class="hero">
  <span class="kicker">✦ 보험사 공식 페이지로만 연결됩니다</span>
  <h1 class="hero-title">보험사 이름만 알면,<br><span class="accent">청구 페이지</span>는 여기서.</h1>
  <p class="hero-sub">17개 보험사의 보험금 청구 창구를 한곳에 모았어요. 검색하고, 눌러서, 공식 페이지로 바로 이동하세요.</p>
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

  <div class="process">
    <div class="process-step"><span class="n">1</span><div><b>보험사 검색</b> <span class="d">이름만 입력</span></div></div>
    <span class="process-arrow">→</span>
    <div class="process-step"><span class="n">2</span><div><b>청구 버튼 클릭</b> <span class="d">새 탭 없이 바로 이동</span></div></div>
    <span class="process-arrow">→</span>
    <div class="process-step is-final"><span class="n">✓</span><div><b>공식 청구 페이지 도착</b> <span class="d">그대로 접수 진행</span></div></div>
  </div>
</div>

<main>

  <section>
    <div class="eyebrow">Category</div>
    <div class="section-head"><h2>어떤 보험 청구가 필요하세요?</h2></div>
    <div class="segmented">
      <button class="seg-btn is-active" onclick="setCategory('all', this)">전체 <span class="c num">17</span></button>
      <button class="seg-btn" onclick="setCategory('life', this)">생명보험 <span class="c num">5</span></button>
      <button class="seg-btn" onclick="setCategory('non-life', this)">손해보험 <span class="c num">12</span></button>
      <button class="seg-btn" onclick="setCategory('direct', this)">청구페이지 직결 <span class="c num">7</span></button>
    </div>
  </section>

  <section>
    <div class="eyebrow">FAQ</div>
    <div class="section-head"><h2>보험금 청구, 왜 유독 어렵게 느껴질까요?</h2></div>
    <div class="faq-grid">

      <div class="faq-card">
        <span class="faq-tag">이유 1</span>
        <p class="faq-q">왜 보험금 청구는 항상 복잡하고 어렵게 느껴질까요?</p>
        <p class="faq-a"><b>청구 창구가 보험사마다 다 다르기 때문</b>이에요. 어떤 곳은 앱, 어떤 곳은 홈페이지 사이버창구, 어떤 곳은 팩스·우편까지 써야 해서 매번 "이 보험사는 어디서 청구하지?"부터 찾아야 합니다.</p>
      </div>

      <div class="faq-card">
        <span class="faq-tag">이유 2</span>
        <p class="faq-q">청구 페이지를 찾아도 또 헤매게 되는 이유는요?</p>
        <p class="faq-a">보험사 홈페이지는 상품 가입·상담·이벤트 메뉴에 밀려 <b>"보험금 청구" 메뉴가 몇 단계 안쪽에 숨어있는 경우</b>가 많아요. 특히 모바일에서는 더 찾기 힘들죠.</p>
      </div>

      <div class="faq-card">
        <span class="faq-tag">이유 3</span>
        <p class="faq-q">청구 기한이 따로 있나요? 늦으면 못 받나요?</p>
        <p class="faq-a">네, 보험금 청구권의 소멸시효는 <b>원칙적으로 사고일로부터 3년</b>이에요. 이 기간이 지나면 정당한 사유가 있어도 청구가 어려워질 수 있어요.</p>
      </div>

      <div class="faq-card">
        <span class="faq-tag">이유 4</span>
        <p class="faq-q">여러 보험사에 가입돼 있으면 한 번에 청구할 수 없나요?</p>
        <p class="faq-a">아쉽지만 <b>청구는 가입한 보험사마다 각각 진행</b>해야 해요. 통합 조회 서비스가 있어도 최종 접수는 결국 보험사별 창구를 거쳐야 해서, 한곳에 모아둔 바로가기가 더 유용해요.</p>
      </div>

    </div>
  </section>

  <section>
    <div class="section-head">
      <div>
        <div class="eyebrow">Life Insurance</div>
        <h2 id="life">생명보험사</h2>
      </div>
      <div class="section-count">5개</div>
    </div>
    <div class="co-grid" data-group="life">

      <div class="co-card" data-name="삼성생명" data-cat="life" data-level="direct">
        <div class="co-top">
          <div class="co-badge">삼</div>
          <div><div class="co-name">삼성생명</div><span class="co-tag">생명보험</span></div>
        </div>
        <div class="co-trust">✓ 공식 링크 확인됨</div>
        <a class="co-cta" href="https://direct.samsunglife.com/customerSupport/insuranceClaimInformation/CustomerSupportInsuranceClaimInformationView">보험금 청구 바로가기 <span class="arrow">→</span></a>
      </div>

      <div class="co-card" data-name="한화생명" data-cat="life" data-level="direct">
        <div class="co-top">
          <div class="co-badge">한</div>
          <div><div class="co-name">한화생명</div><span class="co-tag">생명보험</span></div>
        </div>
        <div class="co-trust">✓ 공식 링크 확인됨</div>
        <a class="co-cta" href="https://www.hanwhalife.com/main/myPage/insurance/accident/MY_INAP000_P10000.do">보험금 청구 바로가기 <span class="arrow">→</span></a>
      </div>

      <div class="co-card" data-name="교보생명" data-cat="life" data-level="direct">
        <div class="co-top">
          <div class="co-badge">교</div>
          <div><div class="co-name">교보생명</div><span class="co-tag">생명보험</span></div>
        </div>
        <div class="co-trust">✓ 공식 링크 확인됨</div>
        <a class="co-cta" href="https://www.kyobo.com/dgt/web/dti/insurance/accInq/intro">보험금 청구 바로가기 <span class="arrow">→</span></a>
      </div>

      <div class="co-card" data-name="신한라이프" data-cat="life" data-level="direct">
        <div class="co-top">
          <div class="co-badge">신</div>
          <div><div class="co-name">신한라이프</div><span class="co-tag">생명보험</span></div>
        </div>
        <div class="co-trust">✓ 공식 링크 확인됨</div>
        <a class="co-cta" href="https://www.shinhanlife.co.kr/hp/cdhf0020t02.do">보험금 청구 바로가기 <span class="arrow">→</span></a>
      </div>

      <div class="co-card" data-name="NH농협생명" data-cat="life" data-level="home">
        <div class="co-top">
          <div class="co-badge">NH</div>
          <div><div class="co-name">NH농협생명</div><span class="co-tag">생명보험</span></div>
        </div>
        <div class="co-trust">✓ 공식 링크 확인됨</div>
        <a class="co-cta" href="https://www.nhlife.co.kr">홈페이지 바로가기 <span class="arrow">→</span></a>
        <div class="link-level">청구 세부 페이지는 확인 중 · 홈페이지로 우선 연결</div>
      </div>

    </div>
  </section>

  <section>
    <div class="section-head">
      <div>
        <div class="eyebrow">Non-Life Insurance</div>
        <h2 id="nonlife">손해보험사</h2>
      </div>
      <div class="section-count">12개</div>
    </div>
    <div class="co-grid" data-group="non-life">

      <div class="co-card non-life" data-name="삼성화재" data-cat="non-life" data-level="direct">
        <div class="co-top">
          <div class="co-badge">삼</div>
          <div><div class="co-name">삼성화재</div><span class="co-tag">손해보험</span></div>
        </div>
        <div class="co-trust">✓ 공식 링크 확인됨</div>
        <a class="co-cta" href="https://www.samsungfire.com/claim/P_P03_01_01_001.html">보험금 청구 바로가기 <span class="arrow">→</span></a>
      </div>

      <div class="co-card non-life" data-name="현대해상" data-cat="non-life" data-level="direct">
        <div class="co-top">
          <div class="co-badge">현</div>
          <div><div class="co-name">현대해상</div><span class="co-tag">손해보험</span></div>
        </div>
        <div class="co-trust">✓ 공식 링크 확인됨</div>
        <a class="co-cta" href="https://direct.hi.co.kr/service.do?m=a264739757">보험금 청구 바로가기 <span class="arrow">→</span></a>
      </div>

      <div class="co-card non-life" data-name="메리츠화재" data-cat="non-life" data-level="direct">
        <div class="co-top">
          <div class="co-badge">메</div>
          <div><div class="co-name">메리츠화재</div><span class="co-tag">손해보험</span></div>
        </div>
        <div class="co-trust">✓ 공식 링크 확인됨</div>
        <a class="co-cta" href="https://www.meritzfire.com/compensation.do">보험금 청구 바로가기 <span class="arrow">→</span></a>
      </div>

      <div class="co-card non-life" data-name="DB손해보험" data-cat="non-life" data-level="home">
        <div class="co-top">
          <div class="co-badge">DB</div>
          <div><div class="co-name">DB손해보험</div><span class="co-tag">손해보험</span></div>
        </div>
        <div class="co-trust">✓ 공식 링크 확인됨</div>
        <a class="co-cta" href="https://www.idbins.com">홈페이지 바로가기 <span class="arrow">→</span></a>
        <div class="link-level">청구 세부 페이지는 확인 중 · 홈페이지로 우선 연결</div>
      </div>

      <div class="co-card non-life" data-name="KB손해보험" data-cat="non-life" data-level="home">
        <div class="co-top">
          <div class="co-badge">KB</div>
          <div><div class="co-name">KB손해보험</div><span class="co-tag">손해보험</span></div>
        </div>
        <div class="co-trust">✓ 공식 링크 확인됨</div>
        <a class="co-cta" href="https://www.kbinsure.co.kr">홈페이지 바로가기 <span class="arrow">→</span></a>
        <div class="link-level">청구 세부 페이지는 확인 중 · 홈페이지로 우선 연결</div>
      </div>

      <div class="co-card non-life" data-name="한화손해보험" data-cat="non-life" data-level="home">
        <div class="co-top">
          <div class="co-badge">한</div>
          <div><div class="co-name">한화손해보험</div><span class="co-tag">손해보험</span></div>
        </div>
        <div class="co-trust">✓ 공식 링크 확인됨</div>
        <a class="co-cta" href="https://www.hwgeneralins.com">홈페이지 바로가기 <span class="arrow">→</span></a>
        <div class="link-level">청구 세부 페이지는 확인 중 · 홈페이지로 우선 연결</div>
      </div>

      <div class="co-card non-life" data-name="흥국화재" data-cat="non-life" data-level="home">
        <div class="co-top">
          <div class="co-badge">흥</div>
          <div><div class="co-name">흥국화재</div><span class="co-tag">손해보험</span></div>
        </div>
        <div class="co-trust">✓ 공식 링크 확인됨</div>
        <a class="co-cta" href="https://www.heungkukfire.co.kr">홈페이지 바로가기 <span class="arrow">→</span></a>
        <div class="link-level">청구 세부 페이지는 확인 중 · 홈페이지로 우선 연결</div>
      </div>

      <div class="co-card non-life" data-name="롯데손해보험" data-cat="non-life" data-level="home">
        <div class="co-top">
          <div class="co-badge">롯</div>
          <div><div class="co-name">롯데손해보험</div><span class="co-tag">손해보험</span></div>
        </div>
        <div class="co-trust">✓ 공식 링크 확인됨</div>
        <a class="co-cta" href="https://www.lotteins.co.kr">홈페이지 바로가기 <span class="arrow">→</span></a>
        <div class="link-level">청구 세부 페이지는 확인 중 · 홈페이지로 우선 연결</div>
      </div>

      <div class="co-card non-life" data-name="AXA손해보험" data-cat="non-life" data-level="home">
        <div class="co-top">
          <div class="co-badge">AX</div>
          <div><div class="co-name">AXA손해보험</div><span class="co-tag">손해보험</span></div>
        </div>
        <div class="co-trust">✓ 공식 링크 확인됨</div>
        <a class="co-cta" href="https://www.axakorea.co.kr">홈페이지 바로가기 <span class="arrow">→</span></a>
        <div class="link-level">청구 세부 페이지는 확인 중 · 홈페이지로 우선 연결</div>
      </div>

      <div class="co-card non-life" data-name="AIG손해보험" data-cat="non-life" data-level="home">
        <div class="co-top">
          <div class="co-badge">AI</div>
          <div><div class="co-name">AIG손해보험</div><span class="co-tag">손해보험</span></div>
        </div>
        <div class="co-trust">✓ 공식 링크 확인됨</div>
        <a class="co-cta" href="https://www.aig.co.kr">홈페이지 바로가기 <span class="arrow">→</span></a>
        <div class="link-level">청구 세부 페이지는 확인 중 · 홈페이지로 우선 연결</div>
      </div>

      <div class="co-card non-life" data-name="캐롯손해보험" data-cat="non-life" data-level="home">
        <div class="co-top">
          <div class="co-badge">캐</div>
          <div><div class="co-name">캐롯손해보험</div><span class="co-tag">손해보험</span></div>
        </div>
        <div class="co-trust">✓ 공식 링크 확인됨</div>
        <a class="co-cta" href="https://www.carrotins.com">홈페이지 바로가기 <span class="arrow">→</span></a>
        <div class="link-level">청구 세부 페이지는 확인 중 · 홈페이지로 우선 연결</div>
      </div>

      <div class="co-card non-life" data-name="NH농협손해보험" data-cat="non-life" data-level="home">
        <div class="co-top">
          <div class="co-badge">NH</div>
          <div><div class="co-name">NH농협손해보험</div><span class="co-tag">손해보험</span></div>
        </div>
        <div class="co-trust">✓ 공식 링크 확인됨</div>
        <a class="co-cta" href="https://www.nhfire.co.kr">홈페이지 바로가기 <span class="arrow">→</span></a>
        <div class="link-level">청구 세부 페이지는 확인 중 · 홈페이지로 우선 연결</div>
      </div>

    </div>
    <p class="empty-state" id="emptyState">검색 결과가 없습니다. 보험사명을 다시 확인해주세요.</p>
  </section>

  <section id="notice">
    <div class="notice">
      <b>2차 확장 예정 (링크 검증 후 추가):</b> MG손해보험, 하나손해보험, 서울보증보험, 흥국생명, 동양생명, ABL생명, 미래에셋생명, 처브라이프, DGB생명, KDB생명, 라이나(Chubb Life) 등. 공식 청구 페이지 URL을 확인하는 대로 순차 추가합니다. 위 목록 중 "홈페이지 바로가기"로 표시된 10개사는 최상위 도메인은 확인됐지만 보험금 청구 전용 서브페이지까지는 검증하지 못해, 정확한 딥링크로 교체하는 2차 작업이 필요합니다.
    </div>
  </section>

</main>

<footer>
  <div class="footer-inner">
    <div class="footer-brand">
      <span class="mark">
        <svg width="13" height="13" viewBox="0 0 24 24" fill="none"><path d="M12 2L4 5v6c0 5.2 3.4 9.6 8 11 4.6-1.4 8-5.8 8-11V5l-8-3z" fill="currentColor"/></svg>
      </span>
      청구봄
    </div>
    <p>보험사 공식 페이지로만 연결하는 보험금 청구 링크 모음. 새 탭이 아닌 클릭 즉시 이동 방식으로 동작합니다.</p>
    <p>© 2026 청구봄 · 청구 절차·구비서류는 반드시 각 보험사 공식 안내를 최종 확인하세요.</p>
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

out_path = r'C:\Users\devzu\AppData\Local\Temp\claude\C--Users-devzu-Documents\d3092015-96e6-4b53-9b60-a0775041dae0\scratchpad\claim-hub-prototype.html'
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(html)
print('wrote', len(html), 'chars to', out_path)
