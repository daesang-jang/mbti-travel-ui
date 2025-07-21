from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 1. 메인 페이지
@app.route("/")
def home():
    return render_template("index.html")

# 2. 드롭다운 선택 결과 처리
@app.route("/redirect", methods=["POST"])
def redirect_to_mbti():
    mbti = request.form["mbti"].upper()
    try:
        return redirect(url_for("static_mbti_page", mbti=mbti))
    except:
        return f"{mbti}.html 페이지가 존재하지 않아요. 해당 MBTI 페이지를 먼저 만들어주세요."

# 3. 정적 MBTI HTML 페이지 렌더링
@app.route("/<mbti>.html")
def static_mbti_page(mbti):
    return render_template(f"{mbti}.html")

# 4. 실행 설정
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
