from logging import getLogger
from pathlib import Path
import subprocess

BASE_DIR = Path(__file__).resolve().parent.parent

log = getLogger(__name__)

def spin_container(workspace_perm="ro", extra_flags=[]) -> subprocess.CompletedProcess:
    # --rm                      remove the container automatically after it exits
    # --network none            no network access from inside the container
    # --memory 256m             hard memory cap
    # --cpus 0.5                limit CPU cores
    # --cap-drop ALL            drop all Linux capabilities (least-privilege)
    # --pids-limit 50           max number of processes/threads (prevents fork bombs)
    # --security-opt ...        prevent processes from gaining new privileges via setuid
    # --ulimit fsize=...        cap any single file write to a max size
    # -v speller:/speller:rw    mount distribution code read-write (compiled output lands here)
    # -v submission:...  :ro    mount student submission files as read-only

    # TODO better to externalize resource limits and docker settings to .env file
    command = [
        "docker", "run", "--rm",
        "--network", "none",
        "--memory", "256m",
        "--cpus", "0.5",
        "--cap-drop", "ALL",
        "--pids-limit", "50",
        "--security-opt", "no-new-privileges",
        "--ulimit", "fsize=26214400",
        "-v", f"{BASE_DIR / 'speller'}:/speller:rw",
        "-v", f"{BASE_DIR / 'speller_workspace'}:/speller_workspace:{workspace_perm}",
        "--entrypoint", "sh",
        "bigboard-sandbox", "/speller_workspace/docker_entry.sh"
    ] + extra_flags

    return subprocess.run(command,
        capture_output=True,
        text=True,
        timeout=20,
    )