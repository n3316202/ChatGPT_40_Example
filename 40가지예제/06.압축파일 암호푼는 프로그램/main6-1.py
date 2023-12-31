import itertools
import zipfile

def crack_zip_password(zipfilename, digits=True, letters=True, max_length=9):
    """주어진 zip 파일에서 비밀번호를 찾습니다.

    zipfilename : str
        비밀번호를 찾을 zip 파일의 경로
    digits : bool (기본값 True)
        비밀번호에 숫자를 포함할 것인지 여부
    letters : bool (기본값 True)
        비밀번호에 문자를 포함할 것인지 여부
    max_length : int (기본값 9)
        비밀번호의 최대 길이

    Returns:
    str : 비밀번호
    """

    # 비밀번호 후보를 생성합니다.
    # digits와 letters 매개변수에 따라 다른 문자 집합을 사용합니다.
    chars = ""
    if digits:
        chars += "0123456789"
    if letters:
        chars += "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    passwords = itertools.chain.from_iterable(
        itertools.product(chars, repeat=i) for i in range(1, max_length + 1)
    )
    #https: // soundprovider.tistory.com / entry / python - itertools
    # A = [1, 2, 3]
    # list(itertools.product(A, repeat=2))
    # >> >> [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]

    # 비밀번호를 하나씩 시도합니다.
    with zipfile.ZipFile(zipfilename) as zf:
        for password in passwords:
            password = "".join(password)
            print(password)
            try:
                zf.extractall(pwd=password.encode())
                return password
            except:
                pass

    # 비밀번호를 찾지 못한 경우 None을 반환합니다.
    return None

#password = crack_zip_password(r"06.압축파일 암호푼는 프로그램\\암호.zip", digits=True, letters=True, max_length=9)
password = crack_zip_password(r"암호.zip", digits=True, letters=True, max_length=9)
print("비밀번호는:",password)

# class Test:
#     def __init__(self):
#         print('초기화')
#
#     def __enter__(self):
#         print("with문 들어왔습니다")
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("with문 종료되었습니다.")
#
# with Test() as f:
#     print("with문 안 입니다.")
#
#
# [결과]:
# 초기화
# with문 들어왔습니다
# with문 안 입니다.
# with문 종료되었습니다.
# 출처: https://aplab.tistory.com/entry/파이썬-with-사용법 [테리엇의 A Python Lab:티스토리]
