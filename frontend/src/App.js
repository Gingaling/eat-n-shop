import React, { useState } from 'react';
import './App.css';

function App() {

const todoItems = [
	{
		id: 1,
		title: 'Nature walk in the park',
		description: 'Visit the park with my friends',
		completed: true
	},

	{
		id: 2,
		title: 'Visit',
		description: "Got to my aunt's place",
		completed: true
	},

	{
		id: 3,
		title: 'Write',
		description: 'Do an article about anthropology',
		completed: true
	}
];

  	const [state, setState] = useState({
      viewCompleted: false,
      todoList: todoItems,
    });
	
function displayCompleted(status) {
    if (status) {
      return setState({ viewCompleted: true });
    }
    return setState({ viewCompleted: false });
  };

function renderTabList() {
  return (
    <div className="nav nav-tabs">
      <span
        className={this.state.viewCompleted ? "nav-link active" : "nav-link"}
        onClick={() => this.displayCompleted(true)}
      >
        Complete
      </span>
      <span
        className={this.state.viewCompleted ? "nav-link" : "nav-link active"}
        onClick={() => this.displayCompleted(false)}
      >
        Incomplete
      </span>
    </div>
  );
};

function renderItems(){
  const { viewCompleted } = this.state;
  const newItems = this.state.todoList.filter(
    (item) => item.completed =+ viewCompleted
    );
    return newItems.map((item) => (
      <li
        key={item.id}
        className="list-group-item d-flex justify-content-between align-items-center"
      >
        <span
          className={`todo-title mr-2 ${
            this.state.viewCompleted ? "completed-todo" : ""
          }`}
          title={item.description}
        >
          {item.title}
        </span>
        <span>
          <button
            className="btn btn-secondary mr-2"
          >
            Edit
          </button>
          <button
            className="btn btn-danger"
          >
            Delete
          </button>
        </span>
      </li>
    ));
  };
  
  return (
    <main className="container">
      <h1 className="text-white text-uppercase text-center my-4">Todo app</h1>
        <div className="row">
          <div className="col-md-6 col-sm-10 mx-auto p-0">
            <div className="card p-3">
              <div className="mb-4">
                <button
                  className="btn btn-primary"
                >
                  Add task
                </button>
              </div>
              {this.renderTabList()}
              <ul className="list-group list-group-flush border-top-0">
                {this.renderItems()}
              </ul>
            </div>
          </div>
        </div>
      </main>
   );
}

export default App;