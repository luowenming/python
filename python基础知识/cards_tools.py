#记录所有的名片字典
card_list = [];
def show_menu():
    '''显示菜单'''
    print('*' * 50)
    print('欢迎使用【名片管理系统】V1.0')
    print('')
    print('1，新增名片')
    print('2，显示全部')
    print('3，搜索名片')
    print('')
    print('0，退出系统')
    print('*' * 50)
def new_card():
    '''新增名片'''
    print('- ' * 50)
    print('新增名片')
    #1,提示用户输入名片详细信息
    name = input('请输入姓名:')
    phone = input('请输入电话:')
    qq = input('请输入QQ:')
    email = input('请输入邮箱:')
    #2,使用用户输入的信息建立一个名片字典
    card_dict = {
        'name' : name,
        'phone': phone,
        'qq': qq,
        'email': email
    }
    #3，将名片字典添加到列表中
    card_list.append(card_dict);
    print(card_list)
    #4，提示用户添加成功
    print('添加%s的名片成功！' % name)

def show_all():
    '''显示所有名片'''
    print('- ' * 50)
    print('显示所有名片')
    if len(card_list) == 0:
        print('当前没有任何名片记录，请使用新增功能添加名片！')
        return
    #打印表头
    for name in ['姓名','电话','QQ','邮箱']:
        print(name, end='\t\t')
    print('')
    print('= ' * 50)
    #1,遍历名片列表
    for card_dict in card_list:
        print('%s\t\t%s\t\t%s\t\t%s' % (card_dict['name'],card_dict['phone'],card_dict['qq'],card_dict['email']))
    print('= ' * 50)

def search_card():
    '''搜索名片'''
    print('- ' * 50)
    print('搜索名片')
    #1,提示用户要搜索的姓名
    find_name = input('请输入要搜索的姓名：')

    #2,遍历列表，查询要搜索的姓名，如果没有找到，需要提示用户
    for card_dict in card_list:
        if card_dict['name'] == find_name:
            print('姓名\t\t电话\t\tQQ\t\t邮箱')
            print('= ' * 50)
            print('%s\t\t%s\t\t%s\t\t%s' % (card_dict['name'], card_dict['phone'], card_dict['qq'], card_dict['email']))
            # TODO 对找到了，进行修改删除
            deal_card(card_dict)
            break
    else:
        print('抱歉，没有找到%s' % find_name)
def deal_card(find_dict):
    print(find_dict)
    actiona_str = input('请选择要执行的操作：'
                        '【1】 修改 【2】 删除 【3】 返回上级菜单')

    if actiona_str == '1':
        find_dict['name'] = inpout_card_info(find_dict['name'],'姓名')
        find_dict['phone'] = inpout_card_info(find_dict['phone'],'电话：')
        find_dict['qq'] = inpout_card_info(find_dict['qq'],'QQ：')
        find_dict['email'] = inpout_card_info(find_dict['email'],'邮箱：')
        print('修改')
    elif actiona_str == '2':
        card_list.remove(find_dict)
        print('删除名片成功！')
def inpout_card_info(dict_value, tip_message):
    result_str = input(tip_message)
    if len(result_str) > 0:
        return  result_str
    else:
        return dict_value
