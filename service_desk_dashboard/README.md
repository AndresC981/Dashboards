# IT Service Desk Executive Dashboard

Dashboard ejecutivo/operativo para analizar encuestas negativas del Global Service Desk, identificar acciones de mejora y monitorear cumplimiento de tiempos de contacto.

##   Descripción del Proyecto

Este dashboard está diseñado para el equipo de Global Service Excellence y permite:

- Analizar tendencias de encuestas negativas mes a mes
- Identificar los principales drivers de insatisfacción
- Monitorear cumplimiento de SLA y tiempos de resolución
- Hacer tracking de acciones correctivas
- Detectar anomalías y patrones recurrentes
- Medir efectividad de mejoras implementadas

##   Arquitectura

```
service_desk_dashboard/
│
├── app.py                    # Dashboard principal de Streamlit
├── data_generator.py         # Generador de datos sintéticos
├── utils.py                  # Funciones auxiliares y helpers
├── charts.py                 # Visualizaciones Plotly
├── styles.py                 # CSS personalizado
├── requirements.txt          # Dependencias
├── README.md                 # Esta documentación
│
├── data/
│   ├── tickets.csv           # Dataset principal (50 registros)
│   └── action_items.csv      # Action items relacionados
│
└── .streamlit/
    └── config.toml           # Configuración de tema y servidor
```

##   Dependencias

- Python 3.8+
- Streamlit 1.28+
- Pandas 2.0+
- NumPy 1.24+
- Plotly 5.15+

##   Instalación

```bash
# 1. Crear entorno virtual (recomendado)
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Generar datos sintéticos
python data_generator.py

# 4. Ejecutar dashboard
streamlit run app.py
```

El dashboard estará disponible en: `http://localhost:8501`

##   Estructura de Datos

### Dataset Principal (tickets.csv)

| Campo | Descripción |
|-------|-------------|
| ticket_id | Identificador único del ticket |
| incident_id | ID del incidente |
| created_date | Fecha de creación |
| closed_date | Fecha de cierre |
| year | Año |
| report_period_month | Mes del reporte |
| analyst | Analista asignado |
| geo_unit | Unidad geográfica |
| assignment_group | Grupo de asignación |
| service | Servicio |
| service_offering | Oferta de servicio |
| category | Categoría del issue |
| subcategory | Subcategoría |
| score | Score de CSAT (1.0 - 3.5) |
| negative_survey_flag | Flag de encuesta negativa |
| severity | Severidad (Low/Medium/High/Critical) |
| impact | Impacto (1-5) |
| resolution_time_hours | Tiempo de resolución en horas |
| sla_target_hours | Objetivo SLA en horas |
| sla_status | Estado del SLA |
| breached_flag | Flag de breach de SLA |
| aging_bucket | Bucket de aging |
| cim_flag | Flag de CIM |
| customer_comment | Comentario del cliente |

### Action Items (action_items.csv)

| Campo | Descripción |
|-------|-------------|
| action_id | ID de la acción |
| linked_ticket_id | Ticket relacionado |
| issue_category | Categoría del issue |
| owner | Responsable |
| status | Estado (Pending/In Progress/Completed/Overdue) |
| created_date | Fecha de creación |
| due_date | Fecha límite |
| completion_date | Fecha de completado |
| overdue_flag | Flag de vencido |
| action_description | Descripción de la acción |
| implemented_flag | Flag de implementación |

##   Funcionalidades del Dashboard

### KPIs Principales
- Total de surveys
- Encuestas negativas y tasa negativa
- Cambio mes a mes (MoM)
- SLA breach %
- Action items overdue
- CIM % por analista

### Secciones del Dashboard

1. **Trends & Variation**: Gráfico de línea temporal con detección de anomalías
2. **Top Drivers - Pareto**: Análisis de Pareto por categoría y service offering
3. **CSAT Correlation**: Heatmap de correlación categoría vs servicio
4. **Action Items Tracker**: Seguimiento de acciones con status y overdue
5. **CIM Analysis**: Análisis de CIM por analista vs promedio del equipo
6. **SLA & Resolution**: Análisis de compliance, aging y distribución de tiempos
7. **Key Insights**: Panel de insights automáticos generados por reglas
8. **Anomaly Detection**: Detección de spikes con z-score configurable
9. **Recurring Issues**: Identificación de problemas recurrentes en múltiples meses
10. **Before vs After**: Comparación de métricas antes/después de implementaciones
11. **Service Segmentation**: Análisis por dimensiones operativas
12. **Detailed View**: Tabla detallada con drill-down y filtros

##   Definiciones de Métricas

| Métrica | Definición |
|---------|------------|
| Negative Survey | Score <= 3.5 |
| SLA Breach | resolution_time_hours > sla_target_hours |
| CIM % | tickets con cim_flag / total tickets del analista |
| Completion Rate | acciones completadas / acciones totales |
| MoM Change | (actual - previo) / previo * 100 |

##   Supuestos

1. **Datos sintéticos**: Se generan 50 registros con distribución realista para demostrar funcionalidades
2. **Score range**: Scores van de 1.0 a 3.5 (donde <= 3.5 se considera negativo)
3. **Distribución temporal**: Algunos meses tienen más encuestas negativas para simular tendencias
4. **Anomalías**: Se detectan usando z-score con umbral configurable (default: 2.0)
5. **Before/After**: Se usa fecha fija "2024-06-01" como punto de corte para comparaciones
6. **Recurring issues**: Se considera recurrente si aparece en 2+ meses

##   Paleta de Colores

### Core
- Primary: `#0014DC`
- White: `#FFFFFF`

### Functional
- Accent: `#00D2DC`
- Dark: `#051464`
- Medium Blue: `#6E8CC8`
- Light Blue: `#AFBEE1`
- Light Gray: `#F0F0F0`
- Border: `#DCE1E1`
- Gray: `#C8CDCD`
- Medium Gray: `#AAAAAA`
- Dark Gray: `#696969`
- Black: `#000000`

##   Filtros Disponibles

- **Year**: Multiselección
- **Report Period**: Multiselección de meses
- **Score**: Rango mínimo/máximo (1.0 - 3.5)
- **GeoUnit**: ECP, ABC, USL, BRZ, ACE
- **Assignment Group**: GBS IT-WH-CIM, GBS IT EH-CIM
- **Service Offering**: Missing patches, M365, PC Reimage, Printing, MyPCP
- **Anomaly Threshold**: Slider para sensibilidad de detección

##   Mejoras Futuras

1. **Conexión a datos reales**: Integrar con ServiceNow o similar
2. **Exportación de reportes**: Generar PDF/Excel desde el dashboard
3. **Alertas por email**: Configurar notificaciones automáticas
4. **ML Predictivo**: Modelos para predecir tendencias
5. **Multi-idioma**: Soporte para español/inglés
6. **Mobile responsive**: Optimización completa para móviles
7. **Cache avanzado**: Redis o similar para producción
8. **Autenticación**: Login y roles de usuario
9. **API REST**: Backend para integración con otros sistemas
10. **Testing automatizado**: Unit tests y integration tests

##   Solución a Historias de Usuario

| # | Historia | Criterios Cubiertos |
|---|----------|---------------------|
| 1 | Tendencias mes a mes | ✅ Gráfico temporal, % cambio, alertas configurables |
| 2 | Top drivers | ✅ Pareto chart, ranking por volumen y severidad |
| 3 | Correlación CSAT | ✅ Heatmap, distribución, drill-down |
| 4 | Action items tracking | ✅ Status, owner, due date, completion rate, overdue |
| 5 | CIM por analista | ✅ % CIM, comparación vs promedio, tendencia |
| 6 | Desviaciones SLA | ✅ Dentro/fuera de target, breaches, aging |
| 7 | Resumen insights | ✅ Panel automático con top issues y focos |
| 8 | Detección anomalías | ✅ Z-score, umbrales configurables, alertas |
| 9 | Drill-down | ✅ Tabla detallada con filtros sincronizados |
| 10 | Issues recurrentes | ✅ Patrones en múltiples meses, persistencia |
| 11 | Segmentación | ✅ Multi-filtro, métricas por dimensión |
| 12 | Efectividad acciones | ✅ Before vs after, tendencias de reducción |

##   Licencia

Proyecto para uso interno del Global Service Desk.

##   Contacto

Para soporte o mejoras, contactar al equipo de Service Excellence.
