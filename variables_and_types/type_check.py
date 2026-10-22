# type_check.py
# This program checks data types and demonstrates type conversions.

# Predictions before running (الي بتوقعه)
# 8080 *int لانها بدون "" *
# "8080" *str لانها مع "" *
# 99.5 *float لوجود فاصله عشرية *
# "198.51.100.7" *str لانه مع "" *
# 1_000 *int لانه _ فقط لتسهيل القراءة وهي عبارة عن رقم *

print(type(8080))
print(type("8080"))
print(type(99.5))
print(type("198.51.100.7"))
print(type(1_000))

print(int("443"), type(int("443")))
print(str(8080), type(str(8080)))
print(float("2.5"), type(float("2.5")))