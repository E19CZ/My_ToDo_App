import streamlit as st
import Functions

todos = Functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    Functions.write_todos(todos)


# The order of the elements matter and it will be reflected on the webb page
st.title("My ToDo App")
st.subheader("This is my ToDo app")
st.write("This app is to increase your productivity")

# Simple check box
for index, todo in enumerate(todos):
# Connect the checkbox with the todos and session_state
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        Functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

# Label, Placeholder(Helps the user know what this box is about)
st.text_input(label="Enter a ToDo", placeholder="Add a new todo...",
              on_change=add_todo, key='new_todo')
