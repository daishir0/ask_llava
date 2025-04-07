import sys
import base64
import requests
import os
import mimetypes
from PIL import Image
import pillow_heif

def convert_heic_to_jpeg(image_path):
    heif_file = pillow_heif.read_heif(image_path)
    image = Image.frombytes(
        heif_file.mode, 
        heif_file.size, 
        heif_file.data,
        "raw",
    )
    # 一時ファイルとしてJPEGを保存
    jpeg_path = os.path.splitext(image_path)[0] + ".jpg"
    image.save(jpeg_path, "JPEG")
    return jpeg_path

def encode_image_with_mime(image_path):
    mime_type, _ = mimetypes.guess_type(image_path)
    if not mime_type:
        raise ValueError(f"対応していない画像形式です: {image_path}")
    
    # HEIC形式の場合はJPEGに変換
    if mime_type == "image/heic":
        image_path = convert_heic_to_jpeg(image_path)
        mime_type = "image/jpeg"
    
    with open(image_path, "rb") as img_file:
        image_bytes = img_file.read()
        encoded_image = base64.b64encode(image_bytes).decode("utf-8")
        return encoded_image

def main():
    if len(sys.argv) < 3:
        print("使い方: python ask_llava.py [画像ファイルパス] [質問プロンプト]")
        sys.exit(1)

    image_path = sys.argv[1]
    prompt = " ".join(sys.argv[2:])

    if not os.path.isfile(image_path):
        print(f"❌ エラー: 画像ファイルが見つかりません → {image_path}")
        sys.exit(1)

    try:
        image_data = encode_image_with_mime(image_path)
    except ValueError as e:
        print("❌", e)
        sys.exit(1)

    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "llava",
        "prompt": prompt,
        "images": [image_data],
        "stream": False
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        result = response.json()
        print("📥 レスポンスステータス:", response.status_code)
        print("🔍 回答:", result["response"])

    except requests.exceptions.HTTPError as e:
        print("❌ HTTPエラーが発生しました:")
        print(f"ステータスコード: {e.response.status_code}")
        print(f"エラーメッセージ: {e.response.text}")
    except Exception as e:
        print("❌ 予期せぬエラーが発生しました:", str(e))

if __name__ == "__main__":
    main()
