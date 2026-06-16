"""
Static Data - Datos estáticos de 50 tickets y 30 action items para el dashboard.
Estos datos están integrados directamente en el código para no depender de archivos CSV.
"""

TICKETS_DATA = [
    {
        "ticket_id": "TKT-2024-0001", "incident_id": "INC-00001", "created_date": "2024-07-18",
        "closed_date": "2024-07-18 12:33", "year": 2024, "report_period_month": "Jul", "month_num": 7,
        "analyst": "Pedro Martinez", "geo_unit": "ACE", "assignment_group": "GBS IT EH-CIM",
        "service": "Endpoint Services", "service_offering": "MyPCP", "category": "Software Issue",
        "subcategory": "License Issue", "score": 2.6, "negative_survey_flag": True, "severity": "High",
        "impact": 2, "resolution_time_hours": 12.6, "sla_target_hours": 8.0, "sla_status": "Breached",
        "breached_flag": True, "aging_bucket": "0-3 days", "cim_flag": True,
        "customer_comment": "No follow-up after escalation"
    },
    {
        "ticket_id": "TKT-2024-0002", "incident_id": "INC-00002", "created_date": "2024-06-03",
        "closed_date": "2024-06-03 19:38", "year": 2024, "report_period_month": "Jun", "month_num": 6,
        "analyst": "Ana Garcia", "geo_unit": "USL", "assignment_group": "GBS IT-WH-CIM",
        "service": "Security", "service_offering": "Printing", "category": "Hardware Failure",
        "subcategory": "Peripheral", "score": 2.5, "negative_survey_flag": True, "severity": "Medium",
        "impact": 1, "resolution_time_hours": 19.6, "sla_target_hours": 28.8, "sla_status": "Within Target",
        "breached_flag": False, "aging_bucket": "0-3 days", "cim_flag": False,
        "customer_comment": "Missing documentation for resolution"
    },
    {
        "ticket_id": "TKT-2024-0003", "incident_id": "INC-00003", "created_date": "2024-05-21",
        "closed_date": "2024-05-21 06:16", "year": 2024, "report_period_month": "May", "month_num": 5,
        "analyst": "Ana Garcia", "geo_unit": "USL", "assignment_group": "GBS IT-WH-CIM",
        "service": "Endpoint Services", "service_offering": "Printing", "category": "Software Issue",
        "subcategory": "Compatibility", "score": 2.8, "negative_survey_flag": True, "severity": "High",
        "impact": 1, "resolution_time_hours": 6.3, "sla_target_hours": 8.0, "sla_status": "Within Target",
        "breached_flag": False, "aging_bucket": "0-3 days", "cim_flag": False,
        "customer_comment": "Solution didn't work as expected"
    },
    {
        "ticket_id": "TKT-2024-0004", "incident_id": "INC-00004", "created_date": "2024-03-13",
        "closed_date": "2024-03-13 15:39", "year": 2024, "report_period_month": "Mar", "month_num": 3,
        "analyst": "Laura Sanchez", "geo_unit": "ABC", "assignment_group": "GBS IT EH-CIM",
        "service": "Endpoint Services", "service_offering": "Missing patches", "category": "Communication",
        "subcategory": "Misunderstanding", "score": 1.2, "negative_survey_flag": True, "severity": "Medium",
        "impact": 2, "resolution_time_hours": 15.7, "sla_target_hours": 16.8, "sla_status": "Within Target",
        "breached_flag": False, "aging_bucket": "0-3 days", "cim_flag": True,
        "customer_comment": "Technical knowledge was lacking"
    },
    {
        "ticket_id": "TKT-2024-0005", "incident_id": "INC-00005", "created_date": "2024-02-24",
        "closed_date": "2024-02-24 04:29", "year": 2024, "report_period_month": "Feb", "month_num": 2,
        "analyst": "Ana Garcia", "geo_unit": "USL", "assignment_group": "GBS IT-WH-CIM",
        "service": "Infrastructure", "service_offering": "Missing patches", "category": "Performance",
        "subcategory": "Memory Leak", "score": 2.6, "negative_survey_flag": True, "severity": "Critical",
        "impact": 1, "resolution_time_hours": 4.5, "sla_target_hours": 4.4, "sla_status": "Breached",
        "breached_flag": True, "aging_bucket": "0-3 days", "cim_flag": False,
        "customer_comment": "Slow response time, very frustrating"
    },
    {
        "ticket_id": "TKT-2024-0006", "incident_id": "INC-00006", "created_date": "2024-10-28",
        "closed_date": "2024-10-28 17:06", "year": 2024, "report_period_month": "Oct", "month_num": 10,
        "analyst": "Maria Rodriguez", "geo_unit": "ACE", "assignment_group": "GBS IT-WH-CIM",
        "service": "Endpoint Services", "service_offering": "PC Reimage", "category": "Configuration",
        "subcategory": "Registry Issue", "score": 2.1, "negative_survey_flag": True, "severity": "Medium",
        "impact": 5, "resolution_time_hours": 17.1, "sla_target_hours": 21.6, "sla_status": "Within Target",
        "breached_flag": False, "aging_bucket": "0-3 days", "cim_flag": False,
        "customer_comment": "No follow-up after escalation"
    },
    {
        "ticket_id": "TKT-2024-0007", "incident_id": "INC-00007", "created_date": "2024-07-18",
        "closed_date": "2024-07-18 18:42", "year": 2024, "report_period_month": "Jul", "month_num": 7,
        "analyst": "Ana Garcia", "geo_unit": "USL", "assignment_group": "GBS IT-WH-CIM",
        "service": "Security", "service_offering": "Missing patches", "category": "Configuration",
        "subcategory": "Policy Conflict", "score": 2.5, "negative_survey_flag": True, "severity": "Medium",
        "impact": 3, "resolution_time_hours": 18.7, "sla_target_hours": 21.6, "sla_status": "Within Target",
        "breached_flag": False, "aging_bucket": "0-3 days", "cim_flag": False,
        "customer_comment": "Problem recurred after fix"
    },
    {
        "ticket_id": "TKT-2024-0008", "incident_id": "INC-00008", "created_date": "2024-03-25",
        "closed_date": "2024-03-26 01:11", "year": 2024, "report_period_month": "Mar", "month_num": 3,
        "analyst": "Ana Garcia", "geo_unit": "ACE", "assignment_group": "GBS IT-WH-CIM",
        "service": "Endpoint Services", "service_offering": "MyPCP", "category": "Documentation",
        "subcategory": "Unclear Steps", "score": 1.8, "negative_survey_flag": True, "severity": "Medium",
        "impact": 5, "resolution_time_hours": 25.2, "sla_target_hours": 36.0, "sla_status": "Within Target",
        "breached_flag": False, "aging_bucket": "0-3 days", "cim_flag": False,
        "customer_comment": "Slow response time, very frustrating"
    },
    {
        "ticket_id": "TKT-2024-0009", "incident_id": "INC-00009", "created_date": "2024-08-20",
        "closed_date": "2024-08-21 12:30", "year": 2024, "report_period_month": "Aug", "month_num": 8,
        "analyst": "Maria Rodriguez", "geo_unit": "ABC", "assignment_group": "GBS IT-WH-CIM",
        "service": "Endpoint Services", "service_offering": "Missing patches", "category": "Documentation",
        "subcategory": "Unclear Steps", "score": 1.7, "negative_survey_flag": True, "severity": "Medium",
        "impact": 1, "resolution_time_hours": 36.5, "sla_target_hours": 36.0, "sla_status": "Breached",
        "breached_flag": True, "aging_bucket": "0-3 days", "cim_flag": False,
        "customer_comment": "Communication was unclear"
    },
    {
        "ticket_id": "TKT-2024-0010", "incident_id": "INC-00010", "created_date": "2024-04-27",
        "closed_date": "2024-04-27 23:55", "year": 2024, "report_period_month": "Apr", "month_num": 4,
        "analyst": "Maria Rodriguez", "geo_unit": "BRZ", "assignment_group": "GBS IT-WH-CIM",
        "service": "Endpoint Services", "service_offering": "Printing", "category": "Configuration",
        "subcategory": "Missing Config", "score": 2.1, "negative_survey_flag": True, "severity": "Medium",
        "impact": 2, "resolution_time_hours": 23.9, "sla_target_hours": 21.6, "sla_status": "Breached",
        "breached_flag": True, "aging_bucket": "0-3 days", "cim_flag": False,
        "customer_comment": "Problem recurred after fix"
    },
    {
        "ticket_id": "TKT-2024-0011", "incident_id": "INC-00011", "created_date": "2024-08-25",
        "closed_date": "2024-08-26 08:51", "year": 2024, "report_period_month": "Aug", "month_num": 8,
        "analyst": "Pedro Martinez", "geo_unit": "BRZ", "assignment_group": "GBS IT EH-CIM",
        "service": "Cloud Services", "service_offering": "Missing patches", "category": "Hardware Failure",
        "subcategory": "Display Problem", "score": 1.6, "negative_survey_flag": True, "severity": "Low",
        "impact": 1, "resolution_time_hours": 32.9, "sla_target_hours": 57.6, "sla_status": "Within Target",
        "breached_flag": False, "aging_bucket": "0-3 days", "cim_flag": True,
        "customer_comment": "Missing documentation for resolution"
    },
    {
        "ticket_id": "TKT-2024-0012", "incident_id": "INC-00012", "created_date": "2024-06-18",
        "closed_date": "2024-06-18 05:48", "year": 2024, "report_period_month": "Jun", "month_num": 6,
        "analyst": "Carlos Lopez", "geo_unit": "ABC", "assignment_group": "GBS IT-WH-CIM",
        "service": "Endpoint Services", "service_offering": "Missing patches", "category": "Software Issue",
        "subcategory": "App Crash", "score": 2.9, "negative_survey_flag": True, "severity": "Critical",
        "impact": 2, "resolution_time_hours": 5.8, "sla_target_hours": 4.0, "sla_status": "Breached",
        "breached_flag": True, "aging_bucket": "0-3 days", "cim_flag": True,
        "customer_comment": "No follow-up after escalation"
    },
    {
        "ticket_id": "TKT-2024-0013", "incident_id": "INC-00013", "created_date": "2024-03-22",
        "closed_date": "2024-03-22 04:15", "year": 2024, "report_period_month": "Mar", "month_num": 3,
        "analyst": "Pedro Martinez", "geo_unit": "ABC", "assignment_group": "GBS IT EH-CIM",
        "service": "Infrastructure", "service_offering": "PC Reimage", "category": "Configuration",
        "subcategory": "Registry Issue", "score": 2.8, "negative_survey_flag": True, "severity": "Critical",
        "impact": 4, "resolution_time_hours": 4.3, "sla_target_hours": 3.6, "sla_status": "Breached",
        "breached_flag": True, "aging_bucket": "0-3 days", "cim_flag": True,
        "customer_comment": "Solution didn't work as expected"
    },
    {
        "ticket_id": "TKT-2024-0014", "incident_id": "INC-00014", "created_date": "2024-02-14",
        "closed_date": "2024-02-14 05:04", "year": 2024, "report_period_month": "Feb", "month_num": 2,
        "analyst": "Pedro Martinez", "geo_unit": "ECP", "assignment_group": "GBS IT EH-CIM",
        "service": "Infrastructure", "service_offering": "Printing", "category": "Software Issue",
        "subcategory": "App Crash", "score": 2.4, "negative_survey_flag": True, "severity": "High",
        "impact": 2, "resolution_time_hours": 5.1, "sla_target_hours": 8.0, "sla_status": "Within Target",
        "breached_flag": False, "aging_bucket": "0-3 days", "cim_flag": True,
        "customer_comment": "Problem recurred after fix"
    },
    {
        "ticket_id": "TKT-2024-0015", "incident_id": "INC-00015", "created_date": "2024-09-15",
        "closed_date": "2024-09-17 02:16", "year": 2024, "report_period_month": "Sep", "month_num": 9,
        "analyst": "Maria Rodriguez", "geo_unit": "BRZ", "assignment_group": "GBS IT-WH-CIM",
        "service": "Endpoint Services", "service_offering": "Missing patches", "category": "Access Problem",
        "subcategory": "Login Failed", "score": 1.8, "negative_survey_flag": True, "severity": "Low",
        "impact": 1, "resolution_time_hours": 50.3, "sla_target_hours": 38.4, "sla_status": "Breached",
        "breached_flag": True, "aging_bucket": "0-3 days", "cim_flag": False,
        "customer_comment": "Technical knowledge was lacking"
    },
    {
        "ticket_id": "TKT-2024-0016", "incident_id": "INC-00016", "created_date": "2024-09-06",
        "closed_date": "2024-09-08 03:14", "year": 2024, "report_period_month": "Sep", "month_num": 9,
        "analyst": "Laura Sanchez", "geo_unit": "ABC", "assignment_group": "GBS IT EH-CIM",
        "service": "Infrastructure", "service_offering": "M365", "category": "Documentation",
        "subcategory": "Missing Guide", "score": 1.0, "negative_survey_flag": True, "severity": "Low",
        "impact": 4, "resolution_time_hours": 51.2, "sla_target_hours": 72.0, "sla_status": "Within Target",
        "breached_flag": False, "aging_bucket": "0-3 days", "cim_flag": True,
        "customer_comment": "No follow-up after escalation"
    },
    {
        "ticket_id": "TKT-2024-0017", "incident_id": "INC-00017", "created_date": "2024-03-14",
        "closed_date": "2024-03-14 22:02", "year": 2024, "report_period_month": "Mar", "month_num": 3,
        "analyst": "Ana Garcia", "geo_unit": "ABC", "assignment_group": "GBS IT-WH-CIM",
        "service": "Cloud Services", "service_offering": "Printing", "category": "Configuration",
        "subcategory": "Registry Issue", "score": 1.7, "negative_survey_flag": True, "severity": "Medium",
        "impact": 5, "resolution_time_hours": 22.0, "sla_target_hours": 21.6, "sla_status": "Breached",
        "breached_flag": True, "aging_bucket": "0-3 days", "cim_flag": False,
        "customer_comment": "Slow response time, very frustrating"
    },
    {
        "ticket_id": "TKT-2024-0018", "incident_id": "INC-00018", "created_date": "2024-06-24",
        "closed_date": "2024-06-24 05:39", "year": 2024, "report_period_month": "Jun", "month_num": 6,
        "analyst": "Ana Garcia", "geo_unit": "ECP", "assignment_group": "GBS IT-WH-CIM",
        "service": "Endpoint Services", "service_offering": "Missing patches", "category": "Access Problem",
        "subcategory": "Permission Denied", "score": 3.0, "negative_survey_flag": True, "severity": "Critical",
        "impact": 2, "resolution_time_hours": 5.7, "sla_target_hours": 3.2, "sla_status": "Breached",
        "breached_flag": True, "aging_bucket": "0-3 days", "cim_flag": False,
        "customer_comment": "Waited too long for callback"
    },
    {
        "ticket_id": "TKT-2024-0019", "incident_id": "INC-00019", "created_date": "2024-08-04",
        "closed_date": "2024-08-05 09:39", "year": 2024, "report_period_month": "Aug", "month_num": 8,
        "analyst": "Maria Rodriguez", "geo_unit": "ACE", "assignment_group": "GBS IT-WH-CIM",
        "service": "Security", "service_offering": "PC Reimage", "category": "Performance",
        "subcategory": "Slow Response", "score": 2.4, "negative_survey_flag": True, "severity": "Medium",
        "impact": 3, "resolution_time_hours": 33.7, "sla_target_hours": 26.4, "sla_status": "Breached",
        "breached_flag": True, "aging_bucket": "0-3 days", "cim_flag": False,
        "customer_comment": "No follow-up after escalation"
    },
    {
        "ticket_id": "TKT-2024-0020", "incident_id": "INC-00020", "created_date": "2024-01-07",
        "closed_date": "2024-01-07 16:56", "year": 2024, "report_period_month": "Jan", "month_num": 1,
        "analyst": "Pedro Martinez", "geo_unit": "USL", "assignment_group": "GBS IT EH-CIM",
        "service": "Cloud Services", "service_offering": "M365", "category": "Hardware Failure",
        "subcategory": "Memory Issue", "score": 2.4, "negative_survey_flag": True, "severity": "Medium",
        "impact": 5, "resolution_time_hours": 16.9, "sla_target_hours": 28.8, "sla_status": "Within Target",
        "breached_flag": False, "aging_bucket": "0-3 days", "cim_flag": True,
        "customer_comment": "Missing documentation for resolution"
    },
    {
        "ticket_id": "TKT-2024-0021", "incident_id": "INC-00021", "created_date": "2024-10-04",
        "closed_date": "2024-10-04 20:02", "year": 2024, "report_period_month": "Oct", "month_num": 10,
        "analyst": "Ana Garcia", "geo_unit": "ECP", "assignment_group": "GBS IT-WH-CIM",
        "service": "Endpoint Services", "service_offering": "Missing patches", "category": "Hardware Failure",
        "subcategory": "Display Problem", "score": 2.3, "negative_survey_flag": True, "severity": "Medium",
        "impact": 5, "resolution_time_hours": 20.0, "sla_target_hours": 28.8, "sla_status": "Within Target",
        "breached_flag": False, "aging_bucket": "0-3 days", "cim_flag": False,
        "customer_comment": "No follow-up after escalation"
    },
    {
        "ticket_id": "TKT-2024-0022", "incident_id": "INC-00022", "created_date": "2024-05-20",
        "closed_date": "2024-05-20 17:03", "year": 2024, "report_period_month": "May", "month_num": 5,
        "analyst": "Ana Garcia", "geo_unit": "ECP", "assignment_group": "GBS IT-WH-CIM",
        "service": "Security", "service_offering": "Printing", "category": "Access Problem",
        "subcategory": "MFA Issue", "score": 2.0, "negative_survey_flag": True, "severity": "Medium",
        "impact": 2, "resolution_time_hours": 17.1, "sla_target_hours": 19.2, "sla_status": "Within Target",
        "breached_flag": False, "aging_bucket": "0-3 days", "cim_flag": False,
        "customer_comment": "No follow-up after escalation"
    },
    {
        "ticket_id": "TKT-2024-0023", "incident_id": "INC-00023", "created_date": "2024-08-10",
        "closed_date": "2024-08-10 18:30", "year": 2024, "report_period_month": "Aug", "month_num": 8,
        "analyst": "Pedro Martinez", "geo_unit": "ACE", "assignment_group": "GBS IT EH-CIM",
        "service": "Cloud Services", "service_offering": "PC Reimage", "category": "Software Issue",
        "subcategory": "License Issue", "score": 2.1, "negative_survey_flag": True, "severity": "Medium",
        "impact": 4, "resolution_time_hours": 18.5, "sla_target_hours": 24.0, "sla_status": "Within Target",
        "breached_flag": False, "aging_bucket": "0-3 days", "cim_flag": True,
        "customer_comment": "No follow-up after escalation"
    },
    {
        "ticket_id": "TKT-2024-0024", "incident_id": "INC-00024", "created_date": "2024-11-02",
        "closed_date": "2024-11-02 07:45", "year": 2024, "report_period_month": "Nov", "month_num": 11,
        "analyst": "Laura Sanchez", "geo_unit": "ABC", "assignment_group": "GBS IT EH-CIM",
        "service": "Endpoint Services", "service_offering": "Printing", "category": "Performance",
        "subcategory": "High CPU", "score": 3.0, "negative_survey_flag": True, "severity": "High",
        "impact": 1, "resolution_time_hours": 7.8, "sla_target_hours": 8.8, "sla_status": "Within Target",
        "breached_flag": False, "aging_bucket": "0-3 days", "cim_flag": False,
        "customer_comment": "Issue not resolved on first contact"
    },
    {
        "ticket_id": "TKT-2024-0025", "incident_id": "INC-00025", "created_date": "2024-10-31",
        "closed_date": "2024-10-31 20:01", "year": 2024, "report_period_month": "Oct", "month_num": 10,
        "analyst": "Ana Garcia", "geo_unit": "ACE", "assignment_group": "GBS IT-WH-CIM",
        "service": "Security", "service_offering": "MyPCP", "category": "Access Problem",
        "subcategory": "MFA Issue", "score": 2.2, "negative_survey_flag": True, "severity": "Medium",
        "impact": 1, "resolution_time_hours": 20.0, "sla_target_hours": 19.2, "sla_status": "Breached",
        "breached_flag": True, "aging_bucket": "0-3 days", "cim_flag": False,
        "customer_comment": "Solution didn't work as expected"
    },
    {
        "ticket_id": "TKT-2024-0026", "incident_id": "INC-00026", "created_date": "2024-08-07",
        "closed_date": "2024-08-07 03:45", "year": 2024, "report_period_month": "Aug", "month_num": 8,
        "analyst": "Ana Garcia", "geo_unit": "ACE", "assignment_group": "GBS IT-WH-CIM",
        "service": "Cloud Services", "service_offering": "PC Reimage", "category": "Hardware Failure",
        "subcategory": "Peripheral", "score": 3.0, "negative_survey_flag": True, "severity": "Critical",
        "impact": 2, "resolution_time_hours": 3.8, "sla_target_hours": 4.8, "sla_status": "Within Target",
        "breached_flag": False, "aging_bucket": "0-3 days", "cim_flag": False,
        "customer_comment": "Waited too long for callback"
    },
    {
        "ticket_id": "TKT-2024-0027", "incident_id": "INC-00027", "created_date": "2024-08-01",
        "closed_date": "2024-08-02 08:07", "year": 2024, "report_period_month": "Aug", "month_num": 8,
        "analyst": "Pedro Martinez", "geo_unit": "ABC", "assignment_group": "GBS IT EH-CIM",
        "service": "Endpoint Services", "service_offering": "MyPCP", "category": "Configuration",
        "subcategory": "Registry Issue", "score": 1.8, "negative_survey_flag": True, "severity": "Medium",
        "impact": 1, "resolution_time_hours": 32.1, "sla_target_hours": 21.6, "sla_status": "Breached",
        "breached_flag": True, "aging_bucket": "0-3 days", "cim_flag": False,
        "customer_comment": "Communication was unclear"
    },
    {
        "ticket_id": "TKT-2024-0028", "incident_id": "INC-00028", "created_date": "2024-05-08",
        "closed_date": "2024-05-08 05:48", "year": 2024, "report_period_month": "May", "month_num": 5,
        "analyst": "Carlos Lopez", "geo_unit": "ABC", "assignment_group": "GBS IT-WH-CIM",
        "service": "Endpoint Services", "service_offering": "MyPCP", "category": "Hardware Failure",
        "subcategory": "Memory Issue", "score": 3.0, "negative_survey_flag": True, "severity": "High",
        "impact": 1, "resolution_time_hours": 5.8, "sla_target_hours": 9.6, "sla_status": "Within Target",
        "breached_flag": False, "aging_bucket": "0-3 days", "cim_flag": False,
        "customer_comment": "No follow-up after escalation"
    },
    {
        "ticket_id": "TKT-2024-0029", "incident_id": "INC-00029", "created_date": "2024-06-12",
        "closed_date": "2024-06-12 04:28", "year": 2024, "report_period_month": "Jun", "month_num": 6,
        "analyst": "Carlos Lopez", "geo_unit": "ECP", "assignment_group": "GBS IT-WH-CIM",
        "service": "Cloud Services", "service_offering": "M365", "category": "Communication",
        "subcategory": "Misunderstanding", "score": 2.9, "negative_survey_flag": True, "severity": "Critical",
        "impact": 3, "resolution_time_hours": 4.5, "sla_target_hours": 2.8, "sla_status": "Breached",
        "breached_flag": True, "aging_bucket": "0-3 days", "cim_flag": False,
        "customer_comment": "Slow response time, very frustrating"
    },
    {
        "ticket_id": "TKT-2024-0030", "incident_id": "INC-00030", "created_date": "2024-10-04",
        "closed_date": "2024-10-05 03:27", "year": 2024, "report_period_month": "Oct", "month_num": 10,
        "analyst": "Maria Rodriguez", "geo_unit": "ACE", "assignment_group": "GBS IT-WH-CIM",
        "service": "Infrastructure", "service_offering": "M365", "category": "Configuration",
        "subcategory": "Registry Issue", "score": 2.3, "negative_survey_flag": True, "severity": "Medium",
        "impact": 1, "resolution_time_hours": 27.5, "sla_target_hours": 21.6, "sla_status": "Breached",
        "breached_flag": True, "aging_bucket": "0-3 days", "cim_flag": False,
        "customer_comment": "Waited too long for callback"
    },
    {
        "ticket_id": "TKT-2024-0031", "incident_id": "INC-00031", "created_date": "2024-11-01",
        "closed_date": "2024-11-02 01:01", "year": 2024, "report_period_month": "Nov", "month_num": 11,
        "analyst": "Laura Sanchez", "geo_unit": "USL", "assignment_group": "GBS IT EH-CIM",
        "service": "Infrastructure", "service_offering": "Printing", "category": "Performance",
        "subcategory": "Timeout", "score": 1.4, "negative_survey_flag": True, "severity": "Low",
        "impact": 1, "resolution_time_hours": 25.0, "sla_target_hours": 52.8, "sla_status": "Within Target",
        "breached_flag": False, "aging_bucket": "0-3 days", "cim_flag": False,
        "customer_comment": "No follow-up after escalation"
    },
    {
        "ticket_id": "TKT-2024-0032", "incident_id": "INC-00032", "created_date": "2024-09-17",
        "closed_date": "2024-09-18 02:10", "year": 2024, "report_period_month": "Sep", "month_num": 9,
        "analyst": "Maria Rodriguez", "geo_unit": "ACE", "assignment_group": "GBS IT-WH-CIM",
        "service": "Endpoint Services", "service_offering": "M365", "category": "Access Problem",
        "subcategory": "MFA Issue", "score": 2.0, "negative_survey_flag": True, "severity": "Medium",
        "impact": 2, "resolution_time_hours": 26.2, "sla_target_hours": 19.2, "sla_status": "Breached",
        "breached_flag": True, "aging_bucket": "0-3 days", "cim_flag": False,
        "customer_comment": "Missing documentation for resolution"
    },
    {
        "ticket_id": "TKT-2024-0033", "incident_id": "INC-00033", "created_date": "2024-08-19",
        "closed_date": "2024-08-19 09:47", "year": 2024, "report_period_month": "Aug", "month_num": 8,
        "analyst": "Laura Sanchez", "geo_unit": "ABC", "assignment_group": "GBS IT EH-CIM",
        "service": "Endpoint Services", "service_offering": "PC Reimage", "category": "Software Issue",
        "subcategory": "License Issue", "score": 2.6, "negative_survey_flag": True, "severity": "High",
        "impact": 4, "resolution_time_hours": 9.8, "sla_target_hours": 8.0, "sla_status": "Breached",
        "breached_flag": True, "aging_bucket": "0-3 days", "cim_flag": False,
        "customer_comment": "Technical knowledge was lacking"
    },
    {
        "ticket_id": "TKT-2024-0034", "incident_id": "INC-00034", "created_date": "2024-10-17",
        "closed_date": "2024-10-17 06:33", "year": 2024, "report_period_month": "Oct", "month_num": 10,
        "analyst": "Laura Sanchez", "geo_unit": "ECP", "assignment_group": "GBS IT EH-CIM",
        "service": "Infrastructure", "service_offering": "MyPCP", "category": "Configuration",
        "subcategory": "Missing Config", "score": 2.5, "negative_survey_flag": True, "severity": "High",
        "impact": 2, "resolution_time_hours": 6.6, "sla_target_hours": 7.2, "sla_status": "Within Target",
        "breached_flag": False, "aging_bucket": "0-3 days", "cim_flag": True,
        "customer_comment": "No follow-up after escalation"
    },
    {
        "ticket_id": "TKT-2024-0035", "incident_id": "INC-00035", "created_date": "2024-03-08",
        "closed_date": "2024-03-08 19:48", "year": 2024, "report_period_month": "Mar", "month_num": 3,
        "analyst": "Maria Rodriguez", "geo_unit": "ACE", "assignment_group": "GBS IT-WH-CIM",
        "service": "Cloud Services", "service_offering": "Missing patches", "category": "Software Issue",
        "subcategory": "Compatibility", "score": 2.4, "negative_survey_flag": True, "severity": "Medium",
        "impact": 4, "resolution_time_hours": 19.8, "sla_target_hours": 24.0, "sla_status": "Within Target",
        "breached_flag": False, "aging_bucket": "0-3 days", "cim_flag": False,
        "customer_comment": "Communication was unclear"
    },
    {
        "ticket_id": "TKT-2024-0036", "incident_id": "INC-00036", "created_date": "2024-11-13",
        "closed_date": "2024-11-14 09:17", "year": 2024, "report_period_month": "Nov", "month_num": 11,
        "analyst": "Maria Rodriguez", "geo_unit": "BRZ", "assignment_group": "GBS IT-WH-CIM",
        "service": "Endpoint Services", "service_offering": "PC Reimage", "category": "Software Issue",
        "subcategory": "App Crash", "score": 2.6, "negative_survey_flag": True, "severity": "Medium",
        "impact": 1, "resolution_time_hours": 33.3, "sla_target_hours": 24.0, "sla_status": "Breached",
        "breached_flag": True, "aging_bucket": "0-3 days", "cim_flag": False,
        "customer_comment": "Problem recurred after fix"
    },
    {
        "ticket_id": "TKT-2024-0037", "incident_id": "INC-00037", "created_date": "2024-11-08",
        "closed_date": "2024-11-08 04:52", "year": 2024, "report_period_month": "Nov", "month_num": 11,
        "analyst": "Laura Sanchez", "geo_unit": "ACE", "assignment_group": "GBS IT EH-CIM",
        "service": "Security", "service_offering": "Missing patches", "category": "Software Issue",
        "subcategory": "Compatibility", "score": 3.1, "negative_survey_flag": True, "severity": "Critical",
        "impact": 5, "resolution_time_hours": 4.9, "sla_target_hours": 4.0, "sla_status": "Breached",
        "breached_flag": True, "aging_bucket": "0-3 days", "cim_flag": False,
        "customer_comment": "Waited too long for callback"
    },
    {
        "ticket_id": "TKT-2024-0038", "incident_id": "INC-00038", "created_date": "2024-02-27",
        "closed_date": "2024-02-27 10:53", "year": 2024, "report_period_month": "Feb", "month_num": 2,
        "analyst": "Laura Sanchez", "geo_unit": "BRZ", "assignment_group": "GBS IT EH-CIM",
        "service": "Security", "service_offering": "M365", "category": "Software Issue",
        "subcategory": "Compatibility", "score": 2.5, "negative_survey_flag": True, "severity": "High",
        "impact": 5, "resolution_time_hours": 10.9, "sla_target_hours": 8.0, "sla_status": "Breached",
        "breached_flag": True, "aging_bucket": "0-3 days", "cim_flag": False,
        "customer_comment": "Communication was unclear"
    },
    {
        "ticket_id": "TKT-2024-0039", "incident_id": "INC-00039", "created_date": "2024-07-21",
        "closed_date": "2024-07-21 22:55", "year": 2024, "report_period_month": "Jul", "month_num": 7,
        "analyst": "Pedro Martinez", "geo_unit": "USL", "assignment_group": "GBS IT EH-CIM",
        "service": "Endpoint Services", "service_offering": "M365", "category": "Configuration",
        "subcategory": "Missing Config", "score": 2.0, "negative_survey_flag": True, "severity": "Medium",
        "impact": 2, "resolution_time_hours": 22.9, "sla_target_hours": 21.6, "sla_status": "Breached",
        "breached_flag": True, "aging_bucket": "0-3 days", "cim_flag": True,
        "customer_comment": "Waited too long for callback"
    },
    {
        "ticket_id": "TKT-2024-0040", "incident_id": "INC-00040", "created_date": "2024-09-23",
        "closed_date": "2024-09-23 19:38", "year": 2024, "report_period_month": "Sep", "month_num": 9,
        "analyst": "Pedro Martinez", "geo_unit": "ACE", "assignment_group": "GBS IT EH-CIM",
        "service": "Endpoint Services", "service_offering": "Missing patches", "category": "Access Problem",
        "subcategory": "MFA Issue", "score": 2.6, "negative_survey_flag": True, "severity": "Medium",
        "impact": 4, "resolution_time_hours": 19.6, "sla_target_hours": 19.2, "sla_status": "Breached",
        "breached_flag": True, "aging_bucket": "0-3 days", "cim_flag": False,
        "customer_comment": "Missing documentation for resolution"
    },
    {
        "ticket_id": "TKT-2024-0041", "incident_id": "INC-00041", "created_date": "2024-02-23",
        "closed_date": "2024-02-24 00:29", "year": 2024, "report_period_month": "Feb", "month_num": 2,
        "analyst": "Laura Sanchez", "geo_unit": "ECP", "assignment_group": "GBS IT EH-CIM",
        "service": "Endpoint Services", "service_offering": "MyPCP", "category": "Performance",
        "subcategory": "Memory Leak", "score": 2.2, "negative_survey_flag": True, "severity": "Medium",
        "impact": 4, "resolution_time_hours": 24.5, "sla_target_hours": 26.4, "sla_status": "Within Target",
        "breached_flag": False, "aging_bucket": "0-3 days", "cim_flag": False,
        "customer_comment": "Problem recurred after fix"
    },
    {
        "ticket_id": "TKT-2024-0042", "incident_id": "INC-00042", "created_date": "2024-08-24",
        "closed_date": "2024-08-25 05:19", "year": 2024, "report_period_month": "Aug", "month_num": 8,
        "analyst": "Pedro Martinez", "geo_unit": "ABC", "assignment_group": "GBS IT EH-CIM",
        "service": "Cloud Services", "service_offering": "Printing", "category": "Documentation",
        "subcategory": "No SOP", "score": 1.8, "negative_survey_flag": True, "severity": "Medium",
        "impact": 4, "resolution_time_hours": 29.3, "sla_target_hours": 36.0, "sla_status": "Within Target",
        "breached_flag": False, "aging_bucket": "0-3 days", "cim_flag": False,
        "customer_comment": "Had to call multiple times for same issue"
    },
    {
        "ticket_id": "TKT-2024-0043", "incident_id": "INC-00043", "created_date": "2024-02-27",
        "closed_date": "2024-02-28 23:58", "year": 2024, "report_period_month": "Feb", "month_num": 2,
        "analyst": "Carlos Lopez", "geo_unit": "BRZ", "assignment_group": "GBS IT-WH-CIM",
        "service": "Infrastructure", "service_offering": "Missing patches", "category": "Performance",
        "subcategory": "Slow Response", "score": 1.6, "negative_survey_flag": True, "severity": "Low",
        "impact": 4, "resolution_time_hours": 48.0, "sla_target_hours": 52.8, "sla_status": "Within Target",
        "breached_flag": False, "aging_bucket": "0-3 days", "cim_flag": True,
        "customer_comment": "Had to call multiple times for same issue"
    },
    {
        "ticket_id": "TKT-2024-0044", "incident_id": "INC-00044", "created_date": "2024-02-02",
        "closed_date": "2024-02-02 06:27", "year": 2024, "report_period_month": "Feb", "month_num": 2,
        "analyst": "Laura Sanchez", "geo_unit": "BRZ", "assignment_group": "GBS IT EH-CIM",
        "service": "Endpoint Services", "service_offering": "M365", "category": "Access Problem",
        "subcategory": "MFA Issue", "score": 2.7, "negative_survey_flag": True, "severity": "High",
        "impact": 1, "resolution_time_hours": 6.5, "sla_target_hours": 6.4, "sla_status": "Breached",
        "breached_flag": True, "aging_bucket": "0-3 days", "cim_flag": True,
        "customer_comment": "Communication was unclear"
    },
    {
        "ticket_id": "TKT-2024-0045", "incident_id": "INC-00045", "created_date": "2024-04-01",
        "closed_date": "2024-04-01 07:35", "year": 2024, "report_period_month": "Apr", "month_num": 4,
        "analyst": "Ana Garcia", "geo_unit": "ECP", "assignment_group": "GBS IT-WH-CIM",
        "service": "Cloud Services", "service_offering": "Missing patches", "category": "Communication",
        "subcategory": "Delayed Response", "score": 2.1, "negative_survey_flag": True, "severity": "High",
        "impact": 1, "resolution_time_hours": 7.6, "sla_target_hours": 5.6, "sla_status": "Breached",
        "breached_flag": True, "aging_bucket": "0-3 days", "cim_flag": False,
        "customer_comment": "Missing documentation for resolution"
    },
    {
        "ticket_id": "TKT-2024-0046", "incident_id": "INC-00046", "created_date": "2024-04-05",
        "closed_date": "2024-04-05 12:14", "year": 2024, "report_period_month": "Apr", "month_num": 4,
        "analyst": "Pedro Martinez", "geo_unit": "BRZ", "assignment_group": "GBS IT EH-CIM",
        "service": "Endpoint Services", "service_offering": "M365", "category": "Software Issue",
        "subcategory": "Update Failed", "score": 2.5, "negative_survey_flag": True, "severity": "High",
        "impact": 1, "resolution_time_hours": 12.2, "sla_target_hours": 8.0, "sla_status": "Breached",
        "breached_flag": True, "aging_bucket": "0-3 days", "cim_flag": False,
        "customer_comment": "Had to call multiple times for same issue"
    },
    {
        "ticket_id": "TKT-2024-0047", "incident_id": "INC-00047", "created_date": "2024-04-10",
        "closed_date": "2024-04-12 21:35", "year": 2024, "report_period_month": "Apr", "month_num": 4,
        "analyst": "Maria Rodriguez", "geo_unit": "BRZ", "assignment_group": "GBS IT-WH-CIM",
        "service": "Endpoint Services", "service_offering": "Missing patches", "category": "Hardware Failure",
        "subcategory": "Peripheral", "score": 2.1, "negative_survey_flag": True, "severity": "Low",
        "impact": 2, "resolution_time_hours": 69.6, "sla_target_hours": 57.6, "sla_status": "Breached",
        "breached_flag": True, "aging_bucket": "0-3 days", "cim_flag": False,
        "customer_comment": "Issue not resolved on first contact"
    },
    {
        "ticket_id": "TKT-2024-0048", "incident_id": "INC-00048", "created_date": "2024-01-23",
        "closed_date": "2024-01-24 10:25", "year": 2024, "report_period_month": "Jan", "month_num": 1,
        "analyst": "Carlos Lopez", "geo_unit": "ACE", "assignment_group": "GBS IT-WH-CIM",
        "service": "Cloud Services", "service_offering": "Printing", "category": "Performance",
        "subcategory": "Slow Response", "score": 2.2, "negative_survey_flag": True, "severity": "Medium",
        "impact": 1, "resolution_time_hours": 34.4, "sla_target_hours": 26.4, "sla_status": "Breached",
        "breached_flag": True, "aging_bucket": "0-3 days", "cim_flag": False,
        "customer_comment": "Problem recurred after fix"
    },
    {
        "ticket_id": "TKT-2024-0049", "incident_id": "INC-00049", "created_date": "2024-02-21",
        "closed_date": "2024-02-21 05:39", "year": 2024, "report_period_month": "Feb", "month_num": 2,
        "analyst": "Laura Sanchez", "geo_unit": "BRZ", "assignment_group": "GBS IT EH-CIM",
        "service": "Endpoint Services", "service_offering": "Printing", "category": "Configuration",
        "subcategory": "Wrong Settings", "score": 2.6, "negative_survey_flag": True, "severity": "High",
        "impact": 4, "resolution_time_hours": 5.7, "sla_target_hours": 7.2, "sla_status": "Within Target",
        "breached_flag": False, "aging_bucket": "0-3 days", "cim_flag": False,
        "customer_comment": "Had to call multiple times for same issue"
    },
    {
        "ticket_id": "TKT-2024-0050", "incident_id": "INC-00050", "created_date": "2024-09-24",
        "closed_date": "2024-09-24 06:59", "year": 2024, "report_period_month": "Sep", "month_num": 9,
        "analyst": "Laura Sanchez", "geo_unit": "BRZ", "assignment_group": "GBS IT EH-CIM",
        "service": "Infrastructure", "service_offering": "PC Reimage", "category": "Performance",
        "subcategory": "Memory Leak", "score": 3.2, "negative_survey_flag": True, "severity": "Critical",
        "impact": 2, "resolution_time_hours": 7.0, "sla_target_hours": 4.4, "sla_status": "Breached",
        "breached_flag": True, "aging_bucket": "0-3 days", "cim_flag": False,
        "customer_comment": "Issue not resolved on first contact"
    }
]

ACTION_ITEMS_DATA = [
    {
        "action_id": "ACT-001", "linked_ticket_id": "TKT-2024-0014", "issue_category": "Software Issue",
        "owner": "Service Excellence", "status": "Overdue", "created_date": "2024-02-14",
        "due_date": "2024-02-29", "completion_date": None, "overdue_flag": True,
        "action_description": "Implement automated monitoring", "implemented_flag": False
    },
    {
        "action_id": "ACT-002", "linked_ticket_id": "TKT-2024-0040", "issue_category": "Access Problem",
        "owner": "Manager", "status": "Pending", "created_date": "2024-09-23",
        "due_date": "2024-10-18", "completion_date": None, "overdue_flag": True,
        "action_description": "Escalate to vendor for resolution", "implemented_flag": False
    },
    {
        "action_id": "ACT-003", "linked_ticket_id": "TKT-2024-0031", "issue_category": "Performance",
        "owner": "Team Lead", "status": "In Progress", "created_date": "2024-11-01",
        "due_date": "2024-11-08", "completion_date": None, "overdue_flag": False,
        "action_description": "Implement additional training session", "implemented_flag": False
    },
    {
        "action_id": "ACT-004", "linked_ticket_id": "TKT-2024-0046", "issue_category": "Software Issue",
        "owner": "Team Lead", "status": "Completed", "created_date": "2024-04-05",
        "due_date": "2024-04-27", "completion_date": "2024-04-25", "overdue_flag": False,
        "action_description": "Schedule follow-up with customer", "implemented_flag": True
    },
    {
        "action_id": "ACT-005", "linked_ticket_id": "TKT-2024-0018", "issue_category": "Access Problem",
        "owner": "Team Lead", "status": "Pending", "created_date": "2024-06-24",
        "due_date": "2024-07-20", "completion_date": None, "overdue_flag": True,
        "action_description": "Review and update troubleshooting procedures", "implemented_flag": False
    },
    {
        "action_id": "ACT-006", "linked_ticket_id": "TKT-2024-0049", "issue_category": "Configuration",
        "owner": "Continuous Improvement", "status": "Overdue", "created_date": "2024-02-21",
        "due_date": "2024-03-15", "completion_date": None, "overdue_flag": True,
        "action_description": "Update knowledge base article", "implemented_flag": False
    },
    {
        "action_id": "ACT-007", "linked_ticket_id": "TKT-2024-0027", "issue_category": "Configuration",
        "owner": "Service Excellence", "status": "In Progress", "created_date": "2024-08-01",
        "due_date": "2024-08-31", "completion_date": None, "overdue_flag": False,
        "action_description": "Implement automated monitoring", "implemented_flag": False
    },
    {
        "action_id": "ACT-008", "linked_ticket_id": "TKT-2024-0026", "issue_category": "Hardware Failure",
        "owner": "Manager", "status": "Pending", "created_date": "2024-08-07",
        "due_date": "2024-09-03", "completion_date": None, "overdue_flag": True,
        "action_description": "Review and update troubleshooting procedures", "implemented_flag": False
    },
    {
        "action_id": "ACT-009", "linked_ticket_id": "TKT-2024-0033", "issue_category": "Software Issue",
        "owner": "Service Excellence", "status": "Completed", "created_date": "2024-08-19",
        "due_date": "2024-08-28", "completion_date": "2024-08-25", "overdue_flag": False,
        "action_description": "Schedule follow-up with customer", "implemented_flag": True
    },
    {
        "action_id": "ACT-010", "linked_ticket_id": "TKT-2024-0020", "issue_category": "Hardware Failure",
        "owner": "Manager", "status": "Pending", "created_date": "2024-01-07",
        "due_date": "2024-02-04", "completion_date": None, "overdue_flag": True,
        "action_description": "Escalate to vendor for resolution", "implemented_flag": False
    },
    {
        "action_id": "ACT-011", "linked_ticket_id": "TKT-2024-0013", "issue_category": "Configuration",
        "owner": "Team Lead", "status": "Overdue", "created_date": "2024-03-22",
        "due_date": "2024-04-11", "completion_date": None, "overdue_flag": True,
        "action_description": "Escalate to vendor for resolution", "implemented_flag": False
    },
    {
        "action_id": "ACT-012", "linked_ticket_id": "TKT-2024-0005", "issue_category": "Performance",
        "owner": "Team Lead", "status": "In Progress", "created_date": "2024-02-24",
        "due_date": "2024-03-24", "completion_date": None, "overdue_flag": False,
        "action_description": "Schedule follow-up with customer", "implemented_flag": False
    },
    {
        "action_id": "ACT-013", "linked_ticket_id": "TKT-2024-0038", "issue_category": "Software Issue",
        "owner": "Team Lead", "status": "Completed", "created_date": "2024-02-27",
        "due_date": "2024-03-12", "completion_date": "2024-03-11", "overdue_flag": False,
        "action_description": "Conduct root cause analysis", "implemented_flag": True
    },
    {
        "action_id": "ACT-014", "linked_ticket_id": "TKT-2024-0009", "issue_category": "Documentation",
        "owner": "Service Excellence", "status": "In Progress", "created_date": "2024-08-20",
        "due_date": "2024-09-19", "completion_date": None, "overdue_flag": False,
        "action_description": "Update knowledge base article", "implemented_flag": False
    },
    {
        "action_id": "ACT-015", "linked_ticket_id": "TKT-2024-0004", "issue_category": "Communication",
        "owner": "Team Lead", "status": "Pending", "created_date": "2024-03-13",
        "due_date": "2024-03-26", "completion_date": None, "overdue_flag": True,
        "action_description": "Schedule follow-up with customer", "implemented_flag": False
    },
    {
        "action_id": "ACT-016", "linked_ticket_id": "TKT-2024-0007", "issue_category": "Configuration",
        "owner": "Team Lead", "status": "Overdue", "created_date": "2024-07-18",
        "due_date": "2024-07-28", "completion_date": None, "overdue_flag": True,
        "action_description": "Update knowledge base article", "implemented_flag": False
    },
    {
        "action_id": "ACT-017", "linked_ticket_id": "TKT-2024-0042", "issue_category": "Documentation",
        "owner": "Service Excellence", "status": "Completed", "created_date": "2024-08-24",
        "due_date": "2024-09-11", "completion_date": "2024-09-11", "overdue_flag": False,
        "action_description": "Schedule follow-up with customer", "implemented_flag": True
    },
    {
        "action_id": "ACT-018", "linked_ticket_id": "TKT-2024-0047", "issue_category": "Hardware Failure",
        "owner": "Team Lead", "status": "Overdue", "created_date": "2024-04-10",
        "due_date": "2024-04-18", "completion_date": None, "overdue_flag": True,
        "action_description": "Implement additional training session", "implemented_flag": False
    },
    {
        "action_id": "ACT-019", "linked_ticket_id": "TKT-2024-0048", "issue_category": "Performance",
        "owner": "Manager", "status": "Overdue", "created_date": "2024-01-23",
        "due_date": "2024-02-19", "completion_date": None, "overdue_flag": True,
        "action_description": "Conduct root cause analysis", "implemented_flag": False
    },
    {
        "action_id": "ACT-020", "linked_ticket_id": "TKT-2024-0016", "issue_category": "Documentation",
        "owner": "Manager", "status": "Pending", "created_date": "2024-09-06",
        "due_date": "2024-09-13", "completion_date": None, "overdue_flag": True,
        "action_description": "Implement automated monitoring", "implemented_flag": False
    },
    {
        "action_id": "ACT-021", "linked_ticket_id": "TKT-2024-0010", "issue_category": "Configuration",
        "owner": "Team Lead", "status": "Completed", "created_date": "2024-04-27",
        "due_date": "2024-05-18", "completion_date": "2024-05-18", "overdue_flag": False,
        "action_description": "Implement automated monitoring", "implemented_flag": True
    },
    {
        "action_id": "ACT-022", "linked_ticket_id": "TKT-2024-0017", "issue_category": "Configuration",
        "owner": "Manager", "status": "Overdue", "created_date": "2024-03-14",
        "due_date": "2024-03-24", "completion_date": None, "overdue_flag": True,
        "action_description": "Implement automated monitoring", "implemented_flag": False
    },
    {
        "action_id": "ACT-023", "linked_ticket_id": "TKT-2024-0025", "issue_category": "Access Problem",
        "owner": "Continuous Improvement", "status": "Pending", "created_date": "2024-10-31",
        "due_date": "2024-11-09", "completion_date": None, "overdue_flag": True,
        "action_description": "Implement additional training session", "implemented_flag": False
    },
    {
        "action_id": "ACT-024", "linked_ticket_id": "TKT-2024-0035", "issue_category": "Software Issue",
        "owner": "Team Lead", "status": "Overdue", "created_date": "2024-03-08",
        "due_date": "2024-03-19", "completion_date": None, "overdue_flag": True,
        "action_description": "Conduct root cause analysis", "implemented_flag": False
    },
    {
        "action_id": "ACT-025", "linked_ticket_id": "TKT-2024-0032", "issue_category": "Access Problem",
        "owner": "Service Excellence", "status": "Completed", "created_date": "2024-09-17",
        "due_date": "2024-10-01", "completion_date": "2024-09-28", "overdue_flag": False,
        "action_description": "Create standard operating procedure", "implemented_flag": True
    },
    {
        "action_id": "ACT-026", "linked_ticket_id": "TKT-2024-0001", "issue_category": "Software Issue",
        "owner": "Team Lead", "status": "Overdue", "created_date": "2024-07-18",
        "due_date": "2024-08-08", "completion_date": None, "overdue_flag": True,
        "action_description": "Create standard operating procedure", "implemented_flag": False
    },
    {
        "action_id": "ACT-027", "linked_ticket_id": "TKT-2024-0045", "issue_category": "Communication",
        "owner": "Continuous Improvement", "status": "Pending", "created_date": "2024-04-01",
        "due_date": "2024-04-17", "completion_date": None, "overdue_flag": True,
        "action_description": "Conduct root cause analysis", "implemented_flag": False
    },
    {
        "action_id": "ACT-028", "linked_ticket_id": "TKT-2024-0028", "issue_category": "Hardware Failure",
        "owner": "Team Lead", "status": "Pending", "created_date": "2024-05-08",
        "due_date": "2024-05-21", "completion_date": None, "overdue_flag": True,
        "action_description": "Conduct root cause analysis", "implemented_flag": False
    },
    {
        "action_id": "ACT-029", "linked_ticket_id": "TKT-2024-0034", "issue_category": "Configuration",
        "owner": "Continuous Improvement", "status": "Completed", "created_date": "2024-10-17",
        "due_date": "2024-10-29", "completion_date": "2024-10-25", "overdue_flag": False,
        "action_description": "Implement additional training session", "implemented_flag": True
    },
    {
        "action_id": "ACT-030", "linked_ticket_id": "TKT-2024-0006", "issue_category": "Configuration",
        "owner": "Manager", "status": "In Progress", "created_date": "2024-10-28",
        "due_date": "2024-11-04", "completion_date": None, "overdue_flag": False,
        "action_description": "Schedule follow-up with customer", "implemented_flag": False
    }
]
