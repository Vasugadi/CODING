from difflib import SequenceMatcher
with open("demo.txt", "r") as f1,open("demo2.txt", "r") as f2:
    
    text1 = f1.read()
    text2 = f2.read()
    
    similarity = SequenceMatcher(None, text1, text2).ratio()
    print(f"Plagiarism similarity: {similarity*100:.2f}%")