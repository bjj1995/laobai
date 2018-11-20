def build_person(first_name,last_name):
    '''返回一个字典,第二行就已经封装到字典了'''
    person = {'first':first_name,'last':last_name}
    return person
musician = build_person('robot','likes')
print(musician)