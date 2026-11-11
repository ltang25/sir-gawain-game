const screen = document.getElementById('screen');
const command = document.getElementById('command');
const form = document.getElementById('command-form');
let pendingInput = null;
let buffer = '';
let passageStart = null;

function scrollToPassage() {
    if (passageStart) {
        passageStart.scrollIntoView({
            behavior: 'instant',
            block: 'start'
        });
    }
}
function flush() {
    if (!buffer) return;

    const line = document.createElement('pre');
    line.textContent = buffer;

    screen.append(line);

    if (!passageStart) {
        passageStart = line;
        requestAnimationFrame(scrollToPassage);
    }

    buffer = '';
}
function write(text) { buffer += String(text); if (buffer.endsWith('\n')) flush(); }
window.gawainPrint = write;
window.gawainInput = prompt => new Promise(resolve => {
  flush();
  if (prompt) write(prompt);
  flush();
  pendingInput = resolve;
  command.disabled = false;
  command.focus();
  requestAnimationFrame(scrollToPassage);

});
form.addEventListener('submit', event => {
    event.preventDefault();
    if (!pendingInput) return;

    passageStart = null;

    const value = command.value;
  command.value = '';
  write(value + '\n');
  flush();
  const resolve = pendingInput;
  pendingInput = null;
  command.disabled = true;
  resolve(value);
});
document.getElementById('restart').addEventListener('click', () => location.reload());
screen.addEventListener('click', () => { if (!command.disabled) command.focus(); });
async function boot() {
  try {
    if (typeof loadPyodide !== 'function') throw new Error('Unable to load Python. Check your connection.');
    const pyodide = await loadPyodide({indexURL: 'https://cdn.jsdelivr.net/pyodide/v0.27.7/full/'});
    const response = await fetch('game.py');
    if (!response.ok) throw new Error('Unable to load game.py.');
    const source = await response.text();
    await pyodide.runPythonAsync(source);
    flush();
  } catch (error) {
    write('\n' + String(error) + '\n');
    flush();
    console.error(error);
  }
}
window.addEventListener('load', boot);
