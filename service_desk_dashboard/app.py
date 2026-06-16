"""
IT Service Desk Executive Dashboard - Global Service Excellence

Dashboard ejecutivo/operativo para analizar encuestas negativas del Global Service Desk,
identificar acciones de mejorar y monitorear cumplimiento de tiempos de contacto.

Autor: Senior Python Developer + Data Analyst
Versión: 1.0.0
"""

import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# Importaciones locales
from utils import (
    apply_filters, calculate_kpis, calculate_monthly_trends,
    calculate_pareto_data, calculate_heatmap_data, calculate_analyst_performance,
    calculate_sla_analysis, detect_anomalies, identify_recurring_issues,
    calculate_before_after, generate_insights, format_percentage, format_delta,
    MONTH_ORDER
)
from charts import (
    create_trend_line, create_pareto_chart, create_heatmap,
    create_analyst_bar_chart, create_sla_pie_chart, create_aging_bar,
    create_resolution_dist, create_before_after_chart, create_recurring_issues_chart,
    create_severity_distribution, create_anomaly_scatter, create_service_breakdown
)
from styles import get_main_css

# Configuración de página
st.set_page_config(
    page_title="IT Service Desk Dashboard",
    page_icon=" ",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Aplicar estilos
st.markdown(get_main_css(), unsafe_allow_html=True)


@st.cache_data
def load_cached_data():
    """Carga datos estáticos integrados en el código."""
    from static_data import TICKETS_DATA, ACTION_ITEMS_DATA
    tickets_df = pd.DataFrame(TICKETS_DATA)
    actions_df = pd.DataFrame(ACTION_ITEMS_DATA)
    return tickets_df, actions_df


def render_sidebar_filters():
    """Renderiza los filtros en el sidebar."""
    st.sidebar.markdown('<div class="filter-header">  FILTROS GLOBALES</div>', unsafe_allow_html=True)

    # Botón para resetear filtros
    if st.sidebar.button("  Resetear Filtros", use_container_width=True):
        for key in list(st.session_state.keys()):
            if key.startswith("filter_"):
                del st.session_state[key]
        st.rerun()

    st.sidebar.markdown("---")

    # Filtro de Year
    years = st.sidebar.multiselect(
        "  Year",
        options=[2024, 2023],
        default=[2024],
        key="filter_years"
    )

    # Filtro de Report Period
    months = st.sidebar.multiselect(
        "  Report Period",
        options=MONTH_ORDER,
        default=MONTH_ORDER[:6],
        key="filter_months"
    )

    # Filtro de Score
    st.sidebar.markdown("**  Score Range**")
    col1, col2 = st.sidebar.columns(2)
    with col1:
        min_score = st.number_input("Min", min_value=1.0, max_value=3.5, value=1.0, step=0.5, key="filter_min_score")
    with col2:
        max_score = st.number_input("Max", min_value=1.0, max_value=3.5, value=3.5, step=0.5, key="filter_max_score")

    # Filtro de GeoUnit
    geo_units = st.sidebar.multiselect(
        "  GeoUnit",
        options=["ECP", "ABC", "USL", "BRZ", "ACE"],
        default=["ECP", "ABC", "USL", "BRZ", "ACE"],
        key="filter_geo_units"
    )

    # Filtro de Assignment Group
    assignment_groups = st.sidebar.multiselect(
        "  Assignment Group",
        options=["GBS IT-WH-CIM", "GBS IT EH-CIM"],
        default=["GBS IT-WH-CIM", "GBS IT EH-CIM"],
        key="filter_assignment_groups"
    )

    # Filtro de Service Offering
    service_offerings = st.sidebar.multiselect(
        "  Service Offering",
        options=["Missing patches", "M365", "PC Reimage", "Printing", "MyPCP"],
        default=["Missing patches", "M365", "PC Reimage", "Printing", "MyPCP"],
        key="filter_service_offerings"
    )

    # Umbral de alerta para anomalías
    st.sidebar.markdown("---")
    st.sidebar.markdown("**  Alert Threshold**")
    anomaly_threshold = st.sidebar.slider(
        "Anomaly Sensitivity",
        min_value=1.0,
        max_value=3.0,
        value=2.0,
        step=0.1,
        key="filter_anomaly_threshold",
        help="Menor valor = más sensible a anomalías"
    )

    return {
        "years": years,
        "months": months,
        "min_score": min_score,
        "max_score": max_score,
        "geo_units": geo_units,
        "assignment_groups": assignment_groups,
        "service_offerings": service_offerings,
        "anomaly_threshold": anomaly_threshold
    }


def render_header():
    """Renderiza el encabezado principal del dashboard."""
    st.markdown("""
    <div class="dashboard-header">
        <h1>  IT Service Desk Executive Dashboard</h1>
        <p>Global Service Excellence | Negative Survey Analysis & Continuous Improvement</p>
    </div>
    """, unsafe_allow_html=True)


def render_kpi_cards(kpis: dict):
    """Renderiza las tarjetas KPI principales."""
    st.markdown('<div class="section-header">  KEY PERFORMANCE INDICATORS</div>', unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        delta_class = "negative" if kpis["mom_change"] > 0 else "positive"
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">TOTAL SURVEYS</div>
            <div class="kpi-value">{kpis['total_surveys']}</div>
            <div class="kpi-delta neutral">Period Total</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="kpi-card warning">
            <div class="kpi-label">NEGATIVE SURVEYS</div>
            <div class="kpi-value">{kpis['negative_surveys']}</div>
            <div class="kpi-delta {delta_class}">{kpis['mom_change']:+.1f}% vs prev month</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="kpi-card accent">
            <div class="kpi-label">NEGATIVE RATE</div>
            <div class="kpi-value">{kpis['negative_rate']:.1f}%</div>
            <div class="kpi-delta neutral">of total surveys</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        breach_class = "warning" if kpis['sla_breach_pct'] > 20 else "accent"
        st.markdown(f"""
        <div class="kpi-card {breach_class}">
            <div class="kpi-label">SLA BREACH %</div>
            <div class="kpi-value">{kpis['sla_breach_pct']:.1f}%</div>
            <div class="kpi-delta negative">above target</div>
        </div>
        """, unsafe_allow_html=True)

    # Segunda fila de KPIs
    col5, col6, col7, col8 = st.columns(4)

    with col5:
        overdue_class = "warning" if kpis['overdue_actions'] > 5 else "success"
        st.markdown(f"""
        <div class="kpi-card {overdue_class}">
            <div class="kpi-label">OVERDUE ACTIONS</div>
            <div class="kpi-value">{kpis['overdue_actions']}</div>
            <div class="kpi-delta negative">require attention</div>
        </div>
        """, unsafe_allow_html=True)

    with col6:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">CIM %</div>
            <div class="kpi-value">{kpis['cim_pct']:.1f}%</div>
            <div class="kpi-delta neutral">Team avg: {kpis['team_avg_cim']:.1f}%</div>
        </div>
        """, unsafe_allow_html=True)

    with col7:
        st.markdown(f"""
        <div class="kpi-card success">
            <div class="kpi-label">COMPLETION RATE</div>
            <div class="kpi-value">{kpis['completion_rate']:.1f}%</div>
            <div class="kpi-delta positive">action items completed</div>
        </div>
        """, unsafe_allow_html=True)

    with col8:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">ANALYSTS ABOVE AVG</div>
            <div class="kpi-value">{kpis['analysts_above_avg']}</div>
            <div class="kpi-delta neutral">need coaching</div>
        </div>
        """, unsafe_allow_html=True)


def render_trends_section(df: pd.DataFrame, threshold: float):
    """Renderiza la sección de tendencias."""
    st.markdown('<div class="section-header">  TRENDS & VARIATION</div>', unsafe_allow_html=True)

    monthly_data = calculate_monthly_trends(df)
    anomaly_data = detect_anomalies(df, threshold)

    col1, col2 = st.columns([2, 1])

    with col1:
        fig_trend = create_trend_line(anomaly_data if not anomaly_data.empty else monthly_data)
        st.plotly_chart(fig_trend, use_container_width=True)

    with col2:
        st.markdown("**Monthly Variation**")
        if not monthly_data.empty:
            for _, row in monthly_data.iterrows():
                delta = row["negative_pct_change"]
                icon = " " if delta > 0 else " " if delta < 0 else "➡️"
                color = "#FF6B6B" if delta > 0 else "#4CAF50" if delta < 0 else "#696969"
                st.markdown(f"""
                <div style="display:flex; justify-content:space-between; padding:0.3rem 0; border-bottom:1px solid #f0f0f0;">
                    <span>{row['report_period_month']}</span>
                    <span style="color:{color}; font-weight:600;">{icon} {delta:+.1f}%</span>
                </div>
                """, unsafe_allow_html=True)

    # Alertas de incremento significativo
    if not anomaly_data.empty:
        anomalies = anomaly_data[anomaly_data["is_anomaly"]]
        if not anomalies.empty:
            st.markdown(f"""
            <div class="alert alert-danger">
                <strong>  Anomaly Detected!</strong>
                Significant spike in negative surveys detected in: {', '.join(anomalies['report_period_month'].tolist())}
            </div>
            """, unsafe_allow_html=True)


def render_pareto_section(df: pd.DataFrame):
    """Renderiza la sección de Pareto / Top Drivers."""
    st.markdown('<div class="section-header">  TOP DRIVERS - PARETO ANALYSIS</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**By Category**")
        pareto_category = calculate_pareto_data(df, "category")
        if not pareto_category.empty:
            fig_pareto_cat = create_pareto_chart(pareto_category, "Category Pareto")
            st.plotly_chart(fig_pareto_cat, use_container_width=True)

    with col2:
        st.markdown("**By Service Offering**")
        pareto_offering = calculate_pareto_data(df, "service_offering")
        if not pareto_offering.empty:
            fig_pareto_off = create_pareto_chart(pareto_offering, "Service Offering Pareto")
            st.plotly_chart(fig_pareto_off, use_container_width=True)

    # Tabla de ranking
    st.markdown("**Ranking by Volume & Severity**")
    ranking = df.groupby(["category", "severity"]).agg(
        count=("ticket_id", "count"),
        avg_impact=("impact", "mean")
    ).reset_index().sort_values("count", ascending=False).head(10)

    st.dataframe(ranking, use_container_width=True, hide_index=True)


def render_heatmap_section(df: pd.DataFrame):
    """Renderiza la sección de heatmap CSAT."""
    st.markdown('<div class="section-header">  CSAT CORRELATION MATRIX</div>', unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])

    with col1:
        heatmap_data = calculate_heatmap_data(df)
        if not heatmap_data.empty:
            fig_heatmap = create_heatmap(heatmap_data)
            st.plotly_chart(fig_heatmap, use_container_width=True)

    with col2:
        st.markdown("**Score Distribution by Category**")
        if not df.empty:
            category_scores = df.groupby("category")["score"].mean().sort_values()
            for cat, score in category_scores.items():
                color = "#FF6B6B" if score < 2.0 else "#FFB74D" if score < 2.5 else "#4CAF50"
                st.markdown(f"""
                <div style="display:flex; justify-content:space-between; padding:0.4rem 0; border-bottom:1px solid #f0f0f0;">
                    <span>{cat}</span>
                    <span style="color:{color}; font-weight:600;">{score:.2f}</span>
                </div>
                """, unsafe_allow_html=True)

    # Drill-down selector
    st.markdown("**  Drill-Down: Select Category to View Tickets**")
    selected_category = st.selectbox("Select Category", options=["All"] + list(df["category"].unique()))

    if selected_category != "All":
        filtered_df = df[df["category"] == selected_category]
        st.dataframe(
            filtered_df[["ticket_id", "incident_id", "service_offering", "subcategory", "score", "severity", "analyst"]],
            use_container_width=True,
            hide_index=True
        )


def render_action_tracker(actions_df: pd.DataFrame, tickets_df: pd.DataFrame):
    """Renderiza la sección de action items tracker."""
    st.markdown('<div class="section-header">  ACTION ITEMS TRACKER</div>', unsafe_allow_html=True)

    if actions_df.empty:
        st.warning("No action items available.")
        return

    # Resumen de status
    col1, col2, col3, col4 = st.columns(4)

    status_counts = actions_df["status"].value_counts()

    with col1:
        completed = status_counts.get("Completed", 0)
        st.markdown(f"""
        <div class="kpi-card success">
            <div class="kpi-label">COMPLETED</div>
            <div class="kpi-value">{completed}</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        in_progress = status_counts.get("In Progress", 0)
        st.markdown(f"""
        <div class="kpi-card accent">
            <div class="kpi-label">IN PROGRESS</div>
            <div class="kpi-value">{in_progress}</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        pending = status_counts.get("Pending", 0)
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">PENDING</div>
            <div class="kpi-value">{pending}</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        overdue = status_counts.get("Overdue", 0)
        st.markdown(f"""
        <div class="kpi-card warning">
            <div class="kpi-label">OVERDUE</div>
            <div class="kpi-value">{overdue}</div>
        </div>
        """, unsafe_allow_html=True)

    # Tabla detallada con highlights
    st.markdown("**Detailed Action Items**")

    # Merge con tickets para contexto
    merged = actions_df.merge(
        tickets_df[["ticket_id", "category", "service_offering", "score"]],
        left_on="linked_ticket_id",
        right_on="ticket_id",
        how="left"
    )

    # Aplicar estilos condicionales
    def highlight_overdue(row):
        if row.get("status") == "Overdue":
            return ["background-color: #FFE8E8"] * len(row)
        elif row.get("status") == "Completed":
            return ["background-color: #E8F5E9"] * len(row)
        return [""] * len(row)

    styled_df = merged.style.apply(highlight_overdue, axis=1)
    st.dataframe(styled_df, use_container_width=True, hide_index=True)


def render_cim_analysis(df: pd.DataFrame):
    """Renderiza la sección de análisis CIM por analista."""
    st.markdown('<div class="section-header">  CIM ANALYSIS BY ANALYST</div>', unsafe_allow_html=True)

    performance = calculate_analyst_performance(df)

    col1, col2 = st.columns([2, 1])

    with col1:
        if not performance.empty:
            fig_cim = create_analyst_bar_chart(performance)
            st.plotly_chart(fig_cim, use_container_width=True)

    with col2:
        st.markdown("**Analyst Performance Details**")
        if not performance.empty:
            for _, row in performance.iterrows():
                vs_avg = row["vs_team_avg"]
                icon = " " if vs_avg > 0 else " " if vs_avg < 0 else "➡️"
                color = "#FF6B6B" if vs_avg > 0 else "#4CAF50" if vs_avg < 0 else "#696969"
                st.markdown(f"""
                <div style="padding:0.5rem; margin:0.3rem 0; background:{'#FFF3E0' if vs_avg > 0 else '#E8F5E9' if vs_avg < 0 else '#F5F5F5'}; border-radius:6px;">
                    <strong>{row['analyst']}</strong><br>
                    <span style="font-size:0.9rem;">CIM: {row['cim_pct']:.1f}% {icon} {vs_avg:+.1f}% vs avg</span>
                </div>
                """, unsafe_allow_html=True)


def render_sla_section(df: pd.DataFrame):
    """Renderiza la sección de análisis SLA."""
    st.markdown('<div class="section-header">  SLA & RESOLUTION ANALYSIS</div>', unsafe_allow_html=True)

    sla_data = calculate_sla_analysis(df)

    col1, col2, col3 = st.columns(3)

    with col1:
        if sla_data:
            fig_pie = create_sla_pie_chart(sla_data)
            st.plotly_chart(fig_pie, use_container_width=True)

    with col2:
        if sla_data and "aging_distribution" in sla_data:
            fig_aging = create_aging_bar(sla_data["aging_distribution"])
            st.plotly_chart(fig_aging, use_container_width=True)

    with col3:
        if not df.empty:
            fig_dist = create_resolution_dist(df)
            st.plotly_chart(fig_dist, use_container_width=True)

    # Breach details
    if sla_data and sla_data.get("breached", 0) > 0:
        breached_tickets = df[df["breached_flag"] == True]
        st.markdown(f"""
        <div class="alert alert-warning">
            <strong>⚠️ SLA Breach Alert:</strong> {sla_data['breached']} tickets exceeded SLA target. 
            Average resolution time: {sla_data['resolution_stats']['avg_resolution_time']:.1f} hours.
        </div>
        """, unsafe_allow_html=True)

        st.dataframe(
            breached_tickets[["ticket_id", "category", "service_offering", "resolution_time_hours", "sla_target_hours", "severity"]],
            use_container_width=True,
            hide_index=True
        )


def render_insights_panel(insights: list):
    """Renderiza el panel de insights automáticos."""
    st.markdown('<div class="section-header">  KEY INSIGHTS & RECOMMENDATIONS</div>', unsafe_allow_html=True)

    for i, insight in enumerate(insights):
        st.markdown(f"""
        <div class="insight-card">
            <div class="insight-title">Insight #{i+1}</div>
            <div style="color:#333;">{insight}</div>
        </div>
        """, unsafe_allow_html=True)


def render_anomaly_section(df: pd.DataFrame, threshold: float):
    """Renderiza la sección de detección de anomalías."""
    st.markdown('<div class="section-header">  ANOMALY DETECTION</div>', unsafe_allow_html=True)

    anomaly_data = detect_anomalies(df, threshold)

    if not anomaly_data.empty:
        col1, col2 = st.columns([2, 1])

        with col1:
            fig_anomaly = create_anomaly_scatter(anomaly_data)
            st.plotly_chart(fig_anomaly, use_container_width=True)

        with col2:
            anomalies = anomaly_data[anomaly_data["is_anomaly"]]
            if not anomalies.empty:
                st.markdown("""
                <div class="alert alert-danger">
                    <strong>  Detected Anomalies</strong>
                </div>
                """, unsafe_allow_html=True)

                for _, anomaly in anomalies.iterrows():
                    st.markdown(f"""
                    <div style="padding:0.5rem; margin:0.3rem 0; background:#FFE8E8; border-radius:6px; border-left:3px solid #F44336;">
                        <strong>{anomaly['report_period_month']}</strong><br>
                        <span>{anomaly['negative_tickets']} negative surveys (Z-score: {anomaly['z_score']:.2f})</span>
                    </div>
                    """, unsafe_allow_html=True)
            else:
                st.markdown("""
                <div class="alert alert-success">
                    <strong>✅ No anomalies detected</strong> based on current threshold.
                </div>
                """, unsafe_allow_html=True)
    else:
        st.info("Insufficient data for anomaly detection.")


def render_recurring_issues(df: pd.DataFrame):
    """Renderiza la sección de issues recurrentes."""
    st.markdown('<div class="section-header">  RECURRING ISSUES ANALYSIS</div>', unsafe_allow_html=True)

    recurring = identify_recurring_issues(df, min_months=2)

    if not recurring.empty:
        col1, col2 = st.columns([2, 1])

        with col1:
            fig_recurring = create_recurring_issues_chart(recurring)
            st.plotly_chart(fig_recurring, use_container_width=True)

        with col2:
            st.markdown("**Persistent Issues**")
            for _, issue in recurring.iterrows():
                st.markdown(f"""
                <div style="padding:0.5rem; margin:0.3rem 0; background:#E3F2FD; border-radius:6px; border-left:3px solid #0014DC;">
                    <strong>{issue['category']}</strong> - {issue['service_offering']}<br>
                    <span style="color:#696969;">Present in {issue['months_count']} months</span>
                </div>
                """, unsafe_allow_html=True)
    else:
        st.info("No recurring issues detected (issues present in 2+ months).")


def render_before_after_section(df: pd.DataFrame, actions_df: pd.DataFrame):
    """Renderiza la sección de before vs after."""
    st.markdown('<div class="section-header">  BEFORE vs AFTER ANALYSIS</div>', unsafe_allow_html=True)

    before_after = calculate_before_after(df)

    if before_after:
        col1, col2 = st.columns([2, 1])

        with col1:
            fig_ba = create_before_after_chart(before_after)
            st.plotly_chart(fig_ba, use_container_width=True)

        with col2:
            st.markdown("**Implementation Impact**")

            # Calcular mejoras
            count_change = before_after["after_count"] - before_after["before_count"]
            score_change = before_after["after_avg_score"] - before_after["before_avg_score"]
            sla_change = before_after["after_sla_breach"] - before_after["before_sla_breach"]

            metrics = [
                ("Ticket Count", before_after["before_count"], before_after["after_count"], count_change, False),
                ("Avg Score", before_after["before_avg_score"], before_after["after_avg_score"], score_change, False),
                ("SLA Breach %", before_after["before_sla_breach"], before_after["after_sla_breach"], sla_change, True)
            ]

            for name, before_val, after_val, change, inverse in metrics:
                if inverse:
                    color = "#4CAF50" if change < 0 else "#FF6B6B" if change > 0 else "#696969"
                    icon = " " if change < 0 else " " if change > 0 else "➡️"
                else:
                    color = "#4CAF50" if change < 0 else "#FF6B6B" if change > 0 else "#696969"
                    icon = " " if change < 0 else " " if change > 0 else "➡️"

                st.markdown(f"""
                <div style="display:flex; justify-content:space-between; padding:0.5rem; margin:0.3rem 0; background:#F5F5F5; border-radius:6px;">
                    <span>{name}</span>
                    <span>
                        <span style="color:#696969;">{before_val:.1f}</span> → 
                        <span style="color:#333; font-weight:600;">{after_val:.1f}</span>
                        <span style="color:{color}; margin-left:0.5rem;">{icon} {change:+.1f}</span>
                    </span>
                </div>
                """, unsafe_allow_html=True)
    else:
        st.info("Insufficient data for before/after comparison.")


def render_detail_table(df: pd.DataFrame):
    """Renderiza la tabla detallada de tickets."""
    st.markdown('<div class="section-header">  DETAILED TICKET VIEW</div>', unsafe_allow_html=True)

    # Filtros adicionales para drill-down
    col1, col2, col3 = st.columns(3)

    with col1:
        detail_category = st.selectbox("Filter by Category", ["All"] + list(df["category"].unique()), key="detail_cat")

    with col2:
        detail_severity = st.selectbox("Filter by Severity", ["All"] + list(df["severity"].unique()), key="detail_sev")

    with col3:
        detail_analyst = st.selectbox("Filter by Analyst", ["All"] + list(df["analyst"].unique()), key="detail_analyst")

    # Aplicar filtros
    filtered_df = df.copy()
    if detail_category != "All":
        filtered_df = filtered_df[filtered_df["category"] == detail_category]
    if detail_severity != "All":
        filtered_df = filtered_df[filtered_df["severity"] == detail_severity]
    if detail_analyst != "All":
        filtered_df = filtered_df[filtered_df["analyst"] == detail_analyst]

    # Mostrar tabla con estilos
    st.markdown(f"**Showing {len(filtered_df)} records**")

    if not filtered_df.empty:
        # Seleccionar columnas relevantes
        display_cols = [
            "ticket_id", "incident_id", "created_date", "analyst", "geo_unit",
            "service_offering", "category", "subcategory", "score", "severity",
            "resolution_time_hours", "sla_status", "cim_flag", "customer_comment"
        ]

        styled_detail = filtered_df[display_cols].style.apply(
            lambda row: ["background-color: #FFE8E8" if row.get("sla_status") == "Breached" else "" for _ in row],
            axis=1
        )

        st.dataframe(styled_detail, use_container_width=True, hide_index=True)
    else:
        st.warning("No records match the selected filters.")


def render_service_segmentation(df: pd.DataFrame):
    """Renderiza la sección de segmentación por dimensiones operativas."""
    st.markdown('<div class="section-header">  SERVICE SEGMENTATION</div>', unsafe_allow_html=True)

    if not df.empty:
        fig_breakdown = create_service_breakdown(df)
        st.plotly_chart(fig_breakdown, use_container_width=True)

        # Severity distribution
        col1, col2 = st.columns(2)

        with col1:
            fig_severity = create_severity_distribution(df)
            st.plotly_chart(fig_severity, use_container_width=True)

        with col2:
            st.markdown("**Segment Summary**")
            segment_summary = df.groupby("service_offering").agg(
                tickets=("ticket_id", "count"),
                avg_score=("score", "mean"),
                breach_rate=("breached_flag", "mean")
            ).round(2)
            segment_summary["breach_rate"] = (segment_summary["breach_rate"] * 100).round(1)

            st.dataframe(segment_summary, use_container_width=True)


def main():
    """Función principal del dashboard."""
    # Cargar datos
    tickets_df, actions_df = load_cached_data()

    # Renderizar header
    render_header()

    # Renderizar filtros
    filters = render_sidebar_filters()

    # Aplicar filtros al dataset
    filtered_tickets = apply_filters(tickets_df, filters)

    if filtered_tickets.empty:
        st.warning("No data matches the selected filters. Please adjust your selection.")
        st.stop()

    # Calcular KPIs
    kpis = calculate_kpis(filtered_tickets, actions_df)

    # Renderizar KPIs
    render_kpi_cards(kpis)

    st.markdown('<hr class="section-divider">', unsafe_allow_html=True)

    # Sección de tendencias
    render_trends_section(filtered_tickets, filters["anomaly_threshold"])

    st.markdown('<hr class="section-divider">', unsafe_allow_html=True)

    # Top Drivers / Pareto
    render_pareto_section(filtered_tickets)

    st.markdown('<hr class="section-divider">', unsafe_allow_html=True)

    # Heatmap CSAT
    render_heatmap_section(filtered_tickets)

    st.markdown('<hr class="section-divider">', unsafe_allow_html=True)

    # Action Tracker
    render_action_tracker(actions_df, tickets_df)

    st.markdown('<hr class="section-divider">', unsafe_allow_html=True)

    # CIM Analysis
    render_cim_analysis(filtered_tickets)

    st.markdown('<hr class="section-divider">', unsafe_allow_html=True)

    # SLA Analysis
    render_sla_section(filtered_tickets)

    st.markdown('<hr class="section-divider">', unsafe_allow_html=True)

    # Key Insights
    insights = generate_insights(filtered_tickets, actions_df)
    render_insights_panel(insights)

    st.markdown('<hr class="section-divider">', unsafe_allow_html=True)

    # Anomaly Detection
    render_anomaly_section(filtered_tickets, filters["anomaly_threshold"])

    st.markdown('<hr class="section-divider">', unsafe_allow_html=True)

    # Recurring Issues
    render_recurring_issues(filtered_tickets)

    st.markdown('<hr class="section-divider">', unsafe_allow_html=True)

    # Before vs After
    render_before_after_section(filtered_tickets, actions_df)

    st.markdown('<hr class="section-divider">', unsafe_allow_html=True)

    # Service Segmentation
    render_service_segmentation(filtered_tickets)

    st.markdown('<hr class="section-divider">', unsafe_allow_html=True)

    # Detail View / Drill-Down
    render_detail_table(filtered_tickets)

    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align:center; color:#696969; padding:1rem;">
        <p>IT Service Desk Executive Dashboard | Global Service Excellence</p>
        <p style="font-size:0.8rem;">Data refreshed: {} | Version 1.0.0</p>
    </div>
    """.format(datetime.now().strftime("%Y-%m-%d %H:%M")), unsafe_allow_html=True)


if __name__ == "__main__":
    main()
