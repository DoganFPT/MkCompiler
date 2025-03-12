from io import BytesIO
import tokenize

def toki_file(path_file):
    with open(path_file,"rb") as file:
        tokens = tokenize.tokenize(file.readline)
        
    
        for token in tokens:
            new_token=f"String:{token.string},Type:{token.type},Start:{token.start},End:{token.end}"
            print(new_token)

path_file="add.py"
toki_file(path_file)


