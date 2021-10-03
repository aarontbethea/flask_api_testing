from flask import Flask, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
	def get(self):
		return {'hello':'world'}

class status(Resource):    
     def get(self):
         try:
            return {'data': 'Api running'}
         except Exception as error: 
            return {'data': error}

class Sum(Resource):
    def get(self, a, b):
        return jsonify({'data': a+b})
		
api.add_resource(HelloWorld,'/')
api.add_resource(status,'/status')
api.add_resource(Sum,'/add/<int:a>,<int:b>')

if __name__ == '__main__':
	app.run(debug=True)