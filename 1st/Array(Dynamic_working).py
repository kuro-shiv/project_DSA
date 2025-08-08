import sys
L = []

s = sys.getsizeof(L)  # This will return the size of the empty list in bytes
print(f"Size of empty list: {s} bytes")

L.append('Hello')
print(L)  # Output: [1]

s = sys.getsizeof(L)  # Size after adding one element
print(f"Size after adding: {s} bytes")

L.append('World')
print(L)  # Output: [1, 2]

s = sys.getsizeof(L)  # Size after adding another element
print(f"Size after adding another element: {s} bytes")

L.append(1)
print(L) # Output: [1, 2, 3]

s= sys.getsizeof(L)  # Size after adding another element
print(f"Size after adding another element: {s} bytes")


L.append(2)
print(L) # Output: [1, 2, 3]

s= sys.getsizeof(L)  # Size after adding another element
print(f"Size after adding another element: {s} bytes")


L.append(3)
print(L) # Output: [1, 2, 3]

s= sys.getsizeof(L)  # Size after adding another element
print(f"Size after adding another element: {s} bytes")



L.append(4)
print(L) # Output: [1, 2, 3]

s= sys.getsizeof(L)  # Size after adding another element
print(f"Size after adding another element: {s} bytes")


L.append(6)
print(L) # Output: [1, 2, 3]

s= sys.getsizeof(L)  # Size after adding another element
print(f"Size after adding another element: {s} bytes")


L.append(7)
print(L) # Output: [1, 2, 3]

s= sys.getsizeof(L)  # Size after adding another element
print(f"Size after adding another element: {s} bytes")


L.append(8)
print(L) # Output: [1, 2, 3]

s= sys.getsizeof(L)  # Size after adding another element
print(f"Size after adding another element: {s} bytes")


L.append(9)
print(L) # Output: [1, 2, 3]

s= sys.getsizeof(L)  # Size after adding another element
print(f"Size after adding another element: {s} bytes")


L.append(10)
print(L) # Output: [1, 2, 3]

s= sys.getsizeof(L)  # Size after adding another element
print(f"Size after adding another element: {s} bytes")


L.append(11)
print(L) # Output: [1, 2, 3]

s= sys.getsizeof(L)  # Size after adding another element
print(f"Size after adding another element: {s} bytes")


L.append(112)
print(L) # Output: [1, 2, 3]

s= sys.getsizeof(L)  # Size after adding another element
print(f"Size after adding another element: {s} bytes")


L.append(13)
print(L) # Output: [1, 2, 3]

s= sys.getsizeof(L)  # Size after adding another element
print(f"Size after adding another element: {s} bytes")
