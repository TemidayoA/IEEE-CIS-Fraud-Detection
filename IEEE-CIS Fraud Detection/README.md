# Fraud Detection Project

## Overview
This is a **production-ready end-to-end fraud detection system** built with Python.  
The project uses real-world e-commerce transaction and identity data to predict fraudulent transactions.  
It includes:

- Data preprocessing and feature engineering
- LightGBM-based model training
- Model evaluation
- Clean and modular project structure
- Notebook for exploration
- Ready for API deployment

---

## Project Structure
fraud-detection/
├── 📁 configs/                 # Configuration files
│   ├── training.yaml          # Training hyperparameters
│   ├── inference.yaml         # Serving configuration
│   └── monitoring.yaml        # Alert thresholds
│
├── 📁 data/                    # Data management
│   ├── raw/                   # Raw transaction data
│   ├── processed/             # Feature engineered data
│   └── feature_store/         # Online feature store
│
├── 📁 src/                     # Source code
│   ├── 📁 api/                # FastAPI application
│   ├── 📁 models/             # ML model implementations
│   ├── 📁 features/           # Feature engineering
│   ├── 📁 monitoring/         # Performance tracking
│   └── 📁 utils/              # Shared utilities
│
├── 📁 models/                  # Trained model artifacts
│   ├── fraud_v1/              # Versioned model packages
│   └── champion_challenger/   # A/B test models
│
├── 📁 notebooks/               # Research & analysis
│   ├── EDA.ipynb              # Exploratory analysis
│   ├── feature_analysis.ipynb # Feature importance
│   └── model_experiments.ipynb# Hyperparameter tuning
│
├── 📁 tests/                   # Test suite
│   ├── unit/                  # Unit tests
│   ├── integration/           # Integration tests
│   └── performance/           # Load tests
│
├── 📁 deployment/              # Deployment configurations
│   ├── docker/                # Container definitions
│   ├── kubernetes/            # K8s manifests
│   └── terraform/             # Infrastructure as code
│
├── requirements.txt           # Python dependencies
├── Dockerfile                 # Container build
├── Makefile                   # Build automation
└── README.md                  # This file

# configs/features.yaml
feature_groups:
  temporal_features:
    - transaction_hour
    - day_of_week
    - time_since_last_transaction
  
  behavioral_features:
    - avg_transaction_amount_7d
    - transaction_velocity_24h
    - device_fingerprint_changes
  
  network_features:
    - ip_address_risk_score
    - geographic_velocity
    - proxy_detection