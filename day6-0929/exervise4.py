import string

#加密解密方法：信息+偏移量 正负数都支持
def caesar_encryption(info, offset):
    list = []

    #获取A-Z列表
    az_Upper = string.ascii_uppercase
    #根据用户提供的偏移量制造密码母本
    offset_index_value = 26 - offset 
    encryption_az_Upper = az_Upper[offset_index_value:26] + az_Upper[:offset_index_value]
    for i in az_Upper:
        list.append(i)
    #print(list)
    #对信息加密
    encryption_info = ""
    for i in info:
        index = list.index(str.upper(i))
        if i.islower(): 
           encryption_info +=  str.lower(encryption_az_Upper[index])
        else:
           encryption_info +=  encryption_az_Upper[index]
    
    print(encryption_info)


#加密
caesar_encryption("AAADDDeee",3)

def caesar_decrypt(info,offset):
    list = []

    #获取A-Z列表
    az_Upper = string.ascii_uppercase
    #根据用户提供的偏移量制造密码母本
    offset_index_value = 26 - offset 
    decrypt_az_Upper = az_Upper[offset_index_value:26] + az_Upper[:offset_index_value]
    for i in decrypt_az_Upper:
        list.append(i)
    #print(list)
    #对信息解密
    decrypt_info = ""
    for i in info:
        index = list.index(str.upper(i))
        if i.islower(): 
           decrypt_info +=  str.lower(az_Upper[index])
        else:
           decrypt_info +=  az_Upper[index]
    
    print(decrypt_info)



#解密
caesar_decrypt("XXXAAAbbb",3)