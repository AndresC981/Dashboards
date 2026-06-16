"""
Chart Functions - Visualizaciones Plotly para el dashboard de Service Desk.

Contiene todas las funciones para crear gráficos interactivos usando Plotly.
"""

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np
from typing import Dict, Optional
from utils import COLORS, MONTH_ORDER


# Configuración de Layout
BASE_LAYOUT = {
    "plot_bgcolor": COLORS["white"],
    "paper_bgcolor": COLORS["white"],
    "font": {"family": "Arial, sans-serif", "color": COLORS["dark"]},
    "margin": {"l": 40, "r": 20, "t": 50, "b": 40}
}


def create_trend_line(monthly_data: pd.DataFrame) -> go.Figure:
    """Crea gráfico de línea de tendencia mensual."""
    if monthly_data.empty:
        return go.Figure().update_layout(title="Sin datos disponibles")

    fig = make_subplots(specs=[[{"secondary_y": True}]])

    # Línea de encuestas negativas
    fig.add_trace(
        go.Scatter(
            x=monthly_data["report_period_month"],
            y=monthly_data["negative_tickets"],
            name="Negative Surveys",
            line=dict(color=COLORS["primary"], width=3),
            mode="lines+markers",
            marker=dict(size=8)
        ),
        secondary_y=False
    )

    # Línea de score promedio
    fig.add_trace(
        go.Scatter(
            x=monthly_data["report_period_month"],
            y=monthly_data["avg_score"],
            name="Avg Score",
            line=dict(color=COLORS["accent"], width=2, dash="dash"),
            mode="lines+markers",
            marker=dict(size=6)
        ),
        secondary_y=True
    )

    # Marcadores de anomalías si existen
    if "is_anomaly" in monthly_data.columns:
        anomalies = monthly_data[monthly_data["is_anomaly"]]
        if not anomalies.empty:
            fig.add_trace(
                go.Scatter(
                    x=anomalies["report_period_month"],
                    y=anomalies["negative_tickets"],
                    name="Anomaly",
                    mode="markers",
                    marker=dict(color="red", size=12, symbol="x")
                ),
                secondary_y=False
            )

    fig.update_xaxes(title_text="Month")
    fig.update_yaxes(title_text="Negative Surveys", secondary_y=False)
    fig.update_yaxes(title_text="Avg Score", secondary_y=True)

    fig.update_layout(
        **BASE_LAYOUT,
        title="Negative Surveys Trend",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    fig.update_xaxes(categoryorder="array", categoryarray=MONTH_ORDER)

    return fig


def create_pareto_chart(pareto_data: pd.DataFrame, title: str = "Pareto Chart") -> go.Figure:
    """Crea diagrama de Pareto."""
    if pareto_data.empty:
        return go.Figure().update_layout(title="Sin datos disponibles")

    fig = make_subplots(specs=[[{"secondary_y": True}]])

    # Barras de frecuencia
    fig.add_trace(
        go.Bar(
            x=pareto_data.iloc[:, 0],
            y=pareto_data["count"],
            name="Count",
            marker_color=COLORS["primary"]
        ),
        secondary_y=False
    )

    # Línea de acumulación
    fig.add_trace(
        go.Scatter(
            x=pareto_data.iloc[:, 0],
            y=pareto_data["cumulative_pct"],
            name="Cumulative %",
            line=dict(color=COLORS["accent"], width=3),
            mode="lines+markers"
        ),
        secondary_y=True
    )

    # Línea del 80%
    fig.add_hline(y=80, line_dash="dash", line_color="gray",
                  annotation_text="80% Threshold", secondary_y=True)

    fig.update_xaxes(title_text="Category")
    fig.update_yaxes(title_text="Count", secondary_y=False)
    fig.update_yaxes(title_text="Cumulative %", secondary_y=True, range=[0, 105])

    fig.update_layout(
        **BASE_LAYOUT,
        title=title,
        showlegend=True,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )

    return fig


def create_heatmap(heatmap_data: pd.DataFrame) -> go.Figure:
    """Crea heatmap de CSAT score promedio."""
    if heatmap_data.empty:
        return go.Figure().update_layout(title="Sin datos disponibles")

    fig = go.Figure(data=go.Heatmap(
        z=heatmap_data.values,
        x=heatmap_data.columns.tolist(),
        y=heatmap_data.index.tolist(),
        colorscale=[
            [0, COLORS["primary"]],
            [0.5, COLORS["light_blue"]],
            [1, COLORS["accent"]]
        ],
        text=heatmap_data.values.round(2),
        texttemplate="%{text}",
        textfont={"size": 12}
    ))

    fig.update_layout(
        **BASE_LAYOUT,
        title="CSAT Score Heatmap: Category vs Service Offering",
        xaxis_title="Service Offering",
        yaxis_title="Category"
    )

    return fig


def create_analyst_bar_chart(performance_data: pd.DataFrame) -> go.Figure:
    """Crea gráfico de barras de rendimiento por analista."""
    if performance_data.empty:
        return go.Figure().update_layout(title="Sin datos disponibles")

    colors = [COLORS["accent"] if v > 0 else COLORS["primary"]
              for v in performance_data["vs_team_avg"]]

    fig = go.Figure(data=[
        go.Bar(
            x=performance_data["analyst"],
            y=performance_data["cim_pct"],
            name="CIM %",
            marker_color=colors,
            text=performance_data["cim_pct"].apply(lambda x: f"{x:.1f}%"),
            textposition="auto"
        )
    ])

    # Línea de promedio del equipo
    avg_cim = performance_data["cim_pct"].mean()
    fig.add_hline(y=avg_cim, line_dash="dash", line_color=COLORS["dark"],
                  annotation_text=f"Team Avg: {avg_cim:.1f}%")

    fig.update_layout(
        **BASE_LAYOUT,
        title="CIM % by Analyst vs Team Average",
        xaxis_title="Analyst",
        yaxis_title="CIM %",
        yaxis_range=[0, max(performance_data["cim_pct"]) * 1.2]
    )

    return fig


def create_sla_pie_chart(sla_data: Dict) -> go.Figure:
    """Crea gráfico de torta para SLA compliance."""
    if not sla_data:
        return go.Figure().update_layout(title="Sin datos disponibles")

    labels = ["Within Target", "Breached"]
    values = [sla_data["within_target"], sla_data["breached"]]
    colors = [COLORS["accent"], COLORS["primary"]]

    fig = go.Figure(data=[go.Pie(
        labels=labels,
        values=values,
        marker=dict(colors=colors),
        hole=0.4,
        textinfo="label+percent"
    )])

    fig.update_layout(
        **BASE_LAYOUT,
        title="SLA Compliance",
        annotations=[dict(text=f"{sla_data['breach_pct']}%", x=0.5, y=0.5,
                         font_size=20, showarrow=False)]
    )

    return fig


def create_aging_bar(aging_data: Dict) -> go.Figure:
    """Crea gráfico de barras para aging analysis."""
    if not aging_data:
        return go.Figure().update_layout(title="Sin datos disponibles")

    # Ordenar buckets
    bucket_order = ["0-3 days", "4-7 days", "8-14 days", "15-30 days", "30+ days"]
    sorted_buckets = [b for b in bucket_order if b in aging_data]
    values = [aging_data[b] for b in sorted_buckets]

    colors = [COLORS["accent"] if "0-3" in b or "4-7" in b else
              COLORS["medium_blue"] if "8-14" in b else
              COLORS["primary"] for b in sorted_buckets]

    fig = go.Figure(data=[go.Bar(
        x=sorted_buckets,
        y=values,
        marker_color=colors,
        text=values,
        textposition="auto"
    )])

    fig.update_layout(
        **BASE_LAYOUT,
        title="Aging Analysis",
        xaxis_title="Aging Bucket",
        yaxis_title="Count"
    )

    return fig


def create_resolution_dist(df: pd.DataFrame) -> go.Figure:
    """Crea histograma de distribución de tiempos de resolución."""
    if df.empty:
        return go.Figure().update_layout(title="Sin datos disponibles")

    fig = go.Figure(data=[
        go.Histogram(
            x=df["resolution_time_hours"],
            nbinsx=15,
            marker_color=COLORS["primary"],
            opacity=0.7
        )
    ])

    # Línea de target promedio
    avg_target = df["sla_target_hours"].mean()
    fig.add_vline(x=avg_target, line_dash="dash", line_color=COLORS["accent"],
                  annotation_text=f"Avg Target: {avg_target:.0f}h")

    fig.update_layout(
        **BASE_LAYOUT,
        title="Resolution Time Distribution",
        xaxis_title="Resolution Time (Hours)",
        yaxis_title="Count"
    )

    return fig


def create_before_after_chart(before_after_data: Dict) -> go.Figure:
    """Crea gráfico comparativo antes vs después."""
    if not before_after_data:
        return go.Figure().update_layout(title="Sin datos disponibles")

    categories = ["Ticket Count", "Avg Score", "SLA Breach %"]
    before_values = [
        before_after_data["before_count"],
        before_after_data["before_avg_score"],
        before_after_data["before_sla_breach"]
    ]
    after_values = [
        before_after_data["after_count"],
        before_after_data["after_avg_score"],
        before_after_data["after_sla_breach"]
    ]

    fig = go.Figure(data=[
        go.Bar(name="Before", x=categories, y=before_values,
               marker_color=COLORS["dark"]),
        go.Bar(name="After", x=categories, y=after_values,
               marker_color=COLORS["accent"])
    ])

    fig.update_layout(
        **BASE_LAYOUT,
        title="Before vs After Implementation",
        barmode="group",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )

    return fig


def create_recurring_issues_chart(recurring_data: pd.DataFrame) -> go.Figure:
    """Crea gráfico de issues recurrentes."""
    if recurring_data.empty:
        return go.Figure().update_layout(title="Sin problemas recurrentes detectados")

    # Crear label combinado
    recurring_data = recurring_data.copy()
    recurring_data["label"] = recurring_data["category"] + " - " + recurring_data["service_offering"]

    fig = go.Figure(data=[go.Bar(
        x=recurring_data["months_count"],
        y=recurring_data["label"],
        orientation="h",
        marker_color=COLORS["primary"],
        text=recurring_data["months_count"].apply(lambda x: f"{x} months"),
        textposition="auto"
    )])

    fig.update_layout(
        **BASE_LAYOUT,
        title="Recurring Issues (Present in Multiple Months)",
        xaxis_title="Number of Months",
        yaxis_title="Issue",
        yaxis=dict(autorange="reversed")
    )

    return fig


def create_severity_distribution(df: pd.DataFrame) -> go.Figure:
    """Crea gráfico de distribución por severidad."""
    if df.empty:
        return go.Figure().update_layout(title="Sin datos disponibles")

    severity_counts = df["severity"].value_counts()
    colors = [COLORS["accent"], COLORS["medium_blue"], COLORS["primary"], COLORS["dark"]]

    fig = go.Figure(data=[go.Pie(
        labels=severity_counts.index,
        values=severity_counts.values,
        marker=dict(colors=colors[:len(severity_counts)]),
        hole=0.3,
        textinfo="label+percent"
    )])

    fig.update_layout(
        **BASE_LAYOUT,
        title="Severity Distribution"
    )

    return fig


def create_anomaly_scatter(anomaly_data: pd.DataFrame) -> go.Figure:
    """Crea scatter plot de anomalías."""
    if anomaly_data.empty:
        return go.Figure().update_layout(title="Sin datos disponibles")

    # Puntos normales
    normal = anomaly_data[~anomaly_data["is_anomaly"]]
    anomalies = anomaly_data[anomaly_data["is_anomaly"]]

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=normal["report_period_month"],
        y=normal["negative_tickets"],
        mode="markers+lines",
        name="Normal",
        marker=dict(color=COLORS["primary"], size=10)
    ))

    if not anomalies.empty:
        fig.add_trace(go.Scatter(
            x=anomalies["report_period_month"],
            y=anomalies["negative_tickets"],
            mode="markers",
            name="Anomaly",
            marker=dict(color="red", size=15, symbol="star")
        ))

    # Línea de media
    mean_val = anomaly_data["negative_tickets"].mean()
    fig.add_hline(y=mean_val, line_dash="dash", line_color="gray",
                  annotation_text=f"Mean: {mean_val:.1f}")

    fig.update_layout(
        **BASE_LAYOUT,
        title="Anomaly Detection in Negative Surveys",
        xaxis_title="Month",
        yaxis_title="Negative Surveys"
    )
    fig.update_xaxes(categoryorder="array", categoryarray=MONTH_ORDER)

    return fig


def create_service_breakdown(df: pd.DataFrame) -> go.Figure:
    """Crea gráfico de desglose por servicio."""
    if df.empty:
        return go.Figure().update_layout(title="Sin datos disponibles")

    service_data = df.groupby("service_offering").agg(
        count=("ticket_id", "count"),
        avg_score=("score", "mean")
    ).reset_index()

    fig = make_subplots(specs=[[{"secondary_y": True}]])

    fig.add_trace(
        go.Bar(
            x=service_data["service_offering"],
            y=service_data["count"],
            name="Ticket Count",
            marker_color=COLORS["primary"]
        ),
        secondary_y=False
    )

    fig.add_trace(
        go.Scatter(
            x=service_data["service_offering"],
            y=service_data["avg_score"],
            name="Avg Score",
            line=dict(color=COLORS["accent"], width=3),
            mode="lines+markers"
        ),
        secondary_y=True
    )

    fig.update_xaxes(title_text="Service Offering")
    fig.update_yaxes(title_text="Count", secondary_y=False)
    fig.update_yaxes(title_text="Avg Score", secondary_y=True)

    fig.update_layout(
        **BASE_LAYOUT,
        title="Service Offering Breakdown",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )

    return fig
