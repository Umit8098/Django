import uuid

def get_random_code():
    # code = uuid.uuid4()
    code = str(uuid.uuid4())[:11].replace('-','')
    return code

# print(get_random_code())

