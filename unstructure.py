from pathlib import Path
from llama_index import download_loader, SimpleDirectoryReader

UnstructuredReader = download_loader("UnstructuredReader")

loader = UnstructuredReader()
documents = loader.load_data(file=Path('./data/UBER_2019.html'))

print(documents)