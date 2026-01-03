from fastapi import Depends, HTTPException
from jwt_utils import decode_token

ROLE_PERMISSIONS = {
    "admin": {"view_incidents", "trigger_analysis", "inject_chaos"},
    "engineer": {"view_incidents", "trigger_analysis"},
    "viewer": {"view_incidents"}
}

def require_permission(permission: str):
    def checker(token: str):
        payload = decode_token(token)
        role = payload.get("role")

        if role not in ROLE_PERMISSIONS:
            raise HTTPException(status_code=403, detail="Invalid role")

        if permission not in ROLE_PERMISSIONS[role]:
            raise HTTPException(status_code=403, detail="Permission denied")

        return payload

    return checker
