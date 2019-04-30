const init = () => {
    const todoBox = document.querySelector('#todo_box');
    const inputArea = document.querySelector('#add_todo_input');
    inputArea.addEventListener('keydown', e => {
        if (e.key === 'Enter') {
            todoBox.appendChild(createToDo(inputArea.value));
        }
    });
    const addButton = document.querySelector('#add_todo_btn');
    addButton.addEventListener('click', e => {
        todoBox.appendChild(createToDo(inputArea.value));
    });
    const fetchButton = document.querySelector('#fetch_btn');
    fetchButton.addEventListener('click', e =>{
        fetchTodos()
    });
    const reverseButton = document.querySelector('#reverse_btn');
    reverseButton.addEventListener('click', e => {
        reverseTodos()
    });

    const fetchTodos = () => {
        fetch('https://koreanjson.com/todos')
            .then(res => res.json())
            .then(todos => {
                for (const todo of todos) {
                    todoBox.appendChild(createToDo(todo.title, todo.completed));
                }
            })
    };

    const createToDo = (inputText, completed=false) => {
        // card > Wrapper
        const todoCard = document.createElement('div');
        todoCard.classList.add('ui', 'segment', 'todo-item');
        if (completed) todoCard.classList.add('secondary');
        // card > Wrapper > input(checkbox)
        const wrapper = document.createElement('div');
        wrapper.classList.add('ui', 'checkbox');
        // card > Wrapper > label(text)
        const input = document.createElement('input');
        input.setAttribute('type', 'checkbox');
        input.checked = completed;
        input.addEventListener('click', e => {
            if (input.checked) {
                todoCard.classList.add('secondary');
                label.classList.add('completed-label');
            } else {
                todoCard.classList.remove('secondary');
                label.classList.remove('completed-label');
            }
            completed = !completed;
        });
        // card > icon
        const label = document.createElement('label');
        label.innerHTML = inputText;
        if (completed) label.classList.add('completed-label');

        const deleteIcon = document.createElement('i');
        deleteIcon.classList.add('close', 'icon', 'delete-icon');
        deleteIcon.addEventListener('click', e => {
            todoBox.removeChild(todoCard);
        });

        wrapper.appendChild(input);
        wrapper.appendChild(label);
        todoCard.appendChild(wrapper);
        todoCard.appendChild(deleteIcon);
        todoBox.appendChild(todoCard);
        return todoCard
    };

    const reverseTodos = () => {
        const allTodos = Array.from(document.querySelectorAll('.todo-item'));
        while (todoBox.firstChild) {
            todoBox.removeChild(todoBox.firstChild);
        }
        for (const todo of allTodos.reverse()) {
            todoBox.appendChild(todo);
        }
    };
};

init();