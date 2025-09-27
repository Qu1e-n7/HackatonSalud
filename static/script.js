// script.js

// Manejo del formulario
document.getElementById('formSintomas').addEventListener('submit', function(e) {
  e.preventDefault();
  const nombre = document.getElementById('nombre').value.trim();
  const sintomas = document.getElementById('sintomas').value.trim();

  if (!nombre || !sintomas) {
    document.getElementById('respuesta').textContent = 'Por favor completa todos los campos.';
    return;
  }

  // Simulación de envío
  document.getElementById('respuesta').textContent = `Gracias, ${nombre}. Registramos tus síntomas: ${sintomas}`;
});

// Jornadas simuladas
const jornadas = [
  { fecha: '2025-10-02', lugar: 'Garagoa', tipo: 'Vacunación' },
  { fecha: '2025-10-05', lugar: 'Provenir', tipo: 'Optometría' },
  { fecha: '2025-10-10', lugar: 'Sáchica', tipo: 'Odontología' }
];

const lista = document.getElementById('listaJornadas');
jornadas.forEach(j => {
  const item = document.createElement('li');
  item.textContent = `${j.fecha} – ${j.lugar} (${j.tipo})`;
  lista.appendChild(item);
});

// Gráfico de demanda
const ctx = document.getElementById('graficoConsultas').getContext('2d');
new Chart(ctx, {
  type: 'bar',
  data: {
    labels: ['Enero', 'Febrero', 'Marzo', 'Abril'],
    datasets: [{
      label: 'Consultas médicas',
      data: [120, 150, 180, 220],
      backgroundColor: '#2e86de'
    }]
  },
  options: {
    responsive: true,
    scales: {
      y: { beginAtZero: true }
    }
  }
});