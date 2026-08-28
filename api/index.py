import sys
from pathlib import Path

# Add project root to Python module search path
project_root = Path(__file__).parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from main import app

# Vercel ASGI serverless handler exports
handler = app
application = app
