# def solution(phone_book):
#     for i in range(len(phone_book)):
#         for j in range(i + 1, len(phone_book)):
#             if phone_book[i].startswith(phone_book[j]):
#                 return False
#             if phone_book[j].startswith(phone_book[i]):
#                 return False
#     return True

def solution (phone_book):
    hash_data = {}
    for phone_number in phone_book:
        hash_data[phone_number] = 1
        
    for phone_number in phone_book:
        prefix = ''
        for number in phone_number:
            prefix += number
            if prefix in hash_data and prefix != phone_number:
                return False
    return True
