function addTask() {
    let taskInput = document.getElementById("taskInput");
    let taskText = taskInput.value.trim();
    if (taskText === "") return;
    
    let taskList = document.getElementById("taskList");
    let li = document.createElement("li");
    let checkbox = document.createElement("input");
    checkbox.type = "checkbox";
    checkbox.onchange = function() {
        li.classList.toggle("completed", checkbox.checked);
    };
    
    let taskSpan = document.createElement("span");
    taskSpan.textContent = taskText;
    
    let deleteBtn = document.createElement("button");
    deleteBtn.textContent = "×";
    deleteBtn.className = "delete";
    deleteBtn.onclick = function() {
        taskList.removeChild(li);
    };
    
    li.appendChild(checkbox);
    li.appendChild(taskSpan);
    li.appendChild(deleteBtn);
    taskList.appendChild(li);
    
    taskInput.value = "";
}
