# Installation Guide

## Prerequisites
- Python 3.8 or higher
- pip package manager

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/Lavanya-Nair/Garbage_Classification.git
cd Garbage_Classification
```

### 2. Create Virtual Environment (Recommended)
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Notebooks
```bash
# Start Jupyter Notebook
jupyter notebook

# Or use VS Code with the Python extension
code .
```

## Dataset
The notebooks will automatically download the TrashNet dataset on first run. If the automatic download fails, you can manually download a garbage classification dataset and organize it into the following structure:

```
TrashType_Image_Dataset/
├── cardboard/
│   ├── image1.jpg
│   └── ...
├── glass/
├── metal/
├── paper/
├── plastic/
└── trash/
```

## Usage
1. Start with `Week_1.ipynb` for data exploration and preprocessing
2. Continue with `Week_2.ipynb` for model training with EfficientNetV2B2
3. Use `Week_3.ipynb` for advanced training and deployment

## Model Performance
- **Architecture**: EfficientNetV2B2 with transfer learning
- **Classes**: 6 (cardboard, glass, metal, paper, plastic, trash)
- **Target Accuracy**: 98%
- **Deployment**: Gradio web interface
