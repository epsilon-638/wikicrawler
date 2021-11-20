import os
import re

if __name__ == "__main__":
    for f in os.listdir("."):
        if f.endswith('test.py') and f != 'test.py':
            os.system(f"python3 {f}")
