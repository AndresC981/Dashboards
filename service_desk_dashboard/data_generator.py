"""
Data Generator - Generación de datos sintéticos para el dashboard de Service Desk.

Genera 50 registros de tickets/encuestas con distribución realista para simular
un entorno de Global Service Desk con encuestas negativas de CSAT.
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import os

# Configuración de semilla para reproducibilidad
np.random.seed(42)
random.seed(42)

# Constantes del dominio
GEO_UNITS = ["ECP", "ABC", "USL", "BRZ", "ACE"]
ASSIGNMENT_GROUPS = ["GBS IT-WH-CIM", "GBS IT EH-CIM"]
SERVICES = ["Endpoint Services", "Infrastructure", "Cloud Services", "Security"]
SERVICE_OFFERINGS = ["Missing patches", "M365", "PC Reimage", "Printing", "MyPCP"]
CATEGORIES = [
    "Software Issue", "Hardware Failure", "Access Problem",
    "Performance", "Configuration", "Documentation", "Communication"
]
SUBCATEGORIES = {
    "Software Issue": ["App Crash", "Update Failed", "License Issue", "Compatibility"],
    "Hardware Failure": ["Disk Failure", "Memory Issue", "Display Problem", "Peripheral"],
    "Access Problem": ["Login Failed", "Permission Denied", "MFA Issue", "Account Locked"],
    "Performance": ["Slow Response", "Timeout", "High CPU", "Memory Leak"],
    "Configuration": ["Wrong Settings", "Missing Config", "Policy Conflict", "Registry Issue"],
    "Documentation": ["Missing Guide", "Outdated Info", "Unclear Steps", "No SOP"],
    "Communication": ["No Update", "Delayed Response", "Misunderstanding", "Escalation"]
}
ANALYSTS = ["Ana Garcia", "Carlos Lopez", "Maria Rodriguez", "Pedro Martinez", "Laura Sanchez"]
SEVERITY_LEVELS = ["Low", "Medium", "High", "Critical"]
AGING_BUCKETS = ["0-3 days", "4-7 days", "8-14 days", "15-30 days", "30+ days"]
ACTION_STATUSES = ["Pending", "In Progress", "Completed", "Overdue"]
MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# Pesos para distribución no uniforme
SERVICE_WEIGHTS = [0.35, 0.25, 0.22, 0.18]
OFFERING_WEIGHTS = [0.28, 0.24, 0.20, 0.16, 0.12]
CATEGORY_WEIGHTS = [0.22, 0.18, 0.16, 0.15, 0.13, 0.09, 0.07]
SEVERITY_WEIGHTS = [0.15, 0.35, 0.30, 0.20]
MONTH_WEIGHTS = [0.06, 0.07, 0.08, 0.09, 0.10, 0.12, 0.11, 0.10, 0.09, 0.08, 0.06, 0.04]


def generate_ticket_id(idx: int) -> str:
    """Genera un ID de ticket formateado."""
    return f"TKT-{2024}-{idx:04d}"


def generate_incident_id(idx: int) -> str:
    """Genera un ID de incidente formateado."""
    return f"INC-{idx:05d}"


def calculate_sla_target(severity: str, category: str) -> float:
    """Calcula horas objetivo de SLA según severidad y categoría."""
    base_targets = {
        "Critical": 4,
        "High": 8,
        "Medium": 24,
        "Low": 48
    }
    category_multiplier = {
        "Software Issue": 1.0,
        "Hardware Failure": 1.2,
        "Access Problem": 0.8,
        "Performance": 1.1,
        "Configuration": 0.9,
        "Documentation": 1.5,
        "Communication": 0.7
    }
    return base_targets[severity] * category_multiplier.get(category, 1.0)


def calculate_resolution_time(severity: str, sla_target: float) -> float:
    """Calcula tiempo real de resolución con variación respecto al target."""
    if severity == "Critical":
        return sla_target * np.random.uniform(0.7, 1.8)
    elif severity == "High":
        return sla_target * np.random.uniform(0.6, 1.6)
    elif severity == "Medium":
        return sla_target * np.random.uniform(0.5, 1.5)
    else:
        return sla_target * np.random.uniform(0.4, 1.4)


def assign_score(severity: str, category: str) -> float:
    """Asigna score de CSAT basado en severidad y categoría."""
    base_score = {
        "Critical": 2.8,
        "High": 2.5,
        "Medium": 2.0,
        "Low": 1.5
    }
    category_adjustment = {
        "Software Issue": 0.2,
        "Hardware Failure": 0.3,
        "Access Problem": 0.1,
        "Performance": 0.15,
        "Configuration": 0.05,
        "Documentation": -0.1,
        "Communication": -0.2
    }
    score = base_score[severity] + category_adjustment.get(category, 0)
    score += np.random.normal(0, 0.3)
    return round(max(1.0, min(3.5, score)), 1)


def assign_analyst(assignment_group: str) -> str:
    """Asigna analista según grupo de asignación."""
    if assignment_group == "GBS IT-WH-CIM":
        return random.choice(["Ana Garcia", "Carlos Lopez", "Maria Rodriguez"])
    else:
        return random.choice(["Pedro Martinez", "Laura Sanchez"])


def generate_tickets(n: int = 50) -> pd.DataFrame:
    """Genera dataset principal de tickets con distribución realista."""
    tickets = []

    # Crear tendencia: algunos meses con más negativos
    month_counts = np.random.multinomial(n, MONTH_WEIGHTS)
    month_indices = []
    for m, count in enumerate(month_counts):
        month_indices.extend([m] * count)
    random.shuffle(month_indices)

    for idx in range(1, n + 1):
        month_idx = month_indices[idx - 1]
        month_num = month_idx + 1

        # Generar fecha dentro del mes
        year = 2024
        start_date = datetime(year, month_num, 1)
        if month_num == 12:
            end_date = datetime(year, 12, 31)
        else:
            end_date = datetime(year, month_num + 1, 1) - timedelta(days=1)
        created_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))

        # Seleccionar atributos con distribución ponderada
        service = random.choices(SERVICES, weights=SERVICE_WEIGHTS)[0]
        offering = random.choices(SERVICE_OFFERINGS, weights=OFFERING_WEIGHTS)[0]
        category = random.choices(CATEGORIES, weights=CATEGORY_WEIGHTS)[0]
        subcategory = random.choice(SUBCATEGORIES[category])
        geo_unit = random.choice(GEO_UNITS)
        assignment_group = random.choice(ASSIGNMENT_GROUPS)
        severity = random.choices(SEVERITY_LEVELS, weights=SEVERITY_WEIGHTS)[0]
        analyst = assign_analyst(assignment_group)

        # Calcular métricas
        sla_target = calculate_sla_target(severity, category)
        resolution_time = calculate_resolution_time(severity, sla_target)
        score = assign_score(severity, category)
        breached = resolution_time > sla_target

        # Determinar aging bucket
        if resolution_time <= 72:
            aging = "0-3 days"
        elif resolution_time <= 168:
            aging = "4-7 days"
        elif resolution_time <= 336:
            aging = "8-14 days"
        elif resolution_time <= 720:
            aging = "15-30 days"
        else:
            aging = "30+ days"

        # CIM flag: mayor probabilidad en ciertos analistas
        cim_prob = 0.3 if analyst in ["Pedro Martinez", "Laura Sanchez"] else 0.15
        cim_flag = random.random() < cim_prob

        # Comentario del cliente
        comments = [
            "Slow response time, very frustrating",
            "Issue not resolved on first contact",
            "Had to call multiple times for same issue",
            "Technical knowledge was lacking",
            "No follow-up after escalation",
            "Solution didn't work as expected",
            "Waited too long for callback",
            "Communication was unclear",
            "Problem recurred after fix",
            "Missing documentation for resolution"
        ]

        # Fecha de cierre
        closed_date = created_date + timedelta(hours=resolution_time)

        ticket = {
            "ticket_id": generate_ticket_id(idx),
            "incident_id": generate_incident_id(idx),
            "created_date": created_date.strftime("%Y-%m-%d"),
            "closed_date": closed_date.strftime("%Y-%m-%d %H:%M"),
            "year": year,
            "report_period_month": MONTHS[month_idx],
            "month_num": month_num,
            "analyst": analyst,
            "geo_unit": geo_unit,
            "assignment_group": assignment_group,
            "service": service,
            "service_offering": offering,
            "category": category,
            "subcategory": subcategory,
            "score": score,
            "negative_survey_flag": True,
            "severity": severity,
            "impact": random.randint(1, 5),
            "resolution_time_hours": round(resolution_time, 1),
            "sla_target_hours": sla_target,
            "sla_status": "Breached" if breached else "Within Target",
            "breached_flag": breached,
            "aging_bucket": aging,
            "cim_flag": cim_flag,
            "customer_comment": random.choice(comments)
        }
        tickets.append(ticket)

    return pd.DataFrame(tickets)


def generate_action_items(tickets_df: pd.DataFrame) -> pd.DataFrame:
    """Genera action items vinculados a tickets negativos."""
    action_items = []
    action_id = 1

    # Seleccionar tickets para generar action items (aproximadamente 60%)
    selected_tickets = tickets_df.sample(n=min(30, len(tickets_df)), random_state=42)

    for _, ticket in selected_tickets.iterrows():
        # Determinar status basado en fecha
        created_date = datetime.strptime(ticket["created_date"], "%Y-%m-%d")
        due_date = created_date + timedelta(days=random.randint(7, 30))

        # Distribución de status
        status_rand = random.random()
        if status_rand < 0.35:
            status = "Completed"
            completion_date = due_date - timedelta(days=random.randint(0, 5))
            overdue = False
            implemented = True
        elif status_rand < 0.55:
            status = "In Progress"
            completion_date = None
            overdue = False
            implemented = False
        elif status_rand < 0.75:
            status = "Pending"
            completion_date = None
            overdue = datetime.now() > due_date
            implemented = False
        else:
            status = "Overdue"
            completion_date = None
            overdue = True
            implemented = False

        # Owner del action item
        owners = ["Continuous Improvement", "Service Excellence", "Team Lead", "Manager"]
        owner = random.choice(owners)

        # Descripción del action item
        descriptions = [
            "Review and update troubleshooting procedures",
            "Conduct root cause analysis",
            "Implement additional training session",
            "Update knowledge base article",
            "Schedule follow-up with customer",
            "Escalate to vendor for resolution",
            "Create standard operating procedure",
            "Implement automated monitoring"
        ]

        action = {
            "action_id": f"ACT-{action_id:03d}",
            "linked_ticket_id": ticket["ticket_id"],
            "issue_category": ticket["category"],
            "owner": owner,
            "status": status,
            "created_date": created_date.strftime("%Y-%m-%d"),
            "due_date": due_date.strftime("%Y-%m-%d"),
            "completion_date": completion_date.strftime("%Y-%m-%d") if completion_date else None,
            "overdue_flag": overdue,
            "action_description": random.choice(descriptions),
            "implemented_flag": implemented
        }
        action_items.append(action)
        action_id += 1

    return pd.DataFrame(action_items)


def main():
    """Función principal para generar y guardar datasets."""
    print("Generando dataset de tickets...")
    tickets_df = generate_tickets(50)
    print(f"Generados {len(tickets_df)} tickets.")

    print("Generando dataset de action items...")
    actions_df = generate_action_items(tickets_df)
    print(f"Generados {len(actions_df)} action items.")

    # Guardar archivos
    output_dir = "data"
    os.makedirs(output_dir, exist_ok=True)

    tickets_path = os.path.join(output_dir, "tickets.csv")
    actions_path = os.path.join(output_dir, "action_items.csv")

    tickets_df.to_csv(tickets_path, index=False)
    actions_df.to_csv(actions_path, index=False)

    print(f"\nArchivos generados exitosamente:")
    print(f"  - {tickets_path}")
    print(f"  - {actions_path}")

    # Estadísticas básicas
    print("\nEstadísticas del dataset:")
    print(f"  - Total tickets: {len(tickets_df)}")
    print(f"  - Scores promedio: {tickets_df['score'].mean():.2f}")
    print(f"  - SLA breaches: {tickets_df['breached_flag'].sum()}")
    print(f"  - Action items: {len(actions_df)}")
    print(f"  - Action items completados: {actions_df[actions_df['status'] == 'Completed'].shape[0]}")

    return tickets_df, actions_df


if __name__ == "__main__":
    main()
