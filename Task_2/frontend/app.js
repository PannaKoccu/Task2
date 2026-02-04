const API_URL = "http://localhost:8081";

async function loadTasks() {
  const res = await fetch(`${API_URL}/api/tasks`);
  const data = await res.json();
  const div = document.getElementById("tasks");
  div.innerHTML = "";

  data.forEach(t => {
    const el = document.createElement("div");
    el.innerHTML = `<span>${t.title}: ${t.description} — ${t.status}</span>`;

    // Create button container
    const btnContainer = document.createElement("div");
    btnContainer.style.marginLeft = "auto";
    btnContainer.style.display = "flex";
    btnContainer.style.gap = "5px";

    // Toggle button
    const toggleBtn = document.createElement("button");
    toggleBtn.textContent = "Toggle";
    toggleBtn.onclick = async () => {
      await fetch(`${API_URL}/api/tasks/${t.id}`, { method: "PATCH" });
      loadTasks();
    };

    // Delete button
    const delBtn = document.createElement("button");
    delBtn.textContent = "Delete";
    delBtn.onclick = async () => {
      await fetch(`${API_URL}/api/tasks/${t.id}`, { method: "DELETE" });
      loadTasks();
    };

    // Append buttons to container, then container to task element
    btnContainer.appendChild(toggleBtn);
    btnContainer.appendChild(delBtn);
    el.appendChild(btnContainer);

    div.appendChild(el);
  });
}

document.getElementById("taskForm").addEventListener("submit", async e => {
  e.preventDefault();
  const form = document.getElementById("taskForm");
  const formData = new FormData(form);

  await fetch(`${API_URL}/api/tasks`, {
    method: "POST",
    body: formData
  });
  document.getElementById("taskForm").reset();
  loadTasks();
});

loadTasks();