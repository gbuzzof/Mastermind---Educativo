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
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=DM+Sans:wght@400;500;600&display=swap');

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
html,body,[data-testid="stAppViewContainer"]{background-color:var(--bg)!important;color:var(--text);font-family:'DM Sans',sans-serif;}
[data-testid="stSidebar"]{background:linear-gradient(180deg,#fff 0%,#f1f5fb 100%)!important;border-right:1px solid var(--border);}
[data-testid="stSidebar"] *{color:var(--text)!important;}
h1,h2,h3{font-family:'Orbitron',monospace!important;}

/* ── Intro / Menu ── */
.intro-wrapper{max-width:640px;margin:0 auto;padding:2rem 0 3rem;}
.intro-title{text-align:center;margin-bottom:1.2rem;}
.intro-title h1{font-size:3rem;font-weight:900;background:linear-gradient(135deg,var(--accent),var(--accent2));-webkit-background-clip:text;-webkit-text-fill-color:transparent;letter-spacing:.1em;margin:0;}
.intro-title p{color:var(--muted);font-size:.85rem;letter-spacing:.1em;margin-top:.3rem;font-family:'Orbitron',monospace;}

.menu-grid{display:grid;grid-template-columns:1fr 1fr 1fr;gap:16px;margin:2rem 0;}
.menu-card{background:var(--panel);border:2px solid var(--border);border-radius:16px;padding:1.6rem 1.2rem;text-align:center;cursor:pointer;transition:all .2s;box-shadow:0 4px 16px var(--shadow);}
.menu-card:hover{transform:translateY(-3px);box-shadow:0 8px 28px rgba(37,99,235,.15);}
.menu-card.game{border-color:#bfdbfe;}
.menu-card.quiz{border-color:#ddd6fe;}
.menu-card.tree{border-color:#fed7aa;}
.menu-icon{font-size:2.4rem;margin-bottom:.6rem;}
.menu-label{font-family:'Orbitron',monospace;font-size:.72rem;font-weight:700;letter-spacing:.08em;color:var(--muted);}
.menu-title{font-size:1rem;font-weight:600;color:var(--text);margin:.3rem 0;}
.menu-desc{font-size:.78rem;color:var(--muted);line-height:1.5;}

/* ── Rules / generic cards ── */
.rules-card{background:var(--panel);border:1px solid var(--border);border-radius:16px;padding:1.8rem 2rem;margin:1.4rem 0;box-shadow:0 4px 20px var(--shadow);}
.rules-card h3{font-size:.85rem!important;color:var(--accent)!important;letter-spacing:.12em;margin-bottom:1rem;margin-top:0;}
.rule-item{display:flex;align-items:flex-start;gap:14px;padding:.75rem 0;border-bottom:1px solid var(--border);font-size:.92rem;line-height:1.55;}
.rule-item:last-child{border-bottom:none;}
.rule-icon{font-size:1.3rem;flex-shrink:0;margin-top:1px;}
.rule-title{font-weight:600;display:block;margin-bottom:2px;}
.rule-desc{color:var(--muted);font-size:.84rem;}
.peg-demo{display:flex;gap:8px;align-items:center;margin:.8rem 0 .4rem;}
.peg-demo-circle{width:32px;height:32px;border-radius:50%;border:2px solid rgba(0,0,0,.08);box-shadow:0 2px 6px rgba(0,0,0,.15),inset 0 1px 3px rgba(255,255,255,.5);flex-shrink:0;}
.feedback-demo{display:flex;gap:6px;align-items:center;margin:.6rem 0;}
.fd-black{width:16px;height:16px;border-radius:50%;background:#1e293b;border:1px solid #334155;flex-shrink:0;}
.fd-white{width:16px;height:16px;border-radius:50%;background:#f1f5f9;border:1px solid #94a3b8;flex-shrink:0;}
.fd-empty{width:16px;height:16px;border-radius:50%;background:#e2e8f0;border:1px dashed #cbd5e1;flex-shrink:0;}

/* ── Game ── */
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
.progress-bar-inner{background:linear-gradient(90deg,var(--accent),var(--accent2));border-radius:99px;height:8px;transition:width .4s;}

/* ── Tree ── */
.tree-header{background:linear-gradient(135deg,#fff7ed,#ffedd5);border:1px solid #fdba74;border-radius:16px;padding:1.4rem 1.8rem;margin-bottom:1.4rem;}
.tree-header h2{font-size:1.1rem!important;color:#c2410c!important;margin:0 0 .3rem;}
.tree-header p{color:#9a3412;font-size:.84rem;margin:0;}
.tree-card{background:var(--panel);border:1px solid var(--border);border-radius:14px;padding:1.4rem 1.6rem;margin:.8rem 0;box-shadow:0 3px 12px var(--shadow);}
.tree-node{display:inline-block;background:var(--accent);color:#fff;border-radius:8px;padding:.4rem .9rem;font-family:'Orbitron',monospace;font-size:.72rem;font-weight:700;letter-spacing:.05em;}
.tree-node.green{background:var(--success);}
.tree-node.orange{background:var(--accent2);}
.tree-node.purple{background:var(--purple);}
.tree-node.red{background:var(--danger);}
.tree-branch{color:var(--muted);font-size:.8rem;margin:.2rem 0 .2rem 1rem;}
.tree-formula-box{background:#f8fafc;border:1px solid var(--border);border-left:3px solid var(--accent2);border-radius:8px;padding:.8rem 1.1rem;font-size:.85rem;color:var(--text);margin:.8rem 0;line-height:1.7;}
</style>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# PALETA DE CORES
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

def color_hex(k): return ALL_COLORS[k][0]

# ══════════════════════════════════════════════════════════════════════════════
# HELPERS JOGO
# ══════════════════════════════════════════════════════════════════════════════
def render_code_pegs(lst):
    h = '<div class="peg-row">'
    for k in lst:
        h += (f'<div class="peg" style="background:{color_hex(k)};'
              f'box-shadow:0 3px 8px {color_hex(k)}66,inset 0 2px 4px rgba(255,255,255,.4);"></div>')
    return h + '</div>'

def render_feedback(blacks, whites, n, use_white):
    h = '<div class="fb-grid">'
    for _ in range(blacks): h += '<div class="peg-sm peg-sm-black"></div>'
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

# ══════════════════════════════════════════════════════════════════════════════
# BANCO DE QUESTÕES – COMBINATÓRIA
# ══════════════════════════════════════════════════════════════════════════════
def build_questions(n_colors, code_len, allow_repeats):
    """Gera questões dinâmicas baseadas nas configurações atuais do jogo."""
    n, k = n_colors, code_len
    if allow_repeats:
        total = n ** k
        formula_total = f"{n}^{k} = {total}"
    else:
        total = math.perm(n, k)
        formula_total = f"P({n},{k}) = {n}!/{n-k}! = {total}"

    questions = [
        # Q1 – Total de combinações
        {
            "num": 1,
            "text": (f"Com {n} cores disponíveis e um código de {k} posições "
                     f"{'(repetição permitida)' if allow_repeats else '(sem repetição)'}, "
                     f"quantos códigos secretos diferentes são possíveis?"),
            "formula": formula_total,
            "options": sorted({total, total*2, total//2 if total>2 else total+5,
                               total+n*k}, key=lambda x: x)[:4],
            "answer": total,
            "hint": ("Use n^k quando repetição é permitida." if allow_repeats
                     else "Use Permutação: P(n,k) = n!/(n-k)!"),
            "explain": (
                f"Com repetição: cada posição tem {n} opções → {n}^{k} = {total} códigos."
                if allow_repeats else
                f"Sem repetição: 1ª posição tem {n} opções, 2ª tem {n-1}, … → {formula_total}"
            ),
        },
        # Q2 – Probabilidade de acertar na 1ª tentativa
        {
            "num": 2,
            "text": (f"Se você chutasse um código aleatório, qual é a probabilidade "
                     f"de acertar o código secreto de {k} posições na primeira tentativa?"),
            "formula": f"P = 1 / {total}",
            "options": [f"1/{total}", f"1/{n}", f"1/{k}", f"1/{n*k}"],
            "answer": f"1/{total}",
            "hint": "Probabilidade = casos favoráveis / total de casos.",
            "explain": (f"Há apenas 1 código correto entre {total} possíveis, "
                        f"portanto P = 1/{total} ≈ {1/total:.4f}"),
        },
        # Q3 – Feedback: quantos resultados de pinos pretos
        {
            "num": 3,
            "text": (f"O feedback do Mastermind indica pinos pretos (0 a {k}) por tentativa. "
                     f"Quantos valores distintos de pinos pretos são possíveis?"),
            "formula": f"0, 1, 2, … , {k}  →  {k+1} valores",
            "options": [str(k+1), str(k), str(k-1), str(k+2)],
            "answer": str(k+1),
            "hint": "Os pinos pretos vão de 0 (nenhum certo) até k (todos certos).",
            "explain": (f"Os pinos pretos variam de 0 a {k}, "
                        f"portanto há {k}+1 = {k+1} valores distintos."),
        },
        # Q4 – Posições fixas
        {
            "num": 4,
            "text": (f"Se você já sabe que 2 posições estão corretas (2 pinos pretos) "
                     f"em um código de {k} posições com {n} cores "
                     f"{'(com repetição)' if allow_repeats else '(sem repetição)'}, "
                     f"quantas possibilidades restam para as outras posições?"),
            "formula": (f"{n}^{k-2}" if allow_repeats else f"P({n-2},{k-2})"),
            "options": None,  # campo aberto
            "answer": (n**(k-2) if allow_repeats else math.perm(n-2, k-2) if k>=2 else 1),
            "hint": ("Fixadas 2 posições, restam k-2 posições livres com n opções cada."
                     if allow_repeats else
                     "Sem repetição: fixadas 2 cores, restam n-2 cores para k-2 posições."),
            "explain": (
                f"Com 2 posições fixas e repetição: {n}^{k-2} = {n**(k-2)} possibilidades."
                if allow_repeats else
                f"Sem repetição: P({n-2},{k-2}) = {math.perm(n-2,k-2) if k>=2 else 1} possibilidades."
            ),
            "open": True,
        },
        # Q5 – Estratégia e informação
        {
            "num": 5,
            "text": (f"Cada tentativa no Mastermind elimina possibilidades. "
                     f"Se uma tentativa reduz as possibilidades à metade, "
                     f"quantas tentativas são necessárias para chegar a 1 possibilidade "
                     f"a partir de {total}?"),
            "formula": f"2^t ≥ {total}  →  t = ⌈log₂({total})⌉",
            "options": None,
            "answer": math.ceil(math.log2(total)) if total > 1 else 1,
            "hint": "Se cada tentativa divide por 2, use logaritmo na base 2.",
            "explain": (f"log₂({total}) ≈ {math.log2(total):.2f}, "
                        f"arredondando para cima: {math.ceil(math.log2(total))} tentativas."),
            "open": True,
        },
    ]
    # Embaralha opções das questões de múltipla escolha
    for q in questions:
        if q.get("options") and not q.get("open"):
            ops = list(dict.fromkeys([str(q["answer"])] + [str(o) for o in q["options"]]))
            ops = list(dict.fromkeys(ops))[:4]
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
    # quiz
    "quiz_idx": 0, "quiz_score": 0, "quiz_answers": {}, "quiz_done": False,
    "quiz_questions": None,
}
for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v

# ══════════════════════════════════════════════════════════════════════════════
# TELA: MENU INICIAL
# ══════════════════════════════════════════════════════════════════════════════
if st.session_state.screen == "intro":

    st.markdown('<div class="intro-wrapper">', unsafe_allow_html=True)
    st.markdown("""
    <div class="intro-title">
      <h1>MASTERMIND</h1>
      <p>JOGO EDUCATIVO DE LÓGICA E DEDUÇÃO</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="menu-grid">
      <div class="menu-card game">
        <div class="menu-icon">🎮</div>
        <div class="menu-label">MODO 1</div>
        <div class="menu-title">Jogar Mastermind</div>
        <div class="menu-desc">Decifre o código secreto usando lógica e dedução.</div>
      </div>
      <div class="menu-card quiz">
        <div class="menu-icon">🧮</div>
        <div class="menu-label">MODO 2</div>
        <div class="menu-title">Quiz de Combinatória</div>
        <div class="menu-desc">Teste seus conhecimentos sobre permutação e probabilidade.</div>
      </div>
      <div class="menu-card tree">
        <div class="menu-icon">🌳</div>
        <div class="menu-label">MODO 3</div>
        <div class="menu-title">Árvore de Decisão</div>
        <div class="menu-desc">Visualize as ramificações lógicas do jogo como ferramenta matemática.</div>
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
            st.session_state.quiz_idx      = 0
            st.session_state.quiz_score    = 0
            st.session_state.quiz_answers  = {}
            st.session_state.quiz_done     = False
            st.session_state.quiz_questions = None
            st.session_state.screen = "quiz"
            st.rerun()
    with c3:
        if st.button("🌳 ÁRVORE", use_container_width=True):
            st.session_state.screen = "tree"
            st.rerun()

    # Regras resumidas
    st.markdown("""
    <div class="rules-card">
      <h3>📋 COMO JOGAR MASTERMIND</h3>
      <div class="rule-item">
        <span class="rule-icon">🔐</span>
        <div>
          <span class="rule-title">Decifre o código secreto</span>
          <span class="rule-desc">O computador sorteia uma sequência de cores. Você tem tentativas limitadas para descobri-la.</span>
        </div>
      </div>
      <div class="rule-item">
        <span class="rule-icon">⚫</span>
        <div>
          <span class="rule-title">Pino preto = cor certa, posição certa</span>
          <span class="rule-desc">Cada pino preto indica uma cor na posição exata.</span>
        </div>
      </div>
      <div class="rule-item">
        <span class="rule-icon">⚪</span>
        <div>
          <span class="rule-title">Pino branco = cor certa, posição errada</span>
          <span class="rule-desc">A cor existe no código, mas está em outra posição (modo com pinos brancos).</span>
        </div>
      </div>
      <div class="rule-item">
        <span class="rule-icon">🧮</span>
        <div>
          <span class="rule-title">Quiz de Combinatória</span>
          <span class="rule-desc">Questões adaptadas às configurações do jogo: permutações, probabilidades e contagem.</span>
        </div>
      </div>
      <div class="rule-item">
        <span class="rule-icon">🌳</span>
        <div>
          <span class="rule-title">Árvore de Decisão</span>
          <span class="rule-desc">Visualize como cada feedback ramifica o espaço de possibilidades — conceito central em Teoria da Informação.</span>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# TELA: QUIZ DE COMBINATÓRIA
# ══════════════════════════════════════════════════════════════════════════════
elif st.session_state.screen == "quiz":

    # Gera questões se ainda não geradas (usa config atual do jogo)
    if st.session_state.quiz_questions is None:
        st.session_state.quiz_questions = build_questions(
            st.session_state.num_colors,
            st.session_state.code_len,
            st.session_state.allow_repeats,
        )

    questions = st.session_state.quiz_questions
    total_q   = len(questions)

    # Header
    st.markdown(f"""
    <div class="quiz-header">
      <h2>🧮 Quiz de Combinatória</h2>
      <p>Questões baseadas nas configurações do seu jogo:
         <b>{st.session_state.num_colors} cores · {st.session_state.code_len} posições ·
         {'com' if st.session_state.allow_repeats else 'sem'} repetição</b></p>
    </div>
    """, unsafe_allow_html=True)

    # Barra de progresso
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
        score = st.session_state.quiz_score
        pct_score = int(score / total_q * 100)
        if pct_score == 100:
            msg, emoji = "Perfeito! Domínio total da combinatória! 🏆", "🏆"
        elif pct_score >= 60:
            msg, emoji = "Muito bem! Você tem boas bases. 👏", "👏"
        else:
            msg, emoji = "Continue praticando! A matemática recompensa quem persiste. 💪", "💪"

        st.markdown(f"""
        <div class="score-box">
          <div style="font-size:2rem;">{emoji}</div>
          <div class="score-big">{score}/{total_q}</div>
          <div class="score-label">PONTUAÇÃO FINAL · {pct_score}%</div>
          <div style="margin-top:.6rem;font-size:.88rem;color:var(--text);">{msg}</div>
        </div>
        """, unsafe_allow_html=True)

        # Revisão
        st.markdown("### 📖 Revisão das questões")
        for q in questions:
            user_ans = str(st.session_state.quiz_answers.get(q["num"], "—"))
            correct  = str(q["answer"])
            ok = user_ans == correct
            st.markdown(f"""
            <div class="q-card">
              <div class="q-number">QUESTÃO {q['num']}</div>
              <div class="q-text">{q['text']}</div>
              <div class="q-formula">{q['formula']}</div>
              <div class="{'answer-correct' if ok else 'answer-wrong'}">
                {'✅' if ok else '❌'} Sua resposta: <b>{user_ans}</b>
                {'· Correto!' if ok else f'· Resposta correta: <b>{correct}</b>'}
              </div>
              <div class="q-hint">💡 {q['explain']}</div>
            </div>
            """, unsafe_allow_html=True)

        c1, c2 = st.columns(2)
        with c1:
            if st.button("🔄 Refazer Quiz", use_container_width=True):
                st.session_state.quiz_idx      = 0
                st.session_state.quiz_score    = 0
                st.session_state.quiz_answers  = {}
                st.session_state.quiz_done     = False
                st.session_state.quiz_questions = None
                st.rerun()
        with c2:
            if st.button("🏠 Menu", use_container_width=True):
                st.session_state.screen = "intro"
                st.rerun()

    else:
        idx = st.session_state.quiz_idx
        if idx >= total_q:
            st.session_state.quiz_done = True
            st.rerun()

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
            ok = user_ans == correct
            st.markdown(f"""
            <div class="{'answer-correct' if ok else 'answer-wrong'}">
              {'✅ Correto!' if ok else f'❌ Errado! Resposta: <b>{correct}</b>'}
            </div>
            <div class="q-hint">💡 {q['explain']}</div>
            """, unsafe_allow_html=True)

            c1, c2 = st.columns([3,1])
            with c1:
                lbl = "➡️ PRÓXIMA" if idx < total_q - 1 else "✅ VER RESULTADO"
                if st.button(lbl, use_container_width=True):
                    st.session_state.quiz_idx += 1
                    if st.session_state.quiz_idx >= total_q:
                        st.session_state.quiz_done = True
                    st.rerun()
            with c2:
                if st.button("🏠 Menu", use_container_width=True):
                    st.session_state.screen = "intro"
                    st.rerun()
        else:
            with st.container():
                st.markdown(f'<div class="q-hint">💡 Dica: {q["hint"]}</div>', unsafe_allow_html=True)

                if q.get("open"):
                    user_input = st.text_input("Sua resposta (número):", key=f"open_{q['num']}")
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
                st.session_state.screen = "intro"
                st.rerun()

# ══════════════════════════════════════════════════════════════════════════════
# TELA: ÁRVORE DE DECISÃO
# ══════════════════════════════════════════════════════════════════════════════
elif st.session_state.screen == "tree":

    n = st.session_state.num_colors
    k = st.session_state.code_len
    rep = st.session_state.allow_repeats
    total = n**k if rep else math.perm(n, k)

    st.markdown(f"""
    <div class="tree-header">
      <h2>🌳 Árvore de Decisão do Mastermind</h2>
      <p>Configuração atual: <b>{n} cores · {k} posições ·
         {'com' if rep else 'sem'} repetição · {total} códigos possíveis</b></p>
    </div>
    """, unsafe_allow_html=True)

    # ── Conceito ──────────────────────────────────────────────────────────────
    st.markdown("""
    <div class="tree-card">
      <h3 style="font-family:'Orbitron',monospace;font-size:.8rem;color:#c2410c;
                 letter-spacing:.1em;margin:0 0 .8rem;">📐 O QUE É UMA ÁRVORE DE DECISÃO?</h3>
      <p style="font-size:.92rem;line-height:1.65;color:var(--text);">
        Uma <b>Árvore de Decisão</b> é um modelo matemático que representa sequências de escolhas
        e seus resultados. No Mastermind, cada <em>tentativa</em> é um nó da árvore, e cada
        <em>feedback</em> possível é um ramo que leva a um subconjunto menor de possibilidades.
      </p>
      <p style="font-size:.92rem;line-height:1.65;color:var(--text);margin-top:.6rem;">
        Quanto mais informativo o feedback, mais ramos são eliminados — e mais rápido chegamos
        ao código secreto. Isso conecta o jogo à <b>Teoria da Informação</b> de Claude Shannon.
      </p>
    </div>
    """, unsafe_allow_html=True)

    # ── Árvore visual (HTML/CSS) ───────────────────────────────────────────────
    st.markdown("### 🌲 Estrutura da Árvore — Primeiras Tentativas")

    t2 = n**(k-1) if rep else math.perm(n-1, k-1) if k > 1 else 1
    t3_bb = n**(k-2) if rep and k >= 2 else (math.perm(n-2, k-2) if k >= 2 else 1)
    t3_bw = max(1, t2 // 3)
    t3_ww = max(1, t2 // 4)
    t3_00 = max(1, t2 // 5)

    st.markdown(f"""
    <div class="tree-card" style="overflow-x:auto;">
      <div style="font-family:'DM Sans',sans-serif;font-size:.88rem;line-height:2.2;
                  min-width:520px;">

        <!-- Raiz -->
        <div style="text-align:center;margin-bottom:.4rem;">
          <span class="tree-node" style="font-size:.8rem;padding:.5rem 1.2rem;">
            🎯 INÍCIO · {total} possibilidades
          </span>
        </div>
        <div style="text-align:center;color:var(--muted);font-size:1.3rem;">↓</div>
        <div style="text-align:center;margin:.2rem 0 .6rem;">
          <span style="font-size:.8rem;color:var(--muted);">1ª tentativa feita</span>
        </div>

        <!-- Ramos nível 1 -->
        <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin:.6rem 0;">
          <div style="text-align:center;">
            <div style="color:var(--muted);font-size:.72rem;margin-bottom:4px;">⚫⚫… ({k} pretos)</div>
            <span class="tree-node green" style="font-size:.7rem;padding:.35rem .7rem;">✅ ACERTO!</span>
            <div style="color:var(--muted);font-size:.7rem;margin-top:4px;">1 possibilidade</div>
          </div>
          <div style="text-align:center;">
            <div style="color:var(--muted);font-size:.72rem;margin-bottom:4px;">⚫… ({k-1} pretos)</div>
            <span class="tree-node orange" style="font-size:.7rem;padding:.35rem .7rem;">≈ {t2} possíveis</span>
            <div style="color:var(--muted);font-size:.7rem;margin-top:4px;">continua…</div>
          </div>
          <div style="text-align:center;">
            <div style="color:var(--muted);font-size:.72rem;margin-bottom:4px;">⚪⚪ (2 brancos)</div>
            <span class="tree-node purple" style="font-size:.7rem;padding:.35rem .7rem;">≈ {t3_ww*2} possíveis</span>
            <div style="color:var(--muted);font-size:.7rem;margin-top:4px;">continua…</div>
          </div>
          <div style="text-align:center;">
            <div style="color:var(--muted);font-size:.72rem;margin-bottom:4px;">0 pinos</div>
            <span class="tree-node red" style="font-size:.7rem;padding:.35rem .7rem;">≈ {t3_00*3} possíveis</span>
            <div style="color:var(--muted);font-size:.7rem;margin-top:4px;">continua…</div>
          </div>
        </div>

        <div style="text-align:center;color:var(--muted);font-size:1.1rem;margin:.4rem 0;">↓ &nbsp; (2ª tentativa)</div>

        <!-- Ramos nível 2 (sub-ramificação do ramo {k-1} pretos) -->
        <div style="background:#f8fafc;border:1px solid var(--border);border-radius:10px;
                    padding:1rem;margin:.4rem 0;">
          <div style="font-size:.78rem;color:var(--muted);margin-bottom:.6rem;">
            📌 Zoom: sub-ramos após feedback de {k-1} pino(s) preto(s)
          </div>
          <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:8px;">
            <div style="text-align:center;">
              <div style="font-size:.7rem;color:var(--muted);margin-bottom:4px;">⚫⚫…⚫ ({k} pretos)</div>
              <span class="tree-node green" style="font-size:.68rem;padding:.3rem .6rem;">✅ ACERTO!</span>
            </div>
            <div style="text-align:center;">
              <div style="font-size:.7rem;color:var(--muted);margin-bottom:4px;">⚫⚪ (1P + 1B)</div>
              <span class="tree-node orange" style="font-size:.68rem;padding:.3rem .6rem;">≈ {t3_bw} possíveis</span>
            </div>
            <div style="text-align:center;">
              <div style="font-size:.7rem;color:var(--muted);margin-bottom:4px;">⚫ (1 preto)</div>
              <span class="tree-node purple" style="font-size:.68rem;padding:.3rem .6rem;">≈ {t3_bb} possíveis</span>
            </div>
          </div>
        </div>

        <div style="text-align:center;margin-top:.8rem;color:var(--muted);font-size:.8rem;">
          ⋮ e assim por diante até encontrar o código secreto ou esgotar tentativas
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Fórmulas e teoria ─────────────────────────────────────────────────────
    st.markdown("### 📐 A Matemática por Trás da Árvore")

    # Pré-computar strings para evitar expressões complexas dentro da f-string
    if rep:
        formula_espaco = f"Com repetição: N = n<sup>k</sup> = {n}<sup>{k}</sup> = <b>{total}</b>"
    else:
        formula_espaco = f"Sem repetição: N = P(n,k) = {n}! / {n-k}! = <b>{total}</b>"

    t_min = math.ceil(math.log2(total)) if total > 1 else 1
    f_ramos = ((k + 1) * (k + 2) // 2) - 1

    st.markdown(f"""
    <div class="tree-card">
      <div class="tree-formula-box">
        <b>1. Espaço de busca inicial</b><br>
        {formula_espaco}<br><br>

        <b>2. Profundidade mínima da árvore (cota de Shannon)</b><br>
        Cada feedback elimina parte das possibilidades. No melhor caso teórico:<br>
        &nbsp;&nbsp;&nbsp;t<sub>min</sub> = ⌈log<sub>2</sub>(N)⌉ = ⌈log<sub>2</sub>({total})⌉ = <b>{t_min} tentativas</b><br><br>

        <b>3. Fator de ramificação</b><br>
        O número de feedbacks distintos por tentativa determina quantos ramos a árvore pode ter.
        Para um código de {k} posições, o número máximo de feedbacks distintos é:<br>
        &nbsp;&nbsp;&nbsp;F = (k+1)(k+2)/2 − 1 = ({k}+1)({k}+2)/2 − 1 = <b>{f_ramos} feedbacks possíveis</b><br><br>

        <b>4. Estratégia ótima (minimax)</b><br>
        A tentativa mais informativa é aquela que divide o espaço de possibilidades
        de forma mais equilibrada — minimizando o pior caso. Isso é chamado de
        <em>estratégia minimax</em> e é a base dos algoritmos de IA para o Mastermind.
      </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Atividade prática ─────────────────────────────────────────────────────
    st.markdown("### ✏️ Atividade Prática")

    st.markdown("""
    <div class="tree-card">
      <h3 style="font-family:'Orbitron',monospace;font-size:.78rem;color:#c2410c;
                 letter-spacing:.1em;margin:0 0 .8rem;">📝 MAPEIE SUA PRÓPRIA ÁRVORE</h3>
      <p style="font-size:.9rem;color:var(--text);line-height:1.65;">
        Após cada partida, tente reconstruir sua árvore de decisão:
      </p>
      <ol style="font-size:.88rem;color:var(--text);line-height:2;padding-left:1.2rem;">
        <li>Anote sua 1ª tentativa e o feedback recebido.</li>
        <li>Liste quantos códigos ainda são possíveis após esse feedback.</li>
        <li>Repita para cada tentativa — observe como o espaço diminui.</li>
        <li>Compare: sua sequência foi próxima do mínimo teórico calculado acima?</li>
      </ol>
      <div style="background:#eff6ff;border:1px solid #bfdbfe;border-radius:8px;
                  padding:.8rem 1rem;font-size:.83rem;color:#1d4ed8;margin-top:.8rem;">
        🔗 <b>Conexão curricular:</b> Árvores de decisão são usadas em Inteligência Artificial,
        Pesquisa Operacional e Teoria dos Jogos — áreas que partem exatamente da
        combinatória estudada no Ensino Médio.
      </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Histórico real do jogo ─────────────────────────────────────────────────
    if st.session_state.history:
        st.markdown("### 🔍 Árvore da Sua Partida Atual")
        remaining = total
        st.markdown('<div class="tree-card">', unsafe_allow_html=True)
        for i, (guess, blacks, whites) in enumerate(st.session_state.history, 1):
            # Estimativa simples de redução
            feedback_weight = (blacks * 2 + (whites if st.session_state.use_white_pegs else 0) + 1)
            max_w = k * 2 + 1
            reduction = max(0.1, 1 - feedback_weight / (max_w * 1.5))
            remaining = max(1, int(remaining * reduction))
            pct_remaining = round(remaining / total * 100, 1)

            color_names = [ALL_COLORS[g][1] for g in guess]
            white_str = f"⚪{whites}" if st.session_state.use_white_pegs else ""
            st.markdown(f"""
            <div style="display:flex;align-items:center;gap:12px;padding:.6rem 0;
                        border-bottom:1px solid var(--border);">
              <span class="tree-node" style="font-size:.68rem;padding:.3rem .7rem;min-width:60px;text-align:center;">
                T{i}
              </span>
              <span style="font-size:.82rem;color:var(--text);flex:1;">
                {' · '.join(color_names)}
              </span>
              <span style="font-size:.78rem;color:var(--muted);">
                ⚫{blacks} {white_str}
              </span>
              <span style="font-size:.78rem;color:var(--accent);font-weight:600;min-width:100px;text-align:right;">
                ≈ {remaining} possíveis ({pct_remaining}%)
              </span>
            </div>
            """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="info-box">
          💡 Jogue uma partida primeiro para ver sua árvore de decisão personalizada aqui!
        </div>
        """, unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        if st.button("🎮 Ir Jogar", use_container_width=True):
            if st.session_state.secret is None:
                init_game()
            st.session_state.screen = "game"
            st.rerun()
    with c2:
        if st.button("🏠 Menu", use_container_width=True):
            st.session_state.screen = "intro"
            st.rerun()

# ══════════════════════════════════════════════════════════════════════════════
# TELA: JOGO
# ══════════════════════════════════════════════════════════════════════════════
else:

    # ── Sidebar ───────────────────────────────────────────────────────────────
    with st.sidebar:
        st.markdown("## ⚙️ Configurações")
        st.markdown("---")
        new_cl  = st.slider("🔢 Tamanho do código", 3, 6, st.session_state.code_len, key="sl_cl")
        new_nc  = st.slider("🎨 Número de cores",   4, 8, st.session_state.num_colors, key="sl_nc")
        new_ma  = st.slider("⏳ Tentativas máximas", 6, 15, st.session_state.max_attempts, key="sl_ma")
        new_wp  = st.toggle("⚪ Pinos brancos",      st.session_state.use_white_pegs, key="tog_wp")
        new_rep = st.toggle("🔁 Cores repetidas",    st.session_state.allow_repeats,  key="tog_rep")

        st.markdown("---")
        st.markdown("**Cores disponíveis:**")
        avail  = COLOR_KEYS[:new_nc]
        cols_c = st.columns(4)
        for i, ck in enumerate(avail):
            with cols_c[i % 4]:
                st.markdown(f'<div style="width:24px;height:24px;border-radius:50%;background:{color_hex(ck)};margin:2px auto;box-shadow:0 2px 6px {color_hex(ck)}88;"></div>', unsafe_allow_html=True)

        st.markdown("---")
        if st.button("🚀 NOVO JOGO", use_container_width=True):
            st.session_state.code_len       = new_cl
            st.session_state.num_colors     = new_nc
            st.session_state.max_attempts   = new_ma
            st.session_state.use_white_pegs = new_wp
            st.session_state.allow_repeats  = new_rep
            init_game()
            st.rerun()

        st.markdown("---")
        if st.button("🧮 Quiz", use_container_width=True):
            st.session_state.quiz_idx = 0; st.session_state.quiz_score = 0
            st.session_state.quiz_answers = {}; st.session_state.quiz_done = False
            st.session_state.quiz_questions = None
            st.session_state.screen = "quiz"; st.rerun()
        if st.button("🌳 Árvore", use_container_width=True):
            st.session_state.screen = "tree"; st.rerun()
        if st.button("🏠 Menu",   use_container_width=True):
            st.session_state.screen = "intro"; st.rerun()

        st.markdown("---")
        wp_hint = "⚪ <b>Pino branco</b> = cor certa, posição errada<br>" if st.session_state.use_white_pegs else ""
        st.markdown(f"""
<div class="info-box">
⚫ <b>Pino preto</b> = cor certa, posição certa<br>
{wp_hint}
Descubra o código em até <b>{st.session_state.max_attempts}</b> tentativas!
</div>
""", unsafe_allow_html=True)

    # ── Header ────────────────────────────────────────────────────────────────
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

    # ── Histórico ─────────────────────────────────────────────────────────────
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
              <span style="font-size:.75rem;color:var(--muted);min-width:60px;">
                ⚫{blacks} {w_str}
              </span>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("---")

    # ── Fim de jogo ───────────────────────────────────────────────────────────
    if st.session_state.game_over:
        if st.session_state.won:
            st.markdown(f'<div class="banner-win">🏆 PARABÉNS! Você decifrou o código em {len(st.session_state.history)} tentativa(s)!</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="banner-lose">💀 GAME OVER — Você usou todas as tentativas!</div>', unsafe_allow_html=True)

        st.markdown('<div class="secret-reveal"><div class="secret-label">🔓 CÓDIGO SECRETO</div>', unsafe_allow_html=True)
        st.markdown(render_code_pegs(st.session_state.secret), unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        c1, c2, c3 = st.columns(3)
        with c1:
            if st.button("🔄 Jogar Novamente", use_container_width=True):
                init_game(); st.rerun()
        with c2:
            if st.button("🌳 Ver Árvore", use_container_width=True):
                st.session_state.screen = "tree"; st.rerun()
        with c3:
            if st.button("🧮 Fazer Quiz", use_container_width=True):
                st.session_state.quiz_idx = 0; st.session_state.quiz_score = 0
                st.session_state.quiz_answers = {}; st.session_state.quiz_done = False
                st.session_state.quiz_questions = None
                st.session_state.screen = "quiz"; st.rerun()

    # ── Tentativa ativa ───────────────────────────────────────────────────────
    else:
        st.markdown(f"### 🎯 Tentativa #{len(st.session_state.history)+1}")

        pool = COLOR_KEYS[:st.session_state.num_colors]
        for i in range(st.session_state.code_len):
            if st.session_state.current[i] not in pool:
                st.session_state.current[i] = pool[0]

        cols = st.columns(st.session_state.code_len)
        for i, col in enumerate(cols):
            with col:
                chosen = st.selectbox(f"P{i+1}", pool,
                                      index=pool.index(st.session_state.current[i]),
                                      key=f"sel_{i}", label_visibility="collapsed")
                st.session_state.current[i] = chosen
                st.markdown(
                    f'<div style="display:flex;justify-content:center;margin-top:4px;">'
                    f'<div class="peg" style="background:{color_hex(chosen)};'
                    f'box-shadow:0 3px 10px {color_hex(chosen)}88,inset 0 2px 4px rgba(255,255,255,.4);"></div></div>',
                    unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        guess = st.session_state.current[:]
        repeat_conflict = (not st.session_state.allow_repeats) and (len(set(guess)) < len(guess))
        if repeat_conflict:
            st.warning("⚠️ Repetição de cores não permitida! Escolha cores diferentes.")

        c1, c2 = st.columns([3, 1])
        with c1:
            if st.button("✅ CONFIRMAR TENTATIVA", use_container_width=True, disabled=repeat_conflict):
                blacks, whites = evaluate_guess(st.session_state.secret, guess)
                st.session_state.history.append((guess[:], blacks, whites))
                if blacks == st.session_state.code_len:
                    st.session_state.game_over = True; st.session_state.won = True
                elif len(st.session_state.history) >= st.session_state.max_attempts:
                    st.session_state.game_over = True; st.session_state.won = False
                st.session_state.current = [pool[0]] * st.session_state.code_len
                st.rerun()
        with c2:
            if st.button("🎲 Aleatório", use_container_width=True):
                st.session_state.current = (
                    [random.choice(pool) for _ in range(st.session_state.code_len)]
                    if st.session_state.allow_repeats else random.sample(pool, st.session_state.code_len))
                st.rerun()

        white_info = "| ⚪ <b>Pino branco</b>: cor certa MAS posição errada" if st.session_state.use_white_pegs else "| modo sem pinos brancos ativo"
        st.markdown(f"""
        <div class="info-box">
        ⚫ <b>Pino preto</b>: cor certa NA posição certa &nbsp;
        {white_info}
        </div>
        """, unsafe_allow_html=True)
