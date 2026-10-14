import random
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)


# 1. คลาสต้นแบบข้อมูลเมนูชาบู
class ShabuItem:

    def __init__(
        self,
        item_id: int,
        name: str,
        category: str,
        price: float,
        availability: str,
        stock: int,
        expiry_date: str,
        calories: int,
        rating: float,
        preparation_time: int,
    ):
        self.item_id = item_id
        self.name = name
        self.category = category
        self.price = price
        self.availability = availability
        self.stock = stock
        self.expiry_date = expiry_date
        self.calories = calories
        self.rating = rating
        self.preparation_time = preparation_time

    def to_dict(self):
        return {
            "item_id": self.item_id,
            "name": self.name,
            "category": self.category,
            "price": self.price,
            "availability": self.availability,
            "stock": self.stock,
            "expiry_date": self.expiry_date,
            "calories": self.calories,
            "rating": self.rating,
            "preparation_time": self.preparation_time,
        }


# ชื่อฟิลด์สำหรับจับคู่กับการเรียงลำดับ
FIELDS = {
    "item_id": "item_id",
    "name": "name",
    "category": "category",
    "price": "price",
    "availability": "availability",
    "stock": "stock",
    "expiry_date": "expiry_date",
    "calories": "calories",
    "rating": "rating",
    "preparation_time": "preparation_time",
}


# 2. ฟังก์ชันสร้างรายการออบเจกต์เมนูชาบู
def generate_shabu_menu():
    shabu_names = [
        ("สันคอหมูสไลซ์", "เนื้อสัตว์"),
        ("สามชั้นหมูสไลซ์", "เนื้อสัตว์"),
        ("เนื้อวากิวพรีเมียม", "เนื้อสัตว์"),
        ("เนื้อริบอาย", "เนื้อสัตว์"),
        ("อกไก่หมักนุ่ม", "เนื้อสัตว์"),
        ("กุ้งแม่น้ำสด", "อาหารทะเล"),
        ("ปลาหมึกกรอบ", "อาหารทะเล"),
        ("หอยแมลงภู่นิวซีแลนด์", "อาหารทะเล"),
        ("ผักกาดขาว", "ผักสด"),
        ("ชุดผักรวมชาบู", "ผักสด"),
        ("เห็ดเข็มทอง", "ผักสด"),
        ("เห็ดออริจิ", "ผักสด"),
        ("ลูกชิ้นชีสลาวา", "ของทอด/ทานเล่น"),
        ("เต้าหู้ปลา", "ของทอด/ทานเล่น"),
        ("สาหร่ายวากาเมะ", "ผักสด"),
        ("เส้นอุด้งญี่ปุ่น", "เส้น/ข้าว"),
        ("เส้นบะหมี่หยก", "เส้น/ข้าว"),
        ("เกี๊ยวซ่าทอด", "ของทอด/ทานเล่น"),
        ("ไก่ทอดซอสเกาหลี", "ของทอด/ทานเล่น"),
        ("ชีสสไลซ์ยืด", "ท็อปปิ้ง"),
    ]

    dates = [
        "2026-10-18",
        "2026-10-20",
        "2026-10-22",
        "2026-10-25",
        "2026-11-01",
    ]

    items = []
    for i, (name, cat) in enumerate(shabu_names):
        stock_qty = random.randint(0, 45)
        status = "พร้อมขาย" if stock_qty > 0 else "หมด"

        item = ShabuItem(
            item_id=201 + i,
            name=name,
            category=cat,
            price=float(random.choice([29, 39, 49, 59, 89, 129, 199])),
            availability=status,
            stock=stock_qty,
            expiry_date=random.choice(dates),
            calories=random.randint(40, 480),
            rating=round(random.uniform(3.5, 5.0), 1),
            preparation_time=random.randint(2, 15),
        )
        items.append(item)
    return items


# 3. อัลกอริทึม Merge Sort (โค้ดเดิมของคุณ)
def merge_sort(items, key, reverse=False):
    if len(items) <= 1:
        return items[:]

    mid = len(items) // 2
    left = merge_sort(items[:mid], key, reverse)
    right = merge_sort(items[mid:], key, reverse)
    return _merge(left, right, key, reverse)


def _merge(left, right, key, reverse):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        a, b = key(left[i]), key(right[j])
        take_left = (a >= b) if reverse else (a <= b)
        if take_left:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def sort_shabu(items, attr, reverse=False):
    def key(p):
        v = getattr(p, attr)
        return v.lower() if isinstance(v, str) else v

    return merge_sort(items, key, reverse)


# สร้างข้อมูลจำลองเริ่มต้น
global_items = generate_shabu_menu()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/menu", methods=["GET"])
def get_menu():
    sort_by = request.args.get("sort", "item_id")
    order = request.args.get("order", "asc")
    reverse = True if order == "desc" else False

    attr = FIELDS.get(sort_by, "item_id")
    sorted_items = sort_shabu(global_items, attr, reverse)

    return jsonify([item.to_dict() for item in sorted_items])


if __name__ == "__main__":
    app.run(debug=True)