import json
import hashlib
import os

def createId(sch):
    hash = hashlib.sha256(str(len(sch)).encode()).hexdigest()
    for item in sch:
        for x in sch[item]:
            if x == "JSONdbId":
                if hash == sch[item][x]:
                    hash = hashlib.sha256(str(len(sch) * len(sch)).encode()).hexdigest()
    return hash

def saveData(sch, docName, data, fileDir):
    if data.get('baseplate') is not None:
        with open(fileDir, "w") as j:
            json.dump(data, j)
        return True
    file = ""
    with open(fileDir, "r+") as e:
        file = json.load(e)
    file = json.dumps(file)
    file = json.loads(file)
    dataconf = file
    base = dataconf['baseplate']
    for item in base:
        if item == "JSONdbId":
            continue
        if data.get("JSONdbId") is None:
            data["JSONdbId"] = createId(sch)
        if base[item][1] == "required" and data.get(item) is None:
            print("DB Error: Missing required field: " + item)
            return False
        match base[item][0]:
            case "int":
                if type(data.get(item)) is not int:
                    print("DB Error: Invalid type for field: " + item)
                    return False
            case "string":
                if type(data.get(item)) is not str:
                    print("DB Error: Invalid type for field: " + item)
                    return False
            case "float":
                if type(data.get(item)) is not float:
                    print("DB Error: Invalid type for field: " + item)
                    return False
            case "bool":
                if type(data.get(item)) is not bool:
                    print("DB Error: Invalid type for field: " + item)
                    return False
            case "list":
                if type(data.get(item)) is not list:
                    print("DB Error: Invalid type for field: " + item)
                    return False
            case "dict":
                if type(data.get(item)) is not dict:
                    print("DB Error: Invalid type for field: " + item)
                    return False
            case "any":
                pass
    dataconf[docName] = data
    with open(fileDir, "w") as j:
        json.dump(dataconf, j)
        return True

def openDB(fileDir):
    if os.stat(fileDir).st_size == 0:
        return {}
    with open(fileDir, "r") as f:
        return json.load(f)
    
def filterOut(s, name, val):
    filtered = []
    for item in s:
        js = json.dumps(s[item])
        jss = json.loads(js)
        if jss[name] == val:
            filtered.append(s[item])
    return filtered

def createSchema(baseplate):
    if type(baseplate) is not dict:
        return False
    baseplateItems = {}
    for item in baseplate:
        rq = "optional"
        if baseplate[item].get('required'):
            rq = "required"
        baseplateItems.update({f'{item}': [f"{baseplate[item].get('type')}", f'{rq}']})
    return dict(baseplateItems)

class db:
    def __init__(self, schema="ns"):
        if schema != "ns":
            self.schema = "./JSONdb/database/" + schema + ".json"
        else:
            self.schema = "ns"
    def createId(self):
        if self.schema == "ns":
            return "Not Allowed"
        return createId(self.schema)
    
    def findAll(self):
        if self.schema == "ns":
            return "Not Allowed"
        return openDB(self.schema)
    
    def findBy(self, name, value):
        if self.schema == "ns":
            return "Not Allowed"
        data = openDB(self.schema)
        return filterOut(data, name, value)
    
    def findById(self, id):
        if self.schema == "ns":
            return "Not Allowed"
        data = openDB(self.schema)
        return filterOut(data, 'JSONdbId', id)
    
    def countDocuments(self):
        if self.schema == "ns":
            return "Not Allowed"
        data = openDB(self.schema)
        return len(data) - 1
    
    def insert(self, docName, arr):
        if self.schema == "ns":
            return "Not Allowed"
        return saveData(openDB(self.schema), docName, arr, self.schema)

    def createSchema(self, schemaName, baseplate):
        if self.schema != "ns":
            return "Not Allowed"
        schema = "./JSONdb/database/" + schemaName + ".json"
        bs = createSchema(baseplate)
        try:
            open(schema, "x")
        except:
            return "Already Exists"
        return saveData(None, 'baseplate', dict({'baseplate':bs}), schema)
        
