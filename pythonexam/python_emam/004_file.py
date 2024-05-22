'''
# 작성일 : 2024년 5월 2일
# 파일명 : 
# 개발자 : 장국진
# 사용 라이브러리 : 
'''

# 파일 저장
save_file = open('save.txt', 'w', encoding='utf8')
print('테스트1 : 테스트1', file=save_file)
print('테스트2 : 테스트2', file=save_file)
save_file.close()

save_file = open('save1.txt', 'w', encoding='utf8')
save_file.write("리스트 파일1\n")
save_file.write("리스트 파일2\n")
save_file.close()

