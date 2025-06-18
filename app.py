from flask import Flask, request, jsonify
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

@app.route("/chat")
def chat():
    user_text = request.args.get("text", "")
    if not user_text:
        return jsonify({"reply": "❗ أكتب سؤال فقط."})

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "أنت مساعد ذكي وهاكر غامض."},
                {"role": "user", "content": user_text}
            ]
        )
        reply = response.choices[0].message.content
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"reply": f"⚠️ خطأ: {str(e)}"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
