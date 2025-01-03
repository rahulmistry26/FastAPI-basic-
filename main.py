from typing import Optional
from fastapi import FastAPI,Path
from enum import Enum
from pydantic import BaseModel
import uvicorn




# class ModelName(str,Enum):
#     alexnet = "alexnet"
#     resnet = "resnet"
#     lenet = "lenet"

# class Item(BaseModel):
#     name :str
#     description: str | None =None
#     price :float
#     tax: float | None=None

Students ={
    1:{
        "Name":"Rahul",
        "Age":22,
        "dept":"IT"
    }
}

class Student(BaseModel):
    Name : str
    Age : int
    dept : str

class UpdateStudent(BaseModel):
    Name: str
    Age: int
    dept :str

app =FastAPI()

@app.get("/get-student/{student_id}")
def get_student(student_id :int = Path(description="This ID you can see the studnts detials",gt=0)):
    return Students[student_id]

# @app.get("/get-by-name")
# def get_student(Name:str):
#     for student_id in Students:
#         if Students[student_id]["Name"] == Name:
#             return Students[student_id]
#     return {"data":"Not found"}

@app.get("/get-by-name/{student_id}")
def get_student(*,student_id: int,Name:str):
    for student_id in Students:
        if Students[student_id]["Name"] == Name:
            return Students[student_id]
    return {"data":"Not found"}

@app.post("/create-student/{student_id}")
def create_student(student_id:int, Student: Student):

    if student_id in Students:
        return {"Eroor":"Student exists"}
    Students[student_id]=Student
    return Students[student_id]

@app.put("/update-student/{student_id}")
def update_student(student_id:int,Student:UpdateStudent):
    if student_id not in Students:
        return {"Message":"Student does not exist"}
    
    if Student.Name != None:
        Students[student_id]['Name'] = Student.Name

    if Student.Age !=None:
        Students[student_id]['Age']=Student.Age

    if Student.dept != None:
        Students[student_id]['dept'] =Student.dept
    
    # Students[student_id]=Student
    return Students[student_id]

@app.delete("/delete-student/{student_id}")
def delete_student(student_id:int):
    if student_id not in Students:
        return {"Message":"Student does not exist"} 
    del Students[student_id]
    return{"Message":"Student deleted succesfully"}
# fake_items_db =[{"item_name":"foo"},{"item_name":"water"},{"item_name":"tea"}]

# @app.get("/")
# async def root():
#     return  {"message":"Hello Wolrd!"}

# @app.get("/items/{item.id}")
# async def read_item(item_id: int):
#     return {"item_id":item_id}


# @app.get("/user/me")
# async def read_user_me():
#     return {"user_id":"the current user"}

# @app.get("/user/{user.id}")
# async def read_user(user_id: str):
#     return {"user_id":user_id}


# @app.get("/models/{model_name}")
# def  get_model(model_name:ModelName):
#     if model_name is  ModelName.alexnet:
#         return {"model_name":model_name,"message":"Deep laerning"}
#     if model_name.value == "lenet":
#         return {"model_name": model_name, "message": "LeCNN all the images"}

#     return {"model_name": model_name, "message": "Have some residuals"}

# @app.post("/user")
# def post_user():
#     pass

# @app.get("/")
# def read_item(skip: int = 0,limt: int =10):
#     return fake_items_db[skip:skip+limt]

# @app.post("/items/")
# def  create_item(item:Item):
#     item_dict = item.dict()
#     if item.tax:
#          price_with_tax = item.price+item.tax
#          item_dict.update({"price_with_tax":price_with_tax})
#     return item_dict

# @app.put("/items/{item.id}")
# def update_item(item_id:int,item:Item):
#     return {"item_id":item_id,**item.dict()}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)


