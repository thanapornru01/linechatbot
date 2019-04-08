from flask import Flask, request
import json
import requests

# ตรง YOURSECRETKEY ต้องนำมาใส่เองครับจะกล่าวถึงในขั้นตอนต่อๆ ไป
global LINE_API_KEY
# ห้ามลบคำว่า Bearer ออกนะครับเมื่อนำ access token มาใส่
LINE_API_KEY = 'Bearer Yt+cFnKVPyfwo0Ji7SgxerlZrFMtIdJFHHK+TIpUU4U1jcfhcEQrmV4h+P4F90YeH0gWIMlUDrFfou9tenDDjlGhA5iomBW80TbRc5SMv+OfKaMqfhcuPNK0FXGD6boCSyeXaijClULPBBneiKWeRwdB04t89/1O/w1cDnyilFU='

app = Flask(__name__)
 
@app.route('/')
def index():
    return 'This is chatbot server.'
@app.route('/bot', methods=['POST'])

def bot():
    # ข้อความที่ต้องการส่งกลับ
    replyQueue = list()
   
    # ข้อความที่ได้รับมา
    msg_in_json = request.get_json()
    msg_in_string = json.dumps(msg_in_json)
    text = msg_in_json["events"][0]['message']['text'].lower().strip()
    print(msg_in_json["events"][0]['message']['text'].lower().strip())
    # Token สำหรับตอบกลับ (จำเป็นต้องใช้ในการตอบกลับ)
    replyToken = msg_in_json["events"][0]['replyToken']
    
    # ส่วนนี้ดึงข้อมูลพื้นฐานออกมาจาก json (เผื่อ)
    userID =  msg_in_json["events"][0]['source']['userId']
    msgType =  msg_in_json["events"][0]['message']['type']
    
    # ตรวจสอบว่า ที่ส่งเข้ามาเป็น text รึป่าว (อาจเป็น รูป, location อะไรแบบนี้ได้ครับ)
    # แต่ก็สามารถประมวลผลข้อมูลประเภทอื่นได้นะครับ
    # เช่น ถ้าส่งมาเป็น location ทำการดึง lat long ออกมาทำบางอย่าง เป็นต้น
    if msgType != 'text':
        reply(replyToken, ['Only text is allowed.'])
        return 'OK',200
    
    # ตรงนี้ต้องแน่ใจว่า msgType เป็นประเภท text ถึงเรียกได้ครับ 
    # lower เพื่อให้เป็นตัวพิมพ์เล็ก strip เพื่อนำช่องว่างหัวท้ายออก ครับ
    if(text == "สวัสดี"):
        print('in if')
        replyQueue.append("สวัสดีค่ะ")
        replyQueue.append("นี่คือบอทสาระน่ารู้เกี่ยวกับสมุนไพรไทยพร้อมแนะนำสรรพคุณรักษาโรคค่ะ")
        replyQueue.append("เริ่มต้นเลยนะค่ะ")
        reply(replyToken, replyQueue[:5])
        return 'OK', 200
        
    if(text == "ขมิ้นชัน"):
        print('in if')
        replyQueue.append("ขมิ้นชันหรอค่ะ")
        replyQueue.append("เป็นไม้ล้มลุกมีสีเหลืองอมส้มมีเหง้าอยู่ใต้ดินมีกลิ่นหอม")
        replyQueue.append("สรรพคุณใช้รักษาอาการที่เกี่ยวกับกระเพาะอาหาร")
        replyQueue.append("รวมทั้งแก้ท้องเสียท้องร่วงจุกเสียดแน่นท้อง")
        replyQueue.append("สนใจสมุนไพรตัวอื่นป้อนชื่อต่อได้เลยน่ะค่ะ")
        reply(replyToken, replyQueue[:5])
        return 'OK', 200
    
    if(text == "ทองพันชั่ง"):
        print('in if')
        replyQueue.append("ทองพันชั่งหรอค่ะ")
        replyQueue.append("เป็นไม้พุ่มขนาดเล็ก ออกดอกสีขาว ส่วนที่ใช้ทำยาคือ ใบและราก ที่หากนำปริมาณ 1 กำมือมาต้มรับประทานเช้าเย็น")
        replyQueue.append("สรรพคุณใช้ช่วยดับพิษไข้ รักษาโรคผิวหนัง ริดสีดวงทวารหนัก แก้ไอเป็นเลือด ฆ่าพยาธิ")
        replyQueue.append("นอกจากนั้น ยังสามารถนำใบและรากมาตำละเอียด เพื่อรักษาโรคกลาก เกลื้อน ได้ด้วย")
        replyQueue.append("สนใจสมุนไพรตัวอื่นอีกไหมค่ะ")
        reply(replyToken, replyQueue[:5])
        return 'OK', 200   
        
    if(text == "สนใจค่ะ"):
        print('in if')
        replyQueue.append("ป้อนชื่อสมุนไพรได้เลยนะคะ")
        reply(replyToken, replyQueue[:5])
        return 'OK', 200

    if(text == "กะเพรา"):
        print('in if')
        replyQueue.append("กะเพราหรอค่ะ")
        replyQueue.append("สรรพคุณมีฤทธิ์ขับลม ช่วยแก้จุดเสียด แน่นท้อง แก้ปวดท้องอุจจาระ")
        replyQueue.append("ส่วนน้ำสกัดทั้งต้น สามารถรักษาแผลในกระเพาะอาหาร")
        replyQueue.append("สำหรับเมล็ดกะเพรา ก็สามารถพอกตาให้ผงหรือฝุ่นที่เข้าตาหลุดออกมาได้อย่างง่ายดาย")
        replyQueue.append("สนใจสมุนไพรตัวอื่นอีกไหมค่ะ")
        reply(replyToken, replyQueue[:5])
        return 'OK', 200 

    if(text == "ไม่"):
        print('in if')
        replyQueue.append("ขอบคุณนะคะ")
        reply(replyToken, replyQueue[:5])
        return 'OK', 200  

    # ตัวอย่างการทำให้ bot ถาม-ตอบได้ แบบ exact match
    # response_dict = {'สวัสดี':'สวัสดีครับ'}
    # if text in response_dict:
    # replyQueue.append(reponse_dict[text])
    # else:
    # replyQueue.append('ไม่รู้ว่าจะตอบอะไรดี TT')
       
    # ตัวอย่างการทำให้ bot ถาม-ตอบได้ แบบ non-exact match
    # โดยที่มี method ชื่อ find_closest_sentence ที่ใช้การเปรียบเทียบประโยค
    # เพื่อค้นหาประโยคที่ใกล้เคียงที่สุด อาจใช้เรื่องของ word embedding มาใช้งานได้ครับ
    # simple sentence embeddings --> https://openreview.net/pdf?id=SyK00v5xx
    # response_dict = {'สวัสดี':'สวัสดีครับ'}
    # closest = find_closest_sentence(response_dict, text)
    # replyQueue.append(reponse_dict[closest])
   
    # ตอบข้อความ "นี่คือรูปแบบข้อความที่รับส่ง" กลับไป
    replyQueue.append('นี่คือรูปแบบข้อความที่รับส่ง')
    
    # ทดลอง Echo ข้อความกลับไปในรูปแบบที่ส่งไปมา (แบบ json)
    replyQueue.append(msg_in_string)
    reply(replyToken, replyQueue[:5])
    
    return 'OK', 200
 
def reply(replyToken, textList):
    # Method สำหรับตอบกลับข้อความประเภท text กลับครับ เขียนแบบนี้เลยก็ได้ครับ
    LINE_API = 'https://api.line.me/v2/bot/message/reply'
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': LINE_API_KEY
    }
    msgs = []
    for text in textList:
        msgs.append({
            "type":"text",
            "text":text
        })
    data = json.dumps({
        "replyToken":replyToken,
        "messages":msgs
    })
    requests.post(LINE_API, headers=headers, data=data)
    return

if __name__ == '__main__':
    app.run()
