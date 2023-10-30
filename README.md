# گزارش آزمایش اول درس مهندسی نرم افزار
## اعضای گروه:
+ سید محمدمهدی حاتمی 98109561
+ پیمان حاجی محمد 98170776
## شرح آزمایش
در ابتدا ما یک مخزن عمومی گیت ایجاد کردیم و فایل های readme و gitignore را برای فایل های پایتونی و نرم افزار pycharm اضافه کردیم.
![Screenshot 2023-10-28 044349](https://github.com/peyman79/SE-Lab1/assets/61017890/c36c4079-a10a-4a4c-a98f-0cfedaa33b92)

سپس برای برنچ main سیاست عدم امکان مرج برنچی دیگر بدون ایجاد pull request را به آن اضافه کردیم
![Screenshot 2023-10-28 044707](https://github.com/peyman79/SE-Lab1/assets/61017890/4dd4b535-239c-423d-a902-b754b50d2ec1)
![Screenshot 2023-10-28 045658](https://github.com/peyman79/SE-Lab1/assets/61017890/2a72bbdc-ece2-4e00-85e9-8b99b4560ff3)

در ادامه شروع به پیاده سازی پروژه انتخاب واحد دانشجویی پرداختیم. بدین صورت که ما یک برنچ develop ایجاد کردیم که برنچ های فیچر ما از آن برنچ منبع گرفته و در نهایت در همان برنچ ادغام می شوند. همچنین در هر بار انتشار پروژه، ابتدا برنچ develop را با برنچ main مرج کرده سپس نسخه را برای انتشار آماده می کنیم. یک نمونه از برنچ های فیچر که pull request آن زده شده و منتظر تایید برای ادغام شدن با برنچ develop می باشد را در تصویر زیر مشاهده می نمایید:
![Screenshot 2023-10-28 115520](https://github.com/peyman79/SE-Lab1/assets/61017890/6b98ceff-198c-4d6b-9c41-fa1f3c04c61c)
![Screenshot 2023-10-28 115557](https://github.com/peyman79/SE-Lab1/assets/61017890/5f8ed96c-a7b7-4a52-b1fb-1f363547c135)
![Screenshot 2023-10-28 115615](https://github.com/peyman79/SE-Lab1/assets/61017890/f7968963-06c8-44e8-b330-3fe9eda3cc6d)

در ادامه کار در هنگام مرج کردن برنچ ها، به دو کانفیلکت در یکی از فایل ها برخوردیم. 
![Screenshot 2023-10-30 111353](https://github.com/peyman79/SE-Lab1/assets/61017890/7f69508b-91a4-4a99-a1cb-a942197f943d)
دو کانفیلکت و resolve شده آنها را در دو تصویر زیر می توانید مشاهده کنید:
![Screenshot 2023-10-30 111420](https://github.com/peyman79/SE-Lab1/assets/61017890/a37dabab-b4e2-4e1b-9145-a19957fc9820)

![Screenshot 2023-10-30 111737](https://github.com/peyman79/SE-Lab1/assets/61017890/e1478128-fbf5-47ce-b262-fd0235601874)

![Screenshot 2023-10-30 111605](https://github.com/peyman79/SE-Lab1/assets/61017890/d6b66ba2-4a49-46cd-a17c-9d22967203fb)

حال دکمه commit merge را می زنیم تا تغییرات انجام شده به صورت یک کامیت برای مرج، ثبت شود:
![Screenshot 2023-10-30 111859](https://github.com/peyman79/SE-Lab1/assets/61017890/23002124-056d-40b0-b9e0-d737b1633452)
حال دکمه مرج برای pull request فعال شده و میتوان آن را مرج کرد:
![Screenshot 2023-10-30 111925](https://github.com/peyman79/SE-Lab1/assets/61017890/5ed9409c-08a3-41f4-bc28-2838225515d4)

## پرسش ها
1. پوشه git یک پوشه hidden بوده که حاوی اطلاعاتی از جمله تاریخچه کامیت ها، برنچ ها، کانفیگ ها (مانند اطلاعات ایمیل و اکانت متصل به مخزن گیت) و... می باشد. این پوشه با دستور git init در ترمینال git bash ساخته می شود.
1. در این دو مفهوم، اتمیک بودن بدین معناست که تغییرات موجود در یک کامیت یا برنچ مشخص بایستی مرتبط با یک هدف خاص باشد. بعنوان مثال یک کامیتی که شامل رفع چندین باگ و افزودن فیچر باشد نمی تواند یک کامیت اتمیک باشد. به صورت معادل یک برنچ که شامل افزودن چندین ویژگی غیر مرتبط به هم در خود میشود نمیتواند برنچ اتمیک شناخته شود
1. دستور fetch اطلاعات و تغییرات جدید از یک ریپازیتوری را دریافت می‌کند، اما تغییرات را در شاخه‌های کاری محلی اعمال نمی‌کند. دستور merge برای ادغام تغییرات از یک شاخه به شاخه دیگر استفاده می‌شود. دستور pull ترکیبی از دستورهای fetch و merge است. ابتدا تغییرات جدید را از ریپازیتوری اصلی با استفاده از fetch دریافت می‌کند و سپس تغییرات را با شاخه کاری محلی merge می‌کند.دستور rebase برای اعمال تغییرات از یک شاخه به شاخه دیگر استفاده می‌شود، اما به جای ادغام تغییرات، تغییرات را به شاخه مقصد اعمال می‌کند. با استفاده از rebase، تاریخچه commit ها در شاخه مقصد تغییر می‌کند و تغییرات جدید به صورت مستقیم بر روی شاخه مقصد اعمال می‌شوند. دستور cherry-pick برای انتخاب و اعمال یک commit خاص از یک شاخه به شاخه دیگر استفاده می‌شود. با استفاده از این دستور، می‌توان یک commit خاص را از یک شاخه را انتخاب کرده و بدون اعمال سایر تغییرات شاخه اصلی، آن را در شاخه مقصد اعمال کرد. در زیر نمونه تصویری این دستورات قابل مشاهده اند:
![image](https://github.com/peyman79/SE-Lab1/assets/61017890/289fea74-89c7-4d7d-96f4-96f4bf80ff8c)
![image](https://github.com/peyman79/SE-Lab1/assets/61017890/db0408b9-af1d-4acd-a011-e9a05e3d389d)
![image](https://github.com/peyman79/SE-Lab1/assets/61017890/2eb14c86-6296-40c6-a721-d625553384c5)


