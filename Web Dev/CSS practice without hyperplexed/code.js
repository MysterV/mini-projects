const track = document.getElementById("image-track");

window.onmousedown = e => {
  track.dataset.mouseDownAt = e.clientY;
}

window.onmouseup = () => {
  track.dataset.mouseDownAt = "0";
  track.dataset.prevPercentage = track.dataset.percentage;
}

window.onmousemove = e => {
  if(track.dataset.mouseDownAt === "0") return;

  const mouseDelta = parseFloat(track.dataset.mouseDownAt) - e.clientY,
    maxDelta = window.innerHeight / 2;

  const percentage = (mouseDelta / maxDelta) * 100,
    nextPercentageUnconstrained = parseFloat(track.dataset.prevPercentage) + percentage
    nextPercentage = Math.max(Math.min(nextPercentageUnconstrained, 25), -100);

  track.dataset.percentage = nextPercentageUnconstrained;
}