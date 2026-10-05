from pinecone import Pinecone, ServerlessSpec
    

pc = Pinecone(api_key="pcsk_GSBuF_RpUazb3CMxqt8ccxYKNWk3m17mhrYNbYpq9ySzMTTZ8wjrBK4SJzK4tLb5Af8Nc")
    
index_name = "student-notes"
    
pc.create_index(
    name=index_name,
    dimension=4,
    metric="cosine",
    spec=ServerlessSpec(cloud="aws", region="us-east-1")
)
    
my_index = pc.Index(index_name)

my_index.upsert(vectors=[
    {"id": "note1", "values": [0.1, 0.9, 0.2, 0.05], "metadata": {"text": "Linked lists"}},
    {"id": "note2", "values": [0.8, 0.1, 0.3, 0.4], "metadata": {"text": "Newton's laws"}}
])
    
search_result = my_index.query(
    vector=[0.15, 0.85, 0.25, 0.1],
    top_k=1,
    include_metadata=True
)
    
print(search_result)