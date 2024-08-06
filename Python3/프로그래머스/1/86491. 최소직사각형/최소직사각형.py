def solution(sizes):
    sizes = [(max(w, h), min(w, h)) for w, h in sizes]
    
    max_width = max(w for w, h in sizes)
    max_height = max(h for w, h in sizes)
    

    return max_width * max_height
