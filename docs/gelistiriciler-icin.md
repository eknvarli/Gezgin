## Gezgin - Geliştiriciler İçin

Gezgin, Flask tabanlı dinamik bir web uygulamasıdır. Gezgin'i forklayabilmek için aşağıdaki aşamaları tamamlamanız gerekmektedir.

- Gezgin'in stillendirmelerini SASS ile geliştirdik. Bu sebeple sayfanın görünümünü önizleyebilmeniz için _.scss_ uzantılı dosyaları compile etmeniz (derlemeniz) gerekmektedir. Bunu en kolay vscode editöründeki _"Live Sass Compiler"_ isimli eklenti ile yapabilirsiniz.

- Gezgin'in altyapısını geliştirebilmek için sisteminizde Python programlama dilinin yüklü olması gerekmektedir. Python yüklü olduğu taktirde komut satırına ```pip install flask``` yazarak Flask modülünü yüklemeniz gerekmektedir. Flask modülü yüklendiğinde _app.py_ isimli dosyayı çalıştırarak uygulamanızı başlatabilirsiniz. Sayfa ```localhost:5000``` adresinde çalışacaktır. Forwarding işlemlerinde port olarak 5000 kullanacaksınız.


### Önemli Not

Gezgin içerisinde dokunmak isteyeceğiniz son şey _.db_ dosyaları olmalıdır. Veritabanı dosyalarına herhangi bir müdahele yaptığınızda (veri ekleyip silmek dahil değildir) program tam anlamıyla bozulacaktır.