const API = 'http://localhost:8000'

const inputTarefa = document.getElementById('input-tarefa')
const btnAdicionar = document.getElementById('btn-adicionar')
const listaTarefas = document.getElementById('lista-tarefas')
const msgVazia = document.getElementById('msg-vazia')

async function carregarTarefas() {
  const res = await fetch(`${API}/tarefas/`)
  const tarefas = await res.json()
  listaTarefas.innerHTML = ''
  tarefas.forEach(renderizarTarefa)
  msgVazia.style.display = tarefas.length === 0 ? 'block' : 'none'
}

function renderizarTarefa(tarefa) {
  const li = document.createElement('li')
  if (tarefa.concluida) li.classList.add('concluida')

  li.innerHTML = `
    <span class="titulo">${tarefa.titulo}</span>
    <button class="btn-concluir">${tarefa.concluida ? '✓ Feita' : 'Concluir'}</button>
    <button class="btn-deletar">✕</button>
  `

  li.querySelector('.btn-concluir').addEventListener('click', () =>
    toggleConcluida(tarefa.id, tarefa.concluida)
  )

  li.querySelector('.btn-deletar').addEventListener('click', () =>
    deletarTarefa(tarefa.id)
  )

  listaTarefas.appendChild(li)
}

async function adicionarTarefa() {
  const titulo = inputTarefa.value.trim()
  if (!titulo) return

  await fetch(`${API}/tarefas/`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ titulo })
  })

  inputTarefa.value = ''
  carregarTarefas()
}

async function toggleConcluida(id, concluida) {
  await fetch(`${API}/tarefas/${id}`, {
    method: 'PATCH',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ concluida: !concluida })
  })
  carregarTarefas()
}

async function deletarTarefa(id) {
  await fetch(`${API}/tarefas/${id}`, { method: 'DELETE' })
  carregarTarefas()
}

btnAdicionar.addEventListener('click', adicionarTarefa)

inputTarefa.addEventListener('keydown', (e) => {
  if (e.key === 'Enter') adicionarTarefa()
})

carregarTarefas()