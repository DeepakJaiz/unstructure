from pathlib import Path
from llama_index import download_loader

UnstructuredReader = download_loader("UnstructuredReader")

loader = UnstructuredReader()
documents = loader.load_data(file=Path('./data/Pride-and-Prejudice.pdf'))

print(documents)