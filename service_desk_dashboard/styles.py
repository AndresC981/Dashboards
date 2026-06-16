"""
Styles - CSS personalizado para el dashboard de Service Desk.

Define estilos consistentes usando la paleta de colores corporativa.
"""

# Paleta de colores
COLORS = {
    "primary": "#0014DC",
    "white": "#FFFFFF",
    "accent": "#00D2DC",
    "dark": "#051464",
    "medium_blue": "#6E8CC8",
    "light_blue": "#AFBEE1",
    "light_gray": "#F0F0F0",
    "border": "#DCE1E1",
    "gray": "#C8CDCD",
    "medium_gray": "#AAAAAA",
    "dark_gray": "#696969",
    "black": "#000000"
}


def get_main_css() -> str:
    """Retorna CSS principal para el dashboard."""
    return f"""
    <style>
    /* ============================================
       GLOBAL STYLES
       ============================================ */
    
    .stApp {{
        background-color: {COLORS["light_gray"]};
    }}
    
    .main .block-container {{
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1200px;
    }}
    
    /* ============================================
       HEADER STYLES
       ============================================ */
    
    .dashboard-header {{
        background: linear-gradient(135deg, {COLORS["dark"]} 0%, {COLORS["primary"]} 100%);
        color: {COLORS["white"]};
        padding: 1.5rem 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }}
    
    .dashboard-header h1 {{
        margin: 0;
        font-size: 1.8rem;
        font-weight: 700;
    }}
    
    .dashboard-header p {{
        margin: 0.5rem 0 0 0;
        opacity: 0.9;
        font-size: 0.95rem;
    }}
    
    /* ============================================
       KPI CARD STYLES
       ============================================ */
    
    .kpi-card {{
        background: {COLORS["white"]};
        border-radius: 12px;
        padding: 1.2rem;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
        border-left: 4px solid {COLORS["primary"]};
        transition: transform 0.2s ease;
        height: 100%;
    }}
    
    .kpi-card:hover {{
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    }}
    
    .kpi-card.accent {{
        border-left-color: {COLORS["accent"]};
    }}
    
    .kpi-card.warning {{
        border-left-color: #FF6B6B;
    }}
    
    .kpi-card.success {{
        border-left-color: #4CAF50;
    }}
    
    .kpi-label {{
        font-size: 0.8rem;
        color: {COLORS["dark_gray"]};
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 0.3rem;
    }}
    
    .kpi-value {{
        font-size: 1.8rem;
        font-weight: 700;
        color: {COLORS["dark"]};
        margin: 0;
    }}
    
    .kpi-delta {{
        font-size: 0.85rem;
        margin-top: 0.3rem;
    }}
    
    .kpi-delta.positive {{
        color: #4CAF50;
    }}
    
    .kpi-delta.negative {{
        color: #FF6B6B;
    }}
    
    .kpi-delta.neutral {{
        color: {COLORS["medium_gray"]};
    }}
    
    /* ============================================
       SECTION STYLES
       ============================================ */
    
    .section-header {{
        background: {COLORS["white"]};
        color: {COLORS["dark"]};
        padding: 0.8rem 1.2rem;
        border-radius: 8px;
        margin: 1.5rem 0 1rem 0;
        border-left: 4px solid {COLORS["primary"]};
        font-weight: 600;
    }}
    
    .section-divider {{
        border: none;
        border-top: 1px solid {COLORS["border"]};
        margin: 2rem 0;
    }}
    
    /* ============================================
       TABLE STYLES
       ============================================ */
    
    .styled-table {{
        width: 100%;
        border-collapse: collapse;
        background: {COLORS["white"]};
        border-radius: 10px;
        overflow: hidden;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
    }}
    
    .styled-table thead tr {{
        background: {COLORS["dark"]};
        color: {COLORS["white"]};
        text-align: left;
    }}
    
    .styled-table th,
    .styled-table td {{
        padding: 0.8rem 1rem;
    }}
    
    .styled-table tbody tr {{
        border-bottom: 1px solid {COLORS["border"]};
    }}
    
    .styled-table tbody tr:nth-of-type(even) {{
        background-color: {COLORS["light_gray"]};
    }}
    
    .styled-table tbody tr:hover {{
        background-color: {COLORS["light_blue"]};
    }}
    
    /* ============================================
       BADGE STYLES
       ============================================ */
    
    .badge {{
        display: inline-block;
        padding: 0.25rem 0.6rem;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 600;
        text-transform: uppercase;
    }}
    
    .badge-danger {{
        background: #FFE8E8;
        color: #D32F2F;
    }}
    
    .badge-warning {{
        background: #FFF3E0;
        color: #F57C00;
    }}
    
    .badge-success {{
        background: #E8F5E9;
        color: #388E3C;
    }}
    
    .badge-info {{
        background: #E3F2FD;
        color: {COLORS["primary"]};
    }}
    
    /* ============================================
       ALERT STYLES
       ============================================ */
    
    .alert {{
        padding: 1rem 1.2rem;
        border-radius: 8px;
        margin: 1rem 0;
        display: flex;
        align-items: center;
        gap: 0.8rem;
    }}
    
    .alert-warning {{
        background: #FFF3E0;
        border-left: 4px solid #FF9800;
        color: #E65100;
    }}
    
    .alert-danger {{
        background: #FFEBEE;
        border-left: 4px solid #F44336;
        color: #B71C1C;
    }}
    
    .alert-success {{
        background: #E8F5E9;
        border-left: 4px solid #4CAF50;
        color: #1B5E20;
    }}
    
    .alert-info {{
        background: #E3F2FD;
        border-left: 4px solid {COLORS["primary"]};
        color: {COLORS["dark"]};
    }}
    
    /* ============================================
       SIDEBAR STYLES
       ============================================ */
    
    .sidebar .sidebar-content {{
        background: {COLORS["white"]};
    }}
    
    .filter-header {{
        background: {COLORS["dark"]};
        color: {COLORS["white"]};
        padding: 0.8rem 1rem;
        border-radius: 8px;
        margin-bottom: 1rem;
        font-weight: 600;
    }}
    
    /* ============================================
       INSIGHT CARD STYLES
       ============================================ */
    
    .insight-card {{
        background: {COLORS["white"]};
        border-radius: 10px;
        padding: 1rem;
        margin: 0.5rem 0;
        border-left: 3px solid {COLORS["accent"]};
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.04);
    }}
    
    .insight-card .insight-title {{
        font-weight: 600;
        color: {COLORS["dark"]};
        margin-bottom: 0.3rem;
    }}
    
    .insight-card .insight-value {{
        color: {COLORS["primary"]};
        font-size: 1.1rem;
        font-weight: 700;
    }}
    
    /* ============================================
       CHART CONTAINER STYLES
       ============================================ */
    
    .chart-container {{
        background: {COLORS["white"]};
        border-radius: 12px;
        padding: 1rem;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
        margin: 1rem 0;
    }}
    
    /* ============================================
       TAB STYLES
       ============================================ */
    
    .stTabs [data-baseweb="tab-list"] {{
        gap: 8px;
        background: {COLORS["light_gray"]};
        padding: 0.5rem;
        border-radius: 10px;
    }}
    
    .stTabs [data-baseweb="tab"] {{
        background: {COLORS["white"]};
        border-radius: 8px;
        padding: 0.5rem 1rem;
        font-weight: 500;
    }}
    
    .stTabs [aria-selected="true"] {{
        background: {COLORS["primary"]};
        color: {COLORS["white"]};
    }}
    
    /* ============================================
       EXPANDER STYLES
       ============================================ */
    
    .streamlit-expanderHeader {{
        background: {COLORS["light_gray"]};
        border-radius: 8px;
        font-weight: 600;
    }}
    
    /* ============================================
       METRIC STYLES
       ============================================ */
    
    [data-testid="stMetric"] {{
        background: {COLORS["white"]};
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.04);
    }}
    
    [data-testid="stMetricLabel"] {{
        color: {COLORS["dark_gray"]};
        font-size: 0.85rem;
    }}
    
    [data-testid="stMetricValue"] {{
        color: {COLORS["dark"]};
        font-weight: 700;
    }}
    
    /* ============================================
       RESPONSIVE ADJUSTMENTS
       ============================================ */
    
    @media (max-width: 768px) {{
        .kpi-value {{
            font-size: 1.4rem;
        }}
        
        .dashboard-header h1 {{
            font-size: 1.4rem;
        }}
    }}
    </style>
    """
