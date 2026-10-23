user = "analyst"
role = "viewer"
failed = 3
port = 22

# 1 == *True*
print("Is user == 'analyst'? I predict True.")
print(user == "analyst")

# 2 == *False*
print("\nIs role == 'admin'? I predict False.")
print(role == "admin")

# 3 != *False*
print("\nIs failed != 3? I predict False.")
print(failed != 3)

# 4 > *True*
print("\nIs failed > 2? I predict True.")
print(failed > 2)

# 5 < *False*
print("\nIs port < 20? I predict False.")
print(port < 20)

# 6 >= *False*
print("\nIs failed >= 4? I predict False.")
print(failed >= 4)

# 7 <= *True*
print("\nIs port <= 22? I predict True.")
print(port <= 22)

# 8 and *True*
print("\nIs failed == 3 and port == 22? I predict True.")
print(failed == 3 and port == 22)

# 9 or *False*
print("\nIs role == 'admin' or user == 'admin'? I predict False.")
print(role == "admin" or user == "admin")

# 10 not *True*
print("\nIs not failed > 5? I predict True.")
print(not failed > 5)