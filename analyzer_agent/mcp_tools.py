import subprocess
def fetch_logs(service):
    return subprocess.getoutput(f"kubectl logs deploy/{service}")
def fetch_commits(service):
    return subprocess.getoutput("git log -5 --oneline")