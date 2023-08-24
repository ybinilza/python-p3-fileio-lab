def write_file(file_name, file_content):
    file_name=str(file_name)+".txt";
    with open(file_name,mode="w",encoding="utf-8") as file_name:
        file_name.write(file_content);


def append_file(file_name, append_content):
    file_name=str(file_name)+".txt";
    with open(file_name,mode="a",encoding="utf-8") as file_name:
        file_name.write(append_content);

def read_file(file_name):
    file_name=str(file_name)+".txt";
    with open(file_name, encoding='utf-8') as file_name:
        contents=file_name.read()
    return contents
