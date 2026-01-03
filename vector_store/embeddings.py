import psycopg2
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-mpnet-base-v2")

def similar_incidents(event, limit=3):
    conn = psycopg2.connect(
        dbname="rca",
        user="postgres",
        password="postgres",
        host="localhost",
        port=5432
    )
    cur = conn.cursor()

    query_embedding = model.encode(
        f"{event['service_name']} {event['metric']}"
    ).tolist()

    cur.execute(
        """
        SELECT description
        FROM incidents
        ORDER BY embedding <-> %s
        LIMIT %s
        """,
        (query_embedding, limit)
    )

    results = [r[0] for r in cur.fetchall()]
    cur.close()
    conn.close()
    return results
