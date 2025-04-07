# ask_llava

## Overview
`ask_llava` is a command-line tool for querying the LLaVA (Large Language and Vision Assistant) model with images. It allows you to ask questions about images by sending them to a locally running LLaVA model through the Ollama API. The tool supports various image formats, including HEIC files which are automatically converted to JPEG.

## Installation

### Prerequisites
- Python 3.6 or higher
- Git
- Ollama with LLaVA model installed

### Steps
1. Clone the repository:
```bash
git clone https://github.com/daishir0/ask_llava
cd ask_llava
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Make sure you have Ollama installed and the LLaVA model pulled:
```bash
ollama pull llava
```

## Usage
Run the script with an image file path and your question:

```bash
python ask_llava.py [image_file_path] [question]
```

Example:
```bash
python ask_llava.py photo.jpg "What can you see in this image?"
```

For HEIC images (commonly used on iOS devices), the tool will automatically convert them to JPEG before processing:
```bash
python ask_llava.py photo.heic "Describe this photo in detail."
```

## Notes
- Ensure that Ollama is running locally with the default API endpoint at `http://localhost:11434/api/generate`.
- The LLaVA model must be pulled in Ollama before using this tool.
- HEIC files will be converted to JPEG format in the same directory as the original file.
- The tool requires an active internet connection to communicate with the local Ollama API.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

---

# ask_llava

## 概要
`ask_llava`は、画像に関する質問をLLaVA（Large Language and Vision Assistant）モデルに問い合わせるためのコマンドラインツールです。Ollama APIを通じてローカルで実行されているLLaVAモデルに画像を送信し、質問することができます。このツールは様々な画像形式をサポートしており、HEIC形式のファイルは自動的にJPEG形式に変換されます。

## インストール方法

### 前提条件
- Python 3.6以上
- Git
- LLaVAモデルがインストールされたOllama

### 手順
1. リポジトリをクローンします：
```bash
git clone https://github.com/daishir0/ask_llava
cd ask_llava
```

2. 必要な依存関係をインストールします：
```bash
pip install -r requirements.txt
```

3. Ollamaがインストールされており、LLaVAモデルが取得されていることを確認してください：
```bash
ollama pull llava
```

## 使い方
スクリプトを画像ファイルのパスと質問と共に実行します：

```bash
python ask_llava.py [画像ファイルパス] [質問]
```

例：
```bash
python ask_llava.py photo.jpg "この画像に何が見えますか？"
```

HEIC画像（iOSデバイスでよく使用される形式）の場合、ツールは処理の前に自動的にJPEGに変換します：
```bash
python ask_llava.py photo.heic "この写真を詳しく説明してください。"
```

## 注意点
- OllamaがデフォルトのAPIエンドポイント（`http://localhost:11434/api/generate`）でローカルに実行されていることを確認してください。
- このツールを使用する前に、OllamaでLLaVAモデルを取得しておく必要があります。
- HEICファイルは、元のファイルと同じディレクトリにJPEG形式で変換されます。
- このツールはローカルのOllama APIと通信するためにアクティブなインターネット接続が必要です。

## ライセンス
このプロジェクトはMITライセンスの下でライセンスされています。詳細はLICENSEファイルを参照してください。