**Nama   : Kaisa Dian Ferdinand**

**NPM    : 2206816494**

**Kelas  : PBP C**

**Link Aplikasi : http://kaisa-dian-tugas.pbp.cs.ui.ac.id**

# TUGAS 2

### 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
a. **Membuat sebuah proyek Django baru**:
Pada direktori yang telah saya tentukan, Saya membuat proyek Django baru yang bernama "harta_karun". Saya membuat proyek tersebut dengan membuka terminal di dalam direktori tersebut dan menjalankan kode :  
```python 
django-admin startporject harta_karun
```
b. **Membuat aplikasi main pada proyek tersebut**:
Saya membuat aplikasi main pada direktori proyek "harta_karun" dan menjalankan kode :  
```python
python manage.py startapp main
```
c. **Melakukan routing pada proyek agar dapat menjalankan aplikasi main**:
Setelah membuat aplikasi main, saya menambahkan aplikasi tersebut pada `settings.py` di direktori proyek supaya aplikasi terdaftar pada proyek tersebut.  
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
]
```
d. **Membuat model pada aplikasi dengan nama `Item` dengan atribut sebagai berikut**:
- `name` dengan tipe `CharField`.  
 Atribut tersebut akan menjelaskan nama dari model.
- `amount` dengan tipe `IntegerField`.  
 Atribut tersebutakan menjelaskan total banyak item yang dapat dikoleksi.
- `description` dengan tipe `TextField`.  
 Atribut tersebut mendeskripsikan item tersebut.

Setelah membuat model tersebut, Saya melakukan migrasi untuk menyimpan model dan atributnya pada database dengan menjalankan kode di bawah ini pada terminal.  
~~~
python manage.py makemigrations
python manage.py migrate
~~~
e. **Membuat fungsi `show_main` pada `views.py` untuk dikembalikan ke dalam sebuah template HTML**:
 Pada `views.py`, Saya membuat fungsi yang nantinya akan memberikan data kepada `main.html`.
```python
from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Kaisa Dian Ferdinand',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)
```
Pada fungsi, Saya membuat `context` yang merupakan sebuah dictionary. Keys dari dictionary tersebut akan menjadi variable yang dapat digunakan pada `main.html` dan values merupakan datanya.

f. **Membuat routing pada `urls.py`**:
Pada langkah ini Saya membuat `urls.py` pada direktori aplikasi `main` dan gunanya untuk memetakan fungsi yang telah dibuat pada `views.py` tadi.
```python
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```
Di dalam fungsi `path`, saya membuat parameter pertama sebagai `''` supaya halaman aplikasi tersebut muncul pada halaman utama localpath. Parameter kedua berisikan fungsi yang telah dibuat pada `views.py` dan parameter `name` adalah untuk pengakses fungsi tersebut.

g. **Melakukan deployment ke Adaptable**:
Untuk menerapkan aplikasi yang telah saya kembangkan sehingga teman-teman dapat mengaksesnya melalui Internet, saya melakukan langkah-langkah berikut:
1. Pertama, saya membuat akun **Adaptable.io** menggunakan akun GitHub yang telah saya gunakan untuk membuat proyek harta_karun.
2. Setelah berhasil login, saya memilih tombol `New App` dan opsi `Connect an Existing Repository`. 
3. Hubungkan **Adaptable.io** dengan GitHub dan pilih `All Repositories` selama proses instalasi.
4. Selanjutnya, saya pilih repositori proyek `harta_karun` sebagai dasar aplikasi yang akan  di-deploy. Saya memastikan juga untuk memilih branch yang akan digunakan sebagai branch deployment.
5. Untuk template deployment, saya memilih `Python App Template`.
6. Pilih jenis basis data yang akan digunakan. Dalam kasus ini, saya memilih `PostgreSQL`.
7. Saya pastikan versi Python sesuai dengan spesifikasi aplikasi harta_karun. Untuk memeriksanya, saya aktifkan virtual environment dan gunakan perintah `python --version`.
8. Pada bagian `Start Command`, saya masukkan perintah `python manage.py migrate && gunicorn harta_karun.wsgi`.
9. Selanjutnya, saya memasukkan nama aplikasi, yang juga akan menjadi nama domain situs web aplikasi kita.
10. Terakhir, saya mencentang opsi `HTTP Listener on PORT`, lalu klik `Deploy App` untuk memulai proses deployment aplikasi.

Dengan mengikuti langkah-langkah di atas, aplikasi saya akan siap untuk diakses oleh teman-teman melalui Internet.
  
### 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html. 
![Bagan](gambar_readme/bagan.png)
- `urls.py` : Ketika User melakukan request kepada website, maka request tersebut akan diteruskan kepada fungsi yang sesuai pada halaman itu dan terdaftar dalam urlpatterns halaman tersebut. Pada halaman utama website ini, request akan diarahkan ke fungsi `show_main` yang terletak di dalam file `views.py`.
- `views.py` : Di dalam berkas `views.py`, terdapat sebuah fungsi bernama `show_main` yang menerima parameter `request` untuk menerima permintaan dari pengguna. Dalam fungsi ini, kita menggunakan `context`, yang merupakan sebuah kamus (dictionary), untuk menyediakan data yang akan ditampilkan di berkas `main.html`. Fungsi ini memilih berkas `main.html` untuk menampilkan data yang diperoleh dari basis data kepada pengguna nantinya.
- `models.py` : Pada aplikasi ini, semua model yang digunakan dibuat dalam bentuk class di file yang bersangkutan. Dalam aplikasi utama ini, ada pembuatan model yang disebut **Item** yang memiliki beberapa atribut. Di dalam file `views.py`, dapat diciptakan beberapa object seperti dictionary context dengan isi nama dan kelas, kemudian dikirim ke halaman `main.html`.
- `main.html` : Data yang diterima dari `views.py` akan ditampilkan pada file html ini dan dapat dilihat oleh User.

### 3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
- **Virtual environment** digunakan dalam pengembangan aplikasi web berbasis Django untuk mengisolasi dependensi dan paket Python proyek secara lokal, menghindari konflik, mengontrol versi, memungkinkan portabilitas, menjaga kebersihan pengembangan, dan meningkatkan keamanan. Meskipun kita dapat membuat aplikasi Django tanpa virtual environment, tetapi sangat disarankan untuk menggunakan alat ini karena jika meng-install semua package pada local environment, bisa terjadi tabrakan ketika kita sedang bekerja pada berbagai proyek yang berbeda.

### 4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
**MVC**, **MVT**, dan **MVVM** adalah tiga pola desain (design pattern) yang digunakan dalam pengembangan perangkat lunak untuk mengorganisasi kode dan logika aplikasi. Masing-masing memiliki tujuan dan struktur yang berbeda. Berikut adalah penjelasan singkat tentang ketiganya beserta perbedaan utama:

a. **MVC (Model-View-Controller)**:
   - **Model**: Mewakili data dan logika bisnis dalam aplikasi. Ini adalah bagian yang bertanggung jawab untuk mengelola data, menghitung, dan mengolah informasi.
   - **View**: Bertanggung jawab untuk menampilkan data dari Model ke pengguna akhir. View berinteraksi dengan pengguna dan menampilkan informasi secara visual.
   - **Controller**: Bertindak sebagai perantara antara Model dan View. Ini mengontrol aliran data dan logika aplikasi. Ketika pengguna berinteraksi dengan View, Controller meresponsnya dengan mengubah Model jika diperlukan.

   **Perbedaan utama**:
   - MVC adalah pola desain yang terpusat pada pemisahan tanggung jawab antara Model, View, dan Controller. Ini sering digunakan dalam pengembangan aplikasi web dan desktop.
   - MVC tidak mengatur secara ketat bagaimana komunikasi antara komponen harus terjadi, sehingga dapat bervariasi dalam implementasinya.

b. **MVT (Model-View-Template)**:
   - **Model**: Sama dengan dalam MVC, mewakili data dan logika bisnis.
   - **View**: Menampilkan data dan mengatur tampilan.
   - **Template**: Bertanggung jawab untuk menghasilkan tampilan dinamis berdasarkan Model. Ini mirip dengan View dalam MVC, tetapi tugasnya lebih fokus pada tampilan.

   **Perbedaan utama**:
   - MVT adalah varian dari MVC yang sering digunakan dalam kerangka kerja Django, yang sangat populer dalam pengembangan web dengan bahasa pemrograman Python.
   - Perbedaan utama adalah penggunaan "Template" yang memisahkan tampilan dari kode HTML dalam konteks MVT.

c. **MVVM (Model-View-ViewModel)**:
   - **Model**: Sama seperti dalam MVC dan MVT, mewakili data dan logika bisnis.
   - **View**: Mirip dengan View dalam MVC dan MVT, menampilkan data ke pengguna.
   - **ViewModel**: Bertindak sebagai perantara antara Model dan View. ViewModel berisi logika presentasi dan transformasi data. Ini memungkinkan View untuk menjadi lebih terpisah dari Model, sehingga lebih mudah untuk mengatur tampilan berdasarkan data.

   **Perbedaan utama**:
   - MVVM adalah pola desain yang sering digunakan dalam pengembangan aplikasi berbasis platform, terutama dalam pengembangan aplikasi berbasis teknologi seperti WPF (Windows Presentation Foundation) dan Xamarin.
   - ViewModel adalah komponen kunci yang membedakan MVVM dari MVC dan MVT. Ini memungkinkan tampilan untuk lebih mandiri dalam memproses dan menampilkan data.

Pilihan antara MVC, MVT, dan MVVM tergantung pada bahasa pemrograman, platform, dan kebutuhan aplikasi. Semua pola desain ini bertujuan untuk meningkatkan pemeliharaan, skalabilitas, dan struktur dalam pengembangan perangkat lunak.

### ----------------------------------------------------------------------------------------------------------------

# TUGAS 3

### 1. Apa perbedaan antara form POST dan form GET dalam Django?
a. `GET` umumnya dipakai untuk operasi baca saja yang aman, di mana data dapat terlihat di `URL` dan dibagikan dengan mudah. `GET` menggabungkan data yang dikirim menjadi **string**, lalu menggunakannya untuk membuat `URL` yang berisi alamat tujuan pengiriman data, beserta kunci dan nilai data. Sementara `POST` digunakan untuk operasi yang mengubah status server atau melibatkan data yang sensitif dan tidak boleh tampil di `URL`. `POST` memiliki proteksi `CSRF Django` yang memberikan kontrol lebih terhadap akses.

b.  Penggunaan `POST` sangat sesuai untuk formulir `login`, karena umumnya memerlukan **kata sandi**. Karena kata sandi adalah informasi sensitif, sebaiknya tidak ditampilkan dalam `URL`. Sedangkan metode `GET` sangat cocok untuk formulir pencarian web, karena `URL` terkait dengan permintaan `GET` bisa dengan mudah di-***bookmark***, dibagikan, atau digunakan kembali.

### 2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
a. **HTML (HyperText Markup Language)** berfungsi sebagai dasar dalam pengembangan web dan digunakan untuk menentukan struktur halaman. Fungsinya adalah menjelaskan tata letak data pada sebuah halaman web. HTML digunakan oleh browser web untuk menginterpretasikan dan merangkai teks, gambar, serta konten lainnya menjadi halaman web yang dapat dilihat atau didengar.

b. **JSON (JavaScript Object Notation)** dipergunakan untuk penyimpanan dan pengiriman data. Ini merupakan metode untuk menggambarkan objek dengan format pertukaran data berbasis teks yang terdiri dari pasangan key-value. File JSON jauh lebih mudah dibaca daripada XML karena lebih singkat.

c. **XML (eXtensible Markup Language)** digunakan untuk merepresentasikan data dengan cara yang dapat dipahami oleh mesin. XML adalah bahasa markup yang bersifat fleksibel dan memungkinkan definisi struktur data yang kompleks. XML menggunakan tag untuk menggambarkan item data.

### 3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
Pada umumnya, **JSON** digunakan untuk mengirim data melalui koneksi internet dan untuk proses serialisasi. **JSON** memiliki peran utama dalam mengirim data antara aplikasi web dan server. **JSON** menjadi populer di dunia ***code programming*** dan layanan web karena mampu meningkatkan pertukaran data dan efisiensi hasil layanan web. **JSON** adalah format data berbasis teks yang ringan dan mudah diurai, sehingga tidak memerlukan kode tambahan untuk parsing.

### 4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
#### a. Membuat input form untuk menambahkan objek model pada app sebelumnya. 
Untuk membuat form, agar aplikasi saya bisa digunakan untuk menginput Item berikut adalah step-stepnya:

1. . Membuat file `forms.py` di direktori main
Isi file tersebut adalah import ModelForm dari django.forms dan import Item dari main.models.
Lalu, saya membuat class ItemForm yang menerima parameter ModelForm, di dalamnya terdapat class Meta dengan `fields` = `name`, `amount`, dan `description"`.
2. Menambahkan import di file `views.py` yang berada di folder main.
Saya menambahkan:
```python
import HttpResponseRedirect, ProductForm, dan reverse.
```
3. Membuat fungsi `create_item` di dalam file `views.py` tersebut.
  Fungsi ini bertujuan agar bisa membuat formulir yang dapat menambahkan data produk ke dalam database secara otomatis ketika pengguna mengirimkan data melalui formulir.
4. Mengubah fungsi `show_main` untuk mengambil semua object Item yang ada di database
  Caranya dengan menambahkan `'items': items` di dalam variable `context`.
5. Mengimport fungsi `create_item` ke file `urls.py` di dalam folder main.
  Saya menambahkan import `create_item` dari `main.views`.
6. Menambahkan path url yang sesuai
  Saya membuat path baru
  ```python
  path('create-item', create_item, name='create_item'),
  ```
7. Membuat file HTML baru bernama `create_item.html` pada direktori main dalam folder templates.
  Saya membuat tabel untuk menunjukkan data yang tersimpan di database.
8. Menambahkan kode di file `main.html` untuk menampilkan data item yang telah di input
  Untuk melakukan hal tersebut, saya menambahkan kode:
```html
    <style>
        .special-paragraph {
            margin-top: 45px;
            margin-bottom: 10px;
        }

        table {
            width: 100%;
            border-collapse: collapse;
        }
    
        th, td {
            border: 1px solid #dddddd;
            text-align: left;
            padding: 8px;
        }
    
        tr:nth-child(even) {
            background-color: #f2f2f2;
        }
    </style>

    <p class="special-paragraph">Kamu menyimpan <strong>{{total}}</strong> item pada aplikasi ini</p>

    <table>
        <tr>
            <th>Name</th>
            <th>Amount</th>
            <th>Description</th>
        </tr>
    
        {% comment %} Berikut cara memperlihatkan data item di bawah baris ini {% endcomment %}
    
        {% for item in items %}
            <tr>
                <td>{{item.name}}</td>
                <td>{{item.amount}}</td>
                <td>{{item.description}}</td>
            </tr>
        {% endfor %}
    </table>
```
Lalu, saya membuaat button untuk menambahkan item dan diarahkan ke url create_item.
```html
    <a href="{% url 'main:create_item' %}">
        <button>
            Add New Item
        </button>
    </a>
```

#### b. Menambahkan fungsi `views` untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID.
Saya menambahkan kode berikut dalam file `views.py` yang berada di main.
```python
def show_main(request):
    items = Item.objects.all()

    context = {
        'name': 'Kaisa Dian Ferdinand', # Nama kamu
        'class': 'PBP C', # Kelas PBP kamu
        'items': items,
        'total': items.count()
    }

    return render(request, "main.html", context)

def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
Dengan lima fungsi views ini, kita dapat melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID di aplikasi Django `harta_karun`.

#### c. Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.
Routing URL memungkinkan aplikasi untuk menghubungkan URL tertentu dengan view yang sesuai. Ketika user mengakses URL tertentu, Django akan menggunakan routing URL untuk menentukan view yang harus dipanggil.
Pada file `urls.py` pada direktori main, saya menambahkan kode berikut:
```python
urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-item', create_item, name='create_item'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
]
```

# POSTMAN

### ***Screenschot*** Postman (HTML)
![Postman HTML](gambar_readme/html.png)

### ***Screenschot*** Postman (XML)
![Postman XML](gambar_readme/xml.png)

### ***Screenschot*** Postman (JSON)
![Postman JSON](gambar_readme/json.png)

### ***Screenschot*** Postman (XML ***by*** ID)
![Postman XML by ID](gambar_readme/xmlbyid.png)

### ***Screenschot*** Postman (JSON ***by*** ID)
![Postman JSON by ID](gambar_readme/jsonbyid.png)


### ----------------------------------------------------------------------------------------------------------------

# TUGAS 4

### 1. Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?

**Django UserCreationForm** adalah kelas `form` bawaan yang disediakan oleh sistem autentikasi pengguna Django. Kelas ini dirancang untuk memudahkan pembuatan akun pengguna baru dalam aplikasi Django. **UserCreationForm** adalah turunan dari kelas `ModelForm`, yang memungkinkan pengembang membuat formulir registrasi pengguna dengan lebih mudah. Form ini menyederhanakan proses pengumpulan dan validasi data pendaftaran pengguna, seperti nama pengguna dan kata sandi, sehingga mempermudah implementasi fungsi registrasi pengguna dalam proyek Django.

Kelebihan dari penggunaan **UserCreationForm** adalah:

1. **Keamanan dan Keandalan**: Django memiliki sistem manajemen kata sandi yang kuat dengan model User bawaan. Defaultnya, sistem kata sandi sudah memberikan tingkat keamanan yang tinggi tanpa memerlukan usaha tambahan dari pengembang.

2. **Validasi Data**: Form ini menyediakan validasi bawaan untuk data pendaftaran pengguna, sehingga memastikan bahwa data yang dimasukkan oleh pengguna sesuai dengan aturan yang ditetapkan.

3. **Unik Username**: UserCreationForm memastikan bahwa nama pengguna yang dibuat oleh pengguna baru adalah unik. Keunikan ini diperiksa pada tingkat database dan juga diverifikasi oleh form yang disediakan oleh Django.

Namun, ada beberapa kekurangan dalam penggunaan **UserCreationForm**:

1. **Keterbatasan Dalam Modifikasi Data Fields**: Memodifikasi data fields seperti menghapus atau menambahkan data pada UserCreationForm tidaklah mudah. Framework ini tidak secara fleksibel mendukung perubahan ini.

2. **Keterbatasan dalam Penggunaan Model User Default**: Model User default yang disediakan oleh Django dibuat di database aplikasi secara otomatis saat pembuatan proyek Django baru. Ini dapat mengakibatkan keterkaitan yang kompleks dengan model pengguna default, sehingga mengubahnya dapat memiliki efek yang tidak diinginkan pada aplikasi, terutama jika Anda menggunakan pustaka pihak ketiga.

### 2. Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?

Perbedaan antara autentikasi dan otorisasi dalam konteks Django adalah sebagai berikut:

- **Autentikasi**: Ini melibatkan verifikasi identitas pengguna melalui proses seperti nama pengguna dan kata sandi. Django memiliki sistem autentikasi yang kuat untuk memastikan bahwa hanya pengguna yang sah yang dapat mengakses aplikasi.
  
- **Otorisasi**: Setelah pengguna berhasil diautentikasi, otorisasi menentukan hak akses pengguna, seperti apa yang dapat dilihat atau diubah. Django menggunakan sistem berbasis peran dan izin untuk mengendalikan otorisasi, memastikan bahwa pengguna hanya memiliki akses sesuai dengan peran atau izin mereka. 

Keduanya penting untuk menjaga keamanan dan integritas aplikasi web. Autentikasi melindungi dari akses tidak sah, sementara otorisasi membatasi hak akses sesuai dengan peran atau izin pengguna.

### 3. Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?

**Cookies** adalah data kecil yang disimpan pada perangkat pengguna oleh ***server web***. Django menggunakan **cookies** untuk menyimpan dan mengelola data sesi pengguna, seperti preferensi dan identifikasi pengguna. Data sesi disimpan dalam **cookies** yang dikirim ke ***browser*** pengguna, dengan pengamanan bawaan untuk melindungi integritasnya. Django memungkinkan pengembang untuk mengonfigurasi pengaturan **cookies**, dan data sesi dapat diakses oleh aplikasi web untuk personalisasi dan otorisasi.

### 4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?

Penggunaan **cookies** dalam pengembangan web memiliki keuntungan, seperti pengelolaan sesi pengguna dan personalisasi, namun juga membawa risiko keamanan. Risiko ini meliputi keamanan data, potensi pencurian cookies, dan masalah privasi. Dengan begitu, untuk mengurangi risiko, perlu mengimplementasikan enkripsi, kebijakan privasi yang jelas, dan pencegahan kerentanan keamanan seperti XSS. Keseluruhan, **cookies** akan aman jika diatur dengan baik dan memperhatikan kebijakan privasi serta keamanan data pengguna.

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

#### a. Menimplementasikan fungsi regitrasi, login, logout, update item amount, dan delete item
Fungsi `register` memungkinkan ***user*** baru untuk membuat akun di aplikasi. Fungsi `login` memungkinkan ***user*** yang telah terdaftar untuk masuk ke dalam akun mereka. Fungsi `logout` memungkinkan ***user*** untuk keluar dari akun mereka dan mengakhiri sesi mereka. Fungsi `update_item_amount` memungkinkan ***user*** untuk menambahkan atau meng-***update*** jumlah item yang telah terdaftar. Fungsi `delete_item` memungkinkan ***user*** untuk menghapus item yang telah terdaftar.

Pertama, pada file `views.py`` dalam direktori main saya mengimport **redirect**, **UserCreationForm**, **messages**, **authenticate**, **login**, **logout**, dan **Http404**. 

Lalu, saya menambahkan beberapa fungsi di dalam file `views.py` dalam direktori main, yaitu:

```python
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/login')
def update_item_amount(request):
    if request.method == "POST":
        item_id = request.POST.get('item_id')
        amount = request.POST.get('amount')

        try:
            item = Item.object.get(pk=item_id)
            if amount == 'add':
                item.amount += 1
            elif amount == 'reduce':
                if item.amount > 0:
                    item.amount -= 1
            item.save()
        except Item.DoesNotExist:
            raise Http404

@login_required(login_url='/login')
def delete_item(request):
    if request.method == "POST":
        item_id = request.POST.get('item_id')

        try:
            item = Item.objects.get(pk=item_id, user=request.user)
            item.delete()
        except Item.DoesNotExist:
            pass

    return redirect('main:show_main')
```

Setelah itu, di direktori `main` > `templates` saya membuat file html baru bernama `register.html` yang berisi form registrasi yang akan mengambil input dari user, mengirimkannya melalui metode POST, dan juga menampilkan pesan-pesan kepada user. Saya juga menghias page tersebut dengan menambahkan style di file html tersebut.

Saya juga membuat file `login.html` dalam direktori `main` > `templates`. File ini berfungsi sebagai halaman ***login*** dalam sebuah aplikasi web. Halaman ini memuat form ***login*** yang mengambil input ***username*** dan ***password*** dari ***user***. Ketika formulir ini di-***submit***, data akan dikirimkan dengan metode **POST**. Halaman juga menampilkan pesan-pesan kepada ***user*** jika terdapat pesan-pesan yang perlu ditampilkan, seperti pesan kesalahan saat ***login*** gagal. Terakhir, halaman ini menyertakan tautan untuk menuju halaman registrasi jika user belum memiliki akun, dengan menggunakan tautan yang mengarah ke URL untuk halaman ***register***.

Untuk ***logout***, saya hanya menambahkan ***button logout*** pada `main.html`. Saya juga membuat halaman main terbatas penggunaannya dengan menambahkan `login_required` pada file `views.py` di direktori main.

Untuk ***update_item_amount*** dan ***delete_item***, saya hanya menambahkan ***button logout*** 
```python
<td>{{item.amount}}</td>
<td class="center-cell">
    <form method="POST" action="{% url 'main:update_item_amount' %}">
        {% csrf_token %}
        <input type="hidden" name="item_id" value="{{ item.id }}">
        <button type ="submit" name="amount" value="add">+</button>
    </form>
</td>
<td>{{item.description}}</td>
<td class="center-cell">
    <form method="POST" action="{% url 'main:delete_item' %}">
        {% csrf_token %}
        <input type="hidden" name="item_id" value="{{ item.id }}">
        <button type ="submit">Delete</button>
    </form>
</td>
```

Di file `urls.py` saya menambahkan import **register**, **login_user** **logout_user**, **update_item_amount**, dan **delete_item**. Saya juga menambahkan path-path yang sesuai pada **urlpatterns**, sebagai berikut:

```python
path('register/', register, name='register'),
path('login/', login_user, name='login'),
path('logout/', logout_user, name='logout'),
path('update_item_amount/', update_item_amount, name='update_item_amount'),
path('delete_item/', delete_item, name='delete_item'),
```

#### b. Membuat dua akun pengguna dengan masing-masing tiga ***dummy data*** menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.
Untuk bagian ini, saya melakukan registrasi 2 kali dengan nama akun yang berbeda, yaitu bambang dan Susanti. Lalu, saya login dan menambahkan 3 item di aplikasi harta karun saya. Saya lalukan hal yang sama untuk akun kedua saya dengan data yang berbeda.

#### c. Menghubungkan model `Item` dengan `User`.
Pertama, pada file `models.py` di direktori `main`, saya meng-***import*** `User`. Dengan meng-***import*** `User`, aplikasi saya bisa digunakan untuk membuat, mengelola, dan mengautentikasi akun ***user***. Saya juga menggunakannya sebagai referensi saat menampilkan data milik ***user***. Lalu, saya menambahkan kode:
```python
user = models.ForeignKey(User, on_delete=models.CASCADE)
```
untuk menghubungkan objek dalam model saat ini dengan objek dalam model `User` dari Django. Opsi `on_delete=models.CASCADE` menentukan bahwa ketika objek `User` terkait dihapus, objek dalam model saat ini yang menggunakan ***foreign key*** tersebut juga akan dihapus secara otomatis untuk menjaga konsistensi dalam database.

Setelah itu, dalam fungsi `create_item` dalam file `views.py` dalam main, saya memodifikasi fungsinya dengan menyisipkan:
```python
if form.is_valid() and request.method == "POST":
     product = form.save(commit=False)
     product.user = request.user
     product.save()
     return HttpResponseRedirect(reverse('main:show_main'))
```
untuk memproses data dari form, menghubungkannya dengan ***user*** yang ***login*** saat ini, menyimpannya ke dalam database, dan mengarahkan ***user*** ke halaman main setelah berhasil tersimpan. Dalam fungsi `show_main` saya mengubah ***value context*** nama menjadi `request.user.username` untuk menyesuaikan ***user*** yang ***login***. Tidak lupa, saya menambahkan `items = Item.objects.filter(user=request.user)` untuk hanya menampilkan data dari ***user*** spesifik yang sedang ***login***.

Terakhir, saya melakukan migrasi untuk menyimpan perubahan data.

#### d. Menampilkan detail informasi pengguna yang sedang logged in seperti ***username dan*** menerapkan `cookies` seperti `last login` pada halaman utama aplikasi.
Pada file `models.py`, saya membuat relasi antara item dengan ***foreign key***. Caranya dengan menambahkan kode
```python
user = models.ForeignKey(User, on_delete=models.CASCADE)
```
***ForeignKey*** digunakan untuk menyambungkan suatu objek dengan objek lain, dalam konteks ini menghubungkan setiap item dengan ***user*** yang membuatnya.

Untuk menampilkan siapa yang sedang ***login*** dalam aplikasi, saya memodifikasi fungsi `show_main` dengan cara mengubah ***value context*** nama menjadi `request.user.username` untuk menyesuaikan ***user*** yang ***login***.

Untuk menampilkan data ***last login*** pada aplikasi, pertama-tama saya mengimport `datetime` di file `views.py` dalam `main`. 
Lalu, saya memodifikasi kode saya bagian `login_user` menjadi:
```python
if user is not None:
    login(request, user)
    response = HttpResponseRedirect(reverse("main:show_main")) 
    response.set_cookie('last_login', str(datetime.datetime.now()))
    return response
```
Bagian ini untuk memproses ***login user*** dalam aplikasi web yang melibatkan otentikasi, pengaturan sesi, mengirim `cookie`, dan mengarahkan ***user*** ke halaman yang sesuai.
Lalu, tidak lupa saya menambahkan `context` pada fungsi `show_main` dengan menambahkan:
```python
'last_login': request.COOKIES['last_login'],
```
Lalu, di bagian fungsi `logout_user` saya menambahkan baris kode:
```python
response = HttpResponseRedirect(reverse('main:login'))
response.delete_cookie('last_login')
```
untuk menghapus data cookie pengguna yang baru saja logout.

Pada file `main.html` saya menggunakan context `last_login` dengan cara:
```html
<h5>Last entered MyWardrobe: {{ last_login }}</h5>
```
untuk memberikan informasi user yang sedang login.


### ----------------------------------------------------------------------------------------------------------------

# TUGAS 5

### 1. Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.
Tentu, saya akan menjelaskan secara detail tentang setiap elemen selector CSS:

#### a. **Universal Selector (*)**: Selector universal memilih semua elemen dalam dokumen HTML. Ini digunakan ketika kita ingin menerapkan gaya ke seluruh elemen di halaman web kita. Contohnya:

   ```css
   * {
       color: red;
   }
   ```

   Ini akan mengubah warna teks semua elemen menjadi merah.

#### b. **Element Selector**: Selector elemen memilih elemen berdasarkan nama elemennya. Misalnya, untuk memilih semua elemen `<p>`, kita dapat menggunakan:

   ```css
   p {
       font-size: 16px;
   }
   ```

   Ini akan mengatur ukuran font untuk semua elemen paragraf menjadi 16 piksel.

#### c. **Class Selector (.)**: Selector kelas memilih elemen berdasarkan nilai atribut `class`. Ini memungkinkan kita untuk memilih satu atau beberapa elemen dengan kelas tertentu. Contohnya:

   ```html
   <p class="highlight">Ini adalah teks yang di-highlight.</p>
   ```

   Kemudian dalam CSS:

   ```css
   .highlight {
       background-color: yellow;
   }
   ```

   Ini akan memberi latar belakang kuning pada semua elemen dengan kelas "highlight".

#### d. **ID Selector (#)**: Selector ID memilih elemen berdasarkan nilai atribut `id`. ID harus unik dalam dokumen. Contohnya:

   ```html
   <div id="header">Ini adalah header.</div>
   ```

   Kemudian dalam CSS:

   ```css
   #header {
       font-weight: bold;
   }
   ```

   Ini akan mengubah teks dalam elemen dengan ID "header" menjadi tebal.

#### e. **Descendant Selector ( )**: Selector turunan memilih elemen yang merupakan keturunan atau nested dalam elemen lain. Ini digunakan dengan spasi. Contohnya:

   ```html
   <div>
       <p>Paragraf dalam div.</p>
   </div>
   ```

   Dalam CSS:

   ```css
   div p {
       color: blue;
   }
   ```

   Ini akan mengubah warna teks dalam paragraf yang berada dalam elemen div.

#### f. **Child Selector (> )**: Selector anak memilih elemen yang langsung merupakan anak dari elemen lain. Ini digunakan dengan tanda ">" . Contohnya:

   ```html
   <ul>
       <li>Item 1</li>
       <li>Item 2</li>
   </ul>
   ```

   Dalam CSS:

   ```css
   ul > li {
       list-style-type: square;
   }
   ```

   Ini akan memberi tipe daftar kotak pada elemen li yang merupakan anak langsung dari elemen ul.

#### g. **Adjacent Sibling Selector (+)**: Selector saudara sejajar memilih elemen yang sejajar atau berdekatan satu sama lain. Ini digunakan dengan tanda "+". Contohnya:

   ```html
   <h2>Heading 1</h2>
   <p>Paragraf 1</p>
   <h2>Heading 2</h2>
   <p>Paragraf 2</p>
   ```

   Dalam CSS:

   ```css
   h2 + p {
       font-style: italic;
   }
   ```

   Ini akan memberi gaya miring pada paragraf yang berada tepat setelah elemen h2.

### 2. Jelaskan HTML5 Tag yang kamu ketahui.

- `<header>`: Digunakan untuk mengelompokkan elemen-elemen pembukaan halaman web atau bagian tertentu dari halaman.
- `<nav>`: Mendefinisikan bagian navigasi dari halaman web.
- `<main>`: Menunjukkan konten utama dalam halaman web.
- `<section>`: Digunakan untuk mengelompokkan konten terkait dalam sebuah halaman.
- `<footer>`: Mendefinisikan bagian bawah halaman atau bagian penutup.
- `<figure>`: Digunakan untuk mengelompokkan elemen-elemen multimedia bersama dengan caption.
- `<figcaption>`: Memberikan caption atau teks deskriptif untuk elemen-elemen dalam `<figure>`.
- `<time>`: Digunakan untuk menandai informasi waktu atau tanggal dalam dokumen.
- `<mark>`: Digunakan untuk menyorot atau menandai teks dalam dokumen.
- `<meter>`: Digunakan untuk mengukur dan menampilkan nilai dalam skala tertentu.
- `<progress>`: Digunakan untuk menampilkan kemajuan dari tugas atau proses.
- `<details>`: Digunakan untuk menyembunyikan atau menampilkan informasi tambahan yang bisa di-expand atau di-collapse.
- `<summary>`: Digunakan sebagai judul atau teks yang menampilkan informasi singkat tentang elemen `<details>`.
- `<code>`: Digunakan untuk menandai kode komputer atau skrip.

### 3. Jelaskan perbedaan antara margin dan padding.

Perbedaan antara Margin dan Padding:

**Margin**: Margin adalah sejenis "ruang tambahan" di sekitar elemen HTML, yang berada di antara elemen tersebut dan elemen-elemen lain yang ada di sekitarnya. Gaya margin digunakan untuk mengontrol jarak antara elemen dengan elemen-elemen lain di sekitarnya. Margin tidak memiliki latar belakang atau warna, fungsinya hanyalah untuk mengatur ruang di sekitar elemen. 

Sedangkan, **Padding**: Padding adalah area "kosong" di sekitar konten dalam elemen HTML. Padding digunakan untuk mengontrol jarak antara batas elemen dan kontennya sendiri. Dengan padding, kita dapat mengubah warna atau latar belakang elemen tersebut sehingga paddingnya bisa terlihat. Padding digunakan untuk mengatur tampilan elemen dari bagian dalamnya.

### 4. Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?

Perbedaan antara Bootstrap dan Tailwind CSS:

**Bootstrap** adalah kerangka kerja CSS yang sudah siap pakai (framework) yang menyediakan berbagai komponen UI dan gaya bawaan.
- Lebih kaya fitur dan komprehensif dibandingkan dengan Tailwind CSS.
- Cocok untuk proyek besar dengan banyak komponen UI yang berbeda.
- Menggunakan kelas-kelas bawaan yang sudah ditentukan dengan baik.
- Lebih mudah untuk pengembang pemula karena menyediakan banyak komponen dan gaya siap pakai.

Sedangkan, **Tailwind CSS** adalah kerangka kerja CSS "utility-first" yang memungkinkan kita untuk membangun komponen dengan mengkombinasikan kelas-kelas kecil.
- Lebih fleksibel dan ringan dibandingkan dengan Bootstrap karena tidak memiliki gaya bawaan.
- Cocok untuk proyek yang memerlukan kustomisasi tingkat tinggi dan ingin menghindari gaya bawaan.
- Mengharuskan pengembang mendefinisikan gaya mereka sendiri dengan menambahkan kelas-kelas sesuai kebutuhan.

Kemudian, sebaiknya menggunakan **Bootstrap** jika kita ingin cepat membangun prototipe atau proyek dengan komponen UI yang sudah siap pakai sehingga ini cocok untuk proyek besar dengan banyak komponen yang sama. Di sisi lain, **Tailwind CSS**sebaiknya digunakan jika kita ingin kustomisasi tingkat tinggi, lebih ringan, dan ingin menghindari gaya bawaan yang cocok untuk proyek yang memerlukan tampilan unik atau tampilan yang sangat disesuaikan.

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

Saya menambahkan style-style menggunakan CSS dan beberapa komponen bootstrap yang berfungsi untuk mengkustomisasi halaman `create_item`, `edit_item`, `login`, `main`, dan juga `register`. Dalam `main.html` saya mengkustomisasi dengan menambahkan style dengan Class Selector seperti berikut:

```html
<style>
    .navbar {
        display: flex;
        justify-content: center;
    }

    .nav-links {
        text-align: center;
    }

    body {
        background: radial-gradient(circle, #FD8D14, #FFDBAA, white);
        margin: 0 70px;
    }

    .container {
        text-align: center;
    }

    .header {
        border-radius: 20px;
        padding: 20px;
        margin: 30px 0 -30px;
    }

    .header h1 {
        font-family: 'Treasure Map', serif;
        font-size: 36px;
    }

    .quote {
        font-style: italic;
        margin-bottom: 50px;
    }

    .info-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .info-container {
        display: flex;
        justify-content: space-between;
        margin: -25px 0 30px;
        padding: 5px;
        width: 30%;
    }

    .info-container h5 {
        margin-bottom: 2px;
        font-family: 'Treasure Map', sans-serif;
    }

    .info-box h5 {
        margin-top: -10px;
    }

    .item-table {
        border-radius: 15px;
        width: 100%;
        margin: 0 auto;
    }

    .item-table th,
    .item-table td {
        border-radius: 15px;
        padding: 10px;
        text-align: center;
    }

    .item-table th {
        background-color: #331D2C;
        color: white;
    }

    .item-table tr:nth-child(odd) {
        background-color: #dddddd;
    }

    .item-table tr:nth-child(even) {
        background-color: #f2f2f2;
    }

    .item-table tr:last-child {
        background-color: #FFA07A;
    }

    .center-cell {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100%;
    }

    .item-actions {
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .item-actions button {
        padding: 5px 10px;
        cursor: pointer;
        margin: 5px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
        border-radius: 15px;
    }

    .create-item {
        margin: 20px 0 50px;
        background-color: #FD8D14;
        color: black;
        border: 2px solid #331D2C;
        border-radius: 15px;
        padding: 10px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
    }

    .last-login {
        font-family: 'Treasure Map', serif;
        font-size: 16px;
    }
</style>
```

Saya juga menambahkan navbar dan beberapa button dengan **Bootstrap**. 
```html
<nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="d-flex justify-content-between w-100">
        <div class="nav-links">
            <span class="nav-link">Logged in as: <strong>{{ name }}</strong> - <strong>{{ class }}</strong></span> 
        </div>
        <div class="nav-links ml-auto">
            <span class="nav-link"><a href="{% url 'main:logout' %}">Logout</a></span>
        </div>
    </div>
</nav>

<div class="container">
    <div class="header">
        <h1>Harta Karun</h1>
    </div>

    <div class="quote-container">
        <p class="quote">"Kekayaan adalah harta yang paling berharga"</p>
    </div>

    <p class="special-paragraph">Kamu menyimpan <strong>{{ total }}</strong> item pada aplikasi ini</p>

    <table class="item-table">
        <thead>
            <tr>
                <th>Name</th>
                <th>Amount</th>
                <th>Description</th>
                <th>Edit/Delete</th>
            </tr>
        </thead>
        <tbody>
            {% for item in items %}
            <tr>
                <td>{{ item.name }}</td>
                <td class="center-cell item-actions">
                    <form method="POST" action="{% url 'main:update_item_amount' %}">
                        {% csrf_token %}
                        <input type="hidden" name="item_id" value="{{ item.id }}">
                        <div class="input-group">
                            <div class="input-group-prepend">
                                <button class="btn btn-outline-secondary" type="submit" name="amount" value="reduce">-</button>
                            </div>
                            <input type="text" class="form-control text-center" value="{{ item.amount }}" readonly>
                            <div class="input-group-append">
                                <button class="btn btn-outline-secondary" type="submit" name="amount" value="add">+</button>
                            </div>
                        </div>
                    </form>
                </td>
                <td>{{ item.description }}</td>
                <td class="center-cell item-actions">
                    <div class="btn-group">
                        <a href="{% url 'main:edit_item' item.pk %}" class="btn btn-primary">
                            ✎ Edit
                        </a>                        
                        <form method="POST" action="{% url 'main:delete_item' %}" class="d-inline">
                            {% csrf_token %}
                            <input type="hidden" name="item_id" value="{{ item.id }}">
                            <button type="submit" class="btn btn-danger">
                                🗑️ Delete
                            </button>
                        </form>
                    </div>
                </td>
            </tr>
            {% endfor %}
        </tbody>
    </table>

    <br />

    <a href="{% url 'main:create_item' %}">
        <button class="btn btn-primary create-item">Add New Item</button>
    </a>

    <h5 class="last-login">Sesi terakhir login: {{ last_login }}</h5>
</div>
```

Sebelumnya, untuk menggunakan **Bootstrap** saya mengikuti tutorial 4 dengan memasukan:
```html
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
        <script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha384-KyZXEAg3QhqLMpG8r+J4jsl5c9zdLKaUk5Ae5f5b1bw6AUn5f5v8FZJoMxm6f5cH1" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js" integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r" crossorigin="anonymous"></script>
```

Kemudian untuk kustomisasi html lain saya berpatokan pada style yang digunakan pada `main.html` saja. Namun, selain itu saya juga menambahkan fungsi `edit_item` seperti yang terdapat pada tutorial 4:
```python
def edit_item(request, id):
    # Get product berdasarkan ID
    product = Item.objects.get(pk = id)

    # Set product sebagai instance dari form
    form = ItemForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_item.html", context)
```

dan tidak lupa menambahkan path pada `urls.py`:
```python
path('edit_item//<int:id>', edit_item, name='edit_item'),
```

### ----------------------------------------------------------------------------------------------------------------

# TUGAS 6

### 1. Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
a. **Synchronous Programming (Pemrograman Sinkron):**
   - Dalam pemrograman sinkron, kode dijalankan langkah demi langkah, satu tugas harus selesai sebelum tugas berikutnya dimulai.
   - Proses eksekusi program berjalan secara linear, di mana setiap perintah dieksekusi satu per satu dalam urutan yang ditentukan.
   - Ini adalah pendekatan yang mudah dipahami dan didebug, karena alur eksekusi program dapat diprediksi dengan jelas.

   **Kelebihan:**
   - Alur eksekusi linear membuat pemrograman sinkron mudah dipahami.
   - Berguna untuk tugas-tugas sederhana dan tidak memerlukan perubahan konteks.

   **Kekurangan:**
   - Tidak efisien untuk tugas yang memerlukan waktu lama, seperti I/O berkepanjangan atau permintaan jaringan, karena program harus menunggu tugas tersebut selesai sebelum melanjutkan pekerjaan berikutnya.

b. **Asynchronous Programming (Pemrograman Asinkron):**
   - Dalam pemrograman asinkron, beberapa tugas dapat dimulai dan dijalankan secara bersamaan tanpa harus menunggu tugas sebelumnya selesai.
   - Proses eksekusi program tidak selalu berjalan dalam urutan yang sama. Tugas dapat dimulai, dihentikan, dan dilanjutkan nanti, bahkan dalam urutan yang berbeda.

   **Kelebihan:**
   - Lebih efisien untuk tugas yang memerlukan waktu lama atau tugas yang membutuhkan waktu tunggu, seperti operasi I/O atau permintaan jaringan, karena program bisa melanjutkan pekerjaan lain sambil menunggu tugas asinkron selesai.
   - Meningkatkan responsivitas aplikasi, terutama dalam kasus aplikasi berbasis jaringan atau server.

   **Kekurangan:**
   - Lebih kompleks untuk dipahami dan didebug, karena tugas-tugas asinkron berjalan dalam urutan yang tidak selalu terlihat atau dapat diprediksi.
   - Memerlukan manajemen perubahan konteks (context switching), yang dapat menambah kompleksitas kode.

Dalam praktiknya, pemrograman asynchronous sangat berguna untuk mengoptimalkan kinerja aplikasi yang memerlukan penanganan banyak operasi I/O atau jaringan bersamaan. Pemrograman synchronous lebih cocok untuk tugas-tugas sederhana di mana alur eksekusi linier cukup efisien. Penggunaan yang tepat tergantung pada jenis tugas yang perlu ditangani dalam aplikasi kita.

### 2. Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma event-driven programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
**Paradigma Event-Driven Programming** adalah suatu model pemrograman di mana program merespons peristiwa (events) yang terjadi secara asinkron. Program dalam paradigma ini biasanya terdiri dari berbagai komponen atau fungsi yang akan dieksekusi ketika peristiwa tertentu terjadi. Peristiwa ini dapat berasal dari berbagai sumber, seperti interaksi pengguna, input dari perangkat, atau bahkan peristiwa internal dalam program.

Beberapa karakteristik utama paradigma event-driven programming adalah:
- **Asynchronous**: Program dapat menjalankan tugas tanpa harus menunggu tugas sebelumnya selesai. Program akan merespons peristiwa saat peristiwa tersebut terjadi.
- **Terpusat pada Peristiwa**: Program berbasis event-driven fokus pada peristiwa atau tindakan yang terjadi. Ketika peristiwa ini terjadi, program akan menjalankan tindakan yang sesuai.
- **Callback Functions**: Program umumnya menggunakan callback functions untuk menentukan tindakan yang harus diambil ketika peristiwa terjadi.

Contoh Penerapan dalam tugas saya adalah penggunaan event handler untuk merespons klik pada tombol "Add Item by AJAX."

```javascript
document.getElementById("button_add").onclick = addItem;
```

Dalam contoh ini, `document.getElementById("button_add").onclick` adalah bagian dari event-driven programming. Ini mengatakan bahwa ketika tombol dengan ID "button_add" diklik, maka fungsi `addItem` akan dieksekusi. Dengan kata lain, program merespons peristiwa "klik" pada tombol dengan menjalankan fungsi yang ditentukan (yaitu, `addItem`).

### 3. Jelaskan penerapan asynchronous programming pada AJAX.
Penerapan **asynchronous programming pada AJAX** adalah prinsip dasar dalam penggunaan teknologi AJAX (Asynchronous JavaScript and XML). AJAX memungkinkan komunikasi antara browser dan server tanpa harus mereload seluruh halaman web. Ini dilakukan dengan cara mengirim permintaan HTTP secara asinkron (tanpa perlu menunggu) dan menerima respons dari server saat respons tersebut siap. Beberapa konsep utama penerapan asynchronous programming pada AJAX meliputi:

a. **Permintaan Asynchronous**: Ketika kita menggunakan AJAX, kita membuat permintaan HTTP (seperti permintaan GET atau POST) ke server tanpa menghentikan eksekusi program JavaScript kita. Program JavaScript kita terus berjalan sambil menunggu respons dari server.

b. **Callback Functions**: Kita mendefinisikan callback functions untuk menangani respons dari server. Ini adalah bagian kunci dari asynchronous programming di AJAX. Ketika respons diterima, callback function yang sesuai akan dipanggil untuk menangani data respons.

c. **Event Handling**: AJAX juga sering menggunakan event handling untuk merespons perubahan status permintaan, seperti ketika permintaan telah berhasil diselesaikan atau ketika terjadi kesalahan. kita dapat menentukan event listener untuk menangani peristiwa ini.

Contoh konkret penerapan asynchronous programming dalam AJAX adalah ketika kita menggunakan metode `fetch` untuk mengambil data dari server dan menangani responsnya dengan menggunakan `.then()` untuk menentukan apa yang harus dilakukan ketika data respons tiba.

### 4. Pada PBP kali ini, penerapan AJAX dilakukan dengan menggunakan Fetch API daripada library jQuery. Bandingkanlah kedua teknologi tersebut dan tuliskan pendapat kamu teknologi manakah yang lebih baik untuk digunakan.
**Fetch API** dan **jQuery** adalah dua teknologi yang dapat digunakan untuk mengimplementasikan AJAX dalam pengembangan web. Berikut perbandingan antara keduanya dan pendapat saya tentang mana yang lebih baik:

**Fetch API:**
- **Ringan**: Fetch API adalah API bawaan dalam JavaScript modern, sehingga tidak memerlukan perpustakaan eksternal. Ini membuatnya lebih ringan dan lebih efisien daripada jQuery.
- **Promise-Based**: Fetch API menggunakan promise, yang membuatnya sangat baik dalam mengelola asynchronous programming. Ini membuat kode kita lebih mudah dibaca dan dipahami.
- **Mendukung JSON secara Bawaan**: Fetch API secara bawaan mendukung parsing JSON dan tidak memerlukan konfigurasi tambahan.

**jQuery:**
- **Lintas Browser**: jQuery adalah perpustakaan JavaScript yang dikembangkan untuk mengatasi perbedaan antara browser-browsers yang berbeda. Ini memberikan fleksibilitas dalam mengembangkan aplikasi web yang kompatibel dengan berbagai browser.
- **Abstraksi yang Kuat**: jQuery menyediakan abstraksi yang kuat untuk berbagai tugas, termasuk AJAX, yang dapat menghemat waktu dan usaha dalam pengembangan.
- **Plugin dan Ekosistem**: jQuery memiliki ekosistem plugin yang luas, yang dapat mempercepat pengembangan aplikasi tertentu.

Oleh karena itu, menurut saya pilihan antara **Fetch API** dan **jQuery** tergantung pada kebutuhan proyek dan preferensi kita. **Fetch API** adalah pilihan yang lebih modern dan lebih ringan untuk proyek-proyek baru, terutama jika kita ingin memanfaatkan fitur promise dan kita tidak perlu mendukung browser-browsers kuno. Sementara itu, **jQuery** tetap relevan dalam konteks proyek yang ada atau proyek yang perlu mendukung sejumlah besar browser lama. Jika kita sudah terbiasa dengan jQuery atau proyek kita sangat bergantung pada plugin-plugin jQuery yang ada, maka jQuery tetap merupakan pilihan yang cocok.

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Saya mengubah tabel saya agar mengimplementasikan cards. Lalu, untuk mengambil item saya menggunakan AJAX GET. Berikut kode yang saya modifikasi: <table id="item_table"></table> -> <div id="item_cards"></div>

Saya juga menambahkan script pada main.html untuk menerapkan AJAX GET, untuk mengambil dan mengirim data ke server tanpa perlu memuat ulang satu halaman penuh seperti ini:
```html
<script>
    async function getItems() {
        return fetch("{% url 'main:get_item_json' %}").then((res) => res.json());
    }

    async function refreshItems() {
        document.getElementById("item_cards").innerHTML = ""; 
        const products = await getItems();

        products.forEach((item) => {
            const editUrl = "{% url 'main:edit_item' 999999 %}".replace('999999', item.pk);
            const deleteUrl = "{% url 'main:delete_item' 999999 %}".replace('999999', item.pk);
            const increaseUrl = `{% url 'main:increase_amount' 999999 %}`.replace('999999', item.pk);
            const decreaseUrl = `{% url 'main:decrease_amount' 999999 %}`.replace('999999', item.pk);

            const newCard = `
            <div class="card">
                <div class="card-body">
                    <h5 class="card-title">${item.fields.name}</h5>
                    <a href="${increaseUrl}" class="btn btn-sm btn-increase">[+]</a>
                    <p class="card-text amount-display">${item.fields.amount} ${item.fields.description}</p>
                    <a href="${decreaseUrl}" class="btn btn-sm btn-increase">[-]</a>
                    <br>
                    <br>
                    <a href="${editUrl}" class="btn btn-sm btn-edit">✎</a>
                    <a href="${deleteUrl}" class="btn btn-sm btn-delete">🗑️</a>
                </div>
            </div>`;

            document.getElementById("item_cards").insertAdjacentHTML('beforeend', newCard);
        });
    }

    refreshItems();

    function addItem() {
        fetch("{% url 'main:add_item_ajax' %}", {
            method: "POST",
            body: new FormData(document.querySelector('#form'))
        })
        .then(refreshItems)
        .catch(error => {
            console.error(error);
        });

        document.getElementById("form").reset();
        return false;
    }

    document.getElementById("button_add").onclick = addItem;
</script>
```

Tidak lupa saya menambahkan path ke urls.py di main seperti ini:
```python
path('get-item/', get_item_json, name='get_item_json'),
path('create-item-ajax/', add_item_ajax, name='add_item_ajax')
```

Implementasi AJAX Post saya terapkan untuk menambahkan item. pada views.py saya menambahkan fungsi ini:
```python
def get_item_json(request):
    product_item = Item.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', product_item))

@csrf_exempt
def add_item_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        description = request.POST.get("description")
        user = request.user

        new_item = Item(name=name, amount=amount, description=description, user=user)
        new_item.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()
```

Pengimplementasian AJAX Post ini mengirimkan POST request ke server dengan data dari addItemForm untuk menambahkan item baru. Respons server kemudian digunakan untuk menambahkan kartu baru untuk item tersebut ke halaman.

Semua implementasi fungsi-fungsi get dan post di atas menggunakan AJAX untuk berkomunikasi dengan server agar memungkinkan pengalaman pengguna yang dinamis dan lancar tanpa perlu memuat ulang halaman penuh.

Penerapan collectstatic saya lakukan dengan mengubah settings.py agar memuat kode berikut:
```python
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```
Lalu, saya menjalankan python manage.py collectstatic pada terminal. STATIC_URL digunakan untuk menentukan bagaimana URL untuk file statis dibuat di template. STATIC_ROOT digunakan untuk menentukan di mana semua file statis dikumpulkan ketika menjalankan perintah collectstatic.