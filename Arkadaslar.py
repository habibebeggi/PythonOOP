#Öğrenci numaranızın son hanesindeki rakam kadar arkadaşınızın adı ve telefon numarasını arkadaslar.txt dosyasına yazdıran program:
def main():
    ogrenci_no=int(input('KKu Öğrenci Numaranızı Giriniz: '))
    adet=ogrenci_no % 10
    dosya=open('arkadaslar.txt','a')
    print(adet, 'adet arkadaşınızın isim ve telefon numaralarını giriniz: ')
    for sayac in range(adet):
        print(sayac+1, '.Arkadaş: ' ,sep='')
        isim=input('İsmi: ')
        telefon=input('Telefonu: ')
        dosya.write('İsim: ' + isim + '\n')
        dosya.write('Telefon: ' + telefon + '\n')
    dosya.close()
    print()
    print('arkadaslar.txt dosyasına yazılan veriler aşağıdadır: ')
    print()
    dos=open('arkadaslar.txt', 'r')
    ad=dos.readline()
    tel=dos.readline()
    ad=ad.rstrip('\n')
    tel=tel.rstrip('\n')
    print(ad)
    print(tel)
    while ad !='':
        ad=dos.readline()
        tel=dos.readline()
        ad=ad.rstrip('\n')
        tel=tel.rstrip('\n')
        print(ad)
        print(tel)
main()