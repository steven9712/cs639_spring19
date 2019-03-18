import MapReduce
import sys

"""
Inverted Index Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

# Implement the MAP function
def mapper(books):
    # YOUR CODE GOES HERE
    document_id = books[0]
    text = books[1]
    words = text.split()
    for w in words:
        mr.emit_intermediate(w, document_id)

# Implement the REDUCE function
def reducer(key, document_id_list):
    # YOUR CODE GOES HERE
    documents = []
    for d in document_id_list:
        if (d not in documents):
            documents.append(d)

    mr.emit((key, documents))
        
    

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
