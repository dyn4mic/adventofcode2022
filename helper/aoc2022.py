import requests as r
import os


def getFile(day):
    f=open('./secret','r')
    cookie = {"session": f.readline()}
    response=r.get(f'https://adventofcode.com/2022/day/{day}/input',cookies=cookie)
    return response

def init(day: int):
    fileName=f'./{day}/input.txt'
    if(not os.path.exists(fileName)):
        response=getFile(day)
        if(not response.text.startswith("Please don't")):
            if(not os.path.exists(f'./{day}/')):
                os.mkdir(f'./{day}')

            with open(fileName,'wb') as f:
                f.write(response.content)
        else:
            raise Exception("Sorry Puzzle not ready!")
    return fileName