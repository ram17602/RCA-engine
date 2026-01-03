from .mcp_tools import fetch_logs, fetch_commits
from vector_store import similar_incidents


def generate_rca(event):
    past = similar_incidents(event)
    logs = fetch_logs(event['service'])
    commits = fetch_commits(event['service'])
    return {
    "summary": "Probable deployment regression",
    "past": past,
    "logs": logs,
    "commits": commits
    }