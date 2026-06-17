from src.data_loader import load_all_documents
from src.vectorstore import FaissVectorStore
from src.search import RAGSearch
#from src.embedding import EmbeddingPipeline

# Example usage
if __name__ == "__main__":
    
    #docs = load_all_documents("data")
    store=FaissVectorStore("faiss_store")
    store.load()
    #print(store.query("What is NLP and Explain it"))
    
    
    rag_search = RAGSearch()
    query = "What is NLP and Explain it"
    summary = rag_search.search_and_summarize(query, top_k=3)
    print("Summary:", summary)
    
    #store.build_from_documents(docs)
    #chunks=EmbeddingPipeline().chunk_documents(docs)
    #chunksvectors=EmbeddingPipeline().embed_chunks(chunks)
    #print(chunksvectors)
    #print(docs)     