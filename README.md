# نرخینو | Nerkhino

یک وب‌سایت ساده برای نمایش قیمت لحظه‌ای ارزها و اطلاعات بازارهای مالی.

این پروژه با استفاده از Django توسعه داده شده و قیمت‌ها را از APIهای مختلف دریافت می‌کند.

---

## ✨ امکانات

- نمایش قیمت ارزها
- نمایش قیمت فعلی
- نمایش بهترین قیمت خرید
- نمایش بهترین قیمت فروش
- نمایش تغییرات ۲۴ ساعت
- نمایش کمترین و بیشترین قیمت روز
- نمایش قیمت شروع روز
- صفحه اختصاصی برای هر ارز
- دریافت اطلاعات از چند منبع مختلف
- طراحی واکنش‌گرا (Responsive)

---

## 🛠️ تکنولوژی‌ها

- Python
- Django
- Requests
- HTML
- CSS
- Django Template Tags

---

## 🔌 منابع داده

در حال حاضر اطلاعات قیمت‌ها از APIهای زیر دریافت می‌شوند:

- Nobitex
- TGJU

---

## 📁 ساختار پروژه

```text
Price/
├── manage.py
├── requirements.txt
├── .gitignore
├── README.md
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
└── Price/
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── views.py
    ├── services.py
    ├── urls.py
    │
    ├── migrations/
    │
    ├── templates/
    │   └── Price/
    │       ├── price.html
    │       └── price_detail.html
    │
    ├── static/
    │   └── css/
    │       ├── style.css
    │       └── style1.css
    │
    └── templatetags/
        ├── __init__.py
        └── price_filters.py
