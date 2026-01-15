# Offline Language Translation System (LTS)

## Project Overview
The **Offline Language Translation System (LTS)** is a Natural Language Processing (NLP) / LLM-based project designed to perform multilingual text translation **without requiring internet connectivity**.  
The system primarily focuses on **Indian regional languages**, ensuring privacy, accessibility, and usability in low-connectivity environments.

---

## Project Track
**Natural Language Processing (NLP) / LLM-based System**

---

## Key Features
- Fully **offline translation**
- Supports multiple Indian languages
- Uses **Transformer-based pretrained models (IndicTrans2)**
- GUI (Tkinter) and CLI support
- Privacy-preserving (no cloud APIs)
- Standalone deployment capability

---

## Repository Structure
```
Offline-LTS/
│
├── Offline_LTS_Main.ipynb   # Main evaluation notebook
├── translator_engine.py    # Core translation logic
├── cli.py                  # Command Line Interface
├── gui.py                  # Graphical User Interface
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

---

## Main Notebook
📌 **Offline_LTS_Main.ipynb**  
This notebook contains:
- Problem definition & objectives  
- Data understanding & preprocessing  
- Model/system design  
- Core implementation  
- Evaluation & analysis  
- Ethical considerations  
- Conclusion & future scope  

> ⚠️ Evaluators are requested to refer to this notebook as the **primary source**.

---

## Technologies Used
- Python
- PyTorch
- HuggingFace Transformers
- IndicTransToolkit
- Tkinter (GUI)

---

## How to Run
### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Run Jupyter Notebook (Recommended)
```bash
jupyter notebook Offline_LTS_Main.ipynb
```

### 3. Run GUI Application
```bash
python gui.py
```

### 4. Run CLI Application
```bash
python cli.py
```

---

## Ethical Considerations
- No user data is stored or transmitted
- Offline inference ensures privacy
- Bias may exist due to pretrained dataset limitations
- Responsible usage is encouraged

---

## Future Scope
- Support for more languages
- Speech-to-text and text-to-speech integration
- Mobile and embedded deployment
- Domain-specific fine-tuned models

---

## Author
**Snehal Modgil**  
Academic Project – Offline Language Translation System