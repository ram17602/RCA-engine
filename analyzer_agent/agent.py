from .anomaly import is_anomaly
from .rca import generate_rca
from .redis_lock import acquire_lock, release_lock

def handle_event(event: dict):
    if not is_anomaly(event):
        return {"status": "normal"}

    incident_id = event["service_name"]

    if not acquire_lock(incident_id):
        return {"status": "already_processing"}

    try:
        report = generate_rca(event)
        return {
            "status": "analyzed",
            "report": report
        }
    finally:
        release_lock(incident_id)
