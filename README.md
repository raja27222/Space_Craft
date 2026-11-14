# SPACE CRAFT — Luxury Event Solutions & Equipment Rental (Saudi Arabia)

A complete, premium, bilingual (English & Arabic), fully responsive and functional multi-page luxury website for **SPACE CRAFT**, operating in Saudi Arabia.

---

## 🌟 Quick Start — How to Run

The website is **already running live** right now! You can view it immediately by opening your browser at:
👉 **[http://localhost:3000](http://localhost:3000)**

### To start it anytime in the future:

#### Option 1: Double-Click
Double-click `run.bat` (production server) or `dev.bat` (development server with hot reload).

#### Option 2: Terminal Commands
```bash
# 1. Run production build (fastest, optimized):
npm start

# OR 2. Run in development mode:
npm run dev
```
Open **[http://localhost:3000](http://localhost:3000)** in your browser.

---

## 👑 Brand & Market Specifications

- **Brand**: SPACE CRAFT
- **Market**: Saudi Arabia (KSA)
- **Primary Phone**: `+966 58 139 1995`
- **Secondary Phone**: `+966 57 177 9065`
- **Email**: `asimmazoor033@gmail.com`
- **WhatsApp**: Floating button + contextual inquiry buttons prefilled with product references.
- **Colour Palette**:
  - Warm Ivory: `#F6F3ED`
  - Champagne Gold: `#C6A46A`
  - Deep Charcoal: `#20201E`
  - Soft Beige: `#E8E0D4`
  - Pure White: `#FFFFFF`
  - Muted Bronze: `#92744F`

---

## 📚 Real Product Photos & 56-Page PDF Catalogue

All product photographs were extracted directly from the uploaded **56-page Space Craft Cataloge.pdf**:
- **152 authentic product photos** extracted into `/public/images/products/`
- **56 high-resolution catalog presentation slides** rendered into `/public/images/catalog_pages/`
- Users can click the **slide icon** on any product card or detail page to inspect the actual catalog slide!
- Preserved confirmed dimensions and quantities (e.g. 500 VIP Bentley Chairs, 1,500 Fabric Cover Chairs, 1,000 Dinner Chairs, verified dimensions `H=90 W=65 SIDE=67`, `W=72 H=93`, `W=55 H=93`, `W=50 H=96`, etc.) without fabricating missing details.

---

## 🏛️ Website Architecture & Key Pages

| Page | URL | Description |
|---|---|---|
| **Home** | `/` | Cinematic full-screen hero, brand story, categories, featured catalogue pieces, 8 services, 5 pillars why choose us, portfolio showcase, final CTA. |
| **About Us** | `/about` | "Creating Spaces. Elevating Experiences.", Vision, Mission, Story, Equipment fleet & commitment to quality. |
| **Services** | `/services` | 8 detailed service sections with related catalogue equipment + clearly marked proposed capabilities. |
| **Catalogue** | `/catalogue` | Complete 56-page digital catalogue with category filters, verified stock toggle, search, sorting, slide modal. |
| **Category Pages** | `/catalogue/[category]` | Direct URLs: `vip-furniture`, `chairs`, `sofas`, `tables`, `outdoor`, `wedding-curtains`, `climate-equipment`, `infrastructure`. |
| **Product Detail** | `/product/[slug]` | Image gallery, confirmed specs, event application tags, quantity selector, Add to Quote, WhatsApp enquiry. |
| **Projects** | `/projects` | Luxury masonry portfolio gallery, category tabs, touch swipe lightbox, concept vs verified badges. |
| **Project Detail** | `/projects/[slug]` | Full-width cover, furniture and equipment used, request similar setup. |
| **Contact** | `/contact` | Validated contact form, real backend storage, reference code generator, verified contact info. |
| **Request a Quote** | `/request-quote` | Persistent basket checkout, event details, unique reference generation (`SC-Q-2026-XXXX`), WhatsApp summary export. |
| **Admin Dashboard** | `/admin` | Protected operations console (`passkey: spacecraft2026`) to view and manage quotations, customer contacts, and inventory. |

---

## 🌐 Bilingual Support (English & Arabic RTL)

- One-click switcher in the navigation bar.
- Changes text, typography (`Cormorant Garamond` / `Cairo`), layout direction (`ltr` / `rtl`), alignment, and form elements.
- Selection is preserved across pages and browser sessions in `localStorage`.

---

## 🔐 Admin Dashboard Access

- **URL**: `http://localhost:3000/admin`
- **Default Passkey**: `spacecraft2026` (or `admin`)
- View and update quotation statuses: *Pending*, *Contacted*, *Quoted*, *Completed*.
- Direct one-click WhatsApp client contact buttons.
