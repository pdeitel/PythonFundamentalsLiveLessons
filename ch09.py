# with open('accounts.txt',mode='w')as accounts:
#     accounts.write('100 Jones 24.99\n')
#     accounts.write('200 Doe 345.67\n')
#     accounts.write('300 White 0.00\n')
#     accounts.write('400 Stone -42.16\n')
#     accounts.write('500 Rich 224.62\n')
#     print('100 Jones 24.98',file=accounts)



# with open('accounts.txt',mode='r') as accounts:
#     print(f'{"Account":<10}{"Name":<10}{"Balance":>10}')
#     for record in accounts:
#         account, name, balance=record.split()
#         print(f'{account:<10}{name:<10}{balance:>10}')

accounts = open('accounts.txt','r')
temp_file = open('temp_file.txt','w')

with accounts,temp_file:
    for record in accounts:
        account, name, balance = record.split()
        if account != '300':
            temp_file.write(record)
        else:
            new_record = ' '.join([account, 'Williams',balance])
            temp_file.write(new_record + '\n')

