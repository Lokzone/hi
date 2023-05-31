# 密码重试程序

password = 'a123456'
pwd_count = 3
while True:
	if pwd_count == 0:
		print('密码输入次数过多，请下次再重新访问~')
		break
	else:
		pwd_input = input('请输入您的密码： ')
		if pwd_input == password:
			print('bingo 欢迎回来~')
			break
		else:
			pwd_count = pwd_count -1
			if pwd_count != 0:
				print('密码错误，您还可以再输入', pwd_count, '次： ')


