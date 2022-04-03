dict = {"Amy": {"likes": 5, "comments": 1},"Ray": {"likes": 5, "comments": 2},\
        "John": {"likes": 5, "comments": 3}}

for person in dict:
        print(f'{person} {dict[person]["likes"]+dict[person]["comments"]}')
