# Kiswahili Language Intelligence Engine

An interactive NLP application for analyzing Kiswahili words and sentences through **morphological analysis, grammatical analysis, explanations, and retrieval-based linguistic knowledge**.

The project combines a **FastAPI backend** with a **Streamlit user interface**, allowing users to enter Kiswahili words or sentences and receive structured linguistic analysis through a web-based interface.

---

## Overview

The Kiswahili Language Intelligence Engine is designed to demonstrate how Natural Language Processing (NLP) techniques can be applied to Kiswahili, with particular emphasis on morphological structure and grammatical analysis.

The system processes user input through a backend NLP pipeline and presents the results through an interactive Streamlit interface.

### Main capabilities

* Word-level morphological analysis
* Sentence tokenization and word-by-word analysis
* Morpheme segmentation
* Root/stem identification
* Subject and object marker detection
* Tense detection
* Kiswahili noun-class analysis
* Subject–verb agreement analysis
* Adjective–noun agreement analysis
* Retrieval of related examples from a Kiswahili linguistic dataset
* Human-readable explanations of analysis results
* Interactive question-and-answer interface based on analysis results
* REST API for accessing NLP functionality
* Web-based demonstration interface

---

## System Architecture

The project uses a layered architecture separating the user interface from the NLP processing layer.

```text
                    USER
                      │
                      ▼
        ┌─────────────────────────┐
        │      Streamlit UI       │
        │                         │
        │  • Input interface      │
        │  • Results display      │
        │  • Explanations         │
        │  • Grammar display      │
        └────────────┬────────────┘
                     │
                  HTTP / JSON
                     │
                     ▼
        ┌─────────────────────────┐
        │       FastAPI API       │
        │                         │
        │  • Word analysis        │
        │  • Sentence analysis    │
        │  • Grammar analysis     │
        │  • Dataset search       │
        └────────────┬────────────┘
                     │
          ┌──────────┼───────────┐
          ▼          ▼           ▼
     Morphology   Grammar       RAG
       Engine      Engine      Retrieval
          │          │           │
          └──────────┼───────────┘
                     ▼
             Linguistic Data
```

The Streamlit frontend acts as the **presentation and interaction layer**, while FastAPI exposes the NLP functionality through REST endpoints.

---

## Project Structure

```text
kiswahili-app/
│
├── main.py
├── requirements.txt
│
├── src/
│   ├── morphology.py
│   ├── tokenizer.py
│   ├── segmenter.py
│   ├── tense.py
│   ├── subject_marker.py
│   ├── object_marker.py
│   ├── noun_class.py
│   └── utils.py
│
├── rules/
│   ├── grammar_engine.py
│   └── agreement_rules.py
│
├── rag/
│   ├── retriever.py
│   ├── explainer.py
│   └── qa.py
│
├── data/
│   ├── sentences_data.json
│   └── noun_classes.json
│
└── kiswahili-app/
    ├── app.py
    ├── backend_client.py
    ├── components/
    ├── demo/
    └── presentation/
```

---

## Morphological Analysis

The morphology engine analyzes individual Kiswahili words and extracts available linguistic information.

For verbs, the system can identify information such as:

* Subject marker
* Tense marker
* Object marker
* Verb root
* Suffix information
* Tense classification

For nouns, the system can provide:

* Noun class
* Prefix
* Stem
* Corresponding plural class
* Possible plural form
* Noun-class description

### Example

Input:

```text
anasoma
```

The system can identify components such as:

```text
Word type: verb
Subject marker: a-
Tense marker: -na-
Root: soma
Tense: present progressive
```

---

## Sentence Analysis

When a sentence is supplied, the system:

1. Tokenizes the sentence.
2. Performs morphological analysis on individual words.
3. Presents the results word by word.
4. Performs sentence-level grammatical analysis.
5. Generates human-readable explanations.

Example:

```text
Mtoto anasoma kitabu.
```

The application can display the morphological analysis of:

```text
Mtoto
anasoma
kitabu
```

followed by sentence-level grammar analysis.

---

## Grammar Analysis

The grammar component evaluates selected Kiswahili agreement relationships.

Current rules include areas such as:

### Subject–Verb Agreement

The system compares the noun class associated with a subject against the subject marker appearing on the verb.

### Adjective–Noun Agreement

The system checks selected noun-class agreement patterns between nouns and adjectives.

The grammar engine returns structured information such as:

```json
{
    "is_grammatically_correct": true,
    "grammar_score": 100,
    "errors": [],
    "warnings": []
}
```

The grammar component is designed as a rule-based layer and is therefore dependent on the linguistic rules and analyses available to it.

---

## Retrieval-Augmented Linguistic Support

The project includes a retrieval component that searches a Kiswahili sentence dataset for relevant examples.

The dataset contains approximately **1,500+ Kiswahili sentences** together with word-level morphological information.

The retrieval process uses relevant terms from the user's input and morphological analysis to locate related examples.

Retrieved information can then be used by the explanation and question-answering components to provide additional linguistic context.

---

## Explanation and Question Answering

The application provides human-readable explanations of the returned NLP analysis.

For example, instead of displaying only:

```text
root: soma
subject_marker: a-
tense_marker: -na-
```

the explanation layer can turn the information into a more accessible linguistic description.

The application also provides an interactive question interface that can answer questions about available analysis information, including areas such as:

* Subject
* Tense
* Root
* Object marker
* Morphological structure

The explanation and Q&A components are designed to use the actual analysis results and retrieved linguistic information rather than presenting unrelated generated information.

---

## API

The backend is implemented using **FastAPI**.

### Health Check

```text
GET /
```

Returns information about the backend status and loaded dataset.

### Word Analysis

```text
POST /api/v1/analyze/word
```

Example request:

```json
{
    "word": "anasoma"
}
```

### Sentence Analysis

```text
POST /api/v1/analyze/sentence
```

Example request:

```json
{
    "sentence": "Mtoto anasoma kitabu"
}
```

### Dataset Search

```text
GET /api/v1/dataset/search
```

The API also provides automatically generated interactive documentation through FastAPI's Swagger interface.

---

## Technology Stack

### Backend

* Python
* FastAPI
* Pydantic
* Uvicorn

### NLP

* Python-based rule-driven morphological analysis
* Tokenization
* Morpheme segmentation
* Tense detection
* Subject/object marker detection
* Noun-class analysis
* Grammar rules
* Retrieval-based linguistic support

### Frontend

* Streamlit

### Data

* JSON-based linguistic resources
* Kiswahili sentence dataset
* Noun-class and agreement rules

### Deployment

* FastAPI backend deployed as a web service
* Streamlit frontend deployed separately
* HTTP/JSON communication between frontend and backend

---

## Installation

Clone the repository:

```bash
git clone https://github.com/CephaMK/Jenny_s-Lectures.git
```

Move into the project directory:

```bash
cd Jenny_s-Lectures/kiswahili-app
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Backend Locally

From the `kiswahili-app` directory:

```bash
uvicorn main:app --reload
```

The API will normally be available at:

```text
http://127.0.0.1:8000
```

Interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

---

## Running the Streamlit Interface

Move into the Streamlit application directory:

```bash
cd kiswahili-app
```

Run:

```bash
streamlit run app.py
```

The interface will normally be available at:

```text
http://localhost:8501
```

---

## Configuration

The Streamlit frontend obtains the backend API address through the `API_BASE_URL` environment variable.

Example:

```text
API_BASE_URL=https://your-backend-url
```

If the variable is not supplied, the application can fall back to the local development backend:

```text
http://127.0.0.1:8000
```

This allows the same frontend code to be used during both local development and deployment.

---

## Deployment Architecture

The deployed application separates the frontend and backend.

```text
Streamlit Cloud
      │
      │ HTTPS / JSON
      ▼
Render
      │
      ▼
FastAPI
      │
      ├── Morphology Engine
      ├── Grammar Engine
      ├── RAG Retriever
      └── Linguistic Dataset
```

This separation allows the NLP processing layer and user interface to be developed and deployed independently.

---

## Current Limitations

The project is an academic NLP prototype and is still under development.

Current limitations include:

* Rule-based linguistic analysis does not cover the full complexity of Kiswahili.
* Morphological rules are dependent on the available linguistic resources.
* Grammar analysis currently evaluates selected agreement patterns rather than the complete Kiswahili grammar.
* Retrieval is based on the available project dataset and matching strategy.
* Unknown or non-Kiswahili words may require additional validation before they can be reliably distinguished from valid Kiswahili vocabulary.
* The system should not be interpreted as a complete computational grammar of Kiswahili.

These limitations provide opportunities for future improvements.

---

## Future Improvements

Potential future development includes:

* Larger Kiswahili lexical resources
* More comprehensive morphological rules
* Improved unknown-word and language validation
* More extensive noun-class agreement rules
* Dependency parsing
* Improved sentence-level grammar analysis
* Semantic search using embeddings
* More advanced RAG pipelines
* Machine-learning-based morphological disambiguation
* Kiswahili language models
* Expanded evaluation datasets
* Automated NLP performance evaluation

---

## Academic Project

This project was developed as a collaborative academic NLP project.

The system demonstrates the integration of:

* Natural Language Processing
* Computational morphology
* Rule-based grammar
* Information retrieval
* Retrieval-augmented explanation
* REST API development
* Interactive user interfaces
* Cloud deployment

The project is intended primarily for **academic demonstration, experimentation, and further development**.

---

## Contributors

The project is developed collaboratively, with responsibilities distributed across different system components, including:

* **NLP / Morphology** — morphological analysis and linguistic processing
* **Grammar & Linguistic Data** — grammar rules and linguistic resources
* **Backend / Evaluation / Deployment** — API, backend integration, testing and deployment
* **UI / Product / AI** — Streamlit interface, visualization, explanation interface, RAG integration and demonstration experience

---

## License

This project is currently an academic project. Licensing terms can be added as the project is prepared for wider public distribution.

