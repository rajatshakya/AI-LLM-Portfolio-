import chromadb
import os


def create_chunks(text, chunk_size=200, overlap=50):
    chunks = []

    start = 0

    while start < len(text):
        end = start + chunk_size

        chunk = text[start:end]

        chunks.append(chunk)

        start = end - overlap

    return chunks


# Create Chroma database
client = chromadb.PersistentClient(path="./chroma_db")

# Create collection
collection = client.get_or_create_collection(
    name="company_documents"
)

# Documents folder
documents_folder = "./documents"

# Store documents as chunks
for filename in os.listdir(documents_folder):

    if filename.endswith(".txt"):

        file_path = os.path.join(documents_folder, filename)

        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()

        chunks = create_chunks(text)

        for index, chunk in enumerate(chunks):

            collection.add(
                documents=[chunk],
                ids=[f"{filename}_{index}"],
                metadatas=[
                    {
                        "source": filename,
                        "chunk": index
                    }
                ]
            )


print("Documents chunked and added successfully!")


# Search
query = input("Enter your question: ")

results = collection.query(
    query_texts=[query],
    n_results=3
)


print("\nSearch Results:\n")


for document, metadata in zip(
    results["documents"][0],
    results["metadatas"][0]
):

    print("Source:", metadata["source"])
    print("Chunk:", metadata["chunk"])
    print("Content:", document)
    print()