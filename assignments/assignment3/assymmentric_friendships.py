import MapReduce
import sys

"""
Assymetric Relationships in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

# Implement the MAP function
def mapper(friends):
    # YOUR CODE GOES HERE
    person = friends[0]
    friend = friends[1]
    mr.emit_intermediate((person, friend), 1)
    mr.emit_intermediate((person, friend), 1)
    mr.emit_intermediate((friend, person), 1)

# Implement the REDUCE function
def reducer(key, value):
    # YOUR CODE GOES HERE
    if len(value) == 1:
        mr.emit(key)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
