#file = "C:/Users/tonka/OneDrive/Рабочий стол/Test.txt"
#with open(file, "w") as file:
    #content = file.write()
    #print(content)

txt_data = "ПРивет"

file_path = "Output.txt"
with open(file_path, "w") as file:
    file.write(txt_data)
    print(f"txt file '{file_path}'")
