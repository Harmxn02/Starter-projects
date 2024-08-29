

def reverse_string(s: str) -> str:
    return s[::-1]

# Test the function
if __name__ == "__main__":
    print("🟩 Test case 'hello'"        if reverse_string("hello") == "olleh"               else "🟥 Test case 'hello'")
    print("🟩 Test case 'test'"         if reverse_string("test") == "tset"                 else "🟥 Test case 'test'")
    print("🟩 Test case 'pomeranian'"   if reverse_string("pomeranian") == "nainaremop"     else "🟥 Test case 'pomeranian'")