while True:
    seçenekler=["Üye olmak istiyorsanız '1' ","Giriş yapmak için '2' ",
               "Şifrenizi unuttuysanız '3' ","Çıkış yapmak için '4' "]
    print("Hoşgeldiniz.")
    for i in seçenekler:
        print(i)
        
    islem=input("Yapmak istediğiniz işlemin numarasını giriniz:")
     
    if islem=="1":
        print("Yeni üyelik oluşturulacaktır.")
        k_adi=input("Kullanıcı adı oluşturun:")  
        sifre=input("Şifrenizi oluşturun:")
        
    elif islem=="2":
        print("Giriş yapmak için:")
        kullanici="kullanıcıadı"
        parola="şifre"
        k_adi=input("Kullanıcı adınızı giriniz:")
        sifre=input("Şifrenizi giriniz:")
        if kullanici==k_adi and parola==sifre:
            print("Hesabınıza giriş yapıldı.")
        else:
            print("Kullanıcı adı veya şifre yanlış.")
            
    elif islem=="3":
        print("Şifre değiştirmek için yönlendiriliyorsunuz...")
        
    elif islem=="4":
        print("Çıkış yapılıyor...")
        break

    else:
            print("Geçersiz işlem. Tekrar deneyin.")

