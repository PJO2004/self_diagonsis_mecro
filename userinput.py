from mecaropythoncode import selfdiaconsis

CityProvince = input('시/도(ex OO도) : ')
SchoolLevel = input('학교급(ex 고등학교) : ')
SchoolName = input('학교이름(ex OO고등학교) : ')
UserName = input('이름(ex 홍길동) : ')
BirthDate = input('생년월일(ex 000000) : ')
Password = input('비밀번호(ex 0000) : ')

diagosis = selfdiaconsis(CityProvince, SchoolLevel, SchoolName, UserName, BirthDate, Password)
diagosis.test()
