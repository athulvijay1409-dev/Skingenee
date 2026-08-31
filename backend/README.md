# Skingenee Backend

## Setup

```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\\Scripts\\activate
pip install fastapi uvicorn sqlalchemy pydantic python-multipart pillow torch torchvision
```

## Initialize database + seed sample products

```bash
python seed.py
```

This creates these tables:
- `products`
- `scans`
- `order_clicks`
