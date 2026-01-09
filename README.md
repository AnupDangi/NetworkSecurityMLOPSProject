# NetworkSecurityMLOPSProject

This project is a comprehensive Machine Learning Operations (MLOps) solution designed for Network Security, specifically focusing on phishing data detection. It implements a full ML pipeline including data ingestion, validation, transformation, model training, and deployment using FastAPI and Docker.

## Project Structure

The project is organized into several key modules:

```
NetworkSecurityMLOPSProject/
├── networksecurity/         # Main package
│   ├── components/          # ML Pipeline components (Ingestion, Validation, Transformation, Model Trainer)
│   ├── pipeline/            # Pipeline orchestration (Training Pipeline)
│   ├── entity/              # Config and Artifact definitions
│   ├── constant/            # Constants used across the project
│   ├── utils/               # Utility functions
│   └── exception/           # Custom exception handling
├── app.py                   # FastAPI application entry point
├── main.py                  # Script to run the training pipeline manually
├── push_data.py             # Script to seed data into MongoDB
├── Dockerfile               # Docker configuration for containerization
├── requirements.txt         # Project dependencies
└── ...
```

## Prerequisites

- Python 3.10+
- MongoDB (Atlas or Local)
- AWS Account (optional, for deployment)
- DagsHub/MLflow Account (optional, for experiment tracking)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/AnupDangi/NetworkSecurityMLOPSProject.git
   cd NetworkSecurityMLOPSProject
   ```

2. Create and activate a virtual environment (recommended):

   ```bash
   conda create -n networksecurity python=3.10 -y
   conda activate networksecurity
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

Create a `.env` file in the root directory and add your MongoDB connection string:

```env
MONGODB_URL="mongodb+srv://<username>:<password>@cluster0.mongodb.net/?retryWrites=true&w=majority"
```

## Data Setup

To initialize the database with network security data, use the `push_data.py` script. This script reads source data (e.g., CSV) and pushes it to your configured MongoDB instance.

```bash
python push_data.py
```

_Note: Ensure you have the source data file available as expected by the script._

## Usage

### Running the Web API (FastAPI)

The application exposes a REST API for interaction.

1. Start the server:

   ```bash
   python app.py
   ```

   The application will run on `http://localhost:8080`.

2. Access the API documentation (Swagger UI):
   Open your browser and navigate to `http://localhost:8080/docs`.

3. **Train Model via API:**
   You can trigger the training pipeline by sending a GET request to the `/train` endpoint.

### Running the Training Pipeline Manually

You can also run the complete training pipeline directly from the command line:

```bash
python main.py
```

This will execute the following steps in order:

1. **Data Ingestion:** Fetch data from MongoDB.
2. **Data Validation:** Validate data schema and statistics.
3. **Data Transformation:** Preprocess data for training.
4. **Model Training:** Train the model and save the artifact.

## Docker Support

To build and run the application using Docker:

1. **Build the image:**

   ```bash
   docker build -t networksecurity .
   ```

2. **Run the container:**
   ```bash
   docker run -p 8080:8080 -e MONGODB_URL="your_mongodb_url" networksecurity
   ```

## MLOps Integration

The project is set up to work with MLflow and DagsHub for experiment tracking. Ensure your environment variables for MLflow are set if you wish to track experiments.

## License

[MIT](LICENSE)
