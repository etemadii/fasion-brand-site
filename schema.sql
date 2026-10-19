-- جداول دیتابیس Cloudflare D1 (SQLite در لبه شبکه کلادفلر)

CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL,
  name TEXT NOT NULL,
  role TEXT DEFAULT 'admin'
);

CREATE TABLE IF NOT EXISTS settings (
  key TEXT PRIMARY KEY,
  value TEXT NOT NULL,
  category TEXT DEFAULT 'general',
  label TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS categories (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  slug TEXT UNIQUE NOT NULL,
  label TEXT NOT NULL,
  sort_order INTEGER DEFAULT 0
);

CREATE TABLE IF NOT EXISTS products (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  code TEXT UNIQUE NOT NULL,
  name TEXT NOT NULL,
  category_slug TEXT NOT NULL,
  cat_label TEXT NOT NULL,
  price INTEGER NOT NULL,
  tag TEXT DEFAULT '',
  image TEXT NOT NULL,
  colors_json TEXT NOT NULL,
  sizes_json TEXT NOT NULL,
  in_stock INTEGER DEFAULT 1
);

CREATE TABLE IF NOT EXISTS sections (
  section TEXT PRIMARY KEY,
  title TEXT NOT NULL,
  subtitle TEXT DEFAULT '',
  body_json TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS page_layouts (
  slug TEXT PRIMARY KEY,
  html TEXT DEFAULT '',
  css TEXT DEFAULT ''
);

-- کاربر ادمین پیش‌فرض (admin / admin123)
INSERT OR IGNORE INTO users (username, password, name, role)
VALUES ('admin', 'admin123', 'مدیر ارشد آوین', 'admin');

-- تنظیمات اولیه برند
INSERT OR IGNORE INTO settings (key, value, category, label) VALUES
('brand_name', 'آوین', 'brand', 'نام برند'),
('brand_latin', 'AVIN STUDIO', 'brand', 'نام لاتین برند'),
('brand_tagline', 'پوشاک زنانه با برشِ آرام', 'brand', 'شعار برند'),
('demo_mode', 'false', 'general', 'نمایش نوار آزمایشی'),
('whatsapp_number', '989121234567', 'contact', 'شماره واتساپ (با کد 98 بدون +)'),
('whatsapp_display', '۰۹۱۲ ۱۲۳ ۴۵۶۷', 'contact', 'نمایش شماره واتساپ'),
('whatsapp_greeting', 'سلام، از سایت آوین پیام می‌دهم.', 'contact', 'پیام آغازین واتساپ'),
('contact_phone', '+98 21 0000 0000', 'contact', 'تلفن تماس'),
('contact_phone_url', 'tel:+98210000000', 'contact', 'لینک تلفن'),
('contact_email', 'hello@example.com', 'contact', 'ایمیل'),
('contact_email_url', 'mailto:hello@example.com', 'contact', 'لینک ایمیل'),
('contact_address', 'تهران، خیابان نمونه، پلاک ۰۰', 'contact', 'آدرس'),
('social_instagram', 'https://instagram.com/avin.studio', 'social', 'لینک اینستاگرام'),
('social_instagram_handle', '@avin.studio', 'social', 'آیدی اینستاگرام'),
('currency', 'تومان', 'general', 'واحد پول');

-- دسته‌بندی‌ها
INSERT OR IGNORE INTO categories (slug, label, sort_order) VALUES
('dress', 'پیراهن', 1),
('manto', 'مانتو', 2),
('shirt', 'شومیز', 3),
('skirt', 'دامن', 4),
('pants', 'شلوار', 5),
('accessory', 'اکسسوری', 6);

-- ۹ محصول اولیه کاتالوگ آوین
INSERT OR IGNORE INTO products (code, name, category_slug, cat_label, price, tag, image, colors_json, sizes_json, in_stock) VALUES
('AV-101', 'پیراهن ابریشمی «نیلا»', 'dress', 'پیراهن', 2850000, 'جدید', 'https://images.unsplash.com/photo-1595777457583-95e059d581b8?auto=format&fit=crop&w=700&h=930&q=75', '[{"name":"زرشکی","hex":"#6E1D2B"},{"name":"کرم","hex":"#E4D6C0"}]', '["S","M","L"]', 1),
('AV-102', 'مانتو لینن «سایه»', 'manto', 'مانتو', 3450000, '', 'https://images.unsplash.com/photo-1591047139829-d91aecb6caea?auto=format&fit=crop&w=700&h=930&q=75', '[{"name":"ذغالی","hex":"#2E2A27"},{"name":"شنی","hex":"#C9B79C"}]', '["S","M","L","XL"]', 1),
('AV-103', 'شومیز ابریشم «ماهور»', 'shirt', 'شومیز', 1980000, '', 'https://images.unsplash.com/photo-1594633312681-425c7b97ccd1?auto=format&fit=crop&w=700&h=930&q=75', '[{"name":"شیری","hex":"#F1E9DC"},{"name":"زرشکی","hex":"#6E1D2B"}]', '["S","M","L"]', 1),
('AV-104', 'دامن پلیسه «آرام»', 'skirt', 'دامن', 2150000, 'کالکشن پاییز', 'https://images.unsplash.com/photo-1583496661160-fb5886a0aaaa?auto=format&fit=crop&w=700&h=930&q=75', '[{"name":"زرشکی","hex":"#6E1D2B"},{"name":"مشکی","hex":"#1F1B19"}]', '["S","M","L"]', 1),
('AV-105', 'شلوار پارچه‌ای «نیوشا»', 'pants', 'شلوار', 1750000, '', 'https://images.unsplash.com/photo-1541099649105-f69ad21f3246?auto=format&fit=crop&w=700&h=930&q=75', '[{"name":"ذغالی","hex":"#2E2A27"},{"name":"کرم","hex":"#E4D6C0"}]', '["36","38","40","42"]', 1),
('AV-106', 'شال پشمی «باد»', 'accessory', 'اکسسوری', 890000, '', 'https://images.unsplash.com/photo-1601924994987-69e26d50dc26?auto=format&fit=crop&w=700&h=930&q=75', '[{"name":"کرم","hex":"#E4D6C0"},{"name":"زرشکی","hex":"#6E1D2B"}]', '["یک سایز"]', 1),
('AV-107', 'پیراهن کتان «نارین»', 'dress', 'پیراهن', 2400000, '', 'https://images.unsplash.com/photo-1496747611176-843222e1e57c?auto=format&fit=crop&w=700&h=930&q=75', '[{"name":"شنی","hex":"#C9B79C"},{"name":"سفید","hex":"#F4EFE6"}]', '["S","M","L"]', 1),
('AV-108', 'مانتو کتان «هستی»', 'manto', 'مانتو', 3100000, 'جدید', 'https://images.unsplash.com/photo-1487222477894-8943e31ef7b2?auto=format&fit=crop&w=700&h=930&q=75', '[{"name":"کرم","hex":"#E4D6C0"},{"name":"زیتونی","hex":"#6B6B4B"}]', '["S","M","L"]', 1),
('AV-109', 'کیف چرم «مینو»', 'accessory', 'اکسسوری', 2600000, '', 'https://images.unsplash.com/photo-1554568218-0f1715e72254?auto=format&fit=crop&w=700&h=930&q=75', '[{"name":"زرشکی","hex":"#6E1D2B"},{"name":"ذغالی","hex":"#2E2A27"}]', '["یک سایز"]', 1);
