from pathlib import Path
from llama_index import download_loader

SimpleDirectoryReader = download_loader("SimpleDirectoryReader")

loader = SimpleDirectoryReader('./data', file_extractor={
  ".pdf": "UnstructuredReader",
  ".html": "UnstructuredReader",
  ".eml": "UnstructuredReader",
  ".pptx": "PptxReader"
})
documents = loader.load_data()
print(documents)
