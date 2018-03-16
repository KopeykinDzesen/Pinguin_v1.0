from django.utils.http import is_safe_url, urlunquote
import random


# def get_next_url(request):
#     next = request.META.get('HTTP_REFERER')
#     if next:
#         next = urlunquote(next)  # HTTP_REFERER may be encoded.
#     if not is_safe_url(url=next, host=request.get_host()):
#         next = '/'
#     return next


def generate_key():
    key = ''
    for i in range(20):
        number = random.randint(0, 9)
        key += str(number)
    return key


# def shifrator(str):
#
#     shifr_str = ''
#     for i in str:
#         shifr_str += chr(ord(i)+10)
#     return shifr_str
#
#
# def deshifrator(shifr_str):
#     str = ''
#     for i in shifr_str:
#         str += chr(ord(i)-10)
#     return str