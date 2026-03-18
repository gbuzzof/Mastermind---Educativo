import streamlit as st
import random

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Mastermind Educativo",
    page_icon="🎯",
    layout="centered",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=DM+Sans:wght@400;500;600&display=swap');

:root {
    --bg:       #f0f4f8;
    --panel:    #ffffff;
    --border:   #dde3ec;
    --accent:   #2563eb;
    --accent2:  #f97316;
    --gold:     #d97706;
    --text:     #1e293b;
    --muted:    #64748b;
    --success:  #16a34a;
    --danger:   #dc2626;
    --shadow:   rgba(30,41,59,0.10);
}

html, body, [data-testid="stAppViewContainer"] {
    background-color: var(--bg) !important;
    color: var(--text);
    font-family: 'DM Sans', sans-serif;
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #ffffff 0%, #f1f5fb 100%) !important;
    border-right: 1px solid var(--border);
}
[data-testid="stSidebar"] * { color: var(--text) !important; }

h1, h2, h3 { font-family: 'Orbitron', monospace !important; }

/* ── Intro screen ── */
.intro-wrapper { max-width:620px; margin:0 auto; padding:2rem 0 3rem; }
.intro-title { text-align:center; margin-bottom:0.2rem; }
.intro-title h1 {
    font-size:3rem; font-weight:900;
    background:linear-gradient(135deg,var(--accent),var(--accent2));
    -webkit-background-clip:text; -webkit-text-fill-color:transparent;
    letter-spacing:0.1em; margin:0;
}
.intro-title p {
    color:var(--muted); font-size:0.85rem; letter-spacing:0.1em;
    margin-top:0.3rem; font-family:'Orbitron',monospace;
}
.rules-card {
    background:var(--panel); border:1px solid var(--border);
    border-radius:16px; padding:1.8rem 2rem; margin:1.6rem 0;
    box-shadow:0 4px 20px var(--shadow);
}
.rules-card h3 {
    font-size:0.85rem !important; color:var(--accent) !important;
    letter-spacing:0.12em; margin-bottom:1rem; margin-top:0;
}
.rule-item {
    display:flex; align-items:flex-start; gap:14px;
    padding:0.75rem 0; border-bottom:1px solid var(--border);
    font-size:0.92rem; color:var(--text); line-height:1.55;
}
.rule-item:last-child { border-bottom:none; }
.rule-icon { font-size:1.3rem; flex-shrink:0; margin-top:1px; }
.rule-title { font-weight:600; display:block; margin-bottom:2px; }
.rule-desc  { color:var(--muted); font-size:0.84rem; }
.peg-demo { display:flex; gap:8px; align-items:center; margin:0.8rem 0 0.4rem; }
.peg-demo-circle {
    width:32px; height:32px; border-radius:50%;
    border:2px solid rgba(0,0,0,0.08);
    box-shadow:0 2px 6px rgba(0,0,0,0.15),inset 0 1px 3px rgba(255,255,255,0.5);
    flex-shrink:0;
}
.feedback-demo { display:flex; gap:6px; align-items:center; margin:0.6rem 0; }
.fd-black { width:16px;height:16px;border-radius:50%;background:#1e293b;border:1px solid #334155;flex-shrink:0; }
.fd-white { width:16px;height:16px;border-radius:50%;background:#f1f5f9;border:1px solid #94a3b8;box-shadow:0 0 3px rgba(0,0,0,0.15);flex-shrink:0; }
.fd-empty { width:16px;height:16px;border-radius:50%;background:#e2e8f0;border:1px dashed #cbd5e1;flex-shrink:0; }

/* ── Game title block ── */
.title-block { text-align:center; padding:1.5rem 1rem 0.5rem; }
.title-block h1 {
    font-size:2.4rem; font-weight:900;
    background:linear-gradient(135deg,var(--accent),var(--accent2));
    -webkit-background-clip:text; -webkit-text-fill-color:transparent;
    letter-spacing:0.1em; margin:0;
}
.title-block p {
    color:var(--muted); font-size:0.78rem; margin-top:0.3rem;
    letter-spacing:0.08em; font-family:'Orbitron',monospace;
}

/* ── Pegs ── */
.peg-row { display:flex; gap:10px; align-items:center; justify-content:center; margin:4px 0; }
.peg {
    width:44px; height:44px; border-radius:50%;
    border:2px solid rgba(0,0,0,0.08);
    box-shadow:0 3px 8px rgba(0,0,0,0.18),inset 0 2px 4px rgba(255,255,255,0.4);
    display:inline-block; flex-shrink:0;
}
.peg-empty { background:#e2e8f0; border:2px dashed var(--border); box-shadow:none; }
.peg-sm { width:16px; height:16px; border-radius:50%; display:inline-block; flex-shrink:0; }
.peg-sm-black { background:#1e293b; border:1px solid #334155; }
.peg-sm-white { background:#f1f5f9; border:1px solid #94a3b8; box-shadow:0 0 3px rgba(0,0,0,0.15); }
.peg-sm-empty { background:#e2e8f0; border:1px dashed #cbd5e1; }
.fb-grid {
    display:grid; grid-template-columns:repeat(auto-fill,16px);
    gap:4px; width:60px; align-items:center;
}

/* ── Row card ── */
.row-card {
    background:var(--panel); border:1px solid var(--border);
    border-radius:10px; padding:10px 16px; margin:6px 0;
    display:flex; align-items:center; gap:14px;
    box-shadow:0 2px 6px var(--shadow);
}
.row-num { font-family:'Orbitron',monospace; font-size:0.7rem; color:var(--muted); width:24px; text-align:right; }
.separator { flex:1; }

/* ── Selectboxes ── */
div[data-baseweb="select"] > div {
    background:#f8fafc !important; border:1px solid var(--border) !important;
    border-radius:8px !important; color:var(--text) !important;
}

/* ── Buttons ── */
.stButton > button {
    font-family:'Orbitron',monospace !important; font-weight:700 !important;
    border-radius:6px !important; border:none !important;
    letter-spacing:0.06em !important; transition:all 0.2s !important;
}
.stButton > button:hover { transform:translateY(-1px); box-shadow:0 4px 16px rgba(37,99,235,0.25) !important; }

/* ── Banners ── */
.banner-win {
    background:linear-gradient(135deg,#f0fdf4,#dcfce7); border:1px solid #86efac;
    border-radius:12px; padding:1.2rem; text-align:center;
    font-family:'Orbitron',monospace; color:var(--success);
    box-shadow:0 4px 16px rgba(22,163,74,0.12); margin:1rem 0;
}
.banner-lose {
    background:linear-gradient(135deg,#fff1f2,#ffe4e6); border:1px solid #fca5a5;
    border-radius:12px; padding:1.2rem; text-align:center;
    font-family:'Orbitron',monospace; color:var(--danger);
    box-shadow:0 4px 16px rgba(220,38,38,0.10); margin:1rem 0;
}

/* ── Info / secret boxes ── */
.info-box {
    background:#eff6ff; border:1px solid #bfdbfe; border-left:3px solid var(--accent);
    border-radius:6px; padding:0.8rem 1rem; font-size:0.82rem;
    color:#1d4ed8; margin:0.6rem 0; line-height:1.6;
}
.secret-reveal {
    background:#fffbeb; border:1px solid #fcd34d;
    border-radius:10px; padding:0.8rem 1.2rem; text-align:center; margin:0.8rem 0;
}
.secret-label {
    font-family:'Orbitron',monospace; font-size:0.65rem;
    color:var(--gold); letter-spacing:0.12em; margin-bottom:8px;
}

/* ── Stats ── */
.stat-grid { display:flex; gap:12px; justify-content:center; flex-wrap:wrap; margin:0.6rem 0; }
.stat-card {
    background:var(--panel); border:1px solid var(--border);
    border-radius:8px; padding:0.5rem 1rem; text-align:center;
    min-width:80px; box-shadow:0 2px 6px var(--shadow);
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
def color_hex(key):  return ALL_COLORS[key][0]

def render_code_pegs(guess_list):
    html = '<div class="peg-row">'
    for k in guess_list:
        html += (f'<div class="peg" style="background:{color_hex(k)};'
                 f'box-shadow:0 3px 8px {color_hex(k)}66,'
                 f'inset 0 2px 4px rgba(255,255,255,0.4);"></div>')
    return html + '</div>'

def render_feedback(blacks, whites, code_len, use_white_pegs):
    html = '<div class="fb-grid">'
    for _ in range(blacks):
        html += '<div class="peg-sm peg-sm-black"></div>'
    if use_white_pegs:
        for _ in range(whites):
            html += '<div class="peg-sm peg-sm-white"></div>'
    for _ in range(code_len - blacks - (whites if use_white_pegs else 0)):
        html += '<div class="peg-sm peg-sm-empty"></div>'
    return html + '</div>'

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
    pool = COLOR_KEYS[:cfg.num_colors]
    cfg.secret    = ([random.choice(pool) for _ in range(cfg.code_len)]
                     if cfg.allow_repeats else random.sample(pool, cfg.code_len))
    cfg.history   = []
    cfg.game_over = False
    cfg.won       = False
    cfg.current   = [COLOR_KEYS[0]] * cfg.code_len

# ── Session defaults ──────────────────────────────────────────────────────────
for k, v in {
    "screen": "intro", "code_len": 4, "num_colors": 6, "max_attempts": 10,
    "use_white_pegs": True, "allow_repeats": True,
    "secret": None, "history": [], "game_over": False, "won": False, "current": None,
}.items():
    if k not in st.session_state:
        st.session_state[k] = v

# ══════════════════════════════════════════════════════════════════════════════
# INTRO SCREEN
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
    <div class="rules-card">
      <h3>🎯 OBJETIVO</h3>
      <div class="rule-item">
        <span class="rule-icon">🔐</span>
        <div>
          <span class="rule-title">Decifre o código secreto!</span>
          <span class="rule-desc">
            O computador escolhe uma sequência secreta de cores. Seu objetivo é descobrir
            quais são as cores e em que posições estão, usando lógica e dedução.
          </span>
        </div>
      </div>
    </div>

    <div class="rules-card">
      <h3>📋 COMO JOGAR</h3>
      <div class="rule-item">
        <span class="rule-icon">1️⃣</span>
        <div>
          <span class="rule-title">Escolha as cores</span>
          <span class="rule-desc">Em cada tentativa, selecione uma cor para cada posição do código usando os menus.</span>
        </div>
      </div>
      <div class="rule-item">
        <span class="rule-icon">2️⃣</span>
        <div>
          <span class="rule-title">Confirme sua tentativa</span>
          <span class="rule-desc">Clique em <b>Confirmar Tentativa</b>. O jogo revelará pinos de feedback.</span>
        </div>
      </div>
      <div class="rule-item">
        <span class="rule-icon">3️⃣</span>
        <div>
          <span class="rule-title">Interprete o feedback</span>
          <span class="rule-desc">Cada tentativa retorna pinos de avaliação:</span>
          <div class="feedback-demo">
            <div class="fd-black"></div>
            <span style="font-size:0.84rem;"><b>Pino preto</b> = cor certa + posição certa</span>
          </div>
          <div class="feedback-demo">
            <div class="fd-white"></div>
            <span style="font-size:0.84rem;"><b>Pino branco</b> = cor certa, mas posição errada</span>
          </div>
          <div class="feedback-demo">
            <div class="fd-empty"></div>
            <span style="font-size:0.84rem;"><b>Vazio</b> = essa cor não está no código</span>
          </div>
        </div>
      </div>
      <div class="rule-item">
        <span class="rule-icon">4️⃣</span>
        <div>
          <span class="rule-title">Use a lógica!</span>
          <span class="rule-desc">
            Analise os feedbacks anteriores para afunilar as possibilidades e chegar ao código
            certo antes de acabar as tentativas.
          </span>
        </div>
      </div>
    </div>

    <div class="rules-card">
      <h3>💡 EXEMPLO</h3>
      <div class="rule-item">
        <span class="rule-icon">🤫</span>
        <div>
          <span class="rule-title">Código secreto (oculto):</span>
          <div class="peg-demo">
            <div class="peg-demo-circle" style="background:#e74c3c;"></div>
            <div class="peg-demo-circle" style="background:#3498db;"></div>
            <div class="peg-demo-circle" style="background:#2ecc71;"></div>
            <div class="peg-demo-circle" style="background:#f1c40f;"></div>
          </div>
        </div>
      </div>
      <div class="rule-item">
        <span class="rule-icon">🎮</span>
        <div>
          <span class="rule-title">Sua tentativa:</span>
          <div class="peg-demo">
            <div class="peg-demo-circle" style="background:#e74c3c;"></div>
            <div class="peg-demo-circle" style="background:#9b59b6;"></div>
            <div class="peg-demo-circle" style="background:#f1c40f;"></div>
            <div class="peg-demo-circle" style="background:#2ecc71;"></div>
          </div>
          <span class="rule-desc">
            Resultado: <b>1 pino preto</b> (Vermelho na pos. 1 ✓) +
            <b>2 pinos brancos</b> (Amarelo e Verde existem, mas estão trocados de posição).
          </span>
        </div>
      </div>
    </div>

    <div class="rules-card">
      <h3>⚙️ CONFIGURAÇÕES DISPONÍVEIS</h3>
      <div class="rule-item">
        <span class="rule-icon">🎨</span>
        <div>
          <span class="rule-title">Número de cores (4–8)</span>
          <span class="rule-desc">Mais cores = mais possibilidades = maior dificuldade.</span>
        </div>
      </div>
      <div class="rule-item">
        <span class="rule-icon">🔢</span>
        <div>
          <span class="rule-title">Tamanho do código (3–6)</span>
          <span class="rule-desc">Códigos mais longos são mais desafiadores.</span>
        </div>
      </div>
      <div class="rule-item">
        <span class="rule-icon">⚪</span>
        <div>
          <span class="rule-title">Pinos brancos</span>
          <span class="rule-desc">Ative ou desative a dica de "cor certa, posição errada".</span>
        </div>
      </div>
      <div class="rule-item">
        <span class="rule-icon">🔁</span>
        <div>
          <span class="rule-title">Cores repetidas</span>
          <span class="rule-desc">Permita ou proíba que a mesma cor apareça mais de uma vez no código.</span>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    col_l, col_c, col_r = st.columns([1, 2, 1])
    with col_c:
        if st.button("🚀 INICIAR JOGO", use_container_width=True):
            init_game()
            st.session_state.screen = "game"
            st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# GAME SCREEN
# ══════════════════════════════════════════════════════════════════════════════
else:

    # ── Sidebar ───────────────────────────────────────────────────────────────
    with st.sidebar:
        st.markdown("## ⚙️ Configurações")
        st.markdown("---")

        new_code_len     = st.slider("🔢 Tamanho do código", 3, 6,
                                     st.session_state.code_len, key="sl_code_len")
        new_num_colors   = st.slider("🎨 Número de cores", 4, 8,
                                     st.session_state.num_colors, key="sl_num_colors")
        new_max_attempts = st.slider("⏳ Tentativas máximas", 6, 15,
                                     st.session_state.max_attempts, key="sl_max")
        new_white  = st.toggle("⚪ Usar pinos brancos",
                               st.session_state.use_white_pegs, key="tog_white")
        new_repeat = st.toggle("🔁 Permitir cores repetidas",
                               st.session_state.allow_repeats, key="tog_repeat")

        st.markdown("---")
        st.markdown("**Cores disponíveis:**")
        avail  = COLOR_KEYS[:new_num_colors]
        cols_c = st.columns(4)
        for i, ck in enumerate(avail):
            with cols_c[i % 4]:
                st.markdown(
                    f'<div style="width:24px;height:24px;border-radius:50%;'
                    f'background:{color_hex(ck)};margin:2px auto;'
                    f'box-shadow:0 2px 6px {color_hex(ck)}88;"></div>',
                    unsafe_allow_html=True,
                )

        st.markdown("---")
        if st.button("🚀 NOVO JOGO", use_container_width=True):
            st.session_state.code_len       = new_code_len
            st.session_state.num_colors     = new_num_colors
            st.session_state.max_attempts   = new_max_attempts
            st.session_state.use_white_pegs = new_white
            st.session_state.allow_repeats  = new_repeat
            init_game()
            st.rerun()

        if st.button("📖 Ver Regras", use_container_width=True):
            st.session_state.screen = "intro"
            st.rerun()

        st.markdown("---")
        st.markdown(f"""
<div class="info-box">
⚫ <b>Pino preto</b> = cor certa, posição certa<br>
{"⚪ <b>Pino branco</b> = cor certa, posição errada<br>" if st.session_state.use_white_pegs else ""}
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

    attempts_left = st.session_state.max_attempts - len(st.session_state.history)
    st.markdown(f"""
    <div class="stat-grid">
      <div class="stat-card"><div class="stat-val">{len(st.session_state.history)}</div><div class="stat-lbl">TENTATIVAS</div></div>
      <div class="stat-card"><div class="stat-val">{attempts_left}</div><div class="stat-lbl">RESTANTES</div></div>
      <div class="stat-card"><div class="stat-val">{st.session_state.code_len}</div><div class="stat-lbl">POSIÇÕES</div></div>
      <div class="stat-card"><div class="stat-val">{st.session_state.num_colors}</div><div class="stat-lbl">CORES</div></div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # ── History ───────────────────────────────────────────────────────────────
    if st.session_state.history:
        st.markdown("### 📋 Tentativas anteriores")
        for i, (guess, blacks, whites) in enumerate(st.session_state.history, 1):
            st.markdown(f"""
            <div class="row-card">
              <span class="row-num">#{i}</span>
              {render_code_pegs(guess)}
              <div class="separator"></div>
              {render_feedback(blacks, whites, st.session_state.code_len, st.session_state.use_white_pegs)}
              <span style="font-size:0.75rem;color:var(--muted);min-width:60px;">
                ⚫{blacks} {"⚪"+str(whites) if st.session_state.use_white_pegs else ""}
              </span>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("---")

    # ── Win / Lose ─────────────────────────────────────────────────────────────
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

        st.markdown('<div class="secret-reveal"><div class="secret-label">🔓 CÓDIGO SECRETO</div>',
                    unsafe_allow_html=True)
        st.markdown(render_code_pegs(st.session_state.secret), unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        c1, c2 = st.columns(2)
        with c1:
            if st.button("🔄 Jogar Novamente", use_container_width=True):
                init_game()
                st.rerun()
        with c2:
            if st.button("📖 Ver Regras", use_container_width=True):
                st.session_state.screen = "intro"
                st.rerun()

    # ── Active guess ──────────────────────────────────────────────────────────
    else:
        st.markdown(f"### 🎯 Tentativa #{len(st.session_state.history)+1}")

        colors_pool = COLOR_KEYS[:st.session_state.num_colors]
        for i in range(st.session_state.code_len):
            if st.session_state.current[i] not in colors_pool:
                st.session_state.current[i] = colors_pool[0]

        cols = st.columns(st.session_state.code_len)
        for i, col in enumerate(cols):
            with col:
                chosen = st.selectbox(
                    f"Pos {i+1}", options=colors_pool,
                    index=colors_pool.index(st.session_state.current[i]),
                    key=f"sel_{i}", label_visibility="collapsed",
                )
                st.session_state.current[i] = chosen
                st.markdown(
                    f'<div style="display:flex;justify-content:center;margin-top:4px;">'
                    f'<div class="peg" style="background:{color_hex(chosen)};'
                    f'box-shadow:0 3px 10px {color_hex(chosen)}88,'
                    f'inset 0 2px 4px rgba(255,255,255,0.4);"></div></div>',
                    unsafe_allow_html=True,
                )

        st.markdown("<br>", unsafe_allow_html=True)

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
                st.session_state.current = [colors_pool[0]] * st.session_state.code_len
                st.rerun()
        with c2:
            if st.button("🎲 Aleatório", use_container_width=True):
                st.session_state.current = (
                    [random.choice(colors_pool) for _ in range(st.session_state.code_len)]
                    if st.session_state.allow_repeats
                    else random.sample(colors_pool, st.session_state.code_len)
                )
                st.rerun()

        st.markdown(f"""
        <div class="info-box">
        ⚫ <b>Pino preto</b>: cor certa NA posição certa &nbsp;{"| ⚪ <b>Pino branco</b>: cor certa MAS posição errada" if st.session_state.use_white_pegs else "| modo sem pinos brancos ativo"}
        </div>
        """, unsafe_allow_html=True)
