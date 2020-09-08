def decToBin(num):
    binary = ""
    while num != 0:
        if num % 2 == 0:
            binary += "0"
        else:
            binary += "1"
        num = num/2
        num = int(num)
    # Ha rövidebb a bináris szám mint 8 bit, feltölti az elejét 0-kal
    if len(binary) < 8:
        for i in range(0, 8-len(binary)):
            binary += "0"

    return binary[::-1]

def binToDec(num):
    decimal = 0
    for i in range(0, len(num)):
        if num[i] != "0" and num[i] != "1":
            return "error"
        if num[i] == "1":
            decimal = decimal + 2**(len(num)-1 - i)
    decimal = str(decimal)
    return decimal

# felismeri es konvertalja az ip-t 10 => 2 -be es 2 => 10 -be
# pl. 255.255.255.0 => 11111111.1111111.11111111.00000000
def ipConverter(ip):
    ip_4bit = ip.split(".")
    ip_res = ""
    if len(ip_4bit[0]) > 3:
        for i in range(0, len(ip_4bit)):
            ip_res += binToDec(ip_4bit[i])
            if i != len(ip_4bit)-1:
                ip_res += "."
    else:
        for i in range(0, len(ip_4bit)):
            ip_res += decToBin(int(ip_4bit[i]))
            if i != len(ip_4bit)-1:
                ip_res += "."

    return ip_res

def check_mask(str):
    mask = ""
    if str.isdigit():
        for i in range(1, 33):
            if i <= int(str):
                mask += "1"
            else:
                mask += "0"
            if i % 8 == 0 and i != 32:
                mask += "."
    else:
        mask = ipConverter(str)

    return mask

def network_ip(ip, mask):
    mask_bin = check_mask(mask) # vissza adja a maszkot binarisan
    ip_bin = ipConverter(ip)

    network = list(ip_bin)
    for i in reversed(range(0, len(mask_bin))):
        if mask_bin[i] == ".":
            continue
        if mask_bin[i] == "1":
            break
        else:
            network[i] = '0'

    network = ''.join(network)
    return ipConverter(network)

def kioszthato_cimek(ip, mask): #visszaadja: elso_kioszthato-utolso-hostok_szama
    mask_bin = check_mask(mask)
    ip_bin = list(ipConverter(ip))
    count_hostbit = 0

    for i in reversed(range(0, len(mask_bin))):
        if mask_bin[i] == ".":
            continue
        if mask_bin[i] == "0":
            ip_bin[i] = "1"
            count_hostbit += 1
        else:
            break
    elso_kioszt = network_ip(ip, mask).split(".")
    elso_kioszt[3] = str(int(elso_kioszt[3]) +1) # +1 et hozza ad az ip vegehez
    #pontokat vissza teszi a tombbe
    elso_kioszt[0] = ''.join(elso_kioszt[0] + ".")
    elso_kioszt[1] = ''.join(elso_kioszt[1] + ".")
    elso_kioszt[2] = ''.join(elso_kioszt[2] + ".")
    elso_kioszt = ''.join(elso_kioszt)

    ip_bin[34] = "0" # utolso kioszthato cim
    utolso_kioszt = ''.join(ip_bin)
    hostok = (2**count_hostbit) -2

    return elso_kioszt + "-" + ipConverter(utolso_kioszt) + "-" + str(hostok)



#print( DecToBin(192) )
#print(BinToDec("11111111"))
#print( network_ip("192.168.64.50", "18") )
#print( kioszthato_cimek("192.168.64.50", "18") )

#print("Eredeti cim: 192.168.10.0")
#print(ipConverter("192.168.10.0"))
#print(ipConverter( ipConverter("192.168.10.0")))

