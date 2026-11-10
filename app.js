const screen = document.getElementById('screen');
const command = document.getElementById('command');
const form = document.getElementById('command-form');
const send = document.getElementById('send');
const status = document.getElementById('status');
let pendingInput = null;
let buffer = '';
let finished = false;
function scrollBottom(){screen.scrollTop=screen.scrollHeight;}
function flush(){if(!buffer)return;const el=document.createElement('pre');el.className='output';el.textContent=buffer;screen.append(el);buffer='';scrollBottom();}
function note(message,cls='system'){flush();const el=document.createElement('p');el.className=cls;el.textContent=message;screen.append(el);scrollBottom();}
window.gawainPrint = text => {buffer+=String(text);if(buffer.length>120000||buffer.endsWith('\n'))flush();};
window.gawainInput = prompt => new Promise(resolve=>{
  flush();
  if(prompt){const el=document.createElement('pre');el.className='output';el.textContent=String(prompt);screen.append(el);}
  pendingInput=resolve;command.disabled=false;send.disabled=false;
  command.placeholder=String(prompt).includes('ENTER')?'Press Enter to continue…':'Type your choice…';
  status.textContent='AWAITING INPUT';command.focus();scrollBottom();
});
form.addEventListener('submit',event=>{
  event.preventDefault();if(!pendingInput)return;
  const value=command.value;command.value='';
  const echo=document.createElement('pre');echo.className='input-echo';echo.textContent='❯ '+value;screen.append(echo);scrollBottom();
  const resolve=pendingInput;pendingInput=null;command.disabled=true;send.disabled=true;
  status.textContent='PLAYING';resolve(value);
});
document.getElementById('restart').addEventListener('click',()=>location.reload());
screen.addEventListener('click',()=>{if(!command.disabled)command.focus();});
async function boot(){
 try{
  if(typeof loadPyodide!=='function')throw new Error('Could not load the Python engine. Check your internet connection.');
  const pyodide=await loadPyodide({indexURL:'https://cdn.jsdelivr.net/pyodide/v0.27.7/full/'});
  status.textContent='LOADING GAME';
  const response=await fetch('game.py');
  if(!response.ok)throw new Error('Could not load game.py (HTTP '+response.status+').');
  const source=await response.text();
  note('The adventure is ready.');
  status.textContent='PLAYING';
  await pyodide.runPythonAsync(source);
  flush();finished=true;status.textContent='GAME COMPLETE';
  command.disabled=true;send.disabled=true;note('Adventure complete. Press Restart to play again.');
 }catch(err){flush();status.textContent='ERROR';note(String(err),'system error');note('Tip: Open the website through GitHub Pages or a local web server, not by double-clicking index.html.');console.error(err);}
}
window.addEventListener('load',boot);
