// Fungsi bantu: tampilkan status proses
function showLoading(targetDiv, message = "⏳ Proses sedang berlangsung...") {
  document.getElementById(targetDiv).innerHTML = `<p>${message}</p>`;
}

// STEGANOGRAFI GAMBAR
document.getElementById("imageStegoForm").onsubmit = async function (e) {
  e.preventDefault();
  const formData = new FormData(this);
  showLoading("imageStegoResult");

  const response = await fetch("/encode-image", {
    method: "POST",
    body: formData,
  });

  const result = await response.json();
  if (result.output_path) {
    document.getElementById("imageStegoResult").innerHTML = `<p>✅ Selesai:</p>
     <img src="${result.output_path}" width="300" />
     <p><a href="${result.output_path}" download>⬇️ Download Gambar Stego</a></p>`;
  } else {
    document.getElementById("imageStegoResult").innerText = "❌ Gagal encode.";
  }
};

// DECODE PESAN dari gambar stego
document.getElementById("decodeForm").onsubmit = async function (e) {
  e.preventDefault();
  const formData = new FormData(this);
  showLoading("decodeResult");

  const response = await fetch("/decode-image", {
    method: "POST",
    body: formData,
  });

  const result = await response.json();
  if (result.message) {
    document.getElementById(
      "decodeResult"
    ).innerHTML = `<p>✅ Pesan tersembunyi:</p><pre>${result.message}</pre>`;
  } else {
    document.getElementById("decodeResult").innerText =
      "❌ Gagal membaca pesan.";
  }
};

// KOMPRESI AUDIO
document.getElementById("audioForm").onsubmit = async function (e) {
  e.preventDefault();
  const formData = new FormData(this);
  showLoading("audioResult");

  const response = await fetch("/compress-audio", {
    method: "POST",
    body: formData,
  });

  const result = await response.json();
  if (result.output_path) {
    document.getElementById("audioResult").innerHTML = `<p>✅ Selesai:</p>
             <audio controls src="${result.output_path}"></audio>
             <p><a href="${result.output_path}" download>Download Audio</a></p>`;
  } else {
    document.getElementById("audioResult").innerText =
      "❌ Gagal kompres audio.";
  }
};

// KOMPRESI VIDEO
document.getElementById("videoForm").onsubmit = async function (e) {
  e.preventDefault();
  const formData = new FormData(this);
  showLoading("videoResult");

  const response = await fetch("/compress-video", {
    method: "POST",
    body: formData,
  });

  const result = await response.json();
  if (result.output_path) {
    document.getElementById("videoResult").innerHTML = `<p>✅ Selesai:</p>
             <video width="320" height="240" controls>
                 <source src="${result.output_path}" type="video/mp4">
                 Your browser does not support the video tag.
             </video>
             <p><a href="${result.output_path}" download>Download Video</a></p>`;
  } else {
    document.getElementById("videoResult").innerText =
      "❌ Gagal kompres video.";
  }
};
