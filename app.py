from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Sample data for demonstration
posts = [
    {"id": 1, "content": "Hello, world!"},
    {"id": 2, "content": "How's it going?"},
    {"id": 3, "content": "Ready to do some debugging?"},
]

@app.route('/')
def index():
    return render_template('index.html', posts=posts)

@app.route('/', methods=['POST'])
def create():
    content = request.form['content']
    if content:
        new_post = {
            'id': len(posts) + 1,
            'content': content
        }
        posts.append(new_post)
    
    return redirect("/")
    # return render_template('index.html', posts=posts)

if __name__ == '__main__':
    app.run(port=8080, debug=True)