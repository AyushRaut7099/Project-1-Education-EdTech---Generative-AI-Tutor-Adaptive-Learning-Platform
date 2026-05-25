from langchain_text_splitters import RecursiveCharacterTextSplitter #used to split extracted text frompdf inot smaller chunks

def create_chunks(text):#function for creating chunks from text extracted from pdf 
    text_splitter = RecursiveCharacterTextSplitter( #used to split extracted text in smaller chunks
        chunk_size=500, #size of chunk
        chunk_overlap=100 
    )
    chunks = text_splitter.split_text(text) #it splits the extracted text into smaller chunks and stores in chunks variable
    return chunks #returning the chunks