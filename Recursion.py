directory = {
    "Document": {
        "work": {"report.dox": None, "file.exe": None},
        "personal": {"vacation.png": None, "birthday.png": None},
    },
    "song": {
        "my_fav": "abc",
        "alltime": "xyz",
    },
    "Downloads": {
        "text.png": None,
    },
}
keys=[]
def search(dic, file_name, path=''):
    for key,value in dic.items():
        keys.append(key)
        curent_path= f"{path} / {key}"
        if key == file_name:
            print(curent_path)
    	    
        if isinstance(value,dict):
    	    search(value, file_name, curent_path)

serching_file = "birthday.png"    
   	    
path=search(directory, serching_file )

if serching_file not in keys:
    print("no such file")

