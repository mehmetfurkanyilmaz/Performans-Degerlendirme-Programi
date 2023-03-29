#Aylık Net Asgari Ücret: 2020 yılı için belirlenen aylık net asgari ücret, 2324,70 TL’dir.
#Emlak Komisyonu: Emlak acentesinin, yapılan her satış için satış bedelinin %4’ü kadar, her kiralama için 1 aylık kira bedeli kadar kazandığı ücreti ifade etmektedir.
#Emlak Danışmanı: Bir emlak acentesine bağlı olarak çalışan tanıtım ve pazarlama elemanını ifade etmektedir.
#Maaş: Emlak acentesinin, danışmanlarına ödediği aylık ücreti ifade etmektedir.
#Prim: Emlak acentesinin, danışmanlarına maaşlarına ek olarak ödediği, 1 ayda kazandırdıkları
#emlak komisyonu miktarının %10’u tutarındaki ücreti ifade etmektedir.
#Kota: Emlak danışmanlarının, bağlı oldukları emlak acentesine 1 ayda kazandırmaları beklenen emlak komisyonu tutarını ifade etmektedir.
#İkramiye: Emlak acentesinin, danışmanlarına kotalarını doldurmaları durumunda maaşlarına ek olarak ödediği, net asgari ücretin yarısı tutarındaki ücreti ifade etmektedir.
#Aylık Toplam Ücret: Emlak acentesinin, danışmanlarına bir ayda ödediği maaş, prim ve ikramiye toplamını ifade etmektedir.


ASGARI_UCRET=2324.70


en_yuksek_konut_kira_geliri=0  #Tüm kiralıklar içinde ücreti en fazla olan


genel_konut_satilik_olcer = 0    #Bütün satılık konutların sayısını verir.
genel_is_yeri_satilik_olcer = 0
genel_arsa_satilik_olcer = 0


#Bütün veriler için ölçerler
genel_is_yeri_satilik_geliri=0
genel_konut_satilik_geliri=0
genel_arsa_satilik_geliri=0

genel_konut_kiralik_olcer=0
genel_is_yeri_kiralik_olcer=0
genel_arsa_kiralik_olcer=0

genel_konut_kiralik_geliri=0
genel_is_yeri_kiralik_geliri=0
genel_arsa_kiralik_geliri=0


en_pahali_emlak_geliri=0
en_pahali_emlak_tipi=str  #satılanlarda

yetenekli_danisman=str #en pahalı satışı yapan danışman

en_pahali_kiralik=str
en_pahali_kiralik_ucreti=0

kirada_yetenekli_danisman=str  #en pahalı kiralık veren


luks_kiralik=0  #kirası asgari ücretten fazla olan konutlar için
kalitesiz_danisman=0

en_cok_satis_adetine_sahip_danisman=str
en_cok_satis_adeti=0
en_fazla_satilik_geliri=0
en_fazla_gelir_getiren_danisman=str #satışlardan

kotayi_dolduran_danisman=0

hirsli_calisan=0  #primi maasşindan yüksek olan çalışan

iyi_kiralayan_danisman=0

en_yuksek_prim=0
en_yuksek_prim_alan_danisman=str
en_yuksek_prim_alan_danisman_maasi=0
en_yuksek_prim_alan_danisman_primi=0
en_yuksek_prim_alan_danisman_toplam_ucreti=0

en_dusuk_prim=999999
en_dusuk_prim_alan_danisman=str
en_dusuk_prim_alan_danisman_maasi=0
en_dusuk_prim_alan_danisman_primi=0
en_dusuk_prim_alan_danisman_toplam_ucreti=0


butun_maaslar=0

aylik_komisyon=0
konut_kira_ort=0
konut_satilik_geliri_toplami=0


en_cok_satan_danisman=str


en_cok_satan_danisman_geliri=0


en_cok_satilik_geliri=0
en_fazla_gelir_getiren_danismanin_satis_adeti=0



danismanan_sayisi=int(input("Acenteye bağlı olarak çalışan emlak danışmanı sayısıni giriniz (0’dan büyük tamsayı): "))

while danismanan_sayisi<1:
    danismanan_sayisi=int(input("Sıfırdan büyük bir sayı giriniz: "))



for i in range(1,danismanan_sayisi+1):

    konut_satilik_olcer = is_yeri_satilik_olcer = arsa_satilik_olcer = 0  # Kaç tane satıldığının sayısını ölçer.
    konut_kiralik_olcer = is_yeri_kiralik_olcer = arsa_kiralik_olcer = 0  # Kaç tane kiralandığının sayısını ölçer.

    satilik_olcer = 0
    kiralik_olcer = 0

    konut_satilik_geliri = 0  # konutun satılmasından elde edilen gelir.
    arsa_satilik_geliri = 0
    is_yeri_satilik_geliri = 0

    konut_kiralik_geliri = 0  # Konutun kiralanmasından elde edilen gelir.
    arsa_kiralik_geliri = 0
    is_yeri_kiralik_geliri = 0

    en_yuksek_konut_kira = 0

    ad_soyad=str(input("Emlak danışmanının adını, soyadını giriniz: "))


    maas=float(input("Emlak danışmanının maaşını giriniz (TL): "))
    while maas<ASGARI_UCRET :
        maas=float(input("Maaş, asgari ücretin altında olmamalıdır. Tekrar giriniz: "))
    kota=float(input("O ayki kotanızı giriniz (Tl): "))
    while kota<(maas*10) :
        kota=float(input("Kota, maaşın 10 katından düşük olamaz. Tekrar giriniz: "))


    baska_emlak="e"

    while baska_emlak=="E" or baska_emlak=="e":

        emlak_tipi=str(input("Emlak tipini giriniz (Konut, İş yeri, Arsa (K/k/İ/i/A/a karakterleri)): "))
        while not ((emlak_tipi=="K") or (emlak_tipi=="k") or (emlak_tipi =="İ") or (emlak_tipi=="i") or (emlak_tipi=="A") or (emlak_tipi=="a")):
            emlak_tipi=str(input("Geçerli bir emlak tipi giriniz (K/k/İ/i/A/a karakterleri): "))

        islem_turu=str(input("Bu emlak tipine yapılan işlem türünü giriniz (Satış, Kiralama (S/s/K/k karakterleri)): "))
        while not ((islem_turu=="S") or (islem_turu=="s") or (islem_turu=="K") or (islem_turu=="k")):
            islem_turu=str(input("Geçerli bir işlem türü giriniz (Satış, Kiralama (S/s/K/k karakterleri)): "))


        if (islem_turu=="S" or islem_turu=="s"):

            satis_bedeli=int(input("Satış bedelini giriniz: "))

            if (emlak_tipi=="K" or emlak_tipi=="k"):
                konut_satilik_olcer+=1
                genel_konut_satilik_olcer+= 1
                konut_satilik_geliri=satis_bedeli
                genel_konut_satilik_geliri+=konut_satilik_geliri
                if konut_satilik_geliri>en_pahali_emlak_geliri:
                    en_pahali_emlak_geliri=konut_satilik_geliri
                    en_pahali_emlak_tipi="Konut"
                    yetenekli_danisman=ad_soyad


            if (emlak_tipi=="İ" or emlak_tipi=="i"):
                is_yeri_satilik_olcer+=1
                genel_is_yeri_satilik_olcer+= 1
                is_yeri_satilik_geliri=satis_bedeli
                genel_is_yeri_satilik_geliri+=satis_bedeli
                if is_yeri_satilik_geliri>en_pahali_emlak_geliri:
                    en_pahali_emlak_geliri=is_yeri_satilik_geliri
                    en_pahali_emlak_tipi="İş yeri"
                    yetenekli_danisman=ad_soyad

            if (emlak_tipi=="A" or emlak_tipi=="a"):
                arsa_satilik_olcer+=1
                genel_arsa_satilik_olcer+= 1
                arsa_satilik_geliri=satis_bedeli
                genel_arsa_satilik_geliri+=satis_bedeli
                if arsa_satilik_geliri>en_pahali_emlak_geliri:
                    en_pahali_emlak_geliri=arsa_satilik_geliri
                    en_pahali_emlak_tipi="Arsa"
                    yetenekli_danisman=ad_soyad



            toplam_satilik_olcer=konut_satilik_olcer+is_yeri_satilik_olcer+arsa_satilik_olcer
            if toplam_satilik_olcer>en_cok_satis_adeti:
                en_cok_satis_adeti=toplam_satilik_olcer
                en_cok_satis_adetine_sahip_danisman=ad_soyad
                en_cok_satan_danisman_geliri=konut_satilik_geliri+is_yeri_satilik_geliri+arsa_satilik_geliri

            toplam_satilik_gelir=konut_satilik_geliri+is_yeri_satilik_geliri+arsa_satilik_geliri
            if toplam_satilik_gelir>en_cok_satilik_geliri:
                en_cok_satilik_geliri=toplam_satilik_gelir
                en_fazla_gelir_getiren_danisman=ad_soyad
                en_fazla_gelir_getiren_danismanin_satis_adeti=toplam_satilik_olcer

            if toplam_satilik_olcer<1:
                kalitesiz_danisman+=1




        if (islem_turu=="K" or islem_turu=="k"):
            kiralik_olcer+=1
            kira_bedeli=int(input("Kira bedelini giriniz: "))

            if emlak_tipi=="K" or emlak_tipi=="k":
                konut_kiralik_olcer+=1
                konut_kiralik_geliri=kira_bedeli
                genel_konut_kiralik_olcer+=1
                genel_konut_kiralik_geliri+=konut_kiralik_geliri
                if kira_bedeli>en_pahali_kiralik_ucreti:
                    satis_veya_kira_bedeli=en_pahali_kiralik_ucreti


                if konut_kiralik_geliri>en_yuksek_konut_kira:
                    en_yuksek_konut_kira=konut_kiralik_geliri

                if konut_kiralik_geliri>en_yuksek_konut_kira_geliri:
                    en_yuksek_konut_kira_geliri=konut_kiralik_geliri
                    kirada_yetenekli_danisman=ad_soyad


                if konut_kiralik_geliri>ASGARI_UCRET:
                    luks_kiralik+=1


            elif (emlak_tipi=="İ" or emlak_tipi=="i"):
                is_yeri_kiralik_olcer+=1
                is_yeri_kiralik_geliri=kira_bedeli
                genel_is_yeri_kiralik_olcer+=1
                genel_is_yeri_kiralik_geliri+=is_yeri_kiralik_geliri


            elif (emlak_tipi=="A" or emlak_tipi=="a"):
                arsa_kiralik_olcer+=1
                arsa_kiralik_geliri=kira_bedeli
                genel_arsa_kiralik_olcer+=1
                genel_arsa_kiralik_geliri+=arsa_kiralik_geliri

            if ((kiralik_olcer>=10) or (konut_kiralik_geliri+is_yeri_kiralik_geliri+arsa_kiralik_geliri>=25000)):
                iyi_kiralayan_danisman+=1



        baska_emlak=str(input("O ay sattığı/kiraladığı başka emlak olup olmadığını giriniz (E/e/H/h karakterleri): "))
        while not ((baska_emlak == "E") or (baska_emlak == "e") or (baska_emlak == "H") or (baska_emlak == "h")):
            baska_emlak = str(input("O ay sattığı/kiraladığı başka emlak olup olmadığını giriniz (E/e/H/h karakterleri): "))


    satilik_olcer=konut_satilik_olcer+is_yeri_satilik_olcer+arsa_satilik_olcer
    konut_kira_ort = konut_kiralik_geliri / konut_kiralik_olcer
    toplam_satis = satilik_olcer + kiralik_olcer
    kiralik_toplamlari=konut_kiralik_geliri+is_yeri_kiralik_geliri+arsa_kiralik_geliri
    satilik_oran = satilik_olcer / toplam_satis * 100
    kiralik_oran = kiralik_olcer / toplam_satis * 100
    kiralik_ortalamasi = kiralik_toplamlari / kiralik_olcer
    toplam_satilik_gelir=konut_satilik_geliri+arsa_satilik_geliri+is_yeri_satilik_geliri
    emlak_komisyonu = (toplam_satilik_gelir * 4 / 100) + (kiralik_toplamlari)
    prim=emlak_komisyonu/10
    ikramiye=0



    aylik_komisyon += emlak_komisyonu

    if emlak_komisyonu >= kota :
        ikramiye=ASGARI_UCRET/2

    toplam_maas = maas + prim + ikramiye
    butun_maaslar += toplam_maas
    if prim>maas:
        hirsli_calisan+=1


    if prim>en_yuksek_prim:
        en_yuksek_prim=prim
        en_yuksek_prim_alan_danisman=ad_soyad
        en_yuksek_prim_alan_danisman_maasi=maas
        en_yuksek_prim_alan_danisman_primi=prim
        en_yuksek_prim_alan_danisman_toplam_ucreti=toplam_maas

    elif prim<en_dusuk_prim:
        en_dusuk_prim=prim
        en_dusuk_prim_alan_danisman=ad_soyad
        en_dusuk_prim_alan_danisman_maasi=maas
        en_dusuk_prim_alan_danisman_primi=prim
        en_dusuk_prim_alan_danisman_toplam_ucreti=toplam_maas



    print("Danışmanın adı ve soyadı: ",ad_soyad)
    print("Danışmanın o ay sattığı emlak adedi, kiraladığı emlak adedi ve oranları (%): ",satilik_olcer,"oranı:","%","{:,.2f}".format(satilik_oran),"ve",kiralik_olcer,"oranı:","%","{:,.2f}".format(kiralik_oran))
    print("Danışmanın o ay sattığı emlakların tiplerine göre toplam bedelleri: Konut:","{:,.2f}".format(konut_satilik_geliri),"TL","İş yeri:","{:,.2f}".format(is_yeri_satilik_geliri),"TL","Arsa:","{:,.2f}".format(arsa_satilik_geliri),"TL")
    print("Danışmanın o ay kiraladığı konutların ortalama kira bedeli: ","{:,.2f}".format(konut_kira_ort),"TL")
    print("Danışmanın o ay en yüksek bedelle kiraladığı konutun kira bedeli (TL): ","{:,.2f}".format(en_yuksek_konut_kira),"TL")
    print("Danışmanın o ay maaşı:","{:,.2f}".format(maas),"TL")
    print("Danışmanın o ay primi:","{:,.2f}".format(prim),"TL")
    print("Danışmanın o ay kotası:","{:,.2f}".format(kota),"TL")
    print("Danışmanın o ay acenteye kazandırdığı toplam komisyon tutarı:","{:,.2f}".format(emlak_komisyonu),"TL")
    if emlak_komisyonu>=kota:
        print("Danışmanın o ay kotasını doldurup dolduramadığı: Doldurdu. ")
        print("Danışmanın o ay kotasını doldurduysa alacağı ikramiye:","{:,.2f}".format(ikramiye),"TL")
        kotayi_dolduran_danisman+=1
    elif emlak_komisyonu<kota :
        print("Danışmanın o ay kotasını doldurup dolduramadığı: Dolduramadı. ")

    print("Danışmanın o ay toplam ücreti:","{:,.2f}".format(toplam_maas),"TL")



    if toplam_satilik_gelir>en_fazla_satilik_geliri:
        toplam_satilik_gelir=en_fazla_satilik_geliri
        en_fazla_gelir_getiren_danisman=ad_soyad

ortalama_konut_fiyati = genel_konut_satilik_geliri / genel_konut_satilik_olcer
ortalama_is_yeri_fiyati = genel_is_yeri_satilik_geliri / genel_is_yeri_satilik_olcer
ortalama_arsa_fiyati = genel_arsa_satilik_geliri / genel_arsa_satilik_olcer

konut_satin_alma_orani=genel_konut_satilik_olcer/(genel_konut_kiralik_olcer+genel_konut_satilik_olcer)*100
is_yeri_satin_alma_orani=genel_is_yeri_satilik_olcer/(genel_is_yeri_kiralik_olcer+genel_is_yeri_satilik_olcer)*100
arsa_satin_alma_orani=genel_arsa_satilik_olcer/(genel_arsa_kiralik_olcer+genel_arsa_satilik_olcer)*100


luks_kiralik_orani=luks_kiralik/genel_konut_kiralik_olcer*100


print("Her emlak tipi için o ay satılan ve kiralanan emlak sayıları ile satılma oranları (%):")
print("Satılan konut sayısı:",genel_konut_satilik_olcer,"Kiralanan konut sayısı:",genel_konut_kiralik_olcer,"Satın alınma oranı:","%","{:.2f}".format(konut_satin_alma_orani))
print("Satılan iş yeri sayısı:",genel_is_yeri_satilik_olcer,"Kiralanan iş yeri sayısı:",genel_is_yeri_kiralik_olcer,"Satın alınma oranı:","%","{:.2f}".format(is_yeri_satin_alma_orani))
print("Satılan arsa sayısı:",genel_arsa_satilik_olcer,"Kiralanan arsa sayısı:",genel_arsa_kiralik_olcer,"Satın alınma oranı:","%","{:.2f}".format(arsa_satin_alma_orani))
print("Her emlak tipi için o ay satılan emlakların satış bedellerinin toplamı (TL) ve ortalaması (TL):")
print("Satılan konutların toplam fiyatı:","{:,.2f}".format(genel_konut_satilik_geliri),"Konut başına düşen ortalam fiyat:","{:,.2f}".format(ortalama_konut_fiyati))
print("Satılan iş yerlerinin toplam fiyatı:","{:,.2f}".format(genel_is_yeri_satilik_geliri),"İş yeri başına düşen ortalam fiyat:","{:,.2f}".format(ortalama_is_yeri_fiyati))
print("Satılan arsaların toplam fiyatı:","{:,.2f}".format(genel_arsa_satilik_geliri),"Konut başına düşen ortalam fiyat:","{:,.2f}".format(ortalama_arsa_fiyati))
print("O ay en yüksek bedelle satılan emlağın tipi:",en_pahali_emlak_tipi,"Satış bedeli:","{:,.2f}".format(en_pahali_emlak_geliri),"TL", "satışı yapan danışmanın adı-soyadı:",yetenekli_danisman)
print("O ay en yüksek bedelle kiralanan konutun kira bedeli:",en_yuksek_konut_kira_geliri,"TL","kiralayan danışmanın adı-soyadı:",kirada_yetenekli_danisman)
print("O ay kiralanan konutlardan kira bedeli, aylık asgari net ücretten yüksek olan konutların sayısı:",luks_kiralik,"ve kiralanan konutlar içindeki oranı:","%",luks_kiralik_orani)
print("O ay hiç satış yapamayan danışmanların sayısı:",kalitesiz_danisman,"ve tüm danışmanlar içindeki oranı (%):","{:,.2f}".format(kalitesiz_danisman/danismanan_sayisi*100))
print("O ay satış adeti olarak en çok satış yapan danışmanın adı-soyadı:",en_cok_satis_adetine_sahip_danisman,"Sattığı emlak sayıları:",en_cok_satis_adeti,"Toplam satış bedeli:","{:,.2f}".format(en_cok_satan_danisman_geliri))
print("O ay satış bedeli olarak en çok satış yapan danışmanın adı-soyadı:",en_fazla_gelir_getiren_danisman,"Sattığı emlak sayısı:",en_fazla_gelir_getiren_danismanin_satis_adeti,"Toplam satış bedeli:","{:,.2f}".format(en_cok_satilik_geliri))
print("o ay kotasını dolduran danışmanların sayısı:",kotayi_dolduran_danisman,"ve tüm danışmanlar içindeki oranı:","%","{:,.2f}".format(kotayi_dolduran_danisman/danismanan_sayisi*100))
print("o ay primi maaşından yüksek olan danışmanların sayısı:",hirsli_calisan,"ve tüm danışmanlar içindekioranı:","%","{:,.2f}".format(hirsli_calisan/danismanan_sayisi*100))
print("o ay en az 10 adet veya en az 25000 TL tutarında emlak kiralayan danışmanların sayısı:",iyi_kiralayan_danisman)
print("o ay en yüksek prim alan danışmanın adı soyadı:",en_yuksek_prim_alan_danisman,"maaşı:","{:,.2f}".format(en_yuksek_prim_alan_danisman_maasi),"primi:","{:,.2f}".format(en_yuksek_prim_alan_danisman_primi),"aylık toplam ücreti:","{:,.2f}".format(en_yuksek_prim_alan_danisman_toplam_ucreti))
print("o ay en düşük prim alan danışmanın adı soyadı:",en_dusuk_prim_alan_danisman,"maaşı:","{:,.2f}".format(en_dusuk_prim_alan_danisman_maasi),"primi:","{:,.2f}".format(en_dusuk_prim_alan_danisman_primi),"aylık toplam ücreti:","{:,.2f}".format(en_dusuk_prim_alan_danisman_toplam_ucreti))
print("o ay tüm emlak danışmanlarına ödenecek toplam ücretlerin toplamı:","{:,.2f}".format(butun_maaslar),"TL","ve ortalaması:","{:,.2f}".format(butun_maaslar/danismanan_sayisi),"TL")
print("o ay acentenin kazandığı toplam komisyon:","{:,.2f}".format(aylik_komisyon),"TL")