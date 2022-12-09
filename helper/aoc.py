import requests as r
import os


def getFile(day: int,year: int=2022):
    f=open('./secret','r')
    cookie = {"session": f.readline()}
    response=r.get(f'https://adventofcode.com/{year}/day/{day}/input',cookies=cookie)
    return response

def init(day: int,year: int=2022):
    fileName=f'./{year}/{day}/input.txt'
    if(not os.path.exists(fileName)):
        response=getFile(day,year)
        if(not response.text.startswith("Please don't")):
            os.makedirs(f'./{year}/{day}',exist_ok=True)

            with open(fileName,'wb') as f:
                f.write(response.content)
        else:
            raise Exception("Sorry Puzzle not ready!")
    return fileName