
from app import create_app

if __name__=='__main__':
    print("---- creating app == ")
    app = create_app('prd')
    app.run(debug=True)