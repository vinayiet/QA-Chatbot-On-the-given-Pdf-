from pinecone import Pinecone, ServerlessSpec

# Initialize Pinecone with your API key
pc = Pinecone(api_key="")

# Define index name and the correct dimension based on your model
index_name = "document-index"
dimension =  384 # Change this if using a model with a different output size


if index_name not in pc.list_indexes():
    pc.create_index(
        name=index_name,
        dimension=dimension,
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        )
    )



index = pc.Index(index_name)


