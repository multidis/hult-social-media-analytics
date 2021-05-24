## System information and selected package version.
import platform
import uuid
import pandas as pd

print(f"My operating system is {platform.system()}")
print(platform.architecture())
print(f"My CPU is {platform.processor()}")

print(f"pandas version is {pd.__version__}")

print("Finally, something unique:")
print(uuid.uuid4())

print("If no errors/warnings, I am good to go with my Python setup. See you in class.")

