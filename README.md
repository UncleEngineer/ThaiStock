# (thaistock) เป็นไลบรารีสำหรับเช็คราคาหุ้นของตลาดหุ้นไทย (SET)

PyPi: https://pypi.org/project/thaistock/

สวัสดีจ้าาา สำหรับไลบรารีนี้ลุงได้เขียนขึ้นมาเพื่ออำนวยความสะดวกในการเช็คราคาหุ้น ใช้เทคนิค web scraping โดยอ้างอิงข้อมูลจากเว็บไซต์ settrade.com ซึ่งความสามารถตอนนี้คือ

- เช็คราคาปัจจุบัน
- เช็คราคาย้อนหลังได้สูงสุด 6 เดือน
- พล็อตกราฟ (ราคาปิด) ย้อนหลังได้
- กราฟแท่งเทียน (จะอัพเดตเพิ่มเติมในเวอร์ชั่นถัดไป)

### วิธีติดตั้ง

เปิด CMD / Terminal

```python
pip install thaistock
```

### วิธีใช้งานแพ็คเพจนี้

- เปิด IDLE/Editor ขึ้นมาแล้วพิมพ์...

```python
from thaistock import SET

#สร้างตัวแปร stock (object)
stock = SET()

#เช็คราคา ณ ปัจจุบัน (ใช้ขณะตลาดเปิดได้)
current = stock.current('TEAMG',show=True,header=True)

#โชว์หัวข้อตารางราคาย้อนหลังเพื่ออ้างอิง index
stock.show_header()

'''
เลือก index ของคอลัมน์ที่ต้องการ
วันที่ [0]
ราคาเปิด [1]
ราคาสูงสุด [2]
ราคาต่ำสุด [3]
ราคาเฉลี่ย [4]
ราคาปิด [5]
เปลี่ยนแปลง [6]
%เปลี่ยนแปลง [7]
ปริมาณ(พันหุ้น) [8]
มูลค่า(ล้านบาท) [9]
SET Index [10]
%เปลี่ยนแปลง [11]

ต้องการแสดงวันที่ ,ราคาปิด, เปลี่ยนแปลง, %เปลี่ยนแปลง
stock.historical('CODEหุ้น', select=[0,5,6,7])

'''

# เช็คราคาย้อนหลัง 30 วัน แสดงวันที่ ,ราคาปิด, เปลี่ยนแปลง, %เปลี่ยนแปลง
historical_price = stock.historical('TEAMG',days=30,show=True,select=[0,5,6,7],header=True)

# พล็อตราคาปิด 30 วันย้อนหลัง
stock.plot('TEAMG',days=30)
```

พัฒนาโดย: ลุงวิศวกร สอนคำนวณ
FB: https://www.facebook.com/UncleEngineer

YouTube: https://www.youtube.com/UncleEngineer
