from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Home Page</h1>
    <p>Welcome to my Dockerized Python App!</p>
    <nav>
        <a href="/about">About Page</a> | 
        <a href="/contact">Contact Page</a> | 
        <a href="/projects">Projects Page</a>
    </nav>
    """

@app.route('/about')
def about():
    return "<h1>About Page</h1><p>This is the about section.</p><a href='/'>Back Home</a>"

@app.route('/contact')
def contact():
    return "<h1>Contact Page</h1><p>Email us at hello@example.com</p><a href='/'>Back Home</a>"

@app.route('/projects')
def projects():
    return "<h1>Projects</h1><p>Check out our Docker projects here.</p><a href='/'>Back Home</a>"

if __name__ == '__main__':
    # Use 0.0.0.0 so it's accessible outside the container
    app.run(host='0.0.0.0', port=5000)
