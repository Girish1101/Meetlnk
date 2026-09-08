import sys
from pathlib import Path

# Ensure parent directory (backend) is in sys.path so app imports resolve
sys.path.insert(0, str(Path(__file__).parent.parent.resolve()))

from main import app

# Vercel Serverless Function entry point
handler = app
