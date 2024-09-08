import json

def load_data(file_path):
    dictinary=dict() 
    li=list() 
    def load_data(file_path): 
            with open(file_path, mode='r') as file: 
                lines=file.readlines() 
                headers=lines[0].split(', ') 
                for line in lines[1:]: 
                    data=line.split(', ') 
                    for i in range(len(headers)): 
                        dictinary[headers[i]]=data[i] 
                    li.append(dictinary)
    print(li)

def save_data(file_path, data):
    with open(file_path, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)


# data = load_data('../database/user.json')
# print(data)