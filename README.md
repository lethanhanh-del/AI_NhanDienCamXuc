# Emotion Detection API / API Nhận Diện Cảm Xúc

## Overview / Tổng quan

**English**:  
This is an AI system built to detect emotions in Vietnamese text using a fine-tuned PhoBERT model. It employs a RobertaForSequenceClassification architecture to classify text into one of five emotion categories: "Happy – Excited", "Calm – Relaxed", "Sad – Lonely – Nostalgic", "Angry – Stressed", and "Other". The system is integrated with FastAPI to provide a RESTful API endpoint, enabling easy integration with other applications. It tokenizes input text, predicts the emotion, and returns the corresponding label and description.

**Tiếng Việt**:  
Đây là một hệ thống AI được xây dựng để nhận diện cảm xúc trong văn bản tiếng Việt bằng cách sử dụng mô hình PhoBERT đã được tinh chỉnh. Hệ thống sử dụng kiến trúc RobertaForSequenceClassification để phân loại văn bản vào một trong năm danh mục cảm xúc: "Vui vẻ – Phấn khích", "Bình yên – Thư giãn", "Buồn bã – Cô đơn – Hoài niệm", "Tức giận – Căng thẳng" và "Khác". Hệ thống được tích hợp với FastAPI để cung cấp một điểm cuối API RESTful, cho phép tích hợp dễ dàng với các ứng dụng khác. Nó mã hóa văn bản đầu vào, dự đoán cảm xúc và trả về nhãn cùng mô tả tương ứng.

## Features / Tính năng

**English**:  
- **Emotion Classification**: Accurately predicts emotions in Vietnamese text using a fine-tuned PhoBERT model.  
- **FastAPI Integration**: Provides a simple and efficient API endpoint for emotion detection.  
- **Pre-trained Model**: Leverages a pre-trained PhoBERT model optimized for emotion recognition.  

**Tiếng Việt**:  
- **Phân loại cảm xúc**: Dự đoán chính xác cảm xúc trong văn bản tiếng Việt bằng mô hình PhoBERT đã được tinh chỉnh.  
- **Tích hợp FastAPI**: Cung cấp một điểm cuối API đơn giản và hiệu quả để nhận diện cảm xúc.  
- **Mô hình được đào tạo sẵn**: Sử dụng mô hình PhoBERT được tối ưu hóa cho việc nhận diện cảm xúc.

## Prerequisites / Yêu cầu

**English**:  
- Python 3.8+  
- PyTorch  
- Transformers (Hugging Face)  
- FastAPI  
- Uvicorn  
- Pyodbc (optional, for potential database integration)  

**Tiếng Việt**:  
- Python 3.8 trở lên  
- PyTorch  
- Transformers (Hugging Face)  
- FastAPI  
- Uvicorn  
- Pyodbc (tùy chọn, cho tích hợp cơ sở dữ liệu tiềm năng)  

## Installation / Cài đặt

**English**:  
1. **Clone the Repository**:  
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```
2. **Install Dependencies**:  
   ```bash
   pip install -r requirements.txt
   ```
3. **Download Pre-trained Model**:  
   Ensure the fine-tuned PhoBERT model and tokenizer are available at the path `api_AmNhac/phobert-emotion-finetuned`. Update the path in `api.py` if necessary.

**Tiếng Việt**:  
1. **Sao chép kho lưu trữ**:  
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```
2. **Cài đặt các thư viện cần thiết**:  
   ```bash
   pip install -r requirements.txt
   ```
3. **Tải mô hình được đào tạo sẵn**:  
   Đảm bảo mô hình PhoBERT đã được tinh chỉnh và tokenizer có sẵn tại đường dẫn `api_AmNhac/phobert-emotion-finetuned`. Cập nhật đường dẫn trong `api.py` nếu cần.

## Usage / Cách sử dụng

**English**:  
1. **Run the API**:  
   Start the FastAPI server using Uvicorn:  
   ```bash
   uvicorn api:app --host 127.0.0.1 --port 7777
   ```
2. **Access the API**:  
   The API is accessible at `http://127.0.0.1:7777`. The primary endpoint is:  
   - **POST /camxuc/**: Analyzes input text and returns the predicted emotion.  
     - **Request Body**:  
       ```json
       "last night in my dream I saw you"
       ```
     - **Response**:  
       ```json
       {
         "label": 2,
         "emotion": "Sad – Lonely – Nostalgic"
       }
       ```
3. **Example Request**:  
   Using `curl`:  
   ```bash
   curl -X POST "http://127.0.0.1:7777/camxuc/" -H "Content-Type: application/json" -d '"đêm qua trong giấc mơ em nhìn thấy anh"'
   ```

**Tiếng Việt**:  
1. **Chạy API**:  
   Khởi động máy chủ FastAPI bằng Uvicorn:  
   ```bash
   uvicorn api:app --host 127.0.0.1 --port 7777
   ```
2. **Truy cập API**:  
   API có thể truy cập tại `http://127.0.0.1:7777`. Điểm cuối chính là:  
   - **POST /camxuc/**: Phân tích văn bản đầu vào và trả về cảm xúc dự đoán.  
     - **Nội dung yêu cầu**:  
       ```json
       "đêm qua trong giấc mơ em nhìn thấy anh"
       ```
     - **Kết quả trả về**:  
       ```json
       {
         "label": 2,
         "emotion": "Buồn bã – Cô đơn – Hoài niệm"
       }
       ```
3. **Ví dụ yêu cầu**:  
   Sử dụng `curl`:  
   ```bash
   curl -X POST "http://127.0.0.1:7777/camxuc/" -H "Content-Type: application/json" -d '"đêm qua trong giấc mơ em nhìn thấy anh"'
   ```

## Project Structure / Cấu trúc dự án

**English**:  
- **api.py**: Main FastAPI application script for loading the model and handling API requests.  
- **tokenizer_config.json**: Configuration for the PhoBERT tokenizer.  
- **special_tokens_map.json**: Mapping of special tokens used by the tokenizer.  
- **config.json**: Configuration for the PhoBERT model.  
- **added_tokens.json**: Additional tokens for the tokenizer.  
- **vocab.txt**: Vocabulary file for the PhoBERT tokenizer.  

**Tiếng Việt**:  
- **api.py**: Tệp chính của ứng dụng FastAPI để tải mô hình và xử lý các yêu cầu API.  
- **tokenizer_config.json**: Cấu hình cho tokenizer PhoBERT.  
- **special_tokens_map.json**: Ánh xạ các token đặc biệt được sử dụng bởi tokenizer.  
- **config.json**: Cấu hình cho mô hình PhoBERT.  
- **added_tokens.json**: Các token bổ sung cho tokenizer.  
- **vocab.txt**: Tệp từ vựng cho tokenizer PhoBERT.

## Model Details / Chi tiết mô hình

**English**:  
- **Model**: PhoBERT (fine-tuned for emotion detection)  
- **Architecture**: RobertaForSequenceClassification  
- **Labels**:  
  - 0: Happy – Excited  
  - 1: Calm – Relaxed  
  - 2: Sad – Lonely – Nostalgic  
  - 3: Angry – Stressed  
  - 4: Other  
- **Tokenizer**: PhobertTokenizer  
- **Model Path**: `api_AmNhac/phobert-emotion-finetuned`  

**Tiếng Việt**:  
- **Mô hình**: PhoBERT (được tinh chỉnh cho nhận diện cảm xúc)  
- **Kiến trúc**: RobertaForSequenceClassification  
- **Nhãn**:  
  - 0: Vui vẻ – Phấn khích  
  - 1: Bình yên – Thư giãn  
  - 2: Buồn bã – Cô đơn – Hoài niệm  
  - 3: Tức giận – Căng thẳng  
  - 4: Khác  
- **Tokenizer**: PhobertTokenizer  
- **Đường dẫn mô hình**: `api_AmNhac/phobert-emotion-finetuned`

## Notes / Ghi chú

**English**:  
- Ensure the model and tokenizer files are correctly placed in the specified directory.  
- The `pyodbc` import is currently unused and can be removed if no database integration is needed.  
- For production, consider adding error handling, logging, and authentication mechanisms.  

**Tiếng Việt**:  
- Đảm bảo các tệp mô hình và tokenizer được đặt đúng trong thư mục được chỉ định.  
- Thư viện `pyodbc` hiện không được sử dụng và có thể được loại bỏ nếu không cần tích hợp cơ sở dữ liệu.  
- Đối với môi trường sản xuất, hãy cân nhắc thêm xử lý lỗi, ghi log và cơ chế xác thực.
