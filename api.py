import random
from typing import Optional
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from fastapi import FastAPI, Body,  HTTPException
import uvicorn
from pydantic import BaseModel
import pyodbc


# Khởi tạo FastAPI
app = FastAPI()
#------------------------------------------------------- phân tích cảm xúc ------------------------------------------------
# Bản đồ nhãn số sang nhãn chữ
label_map = {
    0: "Vui vẻ – Phấn khích",
    1: "Bình yên – Thư giãn",
    2: "Buồn bã – Cô đơn – Hoài niệm",
    3: "Tức giận – Căng thẳng",
    4: "Khác"
}

# Tải tokenizer và mô hình đã fine-tune
model_path = "api_AmNhac/phobert-emotion-finetuned"  # hoặc "vinai/phobert-base" nếu chưa fine-tune
tokenizer = AutoTokenizer.from_pretrained(model_path, use_fast=False)
model = AutoModelForSequenceClassification.from_pretrained(model_path)
model.eval()

# Hàm dự đoán cảm xúc
def predict_emotion(text):
    # Token hóa
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)

    # Dự đoán
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        predicted_class_id = logits.argmax().item()

    # In kết quả
    label_name = label_map[predicted_class_id]
    return predicted_class_id, label_name

# # ✨ Ví dụ sử dụng
# text_input = "đêm qua trong giấc mơ em nhìn thấy anh"

# label_id, label_text = predict_emotion(text_input)
# print(f"Nhận diện cảm xúc: {label_id} - {label_text}")

@app.post("/camxuc/")
async def predict_multiclass(text: str = Body(..., embed=True)):
    predicted_label, emotion= predict_emotion(text)
    results =  {"label": predicted_label, "emotion": emotion}
    return results

#---------------------------------------------------------- phân tích cảm xúc ------------------------------------------------



#----------------------------------------------------------------=main=--------------------------------------------------------
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=7777)
#----------------------------------------------------------------=main=--------------------------------------------------------
