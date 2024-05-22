'''
# 작성일 : 2024년 5월 1일
# 파일명 : 
# 개발자 : 장국진
# 사용 라이브러리 : 
'''

from random import *
import uuid

print(random()) # UUID
print(uuid.uuid4()) # 4가 가장 간결한 코드

print("-"*80)

# 랜덤 UUID 생성
random_uuid = uuid.uuid4()
print(random_uuid)

# 이름 기반 UUID 생성
namespace_uuid = uuid.uuid5(uuid.NAMESPACE_DNS, 'example.com')
print(namespace_uuid)

# 중복 처리
def generate_unique_id():
    unique_id = uuid.uuid4()
    while check_id_duplicate(unique_id):
        unique_id = uuid.uuid4()
    return unique_id

def check_id_duplicate(id):
    # 중복 여부 확인 로직
    return False # 중복되지 않은 경우

print("-"*80)
# 중복되지 않는 UUID 생성
unique_id = generate_unique_id()
print(f"""uniqueID
{unique_id}""")

# 중복 방지 기능 사용
# unique_id = uuid.uuid1(node=get_mac_address())

print("-"*80)

# 랜덤 숫자 범위에서 하나 생성
# 1 ~ 45 사이에서 하나 선택
print(randrange(1, 45)) # 45는 불가능 --> range는 자신 제외
print(randint(1, 45)) # 1 ~ 45 가능

print("-"*80)

for i in range(5):
    print(i)
    
print("-"*80)

a = ['영어', '국어', '수학']
b = [100, 90, 80]
# for i, data in zip(data1, data2):
for a1, b1 in zip(a, b): # zip --> 2개의 데이터를 같이 출력 가능
    print(a1, b1)

print("-"*80)

# 연산자 +, -, *, %, 나머지, 몫 연산자
ia = 10
ib = 3
print(ia % ib)
print(ia // ib)
