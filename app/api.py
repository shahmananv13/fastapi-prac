from fastapi import FastAPI

app = FastAPI()

@app.get('/', tags = ['ROOT'])
async def root() -> dict:
	return {'Manan': 'Using FAST API'}

@app.get('/get', tags = ['todos'])
async def get_todos() -> dict:
	return {'data': todos}

@app.post('/todo', tags = ['todos'])
async def add_todo(todo: dict) -> dict:
	next_ind = todos[-1]['id'] + 1
	todo['id'] = next_ind
	todos.append(todo)
	return {'data': 'Added new todo successfully'}

@app.put('/todo/{id}', tags = ['todos'])
async def update_todo(id: int, body: dict) -> dict:
	for todo in todos:
		if todo['id'] == id:
			todo['todo'] = body['todo']
			return {'data': f'todo for id {id} has been updated successfully'}
	return {'data': f'todo for id {id} has not been found in todos'}

@app.delete('/todo/{id}', tags = ['todos'])
async def update_todo(id: int) -> dict:
	for todo in todos.copy():
		if todo['id'] == id:
			todos.remove(todo)
			return {'data': f'todo for id {id} has been removed successfully'}
	return {'data': f'todo for id {id} has not been found in todos'}


todos = [

	{
		'id': 1,
		'todo': "need to do my homework" 
	},
	{
		'id': 2,
		'todo': "need to do my workout" 
	},
	{
		'id': 3,
		'todo': "need to do my coding practice" 
	}
]