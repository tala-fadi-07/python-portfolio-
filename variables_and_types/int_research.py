# int_research.py
# Gold Task: Research int()

# Read docs: https://docs.python.org/3/library/functions.html#int 

# int(" 22 ") * رح يتجاهل بايثون المسافة *
# int("+22") * رح يشتغل لانو رح يعتبر + كانها موجب ويكمل *
# int("0022") * رح يشتغل لانو الاصفار اللي بالبداية مسموحة وح يعتبرها 22 *
# int("2_2") * _ تستخدم لتسهيل القراءة فقط *

print(int(" 22 "))   # Expected: 22 - works, strips whitespace
print(int("+22"))    # Expected: 22 - works, explicit plus sign is allowed
print(int("0022"))   # Expected: 22 - works, leading zeros are allowed
print(int("2_2"))    # Expected: 22 - works, underscore is allowed as visual separator

# Source: https://docs.python.org/3/library/functions.html#int