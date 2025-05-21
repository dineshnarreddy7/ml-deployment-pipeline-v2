

````markdown
# 🚀 ML Deployment Pipeline (FastAPI + Transformers)

This project demonstrates how to deploy a Machine Learning model using FastAPI and Hugging Face Transformers. It includes endpoints to check service status, deploy a model, and generate completions from user messages. Automated tests are included using `pytest`.

---

## ✨ Features

- Deploy a Hugging Face transformer model dynamically via API.
- Check deployment status.
- Generate completions using the deployed model.
- Includes automated API tests using `pytest`.

---

## ⚙️ Requirements

- Python 3.8+
- pip
- Git
- Docker (for containerized deployment)

---

## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/dineshnarreddy7/ml-deployment-pipeline-v2.git
cd ml-deployment-pipeline-v2
````

### 2. Create and activate virtual environment (optional but recommended)

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🧪 Running the Tests

Make sure you're in the project root folder.

```bash
pytest Technical_Test/test.py
```

---

## 🐳 Docker Deployment

### Step 1: Build the Docker image

```bash
docker build -t ml-deployment-app .
```

### Step 2: Run the Docker container

```bash
docker run -p 8000:8000 ml-deployment-app
```

### Step 3: Access the API

* Status check: [http://localhost:8000/status](http://localhost:8000/status)
* Deploy model: `POST /model` with JSON body:

  ```json
  {
    "model_name": "gpt2"
  }
  ```
* Generate reply: `POST /completion` with JSON body:

  ```json
  {
    "messages": ["Hello, how are you?"]
  }
  ```

---

## 👨‍💻 Author

**Dinesh Narreddy**

[GitHub Profile](https://github.com/dineshnarreddy7)

---

## 📝 License

This test project is for educational/demo purposes only.

````