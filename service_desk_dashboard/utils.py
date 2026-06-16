"""
Utility Functions - Funciones auxiliares para el dashboard de Service Desk.

Contiene helpers para cálculos, transformaciones de datos y análisis
de métricas del Global Service Desk.
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Tuple, Optional
from datetime import datetime, timedelta

# Constantes de colores
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

# Meses en orden
MONTH_ORDER = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
               "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def load_data(tickets_path: str, actions_path: str) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """Carga los datasets de tickets y action items."""
    try:
        tickets_df = pd.read_csv(tickets_path)
        actions_df = pd.read_csv(actions_path)
        return tickets_df, actions_df
    except FileNotFoundError as e:
        print(f"Error al cargar archivos: {e}")
        print("Ejecuta data_generator.py primero para crear los datasets.")
        raise


def apply_filters(df: pd.DataFrame, filters: Dict) -> pd.DataFrame:
    """Aplica filtros al dataframe según los parámetros proporcionados."""
    filtered_df = df.copy()

    if filters.get("years") and len(filters["years"]) > 0:
        filtered_df = filtered_df[filtered_df["year"].isin(filters["years"])]

    if filters.get("months") and len(filters["months"]) > 0:
        filtered_df = filtered_df[filtered_df["report_period_month"].isin(filters["months"])]

    if filters.get("min_score") is not None:
        filtered_df = filtered_df[filtered_df["score"] >= filters["min_score"]]

    if filters.get("max_score") is not None:
        filtered_df = filtered_df[filtered_df["score"] <= filters["max_score"]]

    if filters.get("geo_units") and len(filters["geo_units"]) > 0:
        filtered_df = filtered_df[filtered_df["geo_unit"].isin(filters["geo_units"])]

    if filters.get("assignment_groups") and len(filters["assignment_groups"]) > 0:
        filtered_df = filtered_df[filtered_df["assignment_group"].isin(filters["assignment_groups"])]

    if filters.get("service_offerings") and len(filters["service_offerings"]) > 0:
        filtered_df = filtered_df[filtered_df["service_offering"].isin(filters["service_offerings"])]

    return filtered_df


def calculate_kpis(df: pd.DataFrame, actions_df: pd.DataFrame) -> Dict:
    """Calcula todas las KPIs principales del dashboard."""
    total_surveys = len(df)
    negative_surveys = df["negative_survey_flag"].sum()
    negative_rate = (negative_surveys / total_surveys * 100) if total_surveys > 0 else 0

    # Calcular cambio mes a mes
    if "report_period_month" in df.columns and len(df["report_period_month"].unique()) > 1:
        month_counts = df.groupby("report_period_month").size()
        sorted_months = [m for m in MONTH_ORDER if m in month_counts.index]
        if len(sorted_months) >= 2:
            current_month = sorted_months[-1]
            prev_month = sorted_months[-2]
            current_count = month_counts[current_month]
            prev_count = month_counts[prev_month]
            mom_change = ((current_count - prev_count) / prev_count * 100) if prev_count > 0 else 0
        else:
            mom_change = 0
    else:
        mom_change = 0

    # SLA breach
    sla_breach_count = df["breached_flag"].sum()
    sla_breach_pct = (sla_breach_count / total_surveys * 100) if total_surveys > 0 else 0

    # Action items overdue
    if not actions_df.empty:
        overdue_actions = actions_df["overdue_flag"].sum()
        total_actions = len(actions_df)
        completion_rate = (actions_df["status"] == "Completed").sum() / total_actions * 100 if total_actions > 0 else 0
    else:
        overdue_actions = 0
        completion_rate = 0

    # CIM %
    cim_count = df["cim_flag"].sum()
    cim_pct = (cim_count / total_surveys * 100) if total_surveys > 0 else 0

    # Analysts above team average
    analyst_cim = df.groupby("analyst")["cim_flag"].mean() * 100
    team_avg_cim = analyst_cim.mean()
    analysts_above_avg = (analyst_cim > team_avg_cim).sum()

    return {
        "total_surveys": total_surveys,
        "negative_surveys": negative_surveys,
        "negative_rate": round(negative_rate, 1),
        "mom_change": round(mom_change, 1),
        "sla_breach_pct": round(sla_breach_pct, 1),
        "overdue_actions": int(overdue_actions),
        "cim_pct": round(cim_pct, 1),
        "analysts_above_avg": analysts_above_avg,
        "team_avg_cim": round(team_avg_cim, 1),
        "completion_rate": round(completion_rate, 1)
    }


def calculate_monthly_trends(df: pd.DataFrame) -> pd.DataFrame:
    """Calcula tendencias mensuales de encuestas negativas."""
    if df.empty:
        return pd.DataFrame()

    monthly = df.groupby("report_period_month").agg(
        total_tickets=("ticket_id", "count"),
        negative_tickets=("negative_survey_flag", "sum"),
        avg_score=("score", "mean"),
        sla_breaches=("breached_flag", "sum")
    ).reset_index()

    # Ordenar por mes
    monthly["month_order"] = monthly["report_period_month"].map(
        {m: i for i, m in enumerate(MONTH_ORDER)}
    )
    monthly = monthly.sort_values("month_order")

    # Calcular cambio porcentual
    monthly["negative_pct_change"] = monthly["negative_tickets"].pct_change() * 100
    monthly["negative_pct_change"] = monthly["negative_pct_change"].fillna(0)

    return monthly


def calculate_pareto_data(df: pd.DataFrame, group_col: str) -> pd.DataFrame:
    """Calcula datos para diagrama de Pareto."""
    if df.empty:
        return pd.DataFrame()

    counts = df[group_col].value_counts().reset_index()
    counts.columns = [group_col, "count"]
    counts = counts.sort_values("count", ascending=False)
    counts["cumulative_pct"] = counts["count"].cumsum() / counts["count"].sum() * 100

    return counts


def calculate_heatmap_data(df: pd.DataFrame) -> pd.DataFrame:
    """Calcula matriz de calor para heatmap de CSAT."""
    if df.empty:
        return pd.DataFrame()

    heatmap = df.pivot_table(
        values="score",
        index="category",
        columns="service_offering",
        aggfunc="mean"
    ).round(2)

    return heatmap


def calculate_analyst_performance(df: pd.DataFrame) -> pd.DataFrame:
    """Calcula métricas de rendimiento por analista."""
    if df.empty:
        return pd.DataFrame()

    performance = df.groupby("analyst").agg(
        total_tickets=("ticket_id", "count"),
        cim_count=("cim_flag", "sum"),
        avg_score=("score", "mean"),
        sla_breaches=("breached_flag", "sum")
    ).reset_index()

    performance["cim_pct"] = (performance["cim_count"] / performance["total_tickets"] * 100).round(1)
    team_avg = performance["cim_pct"].mean()
    performance["vs_team_avg"] = (performance["cim_pct"] - team_avg).round(1)

    return performance


def calculate_sla_analysis(df: pd.DataFrame) -> Dict:
    """Calcula análisis de SLA y resolución."""
    if df.empty:
        return {}

    total = len(df)
    breached = df["breached_flag"].sum()
    within_target = total - breached

    aging_dist = df["aging_bucket"].value_counts().to_dict()

    resolution_stats = {
        "avg_resolution_time": df["resolution_time_hours"].mean(),
        "median_resolution_time": df["resolution_time_hours"].median(),
        "max_resolution_time": df["resolution_time_hours"].max()
    }

    return {
        "total": total,
        "breached": int(breached),
        "within_target": int(within_target),
        "breach_pct": round(breached / total * 100, 1) if total > 0 else 0,
        "aging_distribution": aging_dist,
        "resolution_stats": resolution_stats
    }


def detect_anomalies(df: pd.DataFrame, threshold: float = 2.0) -> pd.DataFrame:
    """Detecta anomalías usando z-score."""
    if df.empty or len(df) < 3:
        return pd.DataFrame()

    monthly = calculate_monthly_trends(df)
    if monthly.empty:
        return pd.DataFrame()

    mean_neg = monthly["negative_tickets"].mean()
    std_neg = monthly["negative_tickets"].std()

    if std_neg == 0:
        monthly["z_score"] = 0
    else:
        monthly["z_score"] = (monthly["negative_tickets"] - mean_neg) / std_neg

    monthly["is_anomaly"] = monthly["z_score"].abs() > threshold

    return monthly


def identify_recurring_issues(df: pd.DataFrame, min_months: int = 2) -> pd.DataFrame:
    """Identifica problemas recurrentes en múltiples meses."""
    if df.empty:
        return pd.DataFrame()

    recurring = df.groupby(["category", "service_offering"])["report_period_month"].nunique().reset_index()
    recurring.columns = ["category", "service_offering", "months_count"]
    recurring = recurring[recurring["months_count"] >= min_months]
    recurring = recurring.sort_values("months_count", ascending=False)

    return recurring


def calculate_before_after(df: pd.DataFrame, action_date: str = "2024-06-01") -> Dict:
    """Calcula comparación antes vs después de acciones implementadas."""
    if df.empty:
        return {}

    df_copy = df.copy()
    df_copy["created_date"] = pd.to_datetime(df_copy["created_date"])

    cutoff_date = pd.to_datetime(action_date)

    before = df_copy[df_copy["created_date"] < cutoff_date]
    after = df_copy[df_copy["created_date"] >= cutoff_date]

    return {
        "before_count": len(before),
        "after_count": len(after),
        "before_avg_score": before["score"].mean() if len(before) > 0 else 0,
        "after_avg_score": after["score"].mean() if len(after) > 0 else 0,
        "before_sla_breach": before["breached_flag"].mean() * 100 if len(before) > 0 else 0,
        "after_sla_breach": after["breached_flag"].mean() * 100 if len(after) > 0 else 0
    }


def generate_insights(df: pd.DataFrame, actions_df: pd.DataFrame) -> List[str]:
    """Genera insights automáticos basados en los datos filtrados."""
    insights = []

    if df.empty:
        return ["No hay datos disponibles para generar insights."]

    # Category con mayor volumen negativo
    top_category = df["category"].value_counts().index[0] if len(df["category"].value_counts()) > 0 else "N/A"
    insights.append(f"La categoría con mayor volumen negativo es: {top_category}")

    # Service offering con peor score
    worst_offering = df.groupby("service_offering")["score"].mean().idxmin()
    insights.append(f"El service offering con peor score promedio es: {worst_offering}")

    # Assignment group con mayor breach rate
    worst_breach_group = df.groupby("assignment_group")["breached_flag"].mean().idxmax()
    insights.append(f"El assignment group con mayor breach rate es: {worst_breach_group}")

    # Analista con mayor % CIM
    analyst_cim = df.groupby("analyst")["cim_flag"].mean() * 100
    if not analyst_cim.empty:
        highest_cim_analyst = analyst_cim.idxmax()
        insights.append(f"El analista con mayor % CIM es: {highest_cim_analyst}")

    # Top foco sugerido de mejora
    top_issues = df["category"].value_counts()
    if len(top_issues) > 0:
        insights.append(f"Foco sugerido: Reducir incidencias en {top_issues.index[0]} ({top_issues.iloc[0]} tickets)")

    return insights


def format_percentage(value: float) -> str:
    """Formatea un valor como porcentaje."""
    return f"{value:.1f}%"


def format_delta(current: float, previous: float) -> Tuple[str, str]:
    """Formatea el cambio entre dos valores."""
    if previous == 0:
        return "N/A", "normal"
    delta = ((current - previous) / previous) * 100
    if delta > 0:
        return f"+{delta:.1f}%", "negative"
    elif delta < 0:
        return f"{delta:.1f}%", "positive"
    else:
        return "0.0%", "normal"
