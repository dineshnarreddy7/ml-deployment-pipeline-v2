# ML Deployment Pipeline (FastAPI)

This project serves a Machine Learning model using FastAPI and is packaged in a Docker container.

## 🔧 Tech Stack
- Python 3.12
- FastAPI
- Uvicorn
- Transformers
- Docker
- GitHub Actions

## 📦 Local Development

```bash
# Create and activate virtual environment
python -m venv venv
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the API
uvicorn serving.main:app --reload


