# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 09:10:46 2021

@author: User
"""

#Program membuat kalkulator bangun ruang
pilih = 5
while pilih < 6 :    
    
    pilih = int(input("""===== KALKULATOR LUAS PERMUKAAN BANGUN RUANG =====
            
1. Kubus
2. Balok
3. Tabung
4. Kerucut
5. Bola
6. Exit 

Pilih Menu yang Tersedia : """))

    

    if pilih == 1 :
        r = int(input("Masukkan Nilai Rusuk : "))
        luas = 6*r*r
        print("Luas permukaan Kubus dengan rusuk",r, "adalah",luas)

    elif pilih == 2 :
        p = int(input("Masukkan Nilai Panjang : "))
        l = int(input("Masukkan Nilai Lebar : "))
        t = int(input("Masukkan Nilai Tinggi : "))
        luas = (2*p*l) + (2*p*t) + (2*l*t)
        print("Luas permukaan balok dengan panjang",p, "lebar",l, "& tinggi ",t, "adalah",luas)

    elif pilih == 3 : 
        jari = int(input("Masukkan jari-jari : "))
        t = int(input("Masukkan Nilai Tinggi : "))
        phi = 22/7
        luas = float(2*phi*jari*(jari+t))
        print("Luas permukaan tabung dengan jari-jari",jari, "dan tinggi",t, "adalah",luas)

    elif pilih == 4 : 
        jari = int(input("Masukkan Nilai Jari-jari : "))
        g_lukis = int(input("Masukkan Nilai Garis Lukis : "))
        phi = 22/7
        luas = float(phi*jari*(jari+g_lukis))
        print("Luas permukaan kerucut dengan jari-jari",jari, "dan garis lukis",g_lukis, "adalah",luas)
    
    elif pilih == 5 : 
        jari = int(input("Masukkan Nilai Jari-jari : "))
        phi = 22/7
        luas = 4/3*(phi*jari*jari*jari)
        print("Luas permukaan bola dengan jari-jari",jari, "adalah",luas)
    
    elif pilih == 6 :
        print("TERIMA KASIH !")
    