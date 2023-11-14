print('曾经有一段真挚的爱情摆在我眼前，')
print('我没有去珍惜，等到失去了才追悔莫及。')
print('尘世间最痛苦的事莫过于此,')
print('如果是上天能给我一个再来一次的机会,')
print('我希望能对那个女孩说我爱你，')
print('如果非要给这份爱加一个期限的话,')
print('我希望是一万年。')
print('')
print('    *****    *****')
print('   *******  *******')
print('  ******************')
print('   ****************')
print('    **************')
print('      **********')
print('        ******')
print('          **')
num = 709.0014-99.99-88.88
number = input('猜一猜上述运算的结果吧:')
times = 1

while True:
  if times > 2:
    break
  if number.isnumeric():
    if int(number) == num:
      break
    if int(number) > num:
      number = input('不对哦,猜大了')
    else:
      number = input('不对哦,猜小了')
  else:
    number = input('需要在下方输入数字')
  times += 1

if times > 2 and int(number) != num:
  print('三次机会用完了')
else:
  print('恭喜你,猜中了')
print('结果是' + str(num))



