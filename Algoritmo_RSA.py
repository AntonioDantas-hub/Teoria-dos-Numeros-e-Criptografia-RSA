from collections import deque
alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ ãáabcdeéêfghijklmnopqrstuvwxyz0123456789!@#$%^&*()-=_+[]{}|\\:;\'\",.<>/?~`"
int_char_map={f'{i:02}': alfabeto[i] if i < len(alfabeto) else 'X' for i in range(100)}
char_int_map={v : k for k,v in int_char_map.items()}

def trad(m):
    digit=''
    for char in m:
        if char in char_int_map:
            digit+=char_int_map[char]
        else:
            print('digito ignorado: ',char)
    return digit
def divisão(m):
    blocos =deque()
    for i in range(0,len(m), 2):
        bloco = m[i:i+2]
        blocos.append(int(bloco))
    return blocos
def impressão(m):
    digit = ''
    m_virt=m.copy()
    while m_virt:
        digit+=str(m_virt.popleft())
    return digit
    
def mdc(a,b):
    while b!=0:
        a,b = b,a %b
    return a
def inv(a,phi):
    if mdc(a, phi) != 1:
        raise ValueError(f"Inverso modular não existe para a={a} e phi={phi}")
    for i in range(2,phi):
        if (i*a)%phi==1:
            return i
    return -1
def gerarchaves(p,q):
    n = p*q
    phi= (p-1)*(q-1)
    e=0
    for e in range(2,phi):
        if mdc(e,phi)==1:break
    d= inv(e,phi)
    return e,d,n
def cod(chunks,e,n):
    ped_virt = chunks.copy()
    codificados = deque()
    while ped_virt:
        bloco = ped_virt.popleft()
        bloco = pow(bloco,e,n)
        codificados.append(bloco)
    return codificados

def decod(chunks,d,n):
    blocos = deque()
    ped_virt =chunks.copy()
    while ped_virt:
        bloco = ped_virt.popleft()
        bloco= pow(bloco,d,n)
        blocos.append(bloco)
    return blocos
def destrad(chunks):
    trad=''
    ped_virt = chunks.copy()
    while ped_virt:
        bloco =str(ped_virt.popleft()).zfill(2)
        if bloco in int_char_map:
                trad+=int_char_map[bloco]
        else:
                print('digito ignorado: ',bloco)
    return trad
def cod_para_men(mens_cod, n):
    tam = len(str(n-1))
    arm= ""
    mens_sec=""
    mv = mens_cod.copy()
    while mv:
        arm+=str(mv.popleft()).zfill(tam)
    if len(arm)%2==1:arm+='0'
    for i in range(0,len(arm),2):
        bloco = arm[i:i+2]
        mens_sec+=int_char_map[bloco]
    return mens_sec
        

#setar as chaves
p,q = map(int,input('digite dois primos para realizar a codificação: ').split())
e,d,n =gerarchaves(p,q)

#pré codificação
mensagem = input('digite sua mensagem: ')
print()
print('-pré-codificação- ')
mensagem= trad(mensagem)
print(f'mensagem traduzida: {mensagem}')
traduzida = divisão(mensagem)
print(f"divisão em blocos para codificação : {list(traduzida)}")

#codificação
print()
print("-codificação- ")
print()
mens_cod=cod(traduzida,e,n)
print(f'Mensagem codificada dividida em blocos:  {list(mens_cod)}')
print(f'texto cifrado: {cod_para_men(mens_cod,n)}')

#decodificação
print()
print("-decodificação-")
print()
mens_decod= decod(mens_cod,d,n)
print(f'mensagem decodificada: {impressão(mens_decod)}')
print(f'mensagem decodificada dividida em blocos para a tradução: {list(mens_decod)}')
mensagem_ori = destrad(mens_decod)
print(f'mensagem original: {mensagem_ori}')