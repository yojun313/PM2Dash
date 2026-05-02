# uvicorn app.main:app --host 0.0.0.0 --port 3004 --reload

import uvicorn
import warnings
from requests.exceptions import RequestsDependencyWarning

warnings.filterwarnings("ignore", category=RequestsDependencyWarning)

if __name__ == "__main__":
    print("Starting PM2 Dashboard...")
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        log_level="warning",
        access_log=False,
        timeout_keep_alive=86400,
    )