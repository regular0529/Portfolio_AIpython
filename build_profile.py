from datetime import date
from html import escape
from pathlib import Path

OUTPUT = Path(__file__).with_name("llm-profile.html")

PROFILE = {
    "name": "김정규",
    "name_en": "KIM JEONGGYU",
    "university": "부산대학교",
    "major": "산업공학과",
    "email": "hello@example.com",
    "year": date.today().year,
}

SPECS = [
    ("부산대학교", "University"),
    ("산업공학과", "Major"),
    ("LLM 기초 · 프롬프트 실험", "Currently Learning"),
    ("LLM 기반 업무 도구 제작", "Goal"),
]

INTERESTS = [
    {
        "title": "Transformer 원리",
        "desc": "어텐션과 토큰 흐름을 직접 계산하며 모델 내부가 어떻게 문맥을 만드는지 이해합니다.",
        "tag": "Architecture",
    },
    {
        "title": "프롬프트 엔지니어링",
        "desc": "역할, 제약, 출력 형식을 바꿔가며 같은 모델에서 더 나은 결과를 끌어냅니다.",
        "tag": "Prompting",
    },
    {
        "title": "RAG · 벡터 검색",
        "desc": "외부 문서를 임베딩하고 검색해 모델의 답변 근거를 확장하는 구조를 학습합니다.",
        "tag": "Retrieval",
    },
    {
        "title": "파인튜닝 · 경량화",
        "desc": "LoRA 등 적은 비용으로 모델을 목적에 맞게 조정하는 방법을 실험합니다.",
        "tag": "Training",
    },
    {
        "title": "AI 에이전트",
        "desc": "도구 호출과 계획 수립을 조합해 여러 단계 작업을 수행하는 워크플로를 설계합니다.",
        "tag": "Agents",
    },
    {
        "title": "LLM 윤리 · 안전",
        "desc": "할루시네이션과 편향을 점검하고, 신뢰할 수 있는 사용 기준을 정리합니다.",
        "tag": "Safety",
    },
]

LOG = [
    {
        "date": "2026.09",
        "title": "파이썬 기초 다지기",
        "desc": "변수, 조건문, 반복문을 실습하고 range(start, stop, step)의 증가값으로 짝수 합을 계산했습니다.",
        "status": "live",
        "status_label": "In Progress",
    },
    {
        "date": "2026.10",
        "title": "Transformer 구조 학습",
        "desc": "토큰화, 어텐션, 디코딩 과정을 노트로 정리하고 직접 손으로 계산해 확인했습니다.",
        "status": "live",
        "status_label": "In Progress",
    },
    {
        "date": "2026.10",
        "title": "프롬프트 비교 실험",
        "desc": "역할, 제약, 출력 형식 지정 전후의 응답 차이를 같은 질문으로 비교해 기록했습니다.",
        "status": "live",
        "status_label": "In Progress",
    },
    {
        "date": "2026.11",
        "title": "RAG 입문",
        "desc": "임베딩과 벡터 검색으로 문서 기반 질의응답을 구성할 예정입니다.",
        "status": "planned",
        "status_label": "Planned",
    },
    {
        "date": "2027.01",
        "title": "소형 모델 파인튜닝",
        "desc": "LoRA로 도메인 데이터를 학습시키고 평가 지표로 성능 변화를 확인할 예정입니다.",
        "status": "planned",
        "status_label": "Planned",
    },
]

TOOLS = [
    ("Python", "기초 문법, 반복문, 함수", "Learning"),
    ("Prompt Design", "역할 · 제약 · 출력 형식 설계", "Practicing"),
    ("Data Handling", "CSV 정리, 표 요약", "Learning"),
    ("Documentation", "Markdown 실험 노트", "Practicing"),
]

STATS = [
    ("Interests", len(INTERESTS)),
    ("Log Entries", len(LOG)),
    ("Tools", len(TOOLS)),
    ("In Progress", sum(1 for entry in LOG if entry["status"] == "live")),
]

TOKEN_LINE = (
    "ATTENTION IS ALL YOU NEED · TOKENIZE · EMBED · RETRIEVE · "
    "REASON · GENERATE · EVALUATE · ALIGN ·"
)


def render_specs():
    cells = []
    for index, (value, label) in enumerate(SPECS):
        cells.append(
            f'<div class="spec reveal" style="--delay:{index * 70}ms">'
            f'<span class="spec__value">{escape(value)}</span>'
            f'<span class="spec__label">{escape(label)}</span>'
            f"</div>"
        )
    return "\n".join(cells)


def render_cards():
    cards = []
    for index, item in enumerate(INTERESTS, start=1):
        cards.append(
            f'<article class="card reveal" style="--delay:{index * 60}ms">'
            f'<span class="card__ghost" aria-hidden="true">{index:02d}</span>'
            f'<div class="card__top">'
            f'<span class="card__idx">{index:02d}</span>'
            f'<span class="card__arrow" aria-hidden="true">↗</span>'
            f"</div>"
            f'<h3 class="card__title">{escape(item["title"])}</h3>'
            f'<p class="card__desc">{escape(item["desc"])}</p>'
            f'<span class="card__foot">{escape(item["tag"])}</span>'
            f"</article>"
        )
    return "\n".join(cards)


def render_log():
    rows = []
    for index, entry in enumerate(LOG):
        status_class = "status status--live" if entry["status"] == "live" else "status"
        rows.append(
            f'<li class="log__row reveal" style="--delay:{index * 60}ms">'
            f'<span class="log__date">{escape(entry["date"])}</span>'
            f"<div>"
            f'<h3 class="log__title">{escape(entry["title"])}</h3>'
            f'<p class="log__desc">{escape(entry["desc"])}</p>'
            f"</div>"
            f'<span class="{status_class}">{escape(entry["status_label"])}</span>'
            f"</li>"
        )
    return "\n".join(rows)


def render_tools():
    cards = []
    for index, (name, desc, state) in enumerate(TOOLS):
        cards.append(
            f'<div class="tool reveal" style="--delay:{index * 70}ms">'
            f'<h3 class="tool__name">{escape(name)}</h3>'
            f'<p class="tool__desc">{escape(desc)}</p>'
            f'<span class="tool__state">{escape(state)}</span>'
            f"</div>"
        )
    return "\n".join(cards)


def render_stats():
    cells = []
    for index, (label, value) in enumerate(STATS):
        cells.append(
            f'<div class="stat reveal" style="--delay:{index * 80}ms">'
            f'<span class="stat__num">{value:02d}</span>'
            f'<span class="stat__label">{escape(label)}</span>'
            f"</div>"
        )
    return "\n".join(cells)


def render_ticker():
    return f"<span>{TOKEN_LINE}</span><span aria-hidden=\"true\">{TOKEN_LINE}</span>"


TEMPLATE = """<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#000000">
<meta name="description" content="부산대학교 산업공학과 김정규의 LLM 학습 자기소개 페이지">
<title>{{NAME}} | LLM 자기소개</title>
<style>
  :root {
    --canvas: #000000;
    --soft: #0d0d0d;
    --card: #1a1a1a;
    --elevated: #262626;
    --hairline: #3c3c3c;
    --hairline-strong: #262626;
    --white: #ffffff;
    --body: #bbbbbb;
    --body-strong: #e6e6e6;
    --muted: #7e7e7e;
    --m-blue-light: #0066b1;
    --m-blue-dark: #1c69d4;
    --m-red: #e22718;
    --m-stripe: linear-gradient(90deg,
      var(--m-blue-light) 0 33.333%,
      var(--m-blue-dark) 33.333% 66.666%,
      var(--m-red) 66.666% 100%);
    --mono: "Consolas", "Cascadia Mono", "SFMono-Regular", monospace;
    --nav-h: 64px;
    --max: 1440px;
    --pad: 40px;
    --ease: cubic-bezier(.2, .6, .2, 1);
  }

  *, *::before, *::after { box-sizing: border-box; }

  html {
    scroll-behavior: smooth;
    scroll-padding-top: calc(var(--nav-h) + 16px);
  }

  body {
    margin: 0;
    background: var(--canvas);
    color: var(--body);
    font-family: "Segoe UI", "Malgun Gothic", -apple-system, BlinkMacSystemFont, "Helvetica Neue", Arial, sans-serif;
    font-size: 16px;
    font-weight: 300;
    line-height: 1.5;
    word-break: keep-all;
    overflow-wrap: break-word;
    -webkit-font-smoothing: antialiased;
    text-rendering: optimizeLegibility;
  }

  body.is-locked { overflow: hidden; }

  h1, h2, h3, p, ol, ul { margin: 0; }
  ol, ul { padding: 0; list-style: none; }
  a { color: inherit; text-decoration: none; }
  button { font: inherit; color: inherit; background: none; border: 0; cursor: pointer; }
  img, svg { display: block; max-width: 100%; }

  ::selection { background: var(--white); color: var(--canvas); }
  :focus-visible { outline: 2px solid var(--white); outline-offset: 3px; }

  ::-webkit-scrollbar { width: 10px; }
  ::-webkit-scrollbar-track { background: #0a0a0a; }
  ::-webkit-scrollbar-thumb { background: #2b2b2b; border: 2px solid #0a0a0a; }
  ::-webkit-scrollbar-thumb:hover { background: var(--hairline); }

  .sr-only {
    position: absolute;
    width: 1px;
    height: 1px;
    padding: 0;
    margin: -1px;
    overflow: hidden;
    clip: rect(0 0 0 0);
    white-space: nowrap;
    border: 0;
  }

  .wrap {
    position: relative;
    max-width: var(--max);
    margin: 0 auto;
    padding: 0 var(--pad);
  }

  .eyebrow {
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: var(--muted);
  }

  .display-lg {
    font-size: clamp(32px, 4.4vw, 56px);
    font-weight: 700;
    line-height: 1.05;
    letter-spacing: -0.02em;
    color: var(--white);
  }

  .reveal {
    opacity: 1;
    transform: translateY(18px);
    transition: transform .7s var(--ease);
    transition-delay: var(--delay, 0ms);
  }
  .reveal.in { transform: none; }

  .skip {
    position: fixed;
    top: 8px;
    left: 8px;
    z-index: 300;
    padding: 12px 16px;
    background: var(--white);
    color: var(--canvas);
    font-size: 14px;
    font-weight: 700;
    transform: translateY(-200%);
    transition: transform .2s var(--ease);
  }
  .skip:focus { transform: none; }

  .progress {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    height: 2px;
    z-index: 400;
    background: var(--m-stripe);
    transform: scaleX(0);
    transform-origin: left;
    will-change: transform;
  }

  /* ---------- Top navigation ---------- */
  .nav {
    position: fixed;
    inset: 0 0 auto 0;
    height: var(--nav-h);
    background: var(--canvas);
    border-bottom: 1px solid var(--hairline-strong);
    z-index: 100;
  }

  .nav__inner {
    position: relative;
    z-index: 2;
    height: 100%;
    max-width: var(--max);
    margin: 0 auto;
    padding: 0 var(--pad);
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 24px;
  }

  .brand {
    display: flex;
    align-items: center;
    gap: 12px;
    min-height: 44px;
  }

  .brand__stripe {
    display: flex;
    align-items: flex-end;
    gap: 2px;
    height: 22px;
  }
  .brand__stripe i {
    display: block;
    width: 4px;
    height: 18px;
    transition: height .3s var(--ease);
  }
  .brand:hover .brand__stripe i { height: 22px; }
  .brand__stripe i:nth-child(1) { background: var(--m-blue-light); }
  .brand__stripe i:nth-child(2) { background: var(--m-blue-dark); }
  .brand__stripe i:nth-child(3) { background: var(--m-red); }

  .brand__text {
    display: flex;
    flex-direction: column;
    gap: 3px;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 1.5px;
    line-height: 1;
    color: var(--white);
  }
  .brand__text small {
    font-size: 9px;
    font-weight: 300;
    letter-spacing: 1.2px;
    color: var(--muted);
  }

  .nav__menu {
    display: flex;
    align-items: center;
    gap: 32px;
  }
  .nav__menu a {
    position: relative;
    display: inline-flex;
    align-items: center;
    height: var(--nav-h);
    font-size: 14px;
    font-weight: 400;
    letter-spacing: .5px;
    text-transform: uppercase;
    color: var(--body);
    transition: color .2s;
  }
  .nav__menu a::after {
    content: "";
    position: absolute;
    left: 0;
    right: 0;
    bottom: -1px;
    height: 2px;
    background: var(--white);
    transform: scaleX(0);
    transform-origin: left;
    transition: transform .25s var(--ease);
  }
  .nav__menu a:hover,
  .nav__menu a[aria-current="true"] { color: var(--white); }
  .nav__menu a[aria-current="true"]::after { transform: scaleX(1); }

  .nav__meta { display: flex; align-items: center; gap: 16px; }
  .brand, .nav__meta { position: relative; z-index: 3; }
  .nav__tag {
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: var(--muted);
  }
  .nav__toggle {
    display: none;
    align-items: center;
    justify-content: center;
    height: 36px;
    padding: 0 12px;
    border: 1px solid var(--hairline);
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 1.5px;
    color: var(--white);
    transition: background .2s, color .2s, border-color .2s;
  }
  .nav__toggle:hover { background: var(--white); color: var(--canvas); border-color: var(--white); }

  /* ---------- Hero ---------- */
  .hero {
    position: relative;
    overflow: hidden;
    padding-top: var(--nav-h);
  }
  .hero::before {
    content: "";
    position: absolute;
    inset: 0;
    background-image:
      linear-gradient(to right, rgba(255, 255, 255, .05) 1px, transparent 1px),
      linear-gradient(to bottom, rgba(255, 255, 255, .05) 1px, transparent 1px);
    background-size: 80px 80px;
    -webkit-mask-image: linear-gradient(to bottom, #000 0%, rgba(0, 0, 0, .35) 62%, transparent 100%);
    mask-image: linear-gradient(to bottom, #000 0%, rgba(0, 0, 0, .35) 62%, transparent 100%);
    animation: gridPan 32s linear infinite;
    pointer-events: none;
  }
  @keyframes gridPan {
    to { background-position: 80px 80px, 80px 80px; }
  }

  .hero__spot {
    position: absolute;
    inset: 0;
    z-index: 0;
    background: radial-gradient(560px circle at var(--x, 62%) var(--y, 32%),
      rgba(255, 255, 255, .08), transparent 62%);
    opacity: 0;
    transition: opacity .5s;
    pointer-events: none;
  }
  .hero:hover .hero__spot { opacity: 1; }

  .hero__inner {
    position: relative;
    z-index: 2;
    max-width: var(--max);
    margin: 0 auto;
    padding: 64px var(--pad) 56px;
    display: grid;
    grid-template-columns: minmax(0, 1.4fr) minmax(260px, .6fr);
    gap: 40px;
    align-items: end;
  }

  .hero__eyebrow { margin-bottom: 24px; }

  .hero h1 {
    font-size: clamp(48px, 7.4vw, 80px);
    font-weight: 700;
    line-height: 1;
    letter-spacing: -0.015em;
    text-transform: uppercase;
    color: var(--white);
  }
  .hero h1 .line { display: block; }

  .hero__lead {
    max-width: 52ch;
    margin-top: 24px;
    font-size: 18px;
    line-height: 1.55;
    color: var(--body);
  }
  .hero__lead strong { font-weight: 400; color: var(--body-strong); }

  .hero__actions {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 24px;
    margin-top: 40px;
  }

  .btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    height: 48px;
    padding: 0 32px;
    border: 1px solid var(--white);
    background: transparent;
    color: var(--white);
    font-size: 14px;
    font-weight: 700;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    transition: background .2s, color .2s;
  }
  .btn:hover { background: var(--white); color: var(--canvas); }

  .textlink {
    display: inline-flex;
    align-items: center;
    gap: 12px;
    font-size: 14px;
    font-weight: 700;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: var(--white);
  }
  .textlink span { transition: transform .25s var(--ease); }
  .textlink:hover span { transform: translateX(6px); }

  .attn {
    align-self: end;
    border: 1px solid var(--hairline-strong);
    background: rgba(13, 13, 13, .72);
    padding: 16px;
  }
  .attn__grid {
    display: grid;
    grid-template-columns: repeat(12, 1fr);
    gap: 4px;
    aspect-ratio: 1;
  }
  .attn__grid span {
    display: block;
    aspect-ratio: 1;
    background: #1c1c1c;
    animation: cellPulse 4.2s ease-in-out infinite;
    animation-delay: var(--d, 0ms);
  }
  .attn__grid .on { background: var(--white); }
  .attn__grid .dim { background: #565656; }
  .attn__grid .accent { background: var(--m-red); }
  @keyframes cellPulse {
    0%, 100% { opacity: .3; }
    50% { opacity: 1; }
  }
  .attn__cap {
    display: flex;
    justify-content: space-between;
    gap: 12px;
    margin-top: 12px;
    font-family: var(--mono);
    font-size: 10px;
    font-weight: 400;
    letter-spacing: 1.2px;
    text-transform: uppercase;
    color: var(--muted);
  }

  .ticker {
    position: relative;
    z-index: 2;
    overflow: hidden;
    padding: 12px 0;
    border-top: 1px solid var(--hairline-strong);
  }
  .ticker__track {
    display: flex;
    width: max-content;
    animation: marquee 38s linear infinite;
  }
  .ticker:hover .ticker__track { animation-play-state: paused; }
  .ticker__track span {
    display: block;
    padding-right: 48px;
    font-family: var(--mono);
    font-size: 12px;
    letter-spacing: 2px;
    white-space: nowrap;
    color: var(--muted);
  }
  @keyframes marquee {
    to { transform: translateX(-50%); }
  }

  .hero__meta {
    position: relative;
    z-index: 2;
    border-top: 1px solid var(--hairline-strong);
  }
  .hero__meta-in {
    display: flex;
    justify-content: space-between;
    gap: 16px;
    padding-top: 16px;
    padding-bottom: 16px;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: var(--muted);
  }

  .mstripe { height: 4px; background: var(--m-stripe); }

  /* ---------- Sections ---------- */
  .section {
    position: relative;
    overflow: hidden;
    padding: 96px 0;
  }
  .section--soft {
    background: var(--soft);
    border-top: 1px solid var(--hairline-strong);
    border-bottom: 1px solid var(--hairline-strong);
  }

  .ghost {
    position: absolute;
    top: -32px;
    right: calc(var(--pad) + 48px);
    font-size: clamp(120px, 16vw, 220px);
    font-weight: 700;
    line-height: 1;
    letter-spacing: -0.04em;
    color: transparent;
    -webkit-text-stroke: 1px #2e2e2e;
    pointer-events: none;
    user-select: none;
    z-index: 0;
  }

  .section__head {
    position: relative;
    z-index: 1;
    display: flex;
    flex-direction: column;
    gap: 16px;
    max-width: 900px;
    margin-bottom: 56px;
  }
  .section__lead {
    max-width: 56ch;
    font-size: 18px;
    line-height: 1.6;
    color: var(--body);
  }

  /* ---------- About ---------- */
  .about__grid {
    position: relative;
    z-index: 1;
    display: grid;
    grid-template-columns: 1.1fr .9fr;
    gap: 40px;
    align-items: start;
    margin-bottom: 56px;
  }
  .about__statement {
    font-size: clamp(24px, 3vw, 32px);
    font-weight: 700;
    line-height: 1.25;
    letter-spacing: -0.02em;
    color: var(--white);
  }
  .about__body {
    display: flex;
    flex-direction: column;
    gap: 20px;
    max-width: 60ch;
    font-size: 17px;
    line-height: 1.65;
    color: var(--body);
  }

  .specs {
    position: relative;
    z-index: 1;
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 16px;
  }
  .spec {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    gap: 24px;
    min-height: 132px;
    padding: 24px;
    background: var(--soft);
    transition: background .25s, transform .25s var(--ease);
  }
  .spec:hover { background: #141414; transform: translateY(-4px); }
  .spec__value {
    font-size: 24px;
    font-weight: 700;
    line-height: 1.2;
    letter-spacing: -0.01em;
    color: var(--white);
  }
  .spec__label {
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: var(--muted);
  }

  /* ---------- Interest cards ---------- */
  .cards {
    position: relative;
    z-index: 1;
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 24px;
  }
  .card {
    position: relative;
    overflow: hidden;
    isolation: isolate;
    display: flex;
    flex-direction: column;
    gap: 16px;
    min-height: 260px;
    padding: 24px;
    background: var(--card);
    border: 1px solid var(--hairline-strong);
    transition: background .25s, border-color .25s, transform .35s var(--ease);
  }
  .card:hover { background: #1f1f1f; border-color: var(--hairline); transform: translateY(-4px); }
  .card::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 3px;
    z-index: 3;
    background: var(--m-stripe);
    transform: scaleX(0);
    transform-origin: left;
    transition: transform .45s var(--ease);
  }
  .card:hover::before { transform: scaleX(1); }
  .card::after {
    content: "";
    position: absolute;
    inset: 0;
    z-index: 0;
    background: radial-gradient(420px circle at var(--x, 50%) var(--y, 50%),
      rgba(255, 255, 255, .07), transparent 45%);
    opacity: 0;
    transition: opacity .3s;
    pointer-events: none;
  }
  .card:hover::after { opacity: 1; }
  .card > * { position: relative; z-index: 1; }
  .card > .card__ghost {
    position: absolute;
    right: 12px;
    bottom: -22px;
    z-index: 0;
    font-size: 96px;
    font-weight: 700;
    line-height: 1;
    color: #232323;
    pointer-events: none;
    transition: color .3s;
  }
  .card:hover > .card__ghost { color: #2b2b2b; }

  .card__top {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    gap: 16px;
  }
  .card__idx {
    font-family: var(--mono);
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 1.5px;
    color: var(--muted);
  }
  .card__arrow {
    font-size: 18px;
    line-height: 1;
    color: var(--muted);
    opacity: 0;
    transform: translate(-4px, 4px);
    transition: opacity .3s, transform .3s var(--ease), color .3s;
  }
  .card:hover .card__arrow { opacity: 1; transform: none; color: var(--white); }
  .card__title {
    font-size: 24px;
    font-weight: 700;
    line-height: 1.25;
    letter-spacing: -0.01em;
    color: var(--white);
  }
  .card__desc { font-size: 14px; line-height: 1.6; color: var(--body); }
  .card__foot {
    margin-top: auto;
    padding-top: 16px;
    border-top: 1px solid var(--hairline-strong);
    font-family: var(--mono);
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 1.4px;
    text-transform: uppercase;
    color: var(--muted);
  }

  /* ---------- Learning log ---------- */
  .log { position: relative; z-index: 1; border-top: 1px solid var(--hairline); }
  .log__row {
    display: grid;
    grid-template-columns: 140px minmax(0, 1fr) 140px;
    gap: 24px;
    align-items: start;
    padding: 24px 0;
    border-bottom: 1px solid var(--hairline);
    box-shadow: inset 0 0 0 transparent;
    transition: background .25s, box-shadow .25s, padding-left .25s var(--ease);
  }
  .log__row:hover {
    padding-left: 16px;
    background: #0a0a0a;
    box-shadow: inset 2px 0 0 var(--white);
  }
  .log__date {
    padding-top: 4px;
    font-family: var(--mono);
    font-size: 13px;
    font-weight: 700;
    letter-spacing: .5px;
    color: var(--muted);
  }
  .log__title {
    font-size: 20px;
    font-weight: 700;
    letter-spacing: -0.01em;
    color: var(--white);
  }
  .log__desc { margin-top: 8px; font-size: 15px; line-height: 1.6; color: var(--body); }
  .status {
    justify-self: end;
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding-top: 6px;
    font-family: var(--mono);
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 1.4px;
    text-transform: uppercase;
    color: var(--muted);
    white-space: nowrap;
  }
  .status::before { content: ""; width: 6px; height: 6px; background: var(--muted); }
  .status--live { color: var(--white); }
  .status--live::before {
    background: var(--m-red);
    animation: dotPulse 1.8s ease-in-out infinite;
  }
  @keyframes dotPulse {
    0%, 100% { box-shadow: 0 0 0 0 rgba(226, 39, 24, .5); }
    50% { box-shadow: 0 0 0 6px rgba(226, 39, 24, 0); }
  }

  /* ---------- Toolbox ---------- */
  .tools {
    position: relative;
    z-index: 1;
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 16px;
  }
  .tool {
    display: flex;
    flex-direction: column;
    gap: 12px;
    min-height: 180px;
    padding: 24px;
    background: var(--canvas);
    border: 1px solid var(--hairline-strong);
    transition: border-color .25s, transform .3s var(--ease);
  }
  .tool:hover { border-color: var(--white); transform: translateY(-4px); }
  .tool__name {
    font-size: 20px;
    font-weight: 700;
    letter-spacing: -0.01em;
    color: var(--white);
  }
  .tool__desc { font-size: 14px; line-height: 1.55; color: var(--body); }
  .tool__state {
    margin-top: auto;
    font-family: var(--mono);
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 1.4px;
    text-transform: uppercase;
    color: var(--muted);
  }

  /* ---------- Stats ---------- */
  .stats {
    position: relative;
    overflow: hidden;
    padding: 72px 0;
    border-top: 1px solid var(--hairline);
    border-bottom: 1px solid var(--hairline);
  }
  .stats__head { margin-bottom: 40px; }
  .stats__grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 24px;
  }
  .stat { display: flex; flex-direction: column; gap: 10px; }
  .stat__num {
    font-size: clamp(48px, 6vw, 80px);
    font-weight: 700;
    line-height: 1;
    letter-spacing: -0.03em;
    color: var(--white);
    font-variant-numeric: tabular-nums;
  }
  .stat__label {
    font-family: var(--mono);
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: var(--muted);
  }

  /* ---------- Contact ---------- */
  .cta { position: relative; overflow: hidden; padding: 96px 0; text-align: center; }
  .cta__inner { max-width: 760px; margin: 0 auto; padding: 0 var(--pad); }
  .cta h2 {
    margin-top: 16px;
    font-size: clamp(28px, 4vw, 40px);
    font-weight: 700;
    line-height: 1.15;
    letter-spacing: -0.02em;
    color: var(--white);
  }
  .cta p { margin-top: 20px; font-size: 17px; line-height: 1.6; color: var(--body); }
  .cta .btn { margin-top: 40px; }

  /* ---------- Footer ---------- */
  .footer {
    overflow: hidden;
    padding: 64px 0 32px;
    border-top: 1px solid var(--hairline-strong);
    background: var(--canvas);
  }
  .footer__mark {
    display: block;
    margin-bottom: 48px;
    font-size: clamp(40px, 11.5vw, 168px);
    font-weight: 700;
    line-height: .85;
    letter-spacing: -0.03em;
    white-space: nowrap;
    color: transparent;
    -webkit-text-stroke: 1px #2f2f2f;
    transition: color .4s, -webkit-text-stroke-color .4s;
  }
  .footer__mark:hover { color: var(--white); -webkit-text-stroke-color: var(--white); }
  .footer__grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 24px;
    padding-bottom: 48px;
    border-bottom: 1px solid var(--hairline);
  }
  .footer__h {
    margin-bottom: 16px;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: var(--muted);
  }
  .footer__col li + li { margin-top: 10px; }
  .footer__col a,
  .footer__col span { font-size: 14px; font-weight: 300; line-height: 1.5; color: var(--body); }
  .footer__col a:hover { color: var(--white); }
  .footer__note { font-size: 12px; line-height: 1.6; color: var(--muted); }
  .footer__bottom {
    display: flex;
    justify-content: space-between;
    gap: 16px;
    padding-top: 24px;
    padding-right: 80px;
    font-size: 11px;
    font-weight: 400;
    letter-spacing: 1px;
    text-transform: uppercase;
    color: var(--muted);
  }

  .totop {
    position: fixed;
    right: 24px;
    bottom: 24px;
    z-index: 90;
    display: grid;
    place-items: center;
    width: 48px;
    height: 48px;
    border-radius: 50%;
    background: var(--card);
    border: 1px solid var(--hairline);
    color: var(--white);
    font-size: 18px;
    line-height: 1;
    opacity: 0;
    visibility: hidden;
    transform: translateY(8px);
    transition: opacity .3s, visibility .3s, transform .3s var(--ease), background .2s;
  }
  .totop.show { opacity: 1; visibility: visible; transform: none; }
  .totop:hover { background: var(--white); color: var(--canvas); }

  /* ---------- Responsive ---------- */
  @media (max-width: 1100px) {
    .hero__inner { grid-template-columns: minmax(0, 1fr) minmax(220px, .5fr); }
    .specs { grid-template-columns: repeat(2, 1fr); }
    .cards { grid-template-columns: repeat(2, 1fr); }
    .tools { grid-template-columns: repeat(2, 1fr); }
  }

  @media (max-width: 900px) {
    .ghost { display: none; }
    .hero__inner { grid-template-columns: 1fr; gap: 48px; padding-bottom: 48px; }
    .attn { max-width: 320px; }
    .about__grid { grid-template-columns: 1fr; gap: 32px; }
    .stats__grid { grid-template-columns: repeat(2, 1fr); gap: 32px 24px; }
  }

  @media (max-width: 768px) {
    :root { --pad: 24px; }

    .nav__tag { display: none; }
    .nav__toggle { display: inline-flex; }

    .nav__menu {
      position: fixed;
      inset: 0;
      z-index: 1;
      display: flex;
      flex-direction: column;
      justify-content: center;
      gap: 0;
      padding: 96px var(--pad) 40px;
      background: var(--canvas);
      transform: translateY(-100%);
      visibility: hidden;
      transition: transform .35s var(--ease), visibility .35s;
    }
    .nav.is-open .nav__menu { transform: none; visibility: visible; }
    .nav__menu::before {
      content: "";
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 4px;
      background: var(--m-stripe);
    }
    .nav__menu a {
      display: flex;
      width: 100%;
      height: auto;
      padding: 20px 0;
      border-bottom: 1px solid var(--hairline-strong);
      font-size: clamp(28px, 7vw, 36px);
      font-weight: 700;
      letter-spacing: -0.01em;
      color: var(--white);
    }
    .nav__menu a::after { display: none; }

    .hero__inner { padding-top: 48px; }
    .hero h1 { font-size: clamp(44px, 12vw, 64px); }
    .hero__lead { font-size: 16px; }
    .hero__meta-in { flex-wrap: wrap; gap: 8px 16px; }
    .ticker__track span { font-size: 11px; }

    .section { padding: 64px 0; }
    .section__head { margin-bottom: 40px; }

    .specs,
    .cards,
    .tools { grid-template-columns: 1fr; }

    .log__row { grid-template-columns: 1fr; gap: 8px; }
    .status { justify-self: start; padding-top: 0; }

    .footer__grid { grid-template-columns: repeat(2, 1fr); gap: 32px 24px; }
    .footer__bottom { flex-direction: column; gap: 8px; padding-right: 0; padding-bottom: 56px; }
  }

  @media (max-width: 420px) {
    .specs { grid-template-columns: 1fr; }
    .footer__grid { grid-template-columns: 1fr; }
    .attn { display: none; }
    .stats__grid { grid-template-columns: 1fr 1fr; }
  }

  @media (prefers-reduced-motion: reduce) {
    html { scroll-behavior: auto; }
    .reveal { transform: none; transition: none; }
    .hero::before,
    .attn__grid span,
    .ticker__track,
    .status--live::before { animation: none; }
    *, *::before, *::after {
      transition-duration: .01ms !important;
      animation-duration: .01ms !important;
    }
  }
</style>
</head>
<body>
<div class="progress" aria-hidden="true"></div>
<a class="skip" href="#main">본문으로 건너뛰기</a>

<header class="nav" id="top">
  <div class="nav__inner">
    <a class="brand" href="#top" aria-label="맨 위로">
      <span class="brand__stripe" aria-hidden="true"><i></i><i></i><i></i></span>
      <span class="brand__text">{{NAME_EN}}<small>LLM PORTFOLIO</small></span>
    </a>

    <nav class="nav__menu" id="menu" aria-label="주요 섹션">
      <a href="#about">About</a>
      <a href="#interests">Interests</a>
      <a href="#log">Log</a>
      <a href="#contact">Contact</a>
    </nav>

    <div class="nav__meta">
      <span class="nav__tag">PNU · IE</span>
      <button class="nav__toggle" type="button" aria-expanded="false" aria-controls="menu">MENU</button>
    </div>
  </div>
</header>

<main id="main">

  <section class="hero" aria-labelledby="hero-title">
    <div class="hero__spot" aria-hidden="true"></div>
    <div class="hero__inner">
      <div>
        <p class="eyebrow hero__eyebrow">Pusan National University / Industrial Engineering</p>
        <h1 id="hero-title">
          <span class="line"><span>Learning</span></span>
          <span class="line"><span>Language</span></span>
          <span class="line"><span>Models.</span></span>
        </h1>
        <p class="hero__lead">
          LLM의 원리를 이해하고 직접 만들어보며 배우는 산업공학도
          <strong>{{NAME}}</strong>입니다. 모델을 사용하는 데서 멈추지 않고,
          그 작동 원리를 파고듭니다.
        </p>
        <div class="hero__actions">
          <a class="btn" href="#interests">관심 분야 보기</a>
          <a class="textlink" href="#log">학습 기록 <span aria-hidden="true">→</span></a>
        </div>
      </div>

      <div class="attn" aria-hidden="true">
        <div class="attn__grid" data-attention></div>
        <div class="attn__cap"><span>Attention Map</span><span>12 × 12</span></div>
      </div>
    </div>

    <div class="ticker" aria-hidden="true">
      <div class="ticker__track">{{TICKER}}</div>
    </div>

    <div class="hero__meta">
      <div class="wrap hero__meta-in">
        <span>Scroll</span>
        <span>Busan, KR · {{YEAR}}</span>
        <span>LLM / RAG / Agent</span>
      </div>
    </div>
  </section>

  <div class="mstripe" aria-hidden="true"></div>

  <section class="section" id="about" aria-labelledby="about-title">
    <div class="wrap">
      <span class="ghost" aria-hidden="true">01</span>
      <div class="section__head">
        <p class="eyebrow">01 / About</p>
        <h2 class="display-lg" id="about-title">모델을 쓰는 사람에서,<br>모델을 이해하는 사람으로.</h2>
      </div>

      <div class="about__grid">
        <p class="about__statement reveal">
          산업공학은 시스템을 측정하고 개선하는 학문입니다.
          저는 같은 시선으로 언어 모델을 바라봅니다.
        </p>
        <div class="about__body reveal" style="--delay:120ms">
          <p>
            프롬프트가 왜 특정 출력을 만드는지, 검색된 문서가 답변 품질을 어떻게
            바꾸는지, 작은 모델이 어디까지 감당할 수 있는지를 실험으로 확인합니다.
          </p>
          <p>
            현재는 파이썬 기초를 다지면서 Transformer 구조와 프롬프트 설계를 함께
            공부하고 있습니다. 목표는 LLM을 활용해 실제 업무 흐름을 개선하는
            도구를 만드는 것입니다.
          </p>
        </div>
      </div>

      <div class="specs">
{{SPECS}}
      </div>
    </div>
  </section>

  <section class="section section--soft" id="interests" aria-labelledby="interests-title">
    <div class="wrap">
      <span class="ghost" aria-hidden="true">02</span>
      <div class="section__head">
        <p class="eyebrow">02 / Interests</p>
        <h2 class="display-lg" id="interests-title">여섯 개의 질문,<br>하나의 언어 모델.</h2>
        <p class="section__lead">
          원리에서 안전성까지, LLM을 둘러싼 여섯 가지 주제를 순서대로
          파고들고 있습니다.
        </p>
      </div>

      <div class="cards">
{{CARDS}}
      </div>
    </div>
  </section>

  <section class="section" id="log" aria-labelledby="log-title">
    <div class="wrap">
      <span class="ghost" aria-hidden="true">03</span>
      <div class="section__head">
        <p class="eyebrow">03 / Learning Log</p>
        <h2 class="display-lg" id="log-title">배운 것을 기록하고,<br>기록한 것을 다시 검증합니다.</h2>
      </div>

      <ol class="log">
{{LOG_ROWS}}
      </ol>
    </div>
  </section>

  <section class="section section--soft" id="toolbox" aria-labelledby="toolbox-title">
    <div class="wrap">
      <span class="ghost" aria-hidden="true">04</span>
      <div class="section__head">
        <p class="eyebrow">04 / Toolbox</p>
        <h2 class="display-lg" id="toolbox-title">지금 다루는 것들.</h2>
        <p class="section__lead">숙련도를 수치로 과장하지 않고, 현재 사용하는 범위만 적었습니다.</p>
      </div>

      <div class="tools">
{{TOOLS}}
      </div>
    </div>
  </section>

  <section class="stats" aria-labelledby="stats-title">
    <div class="wrap">
      <div class="stats__head">
        <p class="eyebrow">05 / Snapshot</p>
        <h2 class="sr-only" id="stats-title">학습 현황</h2>
      </div>
      <div class="stats__grid">
{{STATS}}
      </div>
    </div>
  </section>

  <div class="mstripe" aria-hidden="true"></div>

  <section class="cta" id="contact" aria-labelledby="contact-title">
    <div class="cta__inner">
      <p class="eyebrow">06 / Contact</p>
      <h2 id="contact-title">함께 배우고 만들<br>사람을 찾고 있습니다.</h2>
      <p>LLM 학습 기록과 실험 아이디어를 공유하고 있습니다. 편하게 연락 주세요.</p>
      <a class="btn" href="mailto:{{EMAIL}}">이메일 보내기</a>
    </div>
  </section>

</main>

<footer class="footer">
  <div class="wrap">
    <span class="footer__mark" aria-hidden="true">{{NAME_EN}}</span>
    <div class="footer__grid">
      <div class="footer__col">
        <p class="footer__h">Sitemap</p>
        <ul>
          <li><a href="#about">About</a></li>
          <li><a href="#interests">Interests</a></li>
          <li><a href="#log">Learning Log</a></li>
          <li><a href="#contact">Contact</a></li>
        </ul>
      </div>

      <div class="footer__col">
        <p class="footer__h">Interests</p>
        <ul>
          <li><a href="#interests">Transformer</a></li>
          <li><a href="#interests">RAG · Retrieval</a></li>
          <li><a href="#interests">AI Agents</a></li>
        </ul>
      </div>

      <div class="footer__col">
        <p class="footer__h">Contact</p>
        <ul>
          <li><a href="mailto:{{EMAIL}}">이메일 보내기</a></li>
          <li><span>{{UNIVERSITY}} {{MAJOR}}</span></li>
        </ul>
      </div>

      <div class="footer__col">
        <p class="footer__h">About This Page</p>
        <p class="footer__note">
          BMW M 디자인 시스템의 레이아웃 원칙에서 영감을 받은 학습용
          자기소개 페이지입니다. BMW와 무관합니다.
        </p>
      </div>
    </div>

    <div class="footer__bottom">
      <span>© {{YEAR}} {{NAME_EN}}</span>
      <span>Single HTML · Built with Python · Designed after BMW M System</span>
    </div>
  </div>
</footer>

<button class="totop" type="button" aria-label="맨 위로">↑</button>

<script>
(function () {
  var nav = document.querySelector('.nav');
  var toggle = document.querySelector('.nav__toggle');
  var menuLinks = Array.prototype.slice.call(document.querySelectorAll('.nav__menu a'));
  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function setMenu(open) {
    nav.classList.toggle('is-open', open);
    document.body.classList.toggle('is-locked', open);
    toggle.setAttribute('aria-expanded', String(open));
    toggle.textContent = open ? 'CLOSE' : 'MENU';
  }

  if (toggle) {
    toggle.addEventListener('click', function () {
      setMenu(!nav.classList.contains('is-open'));
    });
  }

  menuLinks.forEach(function (link) {
    link.addEventListener('click', function () { setMenu(false); });
  });

  document.addEventListener('keydown', function (event) {
    if (event.key === 'Escape') setMenu(false);
  });

  window.addEventListener('resize', function () {
    if (window.innerWidth > 768) setMenu(false);
    updateProgress();
  });

  var progress = document.querySelector('.progress');
  function updateProgress() {
    if (!progress) return;
    var root = document.documentElement;
    var max = root.scrollHeight - root.clientHeight;
    var ratio = max > 0 ? root.scrollTop / max : 0;
    progress.style.transform = 'scaleX(' + ratio + ')';
  }
  window.addEventListener('scroll', updateProgress, { passive: true });
  updateProgress();

  var toTop = document.querySelector('.totop');
  if (toTop) {
    window.addEventListener('scroll', function () {
      toTop.classList.toggle('show', window.scrollY > 700);
    }, { passive: true });
    toTop.addEventListener('click', function () {
      window.scrollTo({ top: 0, behavior: reduceMotion ? 'auto' : 'smooth' });
    });
  }

  var revealItems = Array.prototype.slice.call(document.querySelectorAll('.reveal'));
  if (reduceMotion || !('IntersectionObserver' in window)) {
    revealItems.forEach(function (el) { el.classList.add('in'); });
  } else {
    var revealObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        entry.target.classList.add('in');
        revealObserver.unobserve(entry.target);
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    revealItems.forEach(function (el) { revealObserver.observe(el); });
  }

  var spyLinks = Array.prototype.slice.call(
    document.querySelectorAll('.nav__menu a[href^="#"]')
  );
  var sections = spyLinks
    .map(function (link) { return document.querySelector(link.getAttribute('href')); })
    .filter(Boolean);

  if ('IntersectionObserver' in window) {
    var spy = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        spyLinks.forEach(function (link) { link.removeAttribute('aria-current'); });
        var active = spyLinks.find(function (link) {
          return link.getAttribute('href') === '#' + entry.target.id;
        });
        if (active) active.setAttribute('aria-current', 'true');
      });
    }, { rootMargin: '-45% 0px -50% 0px' });
    sections.forEach(function (section) { spy.observe(section); });
  }

  var grid = document.querySelector('[data-attention]');
  if (grid) {
    var frag = document.createDocumentFragment();
    for (var i = 0; i < 144; i++) {
      var cell = document.createElement('span');
      var row = Math.floor(i / 12);
      var col = i % 12;
      var distance = Math.abs(row - col);
      if (distance === 0) {
        cell.className = 'on';
      } else if (distance === 1 && row % 4 === 0) {
        cell.className = 'dim';
      } else if (i === 62) {
        cell.className = 'accent';
      }
      cell.style.setProperty('--d', ((row + col) * 45) + 'ms');
      frag.appendChild(cell);
    }
    grid.appendChild(frag);
  }

  var finePointer = window.matchMedia('(hover: hover) and (pointer: fine)').matches;
  if (finePointer) {
    var hero = document.querySelector('.hero');
    if (hero) {
      hero.addEventListener('pointermove', function (event) {
        var rect = hero.getBoundingClientRect();
        hero.style.setProperty('--x', (event.clientX - rect.left) + 'px');
        hero.style.setProperty('--y', (event.clientY - rect.top) + 'px');
      });
    }

    Array.prototype.slice.call(document.querySelectorAll('.card')).forEach(function (card) {
      card.addEventListener('pointermove', function (event) {
        var rect = card.getBoundingClientRect();
        card.style.setProperty('--x', (event.clientX - rect.left) + 'px');
        card.style.setProperty('--y', (event.clientY - rect.top) + 'px');
      });
    });
  }
})();
</script>
</body>
</html>
"""


def build():
    page = TEMPLATE
    replacements = {
        "{{NAME_EN}}": escape(PROFILE["name_en"]),
        "{{NAME}}": escape(PROFILE["name"]),
        "{{UNIVERSITY}}": escape(PROFILE["university"]),
        "{{MAJOR}}": escape(PROFILE["major"]),
        "{{EMAIL}}": escape(PROFILE["email"]),
        "{{YEAR}}": str(PROFILE["year"]),
        "{{SPECS}}": render_specs(),
        "{{CARDS}}": render_cards(),
        "{{LOG_ROWS}}": render_log(),
        "{{TOOLS}}": render_tools(),
        "{{STATS}}": render_stats(),
        "{{TICKER}}": render_ticker(),
    }
    for key, value in replacements.items():
        page = page.replace(key, value)

    OUTPUT.write_text(page, encoding="utf-8")

    print(f"generated : {OUTPUT}")
    print(f"interests : {len(INTERESTS)}")
    print(f"log       : {len(LOG)} (in progress {STATS[3][1]})")
    print(f"tools     : {len(TOOLS)}")
    print(f"bytes     : {len(page.encode('utf-8'))}")


if __name__ == "__main__":
    build()
