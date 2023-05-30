from pathlib import Path
from llama_index import SimpleDirectoryReader

documents = SimpleDirectoryReader('./data').load_data()

print(documents)