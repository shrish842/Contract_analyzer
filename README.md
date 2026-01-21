# Contract Risk Analyzer

AI-powered system for analyzing legal contract risks using rule-based + ML hybrid approach.

## Project Overview

This system analyzes legal contracts to identify risk factors such as:
- Unlimited liability clauses
- Aggressive auto-renewal terms
- Broad indemnification
- IP assignment overreach
- Non-compete restrictions

## Architecture
```
Phase 1: Rule-Based System (High Precision)
Phase 2: Weak Supervision (Auto-labeling)
Phase 3: ML Classifier (High Recall)
Phase 4: Hybrid Inference (Rules + ML)
Phase 5: Optional Transformers
```

## Setup
```bash
# Clone repository
git clone <repo-url>
cd contract-risk-analyzer

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Download spaCy model
python -m spacy download en_core_web_sm
```

## Project Structure
```
contract-risk-analyzer/
├── data/               # All datasets
│   ├── raw/           # Original contracts
│   ├── processed/     # Cleaned data
│   └── labels/        # Risk labels
├── src/               # Source code
│   ├── ingestion/     # Data collection
│   ├── preprocessing/ # Text cleaning
│   ├── rules/         # Risk detection rules
│   ├── ml/            # ML models
│   ├── explainability/# SHAP, LIME
│   └── api/           # Flask API
├── notebooks/         # Jupyter notebooks
└── tests/             # Unit tests
```

## Usage

### 1. Collect Data (SEC EDGAR)
```bash
python src/ingestion/sec_downloader.py --ticker AAPL --count 50
```

### 2. Run Rule-Based Analysis
```bash
python src/rules/risk_analyzer.py --input data/raw/real_contracts/employment/
```

### 3. Train ML Model
```bash
python src/ml/training/train_classifier.py --weak-labels data/labels/weak_supervision/
```

### 4. Start API Server
```bash
python src/api/app.py
```

## Development Roadmap

- [x] Project setup
- [ ] SEC EDGAR data collection (50 contracts)
- [ ] Rule-based risk detection (Phase 1)
- [ ] Weak supervision pipeline (Phase 2)
- [ ] ML classifier training (Phase 3)
- [ ] Hybrid inference system (Phase 4)
- [ ] Web UI for demos

## License

MIT License

## Contact

[Your Name] - [your.email@example.com]
