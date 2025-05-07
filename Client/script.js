const dropZone = document.getElementById('dropZone');
const submitBtn = document.getElementById('submitBtn');
let hasFiles = false;
let iszip = false;

function switchsite(page) {
    for (let i = 1; i <= 2; i++) {
      const tmp = document.getElementById('page' + i);
      tmp.style.display = (i === page) ? 'block' : 'none';
    }
}

function enableButtonIfFilesPresent(dropZone, count) {
    const button = dropZone.parentElement.querySelector('button');
    if (button) {
        button.disabled = count === 0;
    }
}

function showFilePreview(dropZone, files) {
    dropZone.innerHTML = '';
    const filePreview = document.createElement("div");
    filePreview.className = "filePreview";
  
    const file = files[0];
    dropZone.file = file;
    const info = document.createElement('div');
    info.style.marginBottom = '16px';
  
    const text = document.createElement('div');
    text.textContent = `Dateiname: ${file.name} (${file.type || 'Unbekannter Typ'})`;
  
    if (
      file.type === "application/x-zip-compressed" ||
      file.type === "application/zip" ||
      file.name.toLowerCase().endsWith(".zip")
    ) {
      iszip = true;
    }
  
    info.appendChild(text);
    filePreview.appendChild(info);
    dropZone.appendChild(filePreview);
  }

document.querySelectorAll('.drop-zone').forEach((dropZone) => {
    dropZone.addEventListener('dragover', (e) => {
      e.preventDefault();
      dropZone.classList.add('dragover');
    });
  
    dropZone.addEventListener('dragleave', () => {
      dropZone.classList.remove('dragover');
    });
  
    dropZone.addEventListener('drop', (e) => {
      e.preventDefault();
      dropZone.classList.remove('dragover');
      const files = e.dataTransfer.files;
      enableButtonIfFilesPresent(dropZone, files.length);
      showFilePreview(dropZone, files);
    });
  
    dropZone.addEventListener('click', () => {
      const fileInput = document.createElement('input');
      fileInput.type = 'file';
      fileInput.multiple = true;
      fileInput.onchange = () => {
        enableButtonIfFilesPresent(dropZone, fileInput.files.length);
        showFilePreview(dropZone, fileInput.files);
      };
      fileInput.click();
    });
  });

  submitBtn1.addEventListener('click', () => {
    const file = document.querySelector("#page1 .drop-zone").file;
  
    if (
      file.type === "application/x-zip-compressed" ||
      file.type === "application/zip" ||
      file.name.toLowerCase().endsWith(".zip")
    ) {
      const formData = new FormData();
      formData.append("file", file);
  
      const element = document.querySelector("#myBar");
      const bar = document.querySelector("#myProgress");
  
      let interval = setInterval(() => {
        fetch("http://localhost:8000/api/status")
          .then(response => response.json())
          .then(data => {
            const prozent = Math.round((data.verarbeitet / data.gesamt) * 100);
            element.style.width = prozent + "%";
            element.innerHTML = prozent + "%";
            bar.style.display = "block";
  
            if (data.verarbeitet >= data.gesamt) {
              clearInterval(interval);
            }
          })
          .catch(error => console.error("Status-Abfrage fehlgeschlagen:", error));
      }, 1000);
  
      fetch("http://localhost:8000/api/process-zip", {
        method: "POST",
        headers: {
          "Accept": "application/zip"
        },
        body: formData
      })
        .then(response => {
          if (!response.ok) throw new Error("Fehler beim Hochladen");
          return response.blob();
        })
        .then(blob => {
          const url = URL.createObjectURL(blob);
          const a = document.createElement("a");
          a.href = url;
          a.download = "ergebnis_pdfs.zip";
          a.click();
          clearInterval(interval);
        })
        .catch(error => {
          console.error("Upload fehlgeschlagen:", error);
          clearInterval(interval);
        });
  
    } else {
      alert("Bitte wählen Sie eine ZIP-Datei aus, um fortzufahren.");
    }
  });

submitBtn2.addEventListener('click', () => {
    const file = document.querySelector("#page2 .drop-zone").file;
  
    if (file && (file.type === "application/pdf" || file.name.toLowerCase().endsWith(".pdf"))) {
      const formData = new FormData();
      formData.append("file", file);
  
      fetch("http://localhost:8000/api/metadata", {
        method: "POST",
        headers: {
          "Accept": "application/json"
        },
        body: formData
      })
      .then(response => {
        if (!response.ok) throw new Error("Fehler beim Hochladen");
        return response.json();
      })
      .then(data => {
        const element = document.querySelector("#page2result");
        element.style.display = "block";
        element.textContent = `Metadaten der Datei "${file.name}" (${file.type || 'Unbekannter Typ'}):\n\n${JSON.stringify(data, null, 2)}`;
      })
      .catch(error => {
        console.error("Upload fehlgeschlagen:", error);
      });
  
    } else {
      alert("Bitte wählen Sie eine PDF-Datei aus, um fortzufahren.");
    }
  });