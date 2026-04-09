import streamlit as st
import random
import math

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(page_title="Mastermind Educativo", page_icon="🎯", layout="centered")

# ══════════════════════════════════════════════════════════════════════════════
# CSS
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=DM+Sans:wght@400;500;600&family=Nunito:wght@400;600;700;800&display=swap');

:root {
    --bg:      #f0f4f8;
    --panel:   #ffffff;
    --border:  #dde3ec;
    --accent:  #2563eb;
    --accent2: #f97316;
    --purple:  #7c3aed;
    --gold:    #d97706;
    --text:    #1e293b;
    --muted:   #64748b;
    --success: #16a34a;
    --danger:  #dc2626;
    --shadow:  rgba(30,41,59,0.10);
}

html,body,[data-testid="stAppViewContainer"]{
    background-color:var(--bg)!important;
    color:var(--text);
    font-family:'DM Sans',sans-serif;
}
[data-testid="stSidebar"]{
    background:linear-gradient(180deg,#fff 0%,#f1f5fb 100%)!important;
    border-right:1px solid var(--border);
}
[data-testid="stSidebar"] *{color:var(--text)!important;}
h1,h2,h3{font-family:'Orbitron',monospace!important;}

/* ── Menu ── */
.intro-wrapper{max-width:640px;margin:0 auto;padding:2rem 0 3rem;}
.intro-title{text-align:center;margin-bottom:1.4rem;}
.intro-title h1{font-size:3rem;font-weight:900;background:linear-gradient(135deg,var(--accent),var(--accent2));-webkit-background-clip:text;-webkit-text-fill-color:transparent;letter-spacing:.1em;margin:0;}
.intro-title p{color:var(--muted);font-size:.85rem;letter-spacing:.1em;margin-top:.3rem;font-family:'Orbitron',monospace;}
.menu-grid{display:grid;grid-template-columns:1fr 1fr 1fr;gap:16px;margin:1.6rem 0;}
.menu-card{background:var(--panel);border:2px solid var(--border);border-radius:16px;padding:1.6rem 1.2rem;text-align:center;box-shadow:0 4px 16px var(--shadow);}
.menu-card.game{border-color:#bfdbfe;}
.menu-card.quiz{border-color:#ddd6fe;}
.menu-card.inc{border-color:#fde68a;}
.menu-icon{font-size:2.2rem;margin-bottom:.6rem;}
.menu-label{font-family:'Orbitron',monospace;font-size:.7rem;font-weight:700;letter-spacing:.08em;color:var(--muted);}
.menu-title{font-size:.95rem;font-weight:700;color:var(--text);margin:.3rem 0;}
.menu-desc{font-size:.76rem;color:var(--muted);line-height:1.5;}

/* ── Cards genéricos ── */
.rules-card{background:var(--panel);border:1px solid var(--border);border-radius:16px;padding:1.8rem 2rem;margin:1.4rem 0;box-shadow:0 4px 20px var(--shadow);}
.rules-card h3{font-size:.85rem!important;color:var(--accent)!important;letter-spacing:.12em;margin:0 0 1rem;}
.rule-item{display:flex;align-items:flex-start;gap:14px;padding:.75rem 0;border-bottom:1px solid var(--border);font-size:.92rem;line-height:1.55;}
.rule-item:last-child{border-bottom:none;}
.rule-icon{font-size:1.3rem;flex-shrink:0;margin-top:1px;}
.rule-title{font-weight:600;display:block;margin-bottom:2px;}
.rule-desc{color:var(--muted);font-size:.84rem;}

/* ── Jogo principal ── */
.title-block{text-align:center;padding:1.5rem 1rem .5rem;}
.title-block h1{font-size:2.4rem;font-weight:900;background:linear-gradient(135deg,var(--accent),var(--accent2));-webkit-background-clip:text;-webkit-text-fill-color:transparent;letter-spacing:.1em;margin:0;}
.title-block p{color:var(--muted);font-size:.78rem;margin-top:.3rem;letter-spacing:.08em;font-family:'Orbitron',monospace;}
.peg-row{display:flex;gap:10px;align-items:center;justify-content:center;margin:4px 0;}
.peg{width:44px;height:44px;border-radius:50%;border:2px solid rgba(0,0,0,.08);box-shadow:0 3px 8px rgba(0,0,0,.18),inset 0 2px 4px rgba(255,255,255,.4);display:inline-block;flex-shrink:0;}
.peg-empty{background:#e2e8f0;border:2px dashed var(--border);box-shadow:none;}
.peg-sm{width:16px;height:16px;border-radius:50%;display:inline-block;flex-shrink:0;}
.peg-sm-black{background:#1e293b;border:1px solid #334155;}
.peg-sm-white{background:#f1f5f9;border:1px solid #94a3b8;box-shadow:0 0 3px rgba(0,0,0,.15);}
.peg-sm-empty{background:#e2e8f0;border:1px dashed #cbd5e1;}
.fb-grid{display:grid;grid-template-columns:repeat(auto-fill,16px);gap:4px;width:60px;align-items:center;}
.row-card{background:var(--panel);border:1px solid var(--border);border-radius:10px;padding:10px 16px;margin:6px 0;display:flex;align-items:center;gap:14px;box-shadow:0 2px 6px var(--shadow);}
.row-num{font-family:'Orbitron',monospace;font-size:.7rem;color:var(--muted);width:24px;text-align:right;}
.separator{flex:1;}
.stat-grid{display:flex;gap:12px;justify-content:center;flex-wrap:wrap;margin:.6rem 0;}
.stat-card{background:var(--panel);border:1px solid var(--border);border-radius:8px;padding:.5rem 1rem;text-align:center;min-width:80px;box-shadow:0 2px 6px var(--shadow);}
.stat-val{font-family:'Orbitron',monospace;font-size:1.3rem;color:var(--accent);font-weight:700;}
.stat-lbl{font-size:.65rem;color:var(--muted);letter-spacing:.08em;}
.banner-win{background:linear-gradient(135deg,#f0fdf4,#dcfce7);border:1px solid #86efac;border-radius:12px;padding:1.2rem;text-align:center;font-family:'Orbitron',monospace;color:var(--success);box-shadow:0 4px 16px rgba(22,163,74,.12);margin:1rem 0;}
.banner-lose{background:linear-gradient(135deg,#fff1f2,#ffe4e6);border:1px solid #fca5a5;border-radius:12px;padding:1.2rem;text-align:center;font-family:'Orbitron',monospace;color:var(--danger);box-shadow:0 4px 16px rgba(220,38,38,.10);margin:1rem 0;}
.info-box{background:#eff6ff;border:1px solid #bfdbfe;border-left:3px solid var(--accent);border-radius:6px;padding:.8rem 1rem;font-size:.82rem;color:#1d4ed8;margin:.6rem 0;line-height:1.6;}
.secret-reveal{background:#fffbeb;border:1px solid #fcd34d;border-radius:10px;padding:.8rem 1.2rem;text-align:center;margin:.8rem 0;}
.secret-label{font-family:'Orbitron',monospace;font-size:.65rem;color:var(--gold);letter-spacing:.12em;margin-bottom:8px;}
div[data-baseweb="select"]>div{background:#f8fafc!important;border:1px solid var(--border)!important;border-radius:8px!important;color:var(--text)!important;}
.stButton>button{font-family:'Orbitron',monospace!important;font-weight:700!important;border-radius:6px!important;border:none!important;letter-spacing:.06em!important;transition:all .2s!important;}
.stButton>button:hover{transform:translateY(-1px);box-shadow:0 4px 16px rgba(37,99,235,.25)!important;}
div[data-testid="stMetric"]{display:none;}

/* ── Seleção de cores por clique (jogo principal) ── */
.color-palette{display:flex;gap:10px;justify-content:center;flex-wrap:wrap;margin:.6rem 0 .4rem;}
.color-btn{
    width:52px;height:52px;border-radius:50%;cursor:pointer;
    border:3px solid transparent;
    box-shadow:0 3px 8px rgba(0,0,0,.18),inset 0 2px 4px rgba(255,255,255,.3);
    transition:all .15s;flex-shrink:0;
}
.color-btn:hover{transform:scale(1.12);box-shadow:0 5px 14px rgba(0,0,0,.25);}
.color-btn.active{border-color:#1e293b;box-shadow:0 0 0 4px rgba(30,41,59,.2),inset 0 2px 4px rgba(255,255,255,.3);}

.slot-row{display:flex;gap:12px;justify-content:center;margin:.8rem 0;}
.game-slot{
    width:56px;height:56px;border-radius:14px;
    display:flex;align-items:center;justify-content:center;
    border:3px dashed #cbd5e1;background:#f8fafc;
    box-shadow:0 2px 6px rgba(0,0,0,.06);flex-shrink:0;
    transition:all .15s;
}
.game-slot.filled{border-style:solid;border-color:rgba(0,0,0,.12);}
.game-slot.next{border-color:#2563eb;background:#eff6ff;}

/* ── Quiz ── */
.quiz-header{background:linear-gradient(135deg,#f5f3ff,#ede9fe);border:1px solid #c4b5fd;border-radius:16px;padding:1.4rem 1.8rem;margin-bottom:1.4rem;}
.quiz-header h2{font-size:1.1rem!important;color:var(--purple)!important;margin:0 0 .3rem;}
.quiz-header p{color:#6d28d9;font-size:.84rem;margin:0;}
.q-card{background:var(--panel);border:1px solid var(--border);border-radius:14px;padding:1.6rem 1.8rem;margin:1rem 0;box-shadow:0 3px 12px var(--shadow);}
.q-number{font-family:'Orbitron',monospace;font-size:.65rem;color:var(--muted);letter-spacing:.1em;margin-bottom:.5rem;}
.q-text{font-size:1rem;font-weight:600;color:var(--text);line-height:1.55;margin-bottom:1rem;}
.q-formula{background:#f8fafc;border:1px solid var(--border);border-radius:8px;padding:.7rem 1rem;font-size:.95rem;color:var(--accent);font-family:'Orbitron',monospace;margin:.6rem 0;text-align:center;}
.q-hint{background:#fffbeb;border:1px solid #fcd34d;border-left:3px solid var(--gold);border-radius:6px;padding:.6rem .9rem;font-size:.82rem;color:#92400e;margin:.8rem 0;}
.answer-correct{background:#f0fdf4;border:1px solid #86efac;border-radius:8px;padding:.8rem 1rem;color:#166534;font-size:.88rem;margin:.6rem 0;}
.answer-wrong{background:#fff1f2;border:1px solid #fca5a5;border-radius:8px;padding:.8rem 1rem;color:#991b1b;font-size:.88rem;margin:.6rem 0;}
.score-box{background:linear-gradient(135deg,#eff6ff,#dbeafe);border:1px solid #93c5fd;border-radius:14px;padding:1.4rem;text-align:center;margin:1rem 0;}
.score-big{font-family:'Orbitron',monospace;font-size:2.8rem;font-weight:900;color:var(--accent);}
.score-label{color:var(--muted);font-size:.82rem;letter-spacing:.08em;}
.progress-bar-outer{background:#e2e8f0;border-radius:99px;height:8px;margin:.5rem 0;}
.progress-bar-inner{background:linear-gradient(90deg,var(--accent),var(--accent2));border-radius:99px;height:8px;}

/* ══ MODO INCLUSIVO ══════════════════════════════════════════════════════════ */
.inc-wrapper{max-width:580px;margin:0 auto;padding:1rem 0 3rem;}
.inc-title{text-align:center;padding:1rem 1rem .6rem;}
.inc-title h1{font-family:'Nunito',sans-serif!important;font-size:2.4rem;font-weight:900;background:linear-gradient(135deg,#16a34a,#ca8a04);-webkit-background-clip:text;-webkit-text-fill-color:transparent;margin:0;}
.inc-title p{color:var(--muted);font-size:.9rem;margin-top:.3rem;font-family:'Nunito',sans-serif;}

.inc-rules-card{background:#fefce8;border:2px solid #fde68a;border-radius:20px;padding:1.4rem 1.6rem;margin:1rem 0;box-shadow:0 4px 16px rgba(202,138,4,.10);}
.inc-rules-card h3{font-family:'Nunito',sans-serif!important;font-size:1rem!important;color:#92400e!important;margin:0 0 .8rem;letter-spacing:.01em;}
.inc-rule-row{display:flex;align-items:flex-start;gap:12px;padding:.55rem 0;border-bottom:1px solid #fde68a;font-size:.92rem;}
.inc-rule-row:last-child{border-bottom:none;}
.inc-rule-emoji{font-size:1.7rem;flex-shrink:0;line-height:1;}
.inc-rule-b{display:block;font-weight:700;font-size:.95rem;color:#1e293b;margin-bottom:1px;font-family:'Nunito',sans-serif;}
.inc-rule-s{font-size:.83rem;color:#64748b;font-family:'Nunito',sans-serif;}

.inc-stat-row{display:flex;justify-content:center;gap:14px;flex-wrap:wrap;margin:.6rem 0 1rem;}
.inc-stat{background:#fefce8;border:2px solid #fde68a;border-radius:12px;padding:.5rem 1.1rem;font-family:'Nunito',sans-serif;font-size:.95rem;font-weight:700;color:#92400e;}

.seq-row{display:flex;gap:12px;justify-content:center;align-items:center;margin:1rem 0;}
.seq-slot{width:68px;height:68px;border-radius:14px;display:flex;align-items:center;justify-content:center;font-size:2.2rem;border:3px dashed #cbd5e1;background:#f8fafc;box-shadow:0 2px 6px rgba(0,0,0,.06);flex-shrink:0;}
.seq-slot.filled{border:3px solid #fde68a;background:#fefce8;}
.seq-slot.next{border-color:#2563eb;background:#eff6ff;}

.inc-row{background:#fff;border:2px solid #fde68a;border-radius:14px;padding:10px 14px;margin:7px 0;display:flex;align-items:center;gap:10px;box-shadow:0 2px 8px rgba(202,138,4,.08);}
.inc-row-num{font-family:'Nunito',sans-serif;font-size:.85rem;font-weight:800;color:#92400e;width:26px;text-align:center;flex-shrink:0;}
.inc-emojis{display:flex;gap:4px;font-size:1.7rem;flex:1;}
.inc-feedback{display:flex;gap:6px;align-items:center;flex-shrink:0;}
.pin-chip{background:#1e293b;border:1px solid #334155;border-radius:8px;padding:.25rem .65rem;font-size:.82rem;font-weight:700;color:#ffffff;display:flex;align-items:center;gap:5px;white-space:nowrap;font-family:'Nunito',sans-serif;}
.pin-empty-chip{background:#e2e8f0;border:1px dashed #94a3b8;border-radius:8px;padding:.25rem .65rem;font-size:.82rem;font-weight:700;color:#64748b;display:flex;align-items:center;gap:5px;white-space:nowrap;font-family:'Nunito',sans-serif;}
/* pinos pretos visuais no histórico */
.pin-row{display:flex;gap:5px;align-items:center;flex-wrap:wrap;}
.pin-black{width:18px;height:18px;border-radius:50%;background:#1e293b;border:1px solid #334155;flex-shrink:0;}
.pin-grey{width:18px;height:18px;border-radius:50%;background:#e2e8f0;border:1px dashed #94a3b8;flex-shrink:0;}

.inc-banner-win{background:linear-gradient(135deg,#f0fdf4,#dcfce7);border:2px solid #86efac;border-radius:20px;padding:1.6rem;text-align:center;margin:1rem 0;box-shadow:0 4px 20px rgba(22,163,74,.15);}
.inc-banner-win h2{font-family:'Nunito',sans-serif!important;font-size:1.8rem!important;color:#166534!important;margin:.4rem 0 0;}
.inc-banner-win p{font-family:'Nunito',sans-serif;font-size:1rem;color:#166534;margin:.4rem 0 0;}
.inc-banner-lose{background:linear-gradient(135deg,#fff7ed,#ffedd5);border:2px solid #fdba74;border-radius:20px;padding:1.6rem;text-align:center;margin:1rem 0;box-shadow:0 4px 20px rgba(234,88,12,.12);}
.inc-banner-lose h2{font-family:'Nunito',sans-serif!important;font-size:1.8rem!important;color:#c2410c!important;margin:.4rem 0 0;}
.inc-banner-lose p{font-family:'Nunito',sans-serif;font-size:1rem;color:#c2410c;margin:.4rem 0 0;}

.inc-secret{background:#fefce8;border:2px solid #fcd34d;border-radius:16px;padding:1rem 1.4rem;text-align:center;margin:.8rem 0;}
.inc-secret-label{font-family:'Nunito',sans-serif;font-size:.82rem;font-weight:700;color:#92400e;letter-spacing:.05em;margin-bottom:.5rem;}
.inc-secret-emojis{font-size:2.8rem;letter-spacing:6px;}
</style>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# PALETAS
# ══════════════════════════════════════════════════════════════════════════════
ALL_COLORS = {
    "🔴 Vermelho": ("#e74c3c", "Vermelho"),
    "🔵 Azul":     ("#3498db", "Azul"),
    "🟢 Verde":    ("#2ecc71", "Verde"),
    "🟡 Amarelo":  ("#f1c40f", "Amarelo"),
    "🟠 Laranja":  ("#e67e22", "Laranja"),
    "🟣 Roxo":     ("#9b59b6", "Roxo"),
    "⚪ Branco":   ("#ecf0f1", "Branco"),
    "🩷 Rosa":     ("#ff6b9d", "Rosa"),
}
COLOR_KEYS = list(ALL_COLORS.keys())

ANIMALS  = ["⬛", "🟨"]
INC_LEN  = 4
INC_MAX  = 10

# ══════════════════════════════════════════════════════════════════════════════
# HELPERS – jogo principal
# ══════════════════════════════════════════════════════════════════════════════
def color_hex(k): return ALL_COLORS[k][0]

def render_code_pegs(lst):
    h = '<div class="peg-row">'
    for k in lst:
        h += (f'<div class="peg" style="background:{color_hex(k)};'
              f'box-shadow:0 3px 8px {color_hex(k)}66,inset 0 2px 4px rgba(255,255,255,.4);"></div>')
    return h + '</div>'

def render_feedback(blacks, whites, n, use_white):
    h = '<div class="fb-grid">'
    for _ in range(blacks):  h += '<div class="peg-sm peg-sm-black"></div>'
    if use_white:
        for _ in range(whites): h += '<div class="peg-sm peg-sm-white"></div>'
    for _ in range(n - blacks - (whites if use_white else 0)):
        h += '<div class="peg-sm peg-sm-empty"></div>'
    return h + '</div>'

def evaluate_guess(secret, guess):
    blacks = sum(s == g for s, g in zip(secret, guess))
    sr = [s for s, g in zip(secret, guess) if s != g]
    gr = [g for s, g in zip(secret, guess) if s != g]
    whites = 0
    for g in gr:
        if g in sr:
            whites += 1
            sr.remove(g)
    return blacks, whites

def init_game():
    c = st.session_state
    pool = COLOR_KEYS[:c.num_colors]
    c.secret    = ([random.choice(pool) for _ in range(c.code_len)]
                   if c.allow_repeats else random.sample(pool, c.code_len))
    c.history   = []
    c.game_over = False
    c.won       = False
    c.current   = [COLOR_KEYS[0]] * c.code_len
    c.game_cur     = [None] * c.code_len
    c.game_sel_pos = 0

# ══════════════════════════════════════════════════════════════════════════════
# HELPERS – modo inclusivo
# ══════════════════════════════════════════════════════════════════════════════
def init_inclusive():
    st.session_state.inc_secret  = [random.choice(ANIMALS) for _ in range(INC_LEN)]
    st.session_state.inc_history = []
    st.session_state.inc_over    = False
    st.session_state.inc_won     = False
    st.session_state.inc_current = []

def evaluate_inclusive(secret, guess):
    bulls = sum(s == g for s, g in zip(secret, guess))
    sr = [s for s, g in zip(secret, guess) if s != g]
    gr = [g for s, g in zip(secret, guess) if s != g]
    cows = 0
    for g in gr:
        if g in sr:
            cows += 1
            sr.remove(g)
    return bulls, cows

# ══════════════════════════════════════════════════════════════════════════════
# QUIZ – questões dinâmicas
# ══════════════════════════════════════════════════════════════════════════════
def build_questions(n_colors, code_len, allow_repeats):
    n, k = n_colors, code_len
    total = n**k if allow_repeats else math.perm(n, k)
    formula_total = f"{n}^{k} = {total}" if allow_repeats else f"P({n},{k}) = {total}"

    questions = [
        {
            "num": 1,
            "text": (f"Com {n} cores e código de {k} posições "
                     f"({'com' if allow_repeats else 'sem'} repetição), "
                     f"quantos códigos diferentes existem?"),
            "formula": formula_total,
            "options": sorted({total, total * 2, max(1, total // 2), total + n * k})[:4],
            "answer": total,
            "hint": "Com repetição use n^k; sem repetição use P(n,k) = n!/(n-k)!",
            "explain": (f"Com repetição: {n}^{k} = {total}." if allow_repeats
                        else f"Sem repetição: P({n},{k}) = {n}!/{n-k}! = {total}."),
        },
        {
            "num": 2,
            "text": f"Qual a probabilidade de acertar o código de {k} posições na primeira tentativa?",
            "formula": f"P = 1 / {total}",
            "options": [f"1/{total}", f"1/{n}", f"1/{k}", f"1/{n * k}"],
            "answer": f"1/{total}",
            "hint": "Probabilidade = casos favoráveis / total de casos.",
            "explain": f"Apenas 1 código correto entre {total} → P = 1/{total} ≈ {1/total:.5f}",
        },
        {
            "num": 3,
            "text": (f"O feedback indica pinos pretos de 0 a {k}. "
                     f"Quantos valores distintos de pinos pretos existem?"),
            "formula": f"0, 1, 2, … , {k}  →  {k + 1} valores",
            "options": [str(k + 1), str(k), str(k - 1), str(k + 2)],
            "answer": str(k + 1),
            "hint": "Conte de 0 até k, inclusive os dois extremos.",
            "explain": f"Os pinos vão de 0 a {k}: são {k}+1 = {k+1} valores distintos.",
        },
        {
            "num": 4,
            "text": (f"Já sabemos que 2 posições estão corretas (2 pinos pretos). "
                     f"Quantas possibilidades restam para as outras {k-2} posições "
                     f"com {n} cores ({'com' if allow_repeats else 'sem'} repetição)?"),
            "formula": (f"{n}^{k-2} = {n**(k-2)}" if allow_repeats
                        else f"P({n-2},{k-2}) = {math.perm(max(0, n-2), max(0, k-2))}"),
            "answer": (n ** (k - 2) if allow_repeats
                       else math.perm(max(0, n - 2), max(0, k - 2))),
            "hint": "Fixe as 2 posições certas e calcule as combinações das restantes.",
            "explain": (f"Com repetição: {n}^{k-2} = {n**(k-2)}." if allow_repeats
                        else f"Sem repetição: P({n-2},{k-2}) = {math.perm(max(0,n-2),max(0,k-2))}."),
            "open": True,
        },
        {
            "num": 5,
            "text": (f"Se cada tentativa elimina metade das possibilidades, "
                     f"quantas tentativas são necessárias a partir de {total}?"),
            "formula": f"t = log₂({total}) = {math.ceil(math.log2(total)) if total > 1 else 1}",
            "answer": math.ceil(math.log2(total)) if total > 1 else 1,
            "hint": "Se cada passo divide por 2, use logaritmo na base 2.",
            "explain": (f"log₂({total}) ≈ {math.log2(total):.2f} → "
                        f"arredondando: {math.ceil(math.log2(total)) if total > 1 else 1} tentativas."),
            "open": True,
        },
    ]
    for q in questions:
        if q.get("options") and not q.get("open"):
            ops = list(dict.fromkeys([str(q["answer"])] + [str(o) for o in q["options"]]))[:4]
            random.shuffle(ops)
            q["options"] = ops
    return questions

# ══════════════════════════════════════════════════════════════════════════════
# SESSION STATE
# ══════════════════════════════════════════════════════════════════════════════
defaults = {
    "screen": "intro",
    "code_len": 4, "num_colors": 6, "max_attempts": 10,
    "use_white_pegs": True, "allow_repeats": True,
    "secret": None, "history": [], "game_over": False, "won": False, "current": None,
    "quiz_idx": 0, "quiz_score": 0, "quiz_answers": {}, "quiz_done": False, "quiz_questions": None,
    "inc_secret": None, "inc_history": [], "inc_over": False, "inc_won": False, "inc_current": [],
    # posição selecionada no jogo principal (entrada por clique)
    "game_sel_pos": 0, "game_cur": None,
}
for _k, _v in defaults.items():
    if _k not in st.session_state:
        st.session_state[_k] = _v

# ══════════════════════════════════════════════════════════════════════════════
# TELA: MENU
# ══════════════════════════════════════════════════════════════════════════════
if st.session_state.screen == "intro":

    st.markdown('<div class="intro-wrapper">', unsafe_allow_html=True)
    st.markdown("""
    <div class="intro-title">
      <h1>MASTERMIND</h1>
      <p>JOGO EDUCATIVO DE LÓGICA E DEDUÇÃO</p>
    </div>
    <div class="menu-grid">
      <div class="menu-card game">
        <div class="menu-icon">🎮</div>
        <div class="menu-label">MODO 1</div>
        <div class="menu-title">Jogar Mastermind</div>
        <div class="menu-desc">Decifre o código secreto de cores usando lógica e dedução.</div>
      </div>
      <div class="menu-card quiz">
        <div class="menu-icon">🧮</div>
        <div class="menu-label">MODO 2</div>
        <div class="menu-title">Quiz de Combinatória</div>
        <div class="menu-desc">Teste permutações, probabilidades e contagem adaptadas ao jogo.</div>
      </div>
      <div class="menu-card inc">
        <div class="menu-icon">⬛🟨</div>
        <div class="menu-label">MODO 3</div>
        <div class="menu-title">Jogo Adaptado</div>
        <div class="menu-desc">Versão simplificada: 2 símbolos, botões grandes e feedback com pinos.</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("🎮 JOGAR", use_container_width=True):
            if st.session_state.secret is None:
                init_game()
            st.session_state.screen = "game"
            st.rerun()
    with c2:
        if st.button("🧮 QUIZ", use_container_width=True):
            st.session_state.quiz_idx = 0; st.session_state.quiz_score = 0
            st.session_state.quiz_answers = {}; st.session_state.quiz_done = False
            st.session_state.quiz_questions = None
            st.session_state.screen = "quiz"; st.rerun()
    with c3:
        if st.button("⬛ JOGO ADAPTADO", use_container_width=True):
            if st.session_state.inc_secret is None:
                init_inclusive()
            st.session_state.screen = "inclusive"; st.rerun()

    st.markdown("""
    <div class="rules-card">
      <h3>📋 SOBRE OS MODOS</h3>
      <div class="rule-item">
        <span class="rule-icon">🎮</span>
        <div>
          <span class="rule-title">Mastermind clássico</span>
          <span class="rule-desc">Código secreto de cores com pinos de feedback. Configurável: número de cores, posições e tentativas.</span>
        </div>
      </div>
      <div class="rule-item">
        <span class="rule-icon">🧮</span>
        <div>
          <span class="rule-title">Quiz de Combinatória</span>
          <span class="rule-desc">Questões de permutação, probabilidade e contagem geradas a partir das configurações do jogo.</span>
        </div>
      </div>
      <div class="rule-item">
        <span class="rule-icon">⬛🟨</span>
        <div>
          <span class="rule-title">Jogo Adaptado</span>
          <span class="rule-desc">Apenas 2 símbolos visuais (⬛ e 🟨), 4 posições fixas, botões grandes e feedback com pinos pretos. Indicado para alunos com transtornos cognitivos ou como introdução ao raciocínio lógico.</span>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# TELA: VACAS E BOIS (MODO INCLUSIVO)
# ══════════════════════════════════════════════════════════════════════════════
elif st.session_state.screen == "inclusive":

    st.markdown('<div class="inc-wrapper">', unsafe_allow_html=True)

    st.markdown("""
    <div class="inc-title">
      <h1>⬛🟨 Jogo Adaptado 🟨⬛</h1>
      <p>Descubra a sequência secreta de símbolos!</p>
    </div>
    """, unsafe_allow_html=True)

    # Regras sempre visíveis em expander acessível
    with st.expander("📖 Ver as regras do jogo", expanded=False):
        st.markdown("""
        <div class="inc-rules-card">
          <h3>📖 Como jogar</h3>
          <div class="inc-rule-row">
            <span class="inc-rule-emoji">⬛</span>
            <div>
              <span class="inc-rule-b">Quadrado preto ou quadrado amarelo</span>
              <span class="inc-rule-s">Você vai montar uma sequência de 4 símbolos usando ⬛ e 🟨.</span>
            </div>
          </div>
          <div class="inc-rule-row">
            <span class="inc-rule-emoji">●</span>
            <div>
              <span class="inc-rule-b">Pino preto = símbolo certo, lugar certo!</span>
              <span class="inc-rule-s">Cada pino preto significa que um símbolo está na posição exata.</span>
            </div>
          </div>
          <div class="inc-rule-row">
            <span class="inc-rule-emoji">○</span>
            <div>
              <span class="inc-rule-b">Círculo vazio = ainda não acertou essa posição.</span>
              <span class="inc-rule-s">Continue tentando até ter 4 pinos pretos!</span>
            </div>
          </div>
          <div class="inc-rule-row">
            <span class="inc-rule-emoji">🎯</span>
            <div>
              <span class="inc-rule-b">Objetivo: 4 pinos pretos!</span>
              <span class="inc-rule-s">Quando todos os 4 símbolos estiverem certos, você vence!</span>
            </div>
          </div>
          <div class="inc-rule-row">
            <span class="inc-rule-emoji">⏳</span>
            <div>
              <span class="inc-rule-b">Você tem 10 tentativas.</span>
              <span class="inc-rule-s">Use as dicas de cada tentativa para chegar lá!</span>
            </div>
          </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # Estatísticas
    n_hist      = len(st.session_state.inc_history)
    restantes   = INC_MAX - n_hist
    rest_str    = f"{restantes} restantes" if restantes != 1 else "1 restante"
    st.markdown(f"""
    <div class="inc-stat-row">
      <div class="inc-stat">🎯 Tentativa {n_hist + 1} de {INC_MAX}</div>
      <div class="inc-stat">⏳ {rest_str}</div>
    </div>
    """, unsafe_allow_html=True)

    # Histórico
    if st.session_state.inc_history:
        st.markdown("### 📋 Suas tentativas")
        for i, (guess, bulls, cows) in enumerate(st.session_state.inc_history, 1):
            emojis_html = "".join(
                f'<span style="font-size:1.8rem;line-height:1;">{a}</span>'
                for a in guess
            )
            # Feedback: apenas pinos pretos + vazios
            pins_html = '<div class="pin-row">'
            for _ in range(bulls):
                pins_html += '<div class="pin-black"></div>'
            for _ in range(INC_LEN - bulls):
                pins_html += '<div class="pin-grey"></div>'
            pins_html += '</div>'
            st.markdown(f"""
            <div class="inc-row">
              <span class="inc-row-num">#{i}</span>
              <div class="inc-emojis">{emojis_html}</div>
              <div class="inc-feedback">{pins_html}</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)

    # ── Fim de jogo ───────────────────────────────────────────────────────────
    if st.session_state.inc_over:
        if st.session_state.inc_won:
            tent_str = f"{n_hist} tentativas" if n_hist != 1 else "1 tentativa"
            st.markdown(f"""
            <div class="inc-banner-win">
              <div style="font-size:3rem;">🎉</div>
              <h2>Você acertou!</h2>
              <p>Parabéns! Descobriu em {tent_str}!</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="inc-banner-lose">
              <div style="font-size:3rem;">😊</div>
              <h2>Quase lá!</h2>
              <p>Não foi dessa vez — mas você vai conseguir! Tente de novo!</p>
            </div>
            """, unsafe_allow_html=True)

        secret_str = "  ".join(st.session_state.inc_secret)
        st.markdown(f"""
        <div class="inc-secret">
          <div class="inc-secret-label">🔓 A SEQUÊNCIA SECRETA ERA:</div>
          <div class="inc-secret-emojis">{secret_str}</div>
        </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            if st.button("🔄 Jogar de Novo!", use_container_width=True):
                init_inclusive(); st.rerun()
        with col2:
            if st.button("🏠 Menu", use_container_width=True):
                st.session_state.screen = "intro"; st.rerun()

    # ── Interface de jogo ─────────────────────────────────────────────────────
    else:
        cur = st.session_state.inc_current

        st.markdown("### 👇 Monte sua sequência")

        # Slots visuais das 4 posições
        slots_html = '<div class="seq-row">'
        for i in range(INC_LEN):
            if i < len(cur):
                slots_html += f'<div class="seq-slot filled">{cur[i]}</div>'
            elif i == len(cur):
                slots_html += '<div class="seq-slot next">❓</div>'
            else:
                slots_html += '<div class="seq-slot">　</div>'
        slots_html += '</div>'
        st.markdown(slots_html, unsafe_allow_html=True)

        # Botões de escolha
        if len(cur) < INC_LEN:
            st.markdown(
                f"<p style='text-align:center;font-family:Nunito,sans-serif;"
                f"font-size:1rem;color:#64748b;margin:.4rem 0 .8rem;'>"
                f"Escolha o símbolo para a <b>posição {len(cur)+1}</b>:</p>",
                unsafe_allow_html=True,
            )
            col_a, col_b = st.columns(2)
            with col_a:
                if st.button("⬛  Preto", use_container_width=True):
                    st.session_state.inc_current.append("⬛"); st.rerun()
            with col_b:
                if st.button("🟨  Amarelo", use_container_width=True):
                    st.session_state.inc_current.append("🟨"); st.rerun()

        # Confirmar / apagar
        if len(cur) > 0:
            st.markdown("<br>", unsafe_allow_html=True)
            if len(cur) == INC_LEN:
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("✅ CONFIRMAR", use_container_width=True):
                        bulls, cows = evaluate_inclusive(st.session_state.inc_secret, cur)
                        st.session_state.inc_history.append((cur[:], bulls, cows))
                        if bulls == INC_LEN:
                            st.session_state.inc_over = True
                            st.session_state.inc_won  = True
                        elif len(st.session_state.inc_history) >= INC_MAX:
                            st.session_state.inc_over = True
                            st.session_state.inc_won  = False
                        st.session_state.inc_current = []
                        st.rerun()
                with col2:
                    if st.button("🔙 Apagar último", use_container_width=True):
                        st.session_state.inc_current.pop(); st.rerun()
            else:
                if st.button("🔙 Apagar último", use_container_width=True):
                    st.session_state.inc_current.pop(); st.rerun()

        st.markdown("<br>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🔄 Novo Jogo", use_container_width=True):
                init_inclusive(); st.rerun()
        with col2:
            if st.button("🏠 Menu", use_container_width=True):
                st.session_state.screen = "intro"; st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# TELA: QUIZ
# ══════════════════════════════════════════════════════════════════════════════
elif st.session_state.screen == "quiz":

    if st.session_state.quiz_questions is None:
        st.session_state.quiz_questions = build_questions(
            st.session_state.num_colors,
            st.session_state.code_len,
            st.session_state.allow_repeats,
        )

    questions = st.session_state.quiz_questions
    total_q   = len(questions)

    st.markdown(f"""
    <div class="quiz-header">
      <h2>🧮 Quiz de Combinatória</h2>
      <p>Questões baseadas nas configurações do jogo:
         <b>{st.session_state.num_colors} cores · {st.session_state.code_len} posições ·
         {'com' if st.session_state.allow_repeats else 'sem'} repetição</b></p>
    </div>
    """, unsafe_allow_html=True)

    answered = len(st.session_state.quiz_answers)
    pct = int(answered / total_q * 100)
    st.markdown(f"""
    <div style="margin-bottom:1rem;">
      <div style="display:flex;justify-content:space-between;font-size:.78rem;color:var(--muted);margin-bottom:4px;">
        <span>Progresso</span><span>{answered}/{total_q} respondidas</span>
      </div>
      <div class="progress-bar-outer">
        <div class="progress-bar-inner" style="width:{pct}%;"></div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    if st.session_state.quiz_done:
        score     = st.session_state.quiz_score
        pct_score = int(score / total_q * 100)
        if pct_score == 100:
            msg, emo = "Perfeito! Domínio total! 🏆", "🏆"
        elif pct_score >= 60:
            msg, emo = "Muito bem! Boas bases. 👏", "👏"
        else:
            msg, emo = "Continue praticando! 💪", "💪"

        st.markdown(f"""
        <div class="score-box">
          <div style="font-size:2rem;">{emo}</div>
          <div class="score-big">{score}/{total_q}</div>
          <div class="score-label">PONTUAÇÃO FINAL · {pct_score}%</div>
          <div style="margin-top:.6rem;font-size:.88rem;color:var(--text);">{msg}</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("### 📖 Revisão")
        for q in questions:
            user_ans = str(st.session_state.quiz_answers.get(q["num"], "—"))
            correct  = str(q["answer"])
            ok  = user_ans == correct
            cls = "answer-correct" if ok else "answer-wrong"
            mark = "✅" if ok else "❌"
            corr = "Correto!" if ok else f"Resposta: <b>{correct}</b>"
            st.markdown(f"""
            <div class="q-card">
              <div class="q-number">QUESTÃO {q['num']}</div>
              <div class="q-text">{q['text']}</div>
              <div class="q-formula">{q['formula']}</div>
              <div class="{cls}">{mark} Sua resposta: <b>{user_ans}</b> · {corr}</div>
              <div class="q-hint">💡 {q['explain']}</div>
            </div>
            """, unsafe_allow_html=True)

        c1, c2 = st.columns(2)
        with c1:
            if st.button("🔄 Refazer Quiz", use_container_width=True):
                st.session_state.quiz_idx = 0; st.session_state.quiz_score = 0
                st.session_state.quiz_answers = {}; st.session_state.quiz_done = False
                st.session_state.quiz_questions = None; st.rerun()
        with c2:
            if st.button("🏠 Menu", use_container_width=True):
                st.session_state.screen = "intro"; st.rerun()

    else:
        idx = st.session_state.quiz_idx
        if idx >= total_q:
            st.session_state.quiz_done = True; st.rerun()

        q = questions[idx]
        st.markdown(f"""
        <div class="q-card">
          <div class="q-number">QUESTÃO {q['num']} DE {total_q}</div>
          <div class="q-text">{q['text']}</div>
          <div class="q-formula">{q['formula']}</div>
        </div>
        """, unsafe_allow_html=True)

        already = q["num"] in st.session_state.quiz_answers
        if already:
            user_ans = str(st.session_state.quiz_answers[q["num"]])
            correct  = str(q["answer"])
            ok  = user_ans == correct
            cls = "answer-correct" if ok else "answer-wrong"
            mark = "✅ Correto!" if ok else f"❌ Errado! Resposta: <b>{correct}</b>"
            st.markdown(f'<div class="{cls}">{mark}</div><div class="q-hint">💡 {q["explain"]}</div>',
                        unsafe_allow_html=True)
            c1, c2 = st.columns([3, 1])
            with c1:
                lbl = "➡️ PRÓXIMA" if idx < total_q - 1 else "✅ VER RESULTADO"
                if st.button(lbl, use_container_width=True):
                    st.session_state.quiz_idx += 1
                    if st.session_state.quiz_idx >= total_q:
                        st.session_state.quiz_done = True
                    st.rerun()
            with c2:
                if st.button("🏠 Menu", use_container_width=True):
                    st.session_state.screen = "intro"; st.rerun()
        else:
            st.markdown(f'<div class="q-hint">💡 Dica: {q["hint"]}</div>', unsafe_allow_html=True)
            if q.get("open"):
                user_input = st.text_input("Sua resposta (número inteiro):", key=f"open_{q['num']}")
                if st.button("✅ CONFIRMAR", use_container_width=True):
                    if user_input.strip():
                        try:
                            val = int(user_input.strip())
                            st.session_state.quiz_answers[q["num"]] = val
                            if val == int(q["answer"]):
                                st.session_state.quiz_score += 1
                            st.rerun()
                        except ValueError:
                            st.warning("Digite apenas um número inteiro.")
            else:
                choice = st.radio("Escolha a resposta:", q["options"], key=f"radio_{q['num']}")
                if st.button("✅ CONFIRMAR", use_container_width=True):
                    st.session_state.quiz_answers[q["num"]] = choice
                    if str(choice) == str(q["answer"]):
                        st.session_state.quiz_score += 1
                    st.rerun()
            if st.button("🏠 Menu", use_container_width=True, key="menu_mid"):
                st.session_state.screen = "intro"; st.rerun()

# ══════════════════════════════════════════════════════════════════════════════
# TELA: JOGO PRINCIPAL
# ══════════════════════════════════════════════════════════════════════════════
else:

    with st.sidebar:
        st.markdown("## ⚙️ Configurações")
        st.markdown("---")
        new_cl  = st.slider("🔢 Tamanho do código", 3, 6,  st.session_state.code_len,     key="sl_cl")
        new_nc  = st.slider("🎨 Número de cores",   4, 8,  st.session_state.num_colors,   key="sl_nc")
        new_ma  = st.slider("⏳ Tentativas",         6, 15, st.session_state.max_attempts, key="sl_ma")
        new_wp  = st.toggle("⚪ Pinos brancos",      st.session_state.use_white_pegs,      key="tog_wp")
        new_rep = st.toggle("🔁 Cores repetidas",    st.session_state.allow_repeats,       key="tog_rep")

        st.markdown("---")
        st.markdown("**Cores disponíveis:**")
        avail  = COLOR_KEYS[:new_nc]
        cols_c = st.columns(4)
        for i, ck in enumerate(avail):
            with cols_c[i % 4]:
                st.markdown(
                    f'<div style="width:24px;height:24px;border-radius:50%;'
                    f'background:{color_hex(ck)};margin:2px auto;'
                    f'box-shadow:0 2px 6px {color_hex(ck)}88;"></div>',
                    unsafe_allow_html=True)

        st.markdown("---")
        if st.button("🚀 NOVO JOGO", use_container_width=True):
            st.session_state.code_len       = new_cl
            st.session_state.num_colors     = new_nc
            st.session_state.max_attempts   = new_ma
            st.session_state.use_white_pegs = new_wp
            st.session_state.allow_repeats  = new_rep
            init_game(); st.rerun()

        st.markdown("---")
        if st.button("🧮 Quiz",         use_container_width=True):
            st.session_state.quiz_idx = 0; st.session_state.quiz_score = 0
            st.session_state.quiz_answers = {}; st.session_state.quiz_done = False
            st.session_state.quiz_questions = None
            st.session_state.screen = "quiz"; st.rerun()
        if st.button("⬛ Jogo Adaptado", use_container_width=True):
            if st.session_state.inc_secret is None:
                init_inclusive()
            st.session_state.screen = "inclusive"; st.rerun()
        if st.button("🏠 Menu",         use_container_width=True):
            st.session_state.screen = "intro"; st.rerun()

        st.markdown("---")
        wp_hint = "⚪ <b>Pino branco</b> = cor certa, posição errada<br>" if st.session_state.use_white_pegs else ""
        st.markdown(f"""
<div class="info-box">
⚫ <b>Pino preto</b> = cor certa, posição certa<br>
{wp_hint}
Descubra em até <b>{st.session_state.max_attempts}</b> tentativas!
</div>
""", unsafe_allow_html=True)

    st.markdown("""
    <div class="title-block">
      <h1>MASTERMIND</h1>
      <p>JOGO EDUCATIVO DE LÓGICA E DEDUÇÃO</p>
    </div>
    """, unsafe_allow_html=True)

    al = st.session_state.max_attempts - len(st.session_state.history)
    st.markdown(f"""
    <div class="stat-grid">
      <div class="stat-card"><div class="stat-val">{len(st.session_state.history)}</div><div class="stat-lbl">TENTATIVAS</div></div>
      <div class="stat-card"><div class="stat-val">{al}</div><div class="stat-lbl">RESTANTES</div></div>
      <div class="stat-card"><div class="stat-val">{st.session_state.code_len}</div><div class="stat-lbl">POSIÇÕES</div></div>
      <div class="stat-card"><div class="stat-val">{st.session_state.num_colors}</div><div class="stat-lbl">CORES</div></div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    if st.session_state.history:
        st.markdown("### 📋 Tentativas anteriores")
        for i, (guess, blacks, whites) in enumerate(st.session_state.history, 1):
            w_str = f"⚪{whites}" if st.session_state.use_white_pegs else ""
            st.markdown(f"""
            <div class="row-card">
              <span class="row-num">#{i}</span>
              {render_code_pegs(guess)}
              <div class="separator"></div>
              {render_feedback(blacks, whites, st.session_state.code_len, st.session_state.use_white_pegs)}
              <span style="font-size:.75rem;color:var(--muted);min-width:60px;">⚫{blacks} {w_str}</span>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("---")

    if st.session_state.game_over:
        if st.session_state.won:
            st.markdown(f'<div class="banner-win">🏆 PARABÉNS! Código decifrado em {len(st.session_state.history)} tentativa(s)!</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="banner-lose">💀 GAME OVER — Todas as tentativas usadas!</div>', unsafe_allow_html=True)

        st.markdown('<div class="secret-reveal"><div class="secret-label">🔓 CÓDIGO SECRETO</div>', unsafe_allow_html=True)
        st.markdown(render_code_pegs(st.session_state.secret), unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        c1, c2, c3 = st.columns(3)
        with c1:
            if st.button("🔄 Jogar Novamente", use_container_width=True):
                init_game(); st.rerun()
        with c2:
            if st.button("🧮 Fazer Quiz", use_container_width=True):
                st.session_state.quiz_idx = 0; st.session_state.quiz_score = 0
                st.session_state.quiz_answers = {}; st.session_state.quiz_done = False
                st.session_state.quiz_questions = None
                st.session_state.screen = "quiz"; st.rerun()
        with c3:
            if st.button("⬛ Jogo Adaptado", use_container_width=True):
                if st.session_state.inc_secret is None:
                    init_inclusive()
                st.session_state.screen = "inclusive"; st.rerun()
    else:
        n_attempt = len(st.session_state.history) + 1
        st.markdown(f"### 🎯 Tentativa #{n_attempt}")

        pool = COLOR_KEYS[:st.session_state.num_colors]

        # Inicializa o estado de entrada por clique
        if st.session_state.game_cur is None or len(st.session_state.game_cur) != st.session_state.code_len:
            st.session_state.game_cur     = [None] * st.session_state.code_len
            st.session_state.game_sel_pos = 0

        cur      = st.session_state.game_cur
        sel_pos  = st.session_state.game_sel_pos

        # ── Slots da sequência atual ──────────────────────────────────────────
        slots_html = '<div class="slot-row">'
        for i in range(st.session_state.code_len):
            if cur[i] is not None:
                hex_c = color_hex(cur[i])
                slots_html += (
                    f'<div class="game-slot filled" style="background:{hex_c};'
                    f'border-color:rgba(0,0,0,.15);'
                    f'box-shadow:0 3px 8px {hex_c}88,inset 0 2px 4px rgba(255,255,255,.3);">'
                    f'</div>'
                )
            elif i == sel_pos:
                slots_html += '<div class="game-slot next">❓</div>'
            else:
                slots_html += '<div class="game-slot"></div>'
        slots_html += '</div>'
        st.markdown(slots_html, unsafe_allow_html=True)

        # Instrução
        if sel_pos < st.session_state.code_len:
            st.markdown(
                f"<p style='text-align:center;font-size:.9rem;color:#64748b;margin:.2rem 0 .6rem;'>"
                f"Escolha a cor para a <b>posição {sel_pos + 1}</b>:</p>",
                unsafe_allow_html=True,
            )

        # ── Paleta de cores ───────────────────────────────────────────────────
        color_cols = st.columns(len(pool))
        for i, ck in enumerate(pool):
            with color_cols[i]:
                hex_c = color_hex(ck)
                # Botão invisível sobre o círculo colorido
                if st.button(" ", key=f"cpick_{i}", use_container_width=True,
                             help=ck.split()[-1],
                             disabled=(sel_pos >= st.session_state.code_len)):
                    st.session_state.game_cur[sel_pos] = ck
                    st.session_state.game_sel_pos = min(
                        st.session_state.code_len,
                        sel_pos + 1
                    )
                    st.rerun()
                # Círculo colorido decorativo abaixo do botão
                st.markdown(
                    f'<div style="width:44px;height:44px;border-radius:50%;'
                    f'background:{hex_c};margin:-12px auto 4px;pointer-events:none;'
                    f'box-shadow:0 3px 8px {hex_c}88,inset 0 2px 4px rgba(255,255,255,.3);'
                    f'border:2px solid rgba(0,0,0,.08);"></div>',
                    unsafe_allow_html=True,
                )

        st.markdown("<br>", unsafe_allow_html=True)

        # ── Controles ─────────────────────────────────────────────────────────
        ready = all(x is not None for x in cur)
        repeat_conflict = (not st.session_state.allow_repeats) and (len(set(cur)) < len(cur))
        if repeat_conflict:
            st.warning("⚠️ Repetição de cores não permitida! Apague e escolha cores diferentes.")

        c1, c2, c3 = st.columns([3, 1, 1])
        with c1:
            if st.button("✅ CONFIRMAR TENTATIVA", use_container_width=True,
                         disabled=(not ready or repeat_conflict)):
                blacks, whites = evaluate_guess(st.session_state.secret, cur)
                st.session_state.history.append((cur[:], blacks, whites))
                if blacks == st.session_state.code_len:
                    st.session_state.game_over = True; st.session_state.won = True
                elif len(st.session_state.history) >= st.session_state.max_attempts:
                    st.session_state.game_over = True; st.session_state.won = False
                st.session_state.game_cur     = [None] * st.session_state.code_len
                st.session_state.game_sel_pos = 0
                st.rerun()
        with c2:
            if st.button("⬅️ Apagar", use_container_width=True):
                new_pos = max(0, sel_pos - 1)
                st.session_state.game_cur[new_pos] = None
                st.session_state.game_sel_pos = new_pos
                st.rerun()
        with c3:
            if st.button("🗑️ Limpar", use_container_width=True):
                st.session_state.game_cur     = [None] * st.session_state.code_len
                st.session_state.game_sel_pos = 0
                st.rerun()

        white_info = "| ⚪ <b>Pino branco</b>: cor certa MAS posição errada" if st.session_state.use_white_pegs else "| modo sem pinos brancos ativo"
        st.markdown(f"""
        <div class="info-box">
        ⚫ <b>Pino preto</b>: cor certa NA posição certa &nbsp;{white_info}
        </div>
        """, unsafe_allow_html=True)
