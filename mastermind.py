import streamlit as st
import random

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Mastermind Educativo",
    page_icon="🎯",
    layout="centered",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Share+Tech+Mono&display=swap');

:root {
    --bg:       #0a0e1a;
    --panel:    #111827;
    --border:   #1e2d45;
    --accent:   #00d4ff;
    --accent2:  #ff6b35;
    --gold:     #ffd700;
    --white:    #e8f4fd;
    --muted:    #4a5568;
    --success:  #00ff88;
    --danger:   #ff4757;
}

html, body, [data-testid="stAppViewContainer"] {
    background-color: var(--bg) !important;
    color: var(--white);
    font-family: 'Share Tech Mono', monospace;
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0d1526 0%, #0a1020 100%) !important;
    border-right: 1px solid var(--border);
}

[data-testid="stSidebar"] * { color: var(--white) !important; }

h1, h2, h3 { font-family: 'Orbitron', monospace !important; }

.title-block {
    text-align: center;
    padding: 2rem 1rem 1rem;
}
.title-block h1 {
    font-size: 2.8rem;
    font-weight: 900;
    background: linear-gradient(135deg, var(--accent), var(--accent2));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    letter-spacing: 0.12em;
    margin: 0;
}
.title-block p {
    color: var(--muted);
    font-size: 0.85rem;
    margin-top: 0.4rem;
    letter-spacing: 0.08em;
}

/* Peg circles */
.peg-row { display:flex; gap:10px; align-items:center; justify-content:center; margin:4px 0; }

.peg {
    width: 44px; height: 44px;
    border-radius: 50%;
    border: 2px solid rgba(255,255,255,0.12);
    box-shadow: 0 0 10px rgba(0,0,0,0.5), inset 0 2px 4px rgba(255,255,255,0.15);
    display: inline-block;
    flex-shrink: 0;
}
.peg-empty {
    background: #1a2235;
    border: 2px dashed var(--border);
    box-shadow: none;
}
.peg-sm {
    width: 16px; height: 16px;
    border-radius: 50%;
    display: inline-block;
    flex-shrink: 0;
}
.peg-sm-black { background:#222; border:1px solid #444; }
.peg-sm-white { background:#eee; border:1px solid #aaa; box-shadow:0 0 4px rgba(255,255,255,0.4); }
.peg-sm-empty { background:#1a2235; border:1px solid #2a3a55; }

/* Feedback grid */
.fb-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, 16px);
    gap: 4px;
    width: 60px;
    align-items: center;
}

/* Row card */
.row-card {
    background: var(--panel);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 10px 16px;
    margin: 6px 0;
    display: flex;
    align-items: center;
    gap: 14px;
}
.row-num {
    font-family: 'Orbitron', monospace;
    font-size: 0.7rem;
    color: var(--muted);
    width: 24px;
    text-align: right;
}
.separator { flex: 1; }

/* Selectboxes */
div[data-baseweb="select"] > div {
    background: #141e30 !important;
    border: 1px solid var(--border) !important;
    border-radius: 8px !important;
    color: var(--white) !important;
}

/* Buttons */
.stButton > button {
    font-family: 'Orbitron', monospace !important;
    font-weight: 700 !important;
    border-radius: 6px !important;
    border: none !important;
    letter-spacing: 0.06em !important;
    transition: all 0.2s !important;
}
.stButton > button:hover { transform: translateY(-1px); box-shadow: 0 4px 16px rgba(0,212,255,0.25) !important; }

/* Win / Lose banners */
.banner-win {
    background: linear-gradient(135deg, #003322, #004433);
    border: 1px solid var(--success);
    border-radius: 12px;
    padding: 1.2rem;
    text-align: center;
    font-family: 'Orbitron', monospace;
    color: var(--success);
    box-shadow: 0 0 30px rgba(0,255,136,0.15);
    margin: 1rem 0;
}
.banner-lose {
    background: linear-gradient(135deg, #220011, #330022);
    border: 1px solid var(--danger);
    border-radius: 12px;
    padding: 1.2rem;
    text-align: center;
    font-family: 'Orbitron', monospace;
    color: var(--danger);
    box-shadow: 0 0 30px rgba(255,71,87,0.15);
    margin: 1rem 0;
}

/* Info box */
.info-box {
    background: #0d1a2e;
    border: 1px solid var(--border);
    border-left: 3px solid var(--accent);
    border-radius: 6px;
    padding: 0.8rem 1rem;
    font-size: 0.82rem;
    color: #8aa8c8;
    margin: 0.6rem 0;
    line-height: 1.6;
}

/* Secret code reveal */
.secret-reveal {
    background: #0d1a2e;
    border: 1px solid var(--gold);
    border-radius: 10px;
    padding: 0.8rem 1.2rem;
    text-align: center;
    margin: 0.8rem 0;
}
.secret-label {
    font-family: 'Orbitron', monospace;
    font-size: 0.65rem;
    color: var(--gold);
    letter-spacing: 0.12em;
    margin-bottom: 8px;
}

/* Slider */
.stSlider { padding: 0 4px; }

/* Stats */
.stat-grid { display:flex; gap:12px; justify-content:center; flex-wrap:wrap; margin:0.6rem 0; }
.stat-card {
    background: #0d1526;
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 0.5rem 1rem;
    text-align: center;
    min-width: 80px;
}
.stat-val { font-family:'Orbitron',monospace; font-size:1.3rem; color:var(--accent); font-weight:700; }
.stat-lbl { font-size:0.65rem; color:var(--muted); letter-spacing:0.08em; }

div[data-testid="stMetric"] { display:none; }
</style>
""", unsafe_allow_html=True)

# ── Color palette ─────────────────────────────────────────────────────────────
ALL_COLORS = {
    "🔴 Vermelho":  ("#e74c3c", "Vermelho"),
    "🔵 Azul":      ("#3498db", "Azul"),
    "🟢 Verde":     ("#2ecc71", "Verde"),
    "🟡 Amarelo":   ("#f1c40f", "Amarelo"),
    "🟠 Laranja":   ("#e67e22", "Laranja"),
    "🟣 Roxo":      ("#9b59b6", "Roxo"),
    "⚪ Branco":    ("#ecf0f1", "Branco"),
    "🩷 Rosa":      ("#ff6b9d", "Rosa"),
}

COLOR_KEYS = list(ALL_COLORS.keys())

# ── Helpers ───────────────────────────────────────────────────────────────────
def color_hex(key):
    return ALL_COLORS[key][0]

def color_name(key):
    return ALL_COLORS[key][1]

def peg_html(hex_color, size="normal"):
    if size == "normal":
        return f'<div class="peg" style="background:{hex_color};"></div>'
    return f'<div class="peg-empty"></div>'

def render_code_pegs(guess_list):
    html = '<div class="peg-row">'
    for k in guess_list:
        html += f'<div class="peg" style="background:{color_hex(k)};box-shadow:0 0 8px {color_hex(k)}55,inset 0 2px 4px rgba(255,255,255,0.2);"></div>'
    html += '</div>'
    return html

def render_empty_pegs(n):
    html = '<div class="peg-row">'
    for _ in range(n):
        html += '<div class="peg peg-empty"></div>'
    html += '</div>'
    return html

def render_feedback(blacks, whites, code_len, use_white_pegs):
    total = code_len
    html = '<div class="fb-grid">'
    for _ in range(blacks):
        html += '<div class="peg-sm peg-sm-black"></div>'
    if use_white_pegs:
        for _ in range(whites):
            html += '<div class="peg-sm peg-sm-white"></div>'
    remaining = total - blacks - (whites if use_white_pegs else 0)
    for _ in range(remaining):
        html += '<div class="peg-sm peg-sm-empty"></div>'
    html += '</div>'
    return html

def evaluate_guess(secret, guess):
    blacks = sum(s == g for s, g in zip(secret, guess))
    secret_rem = [s for s, g in zip(secret, guess) if s != g]
    guess_rem  = [g for s, g in zip(secret, guess) if s != g]
    whites = 0
    for g in guess_rem:
        if g in secret_rem:
            whites += 1
            secret_rem.remove(g)
    return blacks, whites

def init_game():
    cfg = st.session_state
    colors_pool = COLOR_KEYS[:cfg.num_colors]
    if cfg.allow_repeats:
        secret = [random.choice(colors_pool) for _ in range(cfg.code_len)]
    else:
        secret = random.sample(colors_pool, cfg.code_len)
    cfg.secret     = secret
    cfg.history    = []          # list of (guess, blacks, whites)
    cfg.game_over  = False
    cfg.won        = False
    cfg.current    = [COLOR_KEYS[0]] * cfg.code_len

# ── Session defaults ──────────────────────────────────────────────────────────
def ensure_defaults():
    defaults = {
        "code_len":      4,
        "num_colors":    6,
        "max_attempts":  10,
        "use_white_pegs": True,
        "allow_repeats": True,
        "secret":        None,
        "history":       [],
        "game_over":     False,
        "won":           False,
        "current":       None,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v
    if st.session_state.secret is None:
        init_game()

ensure_defaults()

# ── Sidebar – Configuration ───────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## ⚙️ Configurações")
    st.markdown("---")

    new_code_len = st.slider("🔢 Tamanho do código", 3, 6,
                             st.session_state.code_len, key="sl_code_len")
    new_num_colors = st.slider("🎨 Número de cores", 4, 8,
                               st.session_state.num_colors, key="sl_num_colors")
    new_max_attempts = st.slider("⏳ Tentativas máximas", 6, 15,
                                 st.session_state.max_attempts, key="sl_max")
    new_white = st.toggle("⚪ Usar pinos brancos (posição certa, cor errada)",
                          st.session_state.use_white_pegs, key="tog_white")
    new_repeat = st.toggle("🔁 Permitir cores repetidas",
                           st.session_state.allow_repeats, key="tog_repeat")

    st.markdown("---")
    st.markdown("**Cores disponíveis:**")
    avail = COLOR_KEYS[:new_num_colors]
    cols_c = st.columns(4)
    for i, ck in enumerate(avail):
        with cols_c[i % 4]:
            st.markdown(f'<div style="width:24px;height:24px;border-radius:50%;'
                        f'background:{color_hex(ck)};margin:2px auto;'
                        f'box-shadow:0 0 6px {color_hex(ck)}88;"></div>',
                        unsafe_allow_html=True)

    st.markdown("---")
    if st.button("🚀 NOVO JOGO", use_container_width=True):
        st.session_state.code_len      = new_code_len
        st.session_state.num_colors    = new_num_colors
        st.session_state.max_attempts  = new_max_attempts
        st.session_state.use_white_pegs = new_white
        st.session_state.allow_repeats  = new_repeat
        init_game()
        st.rerun()

    st.markdown("---")
    st.markdown("### 📖 Como jogar")
    st.markdown(f"""
<div class="info-box">
🔴 <b>Pino preto</b> = cor certa, posição certa<br>
{"⚪ <b>Pino branco</b> = cor certa, posição errada<br>" if st.session_state.use_white_pegs else ""}
Descubra o código secreto em até <b>{st.session_state.max_attempts}</b> tentativas!
</div>
""", unsafe_allow_html=True)

# ── Main area ─────────────────────────────────────────────────────────────────
st.markdown("""
<div class="title-block">
  <h1>MASTERMIND</h1>
  <p>JOGO EDUCATIVO DE LÓGICA E DEDUÇÃO</p>
</div>
""", unsafe_allow_html=True)

# Stats bar
attempts_left = st.session_state.max_attempts - len(st.session_state.history)
st.markdown(f"""
<div class="stat-grid">
  <div class="stat-card">
    <div class="stat-val">{len(st.session_state.history)}</div>
    <div class="stat-lbl">TENTATIVAS</div>
  </div>
  <div class="stat-card">
    <div class="stat-val">{attempts_left}</div>
    <div class="stat-lbl">RESTANTES</div>
  </div>
  <div class="stat-card">
    <div class="stat-val">{st.session_state.code_len}</div>
    <div class="stat-lbl">POSIÇÕES</div>
  </div>
  <div class="stat-card">
    <div class="stat-val">{st.session_state.num_colors}</div>
    <div class="stat-lbl">CORES</div>
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ── History ───────────────────────────────────────────────────────────────────
if st.session_state.history:
    st.markdown("### 📋 Tentativas anteriores")
    for i, (guess, blacks, whites) in enumerate(st.session_state.history, 1):
        row_html = f"""
        <div class="row-card">
          <span class="row-num">#{i}</span>
          {render_code_pegs(guess)}
          <div class="separator"></div>
          {render_feedback(blacks, whites, st.session_state.code_len, st.session_state.use_white_pegs)}
          <span style="font-size:0.75rem;color:#4a5568;min-width:60px;">
            ⚫{blacks} {"⚪"+str(whites) if st.session_state.use_white_pegs else ""}
          </span>
        </div>
        """
        st.markdown(row_html, unsafe_allow_html=True)
    st.markdown("---")

# ── Win / Lose ────────────────────────────────────────────────────────────────
if st.session_state.game_over:
    if st.session_state.won:
        st.markdown(f"""
        <div class="banner-win">
          🏆 PARABÉNS! Você decifrou o código em {len(st.session_state.history)} tentativa(s)!
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="banner-lose">
          💀 GAME OVER — Você usou todas as tentativas!
        </div>
        """, unsafe_allow_html=True)

    # Reveal secret
    st.markdown('<div class="secret-reveal"><div class="secret-label">🔓 CÓDIGO SECRETO</div>', unsafe_allow_html=True)
    st.markdown(render_code_pegs(st.session_state.secret), unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("🔄 Jogar Novamente", use_container_width=True):
        init_game()
        st.rerun()

# ── Active guess UI ───────────────────────────────────────────────────────────
else:
    st.markdown(f"### 🎯 Tentativa #{len(st.session_state.history)+1}")

    colors_pool = COLOR_KEYS[:st.session_state.num_colors]

    # Ensure current guess uses valid colors
    for i in range(st.session_state.code_len):
        if st.session_state.current[i] not in colors_pool:
            st.session_state.current[i] = colors_pool[0]

    # Color selectors
    cols = st.columns(st.session_state.code_len)
    for i, col in enumerate(cols):
        with col:
            chosen = st.selectbox(
                f"Pos {i+1}",
                options=colors_pool,
                index=colors_pool.index(st.session_state.current[i]),
                key=f"sel_{i}",
                label_visibility="collapsed",
            )
            st.session_state.current[i] = chosen
            # Preview peg
            st.markdown(
                f'<div style="display:flex;justify-content:center;margin-top:4px;">'
                f'<div class="peg" style="background:{color_hex(chosen)};'
                f'box-shadow:0 0 10px {color_hex(chosen)}88,inset 0 2px 4px rgba(255,255,255,0.2);"></div>'
                f'</div>',
                unsafe_allow_html=True,
            )

    st.markdown("<br>", unsafe_allow_html=True)

    # Validate no-repeat constraint
    guess = st.session_state.current[:]
    repeat_conflict = (not st.session_state.allow_repeats) and (len(set(guess)) < len(guess))

    if repeat_conflict:
        st.warning("⚠️ Repetição de cores não permitida! Escolha cores diferentes.")

    c1, c2 = st.columns([3, 1])
    with c1:
        if st.button("✅ CONFIRMAR TENTATIVA", use_container_width=True,
                     disabled=repeat_conflict):
            blacks, whites = evaluate_guess(st.session_state.secret, guess)
            st.session_state.history.append((guess[:], blacks, whites))

            if blacks == st.session_state.code_len:
                st.session_state.game_over = True
                st.session_state.won = True
            elif len(st.session_state.history) >= st.session_state.max_attempts:
                st.session_state.game_over = True
                st.session_state.won = False

            # Reset current selection
            st.session_state.current = [colors_pool[0]] * st.session_state.code_len
            st.rerun()

    with c2:
        if st.button("🎲 Aleatório", use_container_width=True):
            if st.session_state.allow_repeats:
                st.session_state.current = [random.choice(colors_pool)
                                            for _ in range(st.session_state.code_len)]
            else:
                st.session_state.current = random.sample(colors_pool,
                                                          st.session_state.code_len)
            st.rerun()

    # Hint box
    if st.session_state.use_white_pegs:
        st.markdown("""
        <div class="info-box">
        ⚫ <b>Pino preto</b>: cor certa NA posição certa &nbsp;|&nbsp;
        ⚪ <b>Pino branco</b>: cor certa MAS posição errada
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="info-box">
        ⚫ <b>Pino preto</b>: cor certa NA posição certa &nbsp;
        (modo sem pinos brancos ativo)
        </div>
        """, unsafe_allow_html=True)
