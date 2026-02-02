def text_chunking(tokens, chunk_size, overlap):
    """
    Split tokens into fixed-size chunks with optional overlap.
    """
    # Write code here
    step = chunk_size - overlap
    chunks = []
    
    i = 0
    n = len(tokens)

    while i < n:
        chunk = tokens[i:i + chunk_size]
        chunks.append(chunk)

        if i + chunk_size >= n:
            break  

        i += step

    return chunks