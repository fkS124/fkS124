def load():
    
    try:
        with open("score.txt") as doc:
            return doc.read()
    except FileNotFoundError:
        with open("score.txt", "w") as doc:
            print("File not found, successfully created the highscore file.")
            doc.write("0")
            return None
        
def save(high_score):
    
    try:
        with open("score.txt", "w") as doc:
            doc.write(str(high_score))
            return "successfully stored"
    except Exception as e:
        print(e)
        return f"Error, score couldn't been stored successfully due to an {e}."