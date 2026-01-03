import numpy as np


def is_anomaly(event):
    return event['metric'] == '5xx' and event['value'] > 0.05