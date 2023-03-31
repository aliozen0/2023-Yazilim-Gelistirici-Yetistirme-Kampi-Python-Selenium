### 5. Gun Odev 1

Pytest'de dekoratörler, test fonksiyonlarını veya metotlarını belirli özelliklerle etiketleyerek, test süreçlerini yönetmenize ve özelleştirmenize olanak sağlayan işlevlerdir. BUnlar bazıları şunlardır;

@pytest.fixture: Bu dekoratör, test fonksiyonları tarafından kullanılabilen ve parametrelerle birlikte kullanılabilen bir işlevi işaretlemek için kullanılır. Bu dekoratör ile işaretlenen işlev, test öncesi veya sonrası hazırlık veya temizlik görevleri gibi tekrar eden görevler için kullanılabilir.

@pytest.mark.parametrize: Bu dekoratör, aynı test senaryosunu farklı girdilerle tekrarlayarak testlerin daha geniş bir yelpazede gerçekleştirilmesini sağlar. Bu dekoratör ile birlikte kullanılan parametreler, test fonksiyonunun birden fazla kez çağrılması için kullanılır.

@pytest.mark.skip: Bu dekoratör, belirli bir test işlevinin atlanması gerektiğinde kullanılır. Test fonksiyonunu işaretlemek için bu dekoratörü kullanarak, belirli bir testin geçici olarak atlanmasına izin veririz.

@pytest.mark.xfail: Bu dekoratör, belirli bir test işlevinin geçici olarak başarısız olmasına izin verir. Test fonksiyonunu işaretlemek için bu dekoratörü kullanarak, belirli bir testin bilinen bir sorunu olduğunda başarısız olmasına izin veririz.

@pytest.mark.timeout: Bu dekoratör, belirli bir testin maksimum çalışma süresini belirlemek için kullanılır. Test fonksiyonunu işaretlemek için bu dekoratörü kullanarak, belirli bir testin belirli bir süre içinde tamamlanması gerektiğini belirtebiliriz
