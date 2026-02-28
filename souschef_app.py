import streamlit as st
import json
import os

# ─────────────────────────────────────────────
# PAGINA CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="SousChef 🍝",
    page_icon="🍝",
    layout="wide",
)

# ─────────────────────────────────────────────
# CUSTOM CSS — Italiaanse trattoria-stijl
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;1,400&family=Lato:wght@300;400;700&display=swap');

/* Achtergrond */
.stApp {
    background-color: #FDF6EC;
    font-family: 'Lato', sans-serif;
}

/* Verberg standaard Streamlit elementen */
#MainMenu, footer, header { visibility: hidden; }

/* Hero header */
.hero {
    background: linear-gradient(135deg, #2C1810 0%, #8B2E0A 60%, #C4440F 100%);
    border-radius: 16px;
    padding: 48px 40px;
    margin-bottom: 32px;
    text-align: center;
    position: relative;
    overflow: hidden;
}
.hero::before {
    content: "🍅🫒🧄🌿🍋";
    position: absolute;
    top: 12px;
    left: 0; right: 0;
    font-size: 22px;
    opacity: 0.15;
    letter-spacing: 20px;
}
.hero h1 {
    font-family: 'Playfair Display', serif;
    font-size: 3.2rem;
    color: #F5E6C8;
    margin: 0 0 8px 0;
    letter-spacing: -1px;
}
.hero .subtitle {
    font-family: 'Playfair Display', serif;
    font-style: italic;
    color: #E8C88A;
    font-size: 1.1rem;
    margin: 0;
}
.hero .gino-quote {
    margin-top: 16px;
    color: #F5E6C8;
    font-size: 0.85rem;
    opacity: 0.75;
    font-style: italic;
}

/* Receptkaart sidebar */
.recept-btn {
    width: 100%;
    text-align: left;
    padding: 10px 14px;
    border-radius: 8px;
    border: none;
    background: transparent;
    cursor: pointer;
    font-size: 0.9rem;
}

/* Recept detail sectie */
.recept-header {
    border-left: 5px solid #C4440F;
    padding-left: 20px;
    margin-bottom: 24px;
}
.recept-header h2 {
    font-family: 'Playfair Display', serif;
    font-size: 2rem;
    color: #2C1810;
    margin: 0 0 6px 0;
}
.recept-header .beschrijving {
    color: #5C3D2E;
    font-size: 1.05rem;
    line-height: 1.6;
    font-style: italic;
}

/* Badge */
.badge {
    display: inline-block;
    background: #C4440F;
    color: white;
    border-radius: 20px;
    padding: 3px 12px;
    font-size: 0.78rem;
    font-weight: 700;
    margin-right: 6px;
    margin-bottom: 12px;
    letter-spacing: 0.5px;
}
.badge-groen {
    background: #2D6A4F;
}

/* Ingrediënten kaart */
.ingredienten-kaart {
    background: #FFF8EE;
    border: 1px solid #E8D5B7;
    border-radius: 12px;
    padding: 20px 24px;
    margin-bottom: 24px;
}
.ingredienten-kaart h3 {
    font-family: 'Playfair Display', serif;
    color: #2C1810;
    font-size: 1.2rem;
    margin: 0 0 14px 0;
    border-bottom: 2px solid #E8D5B7;
    padding-bottom: 8px;
}
.ingredient-item {
    padding: 5px 0;
    border-bottom: 1px dashed #E8D5B7;
    color: #3D2B1F;
    font-size: 0.92rem;
}
.ingredient-item:last-child { border-bottom: none; }
.ingredient-item::before {
    content: "✦ ";
    color: #C4440F;
    font-size: 0.7rem;
}

/* Stap kaartjes */
.stap-kaart {
    background: white;
    border-radius: 12px;
    padding: 18px 22px;
    margin-bottom: 14px;
    border: 1px solid #E8D5B7;
    box-shadow: 0 2px 8px rgba(44,24,16,0.06);
    display: flex;
    gap: 16px;
    align-items: flex-start;
}
.stap-nummer {
    background: #C4440F;
    color: white;
    font-family: 'Playfair Display', serif;
    font-weight: 700;
    font-size: 1.1rem;
    min-width: 38px;
    height: 38px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
}
.stap-inhoud { flex: 1; }
.stap-tekst {
    color: #2C1810;
    font-size: 0.97rem;
    line-height: 1.55;
    margin-bottom: 6px;
}
.stap-tijd {
    color: #8B6F5E;
    font-size: 0.82rem;
    font-weight: 700;
    letter-spacing: 0.3px;
}
.stap-tijd::before { content: "⏱ "; }

/* Divider */
.divider {
    border: none;
    border-top: 2px dashed #E8D5B7;
    margin: 28px 0;
}

/* Nona citaat */
.nona-box {
    background: linear-gradient(135deg, #FFF3E0, #FFE8C8);
    border-left: 4px solid #E8A020;
    border-radius: 0 12px 12px 0;
    padding: 14px 18px;
    margin: 20px 0;
    font-style: italic;
    color: #5C3D2E;
    font-size: 0.92rem;
}
.nona-box::before {
    content: "👵🏻 ";
}

/* Sidebar stijl */
section[data-testid="stSidebar"] {
    background: #2C1810 !important;
}
section[data-testid="stSidebar"] .stRadio label {
    color: #F5E6C8 !important;
}
section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3 {
    color: #F5E6C8 !important;
}
section[data-testid="stSidebar"] p {
    color: #C8A882 !important;
}
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# DATA LADEN
# ─────────────────────────────────────────────
# Probeer het JSON-bestand te laden, anders gebruik demo-data
DEMO_DATA = [
    {
        "naam": "One-pan Chicken and Garlic Rice",
        "beschrijving": "Bellissimo! Een hartelijk gerecht waarbij sappige kip en geurige rijst samen in één pan worden bereid. Mijn Nona maakte dit elke vrijdagavond — simpel, eerlijk en vol liefde.",
        "ingredienten": ["5 kipfilets", "1 ui", "2 teentjes knoflook", "1 kop jasmine rijst",
                         "1½ kop kippenbouillon", "1 tl paprikapoeder", "1 tl tijm",
                         "zout en peper", "olijfolie"],
        "stappen": [
            {"stap": "Kruid de kip royaal met paprika, tijm, zout en peper. Wees niet bang — kruiden zijn je vriend!", "tijd": "3 minuten"},
            {"stap": "Verhit olijfolie in een grote pan op middelhoog vuur. Bak de kip 4 minuten per kant goudbruin. My Nona always said: een goed aangekorst stukje kip is het begin van alles.", "tijd": "8 minuten"},
            {"stap": "Leg de kip apart en fruit ui en knoflook in dezelfde pan tot ze glazig zijn.", "tijd": "3 minuten"},
            {"stap": "Voeg de rijst toe en roer 1 minuut zodat elk korreltje de smaken opneemt.", "tijd": "1 minuut"},
            {"stap": "Giet de bouillon erbij, leg de kip terug op de rijst en dek af. Kook 20 minuten op laag vuur.", "tijd": "20 minuten"},
        ],
        "reparatie_pogingen": 0
    },
    {
        "naam": "Creamy Tomato Gnocchi",
        "beschrijving": "Perfetto! Gnocchi in een rijke tomatensaus klaar in 20 minuten. Beter dan pasta? Dat zeg ik nooit hardop, maar... ja.",
        "ingredienten": ["500g gnocchi", "400g cherry tomaten", "1 ui", "3 teentjes knoflook",
                         "200ml room", "50g parmezaan", "2 el boter", "peper", "verse basilicum"],
        "stappen": [
            {"stap": "Snipper de ui fijn, pers de knoflook en halveer de cherry tomaten.", "tijd": "5 minuten"},
            {"stap": "Bak de gnocchi in boter tot ze goudbruin zijn. In Italia doen we dit ZO — niet koken maar bakken!", "tijd": "8 minuten"},
            {"stap": "Fruit ui en knoflook 2 minuten, voeg de tomaten toe en laat 3 minuten inkoken.", "tijd": "5 minuten"},
            {"stap": "Roer de room en parmezaan erdoor tot een fluweelzachte saus.", "tijd": "2 minuten"},
            {"stap": "Gooi de gnocchi terug in de saus, breng op smaak met peper en verse basilicum.", "tijd": "1 minuut"},
        ],
        "reparatie_pogingen": 0
    },
]

@st.cache_data
def laad_recepten():
    pad = "souschef_evaluatie.json"
    if os.path.exists(pad):
        with open(pad, "r", encoding="utf-8") as f:
            return json.load(f)
    return DEMO_DATA

recepten = laad_recepten()


# ─────────────────────────────────────────────
# SIDEBAR — receptenlijst
# ─────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 🍝 SousChef")
    st.markdown("*Kies een recept*")
    st.markdown("---")

    namen = [r["naam"] for r in recepten]
    keuze = st.radio(
        label="Recepten",
        options=namen,
        label_visibility="collapsed"
    )

    st.markdown("---")
    st.markdown(f"**{len(recepten)} recepten** geladen")
    reparaties = sum(r.get("reparatie_pogingen", 0) for r in recepten)
    st.markdown(f"**{reparaties}** repair-loops uitgevoerd")
    st.markdown("*Gegenereerd door LangGraph + Gino d'Acampo*")


# ─────────────────────────────────────────────
# MAIN — hero + recept detail
# ─────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <h1>🍝 SousChef</h1>
    <p class="subtitle">Recepten à la Gino d'Acampo</p>
    <p class="gino-quote">"My Nona would never forgive you for using a jar of sauce."</p>
</div>
""", unsafe_allow_html=True)

# Haal het geselecteerde recept op
recept = next(r for r in recepten if r["naam"] == keuze)

# Header
st.markdown(f"""
<div class="recept-header">
    <h2>{recept["naam"]}</h2>
    <p class="beschrijving">{recept["beschrijving"]}</p>
</div>
""", unsafe_allow_html=True)

# Badges
reparaties = recept.get("reparatie_pogingen", 0)
badge_repair = f'<span class="badge">🔧 {reparaties}x gerepareerd</span>' if reparaties > 0 else '<span class="badge badge-groen">✓ Validatie geslaagd</span>'
st.markdown(f"""
<span class="badge">📋 {len(recept["ingredienten"])} ingrediënten</span>
<span class="badge">👣 {len(recept["stappen"])} stappen</span>
{badge_repair}
""", unsafe_allow_html=True)

st.markdown("<hr class='divider'>", unsafe_allow_html=True)

# Twee kolommen: ingrediënten | stappen
col1, col2 = st.columns([1, 1.8], gap="large")

with col1:
    items_html = "".join([f'<div class="ingredient-item">{ing}</div>' for ing in recept["ingredienten"]])
    st.markdown(f"""
    <div class="ingredienten-kaart">
        <h3>🛒 Wat heb je nodig?</h3>
        {items_html}
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("### 👨‍🍳 Hoe maak je het?")
    for i, stap in enumerate(recept["stappen"]):
        tekst = stap["stap"]
        tijd = stap["tijd"]

        # Detecteer Nona-opmerkingen voor speciale opmaak
        if "Nona" in tekst or "Italia" in tekst or "Bellissimo" in tekst or "Perfetto" in tekst:
            nona_split = tekst.split(". ", 1)
            if len(nona_split) == 2:
                hoofd, nona = nona_split
                st.markdown(f"""
                <div class="stap-kaart">
                    <div class="stap-nummer">{i+1}</div>
                    <div class="stap-inhoud">
                        <div class="stap-tekst">{hoofd}.</div>
                        <div class="nona-box">{nona}</div>
                        <div class="stap-tijd">{tijd}</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="stap-kaart">
                    <div class="stap-nummer">{i+1}</div>
                    <div class="stap-inhoud">
                        <div class="nona-box">{tekst}</div>
                        <div class="stap-tijd">{tijd}</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="stap-kaart">
                <div class="stap-nummer">{i+1}</div>
                <div class="stap-inhoud">
                    <div class="stap-tekst">{tekst}</div>
                    <div class="stap-tijd">{tijd}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
