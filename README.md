<<<<<<< HEAD
# RAG

A lightweight retrieval-augmented generation project for loading local documents,
building a FAISS vector index, and answering questions with retrieved context.

The pipeline can load PDFs, text files, CSVs, Excel files, Word documents, and
JSON files from the `data/` directory. It uses Sentence Transformers for
embeddings, FAISS for vector search, and Google Gemini through LangChain for
summarization.

## Project Structure

```text
.
|-- app.py                  # Example RAG query runner
|-- main.py                 # Minimal project entry point
|-- pyproject.toml          # Project metadata and uv dependencies
|-- requirement.txt         # pip dependency list
|-- data/                   # Source documents and local vector data
|-- faiss_store/            # Saved FAISS index and metadata
|-- notebook/               # Exploration notebooks
`-- src/
    |-- data_loader.py      # Loads supported document formats
    |-- embedding.py        # Chunks documents and creates embeddings
    |-- vectorstore.py      # Builds, saves, loads, and queries FAISS
    `-- search.py           # Retrieves context and summarizes with Gemini
```

## Requirements

- Python 3.14 or newer
- A Google API key for Gemini

## Setup

Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install dependencies with `uv`:

```powershell
uv sync
```

Or install from `requirement.txt` with `pip`:

```powershell
pip install -r requirement.txt
```

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_google_api_key_here
```

## Usage

Place documents under `data/`. The loader searches recursively, so files can be
organized in subfolders such as `data/pdf/` or `data/text_files/`.

Build or rebuild the FAISS index:

```powershell
python -m src.vectorstore
```

Run the example RAG query:

```powershell
python app.py
```

The default example asks:

```text
What is NLP and Explain it
```

You can change the query in `app.py`, or use the classes directly:

```python
from src.search import RAGSearch

rag = RAGSearch()
answer = rag.search_and_summarize("What is attention mechanism?", top_k=3)
print(answer)
```

## Supported Documents

`src.data_loader.load_all_documents()` currently supports:

- PDF (`.pdf`)
- Text (`.txt`)
- CSV (`.csv`)
- Excel (`.xlsx`)
- Word (`.docx`)
- JSON (`.json`)

## Notes

- The FAISS index is stored in `faiss_store/faiss.index`.
- Metadata for retrieved chunks is stored in `faiss_store/metadata.pkl`.
- If the FAISS files are missing, `RAGSearch` attempts to build the index from
  documents in `data/`.
- The default embedding model is `all-MiniLM-L6-v2`.
- The default LLM model is `gemini-2.5-flash`.
=======
 
>>>>>>> 89aee154e51ce30ebb28c02c43a56e57e5810806
