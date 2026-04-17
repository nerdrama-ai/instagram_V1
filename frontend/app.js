
const API = "https://instabeat-backend.onrender.com";

let tracks = [];
let current = 0;
let audio = new Audio();

async function load() {
  const res = await fetch(`${API}/api/tracks`);
  tracks = await res.json();
  render();
}

function render() {
  const container = document.getElementById("tracks");
  container.innerHTML = "";

  tracks.forEach((t, i) => {
    const div = document.createElement("div");
    div.innerText = t.title;
    div.onclick = () => play(i);
    container.appendChild(div);
  });
}

function play(i) {
  current = i;
  audio.src = `${API}/api/proxy?url=${encodeURIComponent(tracks[i].audio_url)}`;
  audio.play();
}

function toggle() {
  if (audio.paused) audio.play();
  else audio.pause();
}

function next() {
  play((current + 1) % tracks.length);
}

function prev() {
  play((current - 1 + tracks.length) % tracks.length);
}

load();
